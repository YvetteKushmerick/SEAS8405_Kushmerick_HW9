# Use OpenJDK as base image
FROM maven:3.8.5-openjdk-11 AS build
WORKDIR /app
COPY . .
RUN mvn clean package -DskipTests

FROM openjdk:17

# Set working directory
WORKDIR /app

# Copy built jar from Maven build
COPY target/log4shell-homework-0.0.1-SNAPSHOT.jar app.jar

# Run the application
ENTRYPOINT ["java", "-jar", "app.jar"]

