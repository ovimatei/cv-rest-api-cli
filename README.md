# CV REST API and CLI

## A simple Flask app that presents CV information

### Requirements:
    - Docker
    - Docker Compose

### How to run:
```shell
docker-compose up -d
```
- visit [http://localhost:5001](http://localhost:5001)

### Endpoints:
    - GET /personal
    - GET /experience
    - GET /education

### CLI command:
```sh 
docker exec -it read_cv /bin/sh -c "cd /app && flask print_data"
```

