FROM java:8

RUN mkdir /compiler/

WORKDIR /compiler/

RUN mkdir -p org/
RUN git clone https://github.com/douglascrockford/JSON-java.git org/json/
RUN cd org/json && git checkout 20150729

ADD Compiler.java /compiler/
RUN javac Compiler.java
RUN rm Compiler.java

CMD java Compiler
