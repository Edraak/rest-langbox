import java.nio.file.Files;
import java.nio.file.Paths;

import org.json.JSONObject;
import org.json.JSONTokener;

import java.io.ByteArrayOutputStream;
import java.io.IOException;

public class Compiler {

    private static final int BUFFER_SIZE = 1024 * 4; // 4KB of data.

    private static String getStdInAsString() throws IOException {
        ByteArrayOutputStream buffer = new ByteArrayOutputStream();

        int byteCount;
        byte[] data = new byte[BUFFER_SIZE];

        while ((byteCount = System.in.read(data, 0, data.length)) > 0) {
            buffer.write(data, 0, byteCount);
        }

        return new String(buffer.toByteArray(), "UTF-8");
    }

    private static void runCommand(String... args) throws Exception {
        runCommand("", args);
    }

    private static void runCommand(String stdin, String[] args) throws Exception {
        ProcessBuilder procBuilder = new ProcessBuilder(args);
        procBuilder.redirectOutput(ProcessBuilder.Redirect.INHERIT);
        procBuilder.redirectError(ProcessBuilder.Redirect.INHERIT);

        Process proc = procBuilder.start();

        if (stdin.length() > 0) {
            proc.getOutputStream().write(stdin.getBytes());
        }

        proc.waitFor();
    }

    public static void main(String[] args) throws Exception {
        JSONObject input = new JSONObject(getStdInAsString());

        String code = input.getString("code");
        String stdin = input.getString("stdin");

        Files.write(Paths.get("Main.java"), code.getBytes());

        runCommand("javac", "Main.java");
        runCommand(stdin, new String[] {"java", "Main"});
    }

}
