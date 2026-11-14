# Docker Learning – Commands and Hands-on Practice

This repository contains Docker commands, Docker Compose commands, and hands-on projects that I practised while learning DevOps.

---

## 1. Docker Version and Information

**Check Docker version:**

```bash
docker --version
```

**Display Docker system information:**

```bash
docker info
```

**Check Docker contexts:**

```bash
docker context ls
```

**Check Docker Compose version:**

```bash
docker compose version
```

---

## 2. Docker Images

**List downloaded images:**

```bash
docker images
```

**Download an image from Docker Hub:**

```bash
docker pull ubuntu:24.04
```

**Build an image using Dockerfile:**

```bash
docker build -t flask_app .
```

**Build an image without using cached layers:**

```bash
docker build --no-cache -t flask_app .
```

**Remove an image:**

```bash
docker rmi flask_app
```

**Remove unused images:**

```bash
docker image prune
```

**Inspect an image:**

```bash
docker image inspect flask_app
```

---

## 3. Docker Containers

**Create and run a container:**

```bash
docker run ubuntu:24.04
```

**Run a container interactively:**

```bash
docker run -it ubuntu:24.04 bash
```

**Run a container in detached mode:**

```bash
docker run -d --name mycontainer ubuntu:24.04 sleep infinity
```

**List running containers:**

```bash
docker ps
```

**List all containers, including stopped containers:**

```bash
docker ps -a
```

**Stop a container:**

```bash
docker stop mycontainer
```

**Start an existing stopped container:**

```bash
docker start mycontainer
```

**Restart a container:**

```bash
docker restart mycontainer
```

**Remove a stopped container:**

```bash
docker rm mycontainer
```

**Forcefully remove a container:**

```bash
docker rm -f mycontainer
```

**Run a container and automatically remove it after exit:**

```bash
docker run --rm ubuntu:24.04
```

---

## 4. Accessing Containers

**Access a running container using Bash:**

```bash
docker exec -it mycontainer bash
```

**Execute a command inside a running container:**

```bash
docker exec mycontainer ls /
```

**Check container logs:**

```bash
docker logs mycontainer
```

**Follow container logs:**

```bash
docker logs -f mycontainer
```

**Display the last 50 log lines:**

```bash
docker logs --tail 50 mycontainer
```

**Inspect container details:**

```bash
docker inspect mycontainer
```

**Display container resource usage:**

```bash
docker stats
```

---

## 5. Docker Port Mapping

**Run a container with port mapping:**

```bash
docker run -d --name flask_webapp -p 8080:5000 flask_app
```

**Port mapping syntax:**

```text
Host Port : Container Port
```

**Example:**

```text
8080:5000
```

- Host port: `8080`
- Container port: `5000`

**Access the Flask application through:**

```text
http://localhost:8080
```

---

## 6. Docker Volumes

**List Docker volumes:**

```bash
docker volume ls
```

**Create a named volume:**

```bash
docker volume create employee_data
```

**Inspect a volume:**

```bash
docker volume inspect employee_data
```

**Use a named volume inside a container:**

```bash
docker run -it --name volume_test -v employee_data:/data ubuntu:24.04 bash
```

**Create a file inside the mounted volume:**

```bash
echo "Docker volume learning" > /data/test.txt
```

**Read the file:**

```bash
cat /data/test.txt
```

**Remove the container:**

```bash
docker rm -f volume_test
```

**Verify that the data persists:**

```bash
docker run --rm -v employee_data:/data ubuntu:24.04 cat /data/test.txt
```

**Remove a volume:**

```bash
docker volume rm employee_data
```

---

## 7. Docker Bind Mounts

Bind mounts connect a host directory or file to a directory inside a container.

**Check the current working directory:**

```bash
pwd
```

**Run a container with a bind mount:**

```bash
docker run -d \
  --name volume_test \
  -p 8080:5000 \
  -v "$(pwd):/app" \
  flask_app
```

**Bind mount syntax:**

```text
-v HOST_DIRECTORY:CONTAINER_DIRECTORY
```

**Example:**

```text
-v "$(pwd):/app"
```

- Host directory: Current working directory
- Container directory: `/app`

**Benefit:** Changes made to source files in the host directory become visible inside the container without rebuilding the image.

---

## 8. Dockerfile Instructions

Common Dockerfile instructions:

| Instruction | Purpose |
|---|---|
| `FROM` | Specifies the base image |
| `WORKDIR` | Sets the working directory |
| `RUN` | Executes commands during image building |
| `COPY` | Copies files into the image |
| `ENV` | Sets environment variables |
| `EXPOSE` | Documents the container port |
| `CMD` | Specifies the default command when the container starts |

**Example Dockerfile:**

```dockerfile
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
```

**Build the image:**

```bash
docker build -t flask_app .
```

**Run the container:**

```bash
docker run -d --name flask_webapp -p 8080:5000 flask_app
```

---

## 9. Docker Compose Commands

**Check Docker Compose version:**

```bash
docker compose version
```

**Validate the Compose configuration:**

```bash
docker compose config
```

**Build and start services:**

```bash
docker compose up -d --build
```

**Start services:**

```bash
docker compose up -d
```

**List Compose services:**

```bash
docker compose ps
```

**View logs of all services:**

```bash
docker compose logs
```

**View logs of a particular service:**

```bash
docker compose logs web
docker compose logs db
```

**Follow logs:**

```bash
docker compose logs -f
```

**Stop services:**

```bash
docker compose stop
```

**Start existing stopped services:**

```bash
docker compose start
```

**Restart services:**

```bash
docker compose restart
```

**Stop and remove containers and the Compose network:**

```bash
docker compose down
```

**Stop and remove containers, network, and named volumes:**

```bash
docker compose down -v
```

> **Warning:** `docker compose down -v` deletes Compose-managed named volumes and their stored data. Use it only when you intend to remove that data.

### Using a Custom Compose Filename

If the Compose file has a different name, use the `-f` option.

**Start services:**

```bash
docker compose -f mycompose.yml up -d
```

**Check services:**

```bash
docker compose -f mycompose.yml ps
```

**View logs:**

```bash
docker compose -f mycompose.yml logs
```

**Stop and remove services:**

```bash
docker compose -f mycompose.yml down
```

---

## 10. Docker Cleanup Commands

**Remove stopped containers:**

```bash
docker container prune
```

**Remove unused images:**

```bash
docker image prune
```

**Remove unused volumes:**

```bash
docker volume prune
```

**Remove unused Docker resources:**

```bash
docker system prune
```

**Check Docker disk usage:**

```bash
docker system df
```

> **Warning:** Cleanup commands can remove resources you may want to keep. Review what is unused before cleaning up.

---

## Learning Objective

My objective is to understand Docker concepts through practical implementation, troubleshooting, and real-world DevOps scenarios.

More commands and hands-on projects will be added as I continue learning Docker.
