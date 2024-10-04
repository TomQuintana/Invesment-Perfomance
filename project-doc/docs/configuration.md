# Configuration
This section describes the configuration for uses this project.

### Setup Database
- For create a Database I use a docker container with PostgreSQL, you can use the command below to create a container with the PostgreSQL image.
```bash
docker run --name <name> -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=<password> -e POSTGRES_DB=<db name> -p 5432:5432 -d postgres
```
- Then connect to the db using or any other tool you prefer, I use a TablePlus.
