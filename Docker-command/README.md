Docker Learning – Commands and Hands-on Practice

This repository contains Docker commands, Docker Compose commands, and hands-on projects that I practised while learning DevOps.

1. Docker Version and Information

Check Docker version:

docker --version

Display Docker system information:

docker info

Check Docker contexts:

docker context ls

Check Docker Compose version:

docker compose version

2. Docker Images

List downloaded images:

docker images

Download an image from Docker Hub:

docker pull ubuntu:24.04

Build an image using Dockerfile:

docker build -t flask_app .

Build an image without using cached layers:

docker build --no-cache -t flask_app .

Remove an image:

docker rmi flask_app

Remove unused images:

docker image prune

Inspect an image:

docker image inspect flask_app

3. Docker Containers

Create and run a container:

docker run ubuntu:24.04

Run a container interactively:

docker run -it ubuntu:24.04 bash

Run a container in detached mode:

docker run -d --name mycontainer ubuntu:24.04 sleep infinity

List running containers:

docker ps

List all containers, including stopped containers:

docker ps -a

Stop a container:

docker stop mycontainer

Start an existing stopped container:

docker start mycontainer

Restart a container:

docker restart mycontainer

Remove a stopped container:

docker rm mycontainer

Forcefully remove a container:

docker rm -f mycontainer

Run a container and automatically remove it after exit:

docker run --rm ubuntu:24.04

4. Accessing Containers

Access a running container using Bash:

docker exec -it mycontainer bash

Execute a command inside a running container:

docker exec mycontainer ls /

Check container logs:

docker logs mycontainer

Follow container logs:

docker logs -f mycontainer

Display the last 50 log lines:

docker logs --tail 50 mycontainer

Inspect container details:

docker inspect mycontainer

Display container resource usage:

docker stats

5. Docker Port Mapping

Run a container with port mapping:

docker run -d --name flask_webapp -p 8080:5000 flask_app

Port mapping syntax:

Host Port : Container Port

Example:

8080:5000

Host port: 8080

Container port: 5000

Access the Flask application through:

http://localhost:8080

6. Docker Volumes

List Docker volumes:

docker volume ls

Create a named volume:

docker volume create employee_data

Inspect a volume:

docker volume inspect employee_data

Use a named volume inside a container:

docker run -it --name volume_test -v employee_data:/data ubuntu:24.04 bash

Create a file inside the mounted volume:

echo "Docker volume learning" > /data/test.txt

Read the file:

cat /data/test.txt

Remove the container:

docker rm -f volume_test

Verify that the data persists:

docker run --rm -v employee_data:/data ubuntu:24.04 cat /data/test.txt

Remove an unused volume:

docker volume rm employee_data

7. Docker Bind Mounts

Bind mounts connect a host directory or file to a directory inside a container.

Check the current working directory:

pwd

Run a container with a bind mount:

docker run -d \
  --name volume_test \
  -p 8080:5000 \
  -v "$(pwd):/app" \
  flask_app

Syntax:

-v HOST_DIRECTORY:CONTAINER_DIRECTORY

Example:

-v "$(pwd):/app"

Host directory: Current working directory

Container directory: /app

Changes made to source files in the host directory become visible inside the container.

8. Dockerfile Instructions

Common Dockerfile instructions practised:

Instruction

Purpose

FROM

Specifies the base image

WORKDIR

Sets the working directory

RUN

Executes commands during image building

COPY

Copies files into the image

ENV

Sets environment variables

EXPOSE

Documents the container port

CMD

Specifies the default command when the container starts

Example Dockerfile:

FROM ubuntu:24.04

WORKDIR /app

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv

RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]

Build the image:

docker build -t flask_app .

Run the container:

docker run -d --name flask_webapp -p 8080:5000 flask_app

9. Docker Compose Commands

Check Docker Compose version:

docker compose version

Validate the Compose configuration:

docker compose config

Build and start services:

docker compose up -d --build

Start services:

docker compose up -d

List Compose services:

docker compose ps

View logs of all services:

docker compose logs

View logs of a particular service:

docker compose logs web
docker compose logs db

Follow logs:

docker compose logs -f

Stop services:

docker compose stop

Start existing stopped services:

docker compose start

Restart services:

docker compose restart

Stop and remove containers and the Compose network:

docker compose down

Stop and remove containers, network, and named volumes:

docker compose down -v

Warning: docker compose down -v deletes the Compose-managed named volumes and their stored data. Use it only when you intend to remove that data.

Using a custom Compose filename

If the Compose file has a different name:

docker compose -f mycompose.yml up -d

Check services:

docker compose -f mycompose.yml ps

View logs:

docker compose -f mycompose.yml logs

Stop and remove services:

docker compose -f mycompose.yml down

10. Docker Cleanup Commands

Remove stopped containers:

docker container prune

Remove unused images:

docker image prune

Remove unused volumes:

docker volume prune

Remove unused Docker resources:

docker system prune

Check Docker disk usage:

docker system df

Warning: Cleanup commands can remove resources you may want to keep. Review what is unused before cleaning up.
