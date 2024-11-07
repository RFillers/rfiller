# Variables
DOCKER_COMPOSE_FILE=docker-compose.yml

# Docker Compose commands
up:
	docker compose -f $(DOCKER_COMPOSE_FILE) up

down:
	docker compose -f $(DOCKER_COMPOSE_FILE) down

build:
	docker compose -f $(DOCKER_COMPOSE_FILE) build

restart: down up

# Build and then start all services
start: build up

# Stop all services without removing them
stop:
	docker compose -f $(DOCKER_COMPOSE_FILE) stop

# View logs for all services
logs:
	docker compose -f $(DOCKER_COMPOSE_FILE) logs -f

# Build and start the specific frontend service
build-front:
	docker compose -f $(DOCKER_COMPOSE_FILE) build front-end

# Start just the frontend service
up-front:
	docker compose -f $(DOCKER_COMPOSE_FILE) up -d front-end

# Build and start the analyser (FastAPI) service
build-analyser:
	docker compose -f $(DOCKER_COMPOSE_FILE) build analyser

# Start just the analyser (FastAPI) service
up-analyser:
	docker compose -f $(DOCKER_COMPOSE_FILE) up -d analyser

# Start just the Postgres service
up-postgres:
	docker compose -f $(DOCKER_COMPOSE_FILE) up -d postgres

# Rebuild and restart all containers
rebuild: down build up

# Clean dangling Docker images and stopped containers
clean:
	docker system prune -f
	docker compose -f $(DOCKER_COMPOSE_FILE) down -v

# Clean up everything, rebuild, and start services
clean-install: clean build up

# Stop a specific container (frontend, analyser, or postgres)
stop-front:
	docker compose -f $(DOCKER_COMPOSE_FILE) stop front-end

stop-analyser:
	docker compose -f $(DOCKER_COMPOSE_FILE) stop analyser

stop-postgres:
	docker compose -f $(DOCKER_COMPOSE_FILE) stop postgres

# Stop and remove containers, networks, and volumes
purge:
	docker compose -f $(DOCKER_COMPOSE_FILE) down --volumes --remove-orphans