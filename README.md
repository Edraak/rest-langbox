#Edraak's Programming Language Compiler REST API

[![Build Status](https://travis-ci.org/Edraak/rest-langbox.svg?branch=master)](https://travis-ci.org/Edraak/rest-langbox)


This is a simple Docker container to compile and execute a code files
and returns the output as a response body.

#Installation
To install this service run the following command:

    $ cd docker
    $ docker build --tag=lang-box/java .
    $ cd ..
    $ # Optionally make a virtual env
    $ pip install -r requirements.txt
    $ python app.py


#API Usage
Assuming that you have a file called `Main.java` with the following content:

    public class Main {
        public static void main(String[] args) {
            System.out.println("Hello, World");
        }
    }


Use `curl` to compile and run this file:

    $ curl -X POST -d @Main.java http://localhost:8000/v1/run

Then the API should returns `Hello, World`.


#TODO
Address the following security issues:

 - [ ] Fork bomb
 - [ ] Memory over consumption
 - [ ] CPU core and time over consumption
 - [ ] Data abuse e.g. uploading very large input or very large output
 - [ ] Escape out of docker attack (is that possible)
 - [ ] DDoS attacks against others using the Docker resources
 - [ ] Prevent disk space over-consumption
 - [ ] Create a Python docker instance using the same rest API
 - [ ] Have someone to attack the system
 - [ ] Other issues?
