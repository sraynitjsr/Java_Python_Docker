# Use a base image with Debian 11 (Slim) and Java already installed
FROM debian:11-slim

# Install OpenJDK 8
RUN apt-get update && apt-get install -y openjdk-8-jre

# Set the working directory inside the container
WORKDIR /app

# Copy the Java program (HelloWorld.java) into the container
COPY HelloWorld.java .

# Compile the Java program inside the container
RUN javac HelloWorld.java

# Expose the port the Java program will listen on
EXPOSE 8080

# Run the Java program when the container starts
CMD ["java", "HelloWorld"]
