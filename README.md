# Automating Java Maven Application Containerization Using Python

# Building Docker Image
docker build -t helloworld-java-image .

# Running Docker Image
docker run -d --name helloworld-java-image-app helloworld-java-image
