#Edraak's Java Compiler REST API

 [![Build Status](https://travis-ci.org/Edraak/rest-javac.svg?branch=master)](https://travis-ci.org/Edraak/rest-javac)
 

This is a simple Docker container to compile and execute a Java file
and returns the output as a response body.

#Installation
To install this service run the following command:

    $ docker-compose up


If you'd like to change something in the code, re-build the container:

    $ docker-compose build
    $ docker-compose up


#API Usage
Assuming that you have a file called `main.java` with the following content:

    public class Main {
        public static void main(String[] args) {
            System.out.println("Hello, World");
        }
    }


Use `curl` to compile and run this file:

    $ curl -X POST -d @Main.java http://localhost:8000/v1/run

Then the API should returns `Hello, World`.
