FROM maven:3.8.5-openjdk-18-slim as build

COPY /src src
COPY pom.xml .

RUN mvn clean package

CMD ["java","-jar","target/Docker_POC-1.0-SNAPSHOT.jar"]