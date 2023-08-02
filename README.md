# Automating Java Maven Application Containerization Using Python

# Building Docker Image
docker build -t helloworld-java-image .

# Running Docker Image
docker run -d --name helloworld-java-image-app helloworld-java-image

# Run Program Using Python
python app_script.py

# Installing via Helm Chart
helm upgrade --install my-java-app ./java-app-chart -n my-namespace -f values.yaml
