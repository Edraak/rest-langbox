from os import environ
from shutil import rmtree

from subprocess import Popen, PIPE
from flask import Flask, Response, request


app = Flask(__name__)


@app.route('/v1/run', methods=['POST'])
def run():

    with open('/rest-javac/Main.java', 'w+') as main:
        main.write(request.get_data())

    compile_stdout, compile_stderr = Popen(
        ['javac', '/rest-javac/Main.java'],
        stdout=PIPE,
        stderr=PIPE,
    ).communicate()

    run_stdout, run_stderr = Popen(
        ['java', 'Main'],
        cwd='/rest-javac/',
        stdout=PIPE,
        stderr=PIPE,
    ).communicate()

    rmtree('/rest-javac/Main.java', ignore_errors=True)
    rmtree('/rest-javac/Main.class', ignore_errors=True)

    if run_stdout:
        response_body = run_stdout
    else:
        response_body = '\n'.join([
            compile_stdout,
            compile_stderr,
            run_stderr,
        ])

    return Response(
        response_body,
        mimetype='text/plain',
    )


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return Response(
        """
        Edraak's REST API Java Compiler is working.
        """,
        mimetype='text/plain',
    )

if __name__ == '__main__':
    app.run(
        host=environ['HOST'],
        port=int(environ['PORT']),
    )
