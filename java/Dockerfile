# Datei: prog/java/Dockerfile (docbuc/printheadlines:java)
FROM openjdk:13
RUN adduser -r java
WORKDIR /src
RUN chown java /src
USER java
ENV JSOUP_VER 1.12.1

RUN curl -SL https://jsoup.org/packages/jsoup-$JSOUP_VER.jar \
  -o jsoup-$JSOUP_VER.jar
COPY printheadlines.java /src/
RUN javac -cp /src/jsoup-$JSOUP_VER.jar:. \
  printheadlines.java
CMD java -cp jsoup-$JSOUP_VER.jar:. printheadlines

