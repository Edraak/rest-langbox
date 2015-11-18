from os import environ
from shutil import rmtree

from subprocess import Popen, PIPE
from flask import Flask, Response, request


app = Flask(__name__)


@app.route('/v1/run', methods=['POST'])
def run():
    javac = Popen([
        'docker',
        'run',
        '-i', 'lang-box/java',
    ], stdin=PIPE, stdout=PIPE, stderr=PIPE)

    stdout, stderr = javac.communicate(
        input=request.get_data()
    )

    if stdout:
        response_body = stdout
    else:
        response_body = stderr

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
