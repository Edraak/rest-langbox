from os import environ, remove
from subprocess import Popen, PIPE
from flask import Flask, Response, request


app = Flask(__name__)


@app.route('/v1/run', methods=['POST'])
def run():

    with open('/rest-javac/Main.java', 'w+') as main:
        main.write(request.get_data())

    stdout, stderr = Popen(
        ['javac', '/rest-javac/Main.java'],
        stdout=PIPE,
        stderr=PIPE,
    ).communicate()

    stdout, stderr = Popen(
        ['java', 'Main'],
        cwd='/rest-javac/',
        stdout=PIPE,
        stderr=PIPE,
    ).communicate()

    remove('/rest-javac/Main.java')
    remove('/rest-javac/Main.class')

    return Response(
        u'{}{}'.format(stdout),
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


app.run(
    host=environ['HOST'],
    port=int(environ['PORT']),
)
