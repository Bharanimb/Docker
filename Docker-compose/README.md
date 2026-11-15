
## Hands-on Projects

### Project 1: Flask Application using Docker

**Topics Covered:**

- Dockerfile creation
- Building custom Docker images
- Running containers
- Port mapping
- Docker logs
- Environment setup using Python virtual environments
- Bind mounts

### Project 2: Flask + PostgreSQL using Docker Compose

**Topics Covered:**

- Multiple containers using Docker Compose
- Flask and PostgreSQL integration
- Environment variables
- Container-to-container communication
- PostgreSQL database and table creation
- Docker bind mounts
- Docker named volumes
- PostgreSQL data persistence
- Container recreation and volume verification
- Docker Compose commands (`up`, `down`, `stop`, `start`, `restart`)

### PostgreSQL Commands Used

**1. Connect to the PostgreSQL container**

```bash
docker exec -it postgres_db bash
```

**2. Connect to the database**

```bash
psql -U username -d employee_db
```

**3. List databases**

```sql
\l
```

**4. List tables**

```sql
\dt
```

**5. Create a table**

```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    role VARCHAR(100)
);
```

**6. Exit PostgreSQL**

```sql
\q
```

---

## Learning Objective

My objective is to understand Docker concepts through practical implementation, troubleshooting, and real-world DevOps scenarios.

