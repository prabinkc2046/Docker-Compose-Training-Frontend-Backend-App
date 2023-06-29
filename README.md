# Docker Compose Project: Frontend-Backend Application

This project is a simple frontend-backend application built using Docker Compose. It demonstrates the setup of a web application with a frontend service, a backend service, and a MySQL database.

## Prerequisites

- Docker
- Docker Compose

## Project Structure

- `docker-compose.yml`: Docker Compose configuration file defining the services and their dependencies.
- `backend/`: Directory containing the backend code.
- `frontend/`: Directory containing the frontend code.

## Usage

1. Clone the repository:

	```
	git clone <repository_url>
	```

2. Navigate to the project directory

```shell
cd <repository_name>```

3. Start the application

```shell
docker-compose up -d```

This command will build the necessary Docker images, create the required containers, and start the services.

1. Access the application

	- Frontend: Open your browser and visit http://localhost.
	- Backend: Make API requests to http://localhost:8000.

2. Stop the application
```shel
docker-compose down --volumes```

This will stop the running containers and remove the associated volumes.

## References

This project was created as part of my training after learning Docker Compose from Kokedloud. For more information and tutorials on Docker Compose, you can visit the Kokedloud website:[https://kodekloud.com/]

