# Docker Compose Project: Frontend-Backend Application

This project is a simple frontend-backend application built using Docker Compose. It serves as a practical implementation of the concepts learned during my Docker Compose training, showcasing my understanding of containerized application development.

# Project Overview

The application consists of the following components:

	- Frontend: An Nginx web server serving static files for the frontend interface.
	- Backend: A Flask-based backend server that communicates with the database and provides data to the frontend.
	- Database: A MySQL database container to store and retrieve data.

The project demonstrates how to orchestrate these components using Docker Compose, enabling easy deployment and management of the entire application stack.

## Project Structure

The project structure is as follows:

```
docker-compose/
├── backend
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── database
│   └── init.sql
├── docker-compose.yaml
├── frontend
│   ├── index.html
│   └── script.js
└── README.md
```
1.  The backend directory contains the Flask application code (app.py), a Dockerfile for building the backend image, and a requirements.txt file listing the necessary dependencies.
2.  The frontend directory contains the HTML (index.html) and JavaScript (script.js) files for the frontend interface.
3.  The database directory includes the init.sql script to initialize the MySQL database with the necessary table.
4.  The docker-compose.yml file defines the services, their configurations, and the network setup for the application.

## Prerequisites

- Docker
- Docker Compose

## Usage

1. Clone the repository:

	```
	git clone <repository_url>
	```

2. Navigate to the project directory

	```
	cd <repository_name>
	```

3. Start the application

	```
	docker-compose up -d
	```

This command will build the necessary Docker images, create the required
 containers, and start the services.

1. Access the application

	- Frontend: Open your browser and visit http://localhost.
	- Backend: Make API requests to http://localhost:8000.

2. Stop the application

	```s
	docker-compose down --volumes
	```

This will stop the running containers and remove the associated volumes.

## Conclusion

This project showcases my practical knowledge and understanding of Docker Compose for building and managing a frontend-backend application. It demonstrates my passion for learning and applying containerization concepts in real-world scenarios. Feel free to modify.

If you have any questions or suggestions for improvements, feel free to reach out. Happy coding!

