import subprocess

def build_docker_image():
    try:
        subprocess.run(["docker", "build", "-t", "helloworld-java-image", "."], check=True)
        print("Docker image built successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error building Docker image: {e}")

def run_docker_container():
    try:
        subprocess.run(["docker", "run", "helloworld-java-image"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Docker container: {e}")

if __name__ == "__main__":
    build_docker_image()
    run_docker_container()
