# Business Card Site

This is a Django-based web application designed to manage and showcase business card-related services. The project is designed to run in a Docker environment for easier setup and deployment.

## Features

- Manage business cards through the Django admin panel.
- Upload videos through the Django admin panel and display them on the website.
- Responsive design for easy access across devices.
- Database integration with PostgreSQL.
- Static and media file handling.

## Prerequisites

Before you start, make sure you have the following tools installed:

- Docker
- Docker Compose

## Getting Started

1. ### Clone the Repository

First, clone this repository to your local machine:

    git clone https://github.com/igor20192/business_card_site.git
    cd business-card-site


2. ### Create Environment Files

You need to create environment files for the web and database services.

***Create*** .env ***for the Django application:***

```bash
DEBUG=1
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your_db_password
DB_HOST=db
DB_PORT=5432
```
***Create*** .env.db ***for the PostgreSQL service:***

```bash
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_db_password
```

3. ### Build and Run the Docker Containers

To build and start the containers, run:

```bash
docker-compose up --build
```

This command will:

- Build the Docker image for your Django application.
- Start the PostgreSQL database.
- Run Django migrations and collect static files.
- Start the Django development server at http://localhost:8080.

4. ### Accessing the Application

Once the containers are running, you can access the application in your browser at:

```arduino
http://localhost:8080
```

To access the Django admin panel, append /admin to the URL.

5. ### Running Management Commands

You can run Django management commands inside the Docker container using `docker-compose exec`. For example:

```bash
docker-compose exec web python manage.py createsuperuser
```

6. ### Static and Media Files

Static and media files are mounted as volumes in the Docker container:

- Static files are stored in the `./staticfiles/` directory.
- Media uploads are stored in the `./media/` directory.

These directories are automatically synchronized between the local machine and the container.

7. ### Stopping the Application

To stop the containers, press `Ctrl+C` or run:

```bash
docker-compose down
```

This will stop and remove the containers, but the data in the database will be preserved in the `postgres_data` volume.

8. ### Running in Production

If you're running this application in production, remember to:

- Set `DEBUG=0` in the `.env` file.
- Use a strong, unique `SECRET_KEY`.
- Properly configure the `ALLOWED_HOSTS` setting with your production domain.

## Docker Configuration Details

```dockerfile
# Base image
FROM python:3.12-bullseye

# Set working directory
WORKDIR /usr/src/business_card_site

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt .
RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev pkg-config curl gettext && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove -y gcc pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .
```

### 
Here's a detailed README.md for your project, which includes instructions for setting up and running the project using Docker:

Business Card Site
This is a Django-based web application designed to manage and showcase business card-related services. The project is designed to run in a Docker environment for easier setup and deployment.

Features
Manage business cards through the Django admin panel.
Upload videos through the Django admin panel and display them on the website.
Responsive design for easy access across devices.
Database integration with PostgreSQL.
Static and media file handling.
Prerequisites
Before you start, make sure you have the following tools installed:

Docker
Docker Compose
Getting Started
1. Clone the Repository
First, clone this repository to your local machine:

bash
Копировать код
git clone https://github.com/your-username/business-card-site.git
cd business-card-site
2. Create Environment Files
You need to create environment files for the web and database services.

Create .env for the Django application:
bash
Копировать код
DEBUG=1
SECRET_KEY=your_secret_key
ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your_db_password
DB_HOST=db
DB_PORT=5432
Create .env.db for the PostgreSQL service:
bash
Копировать код
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_db_password
3. Build and Run the Docker Containers
To build and start the containers, run:

bash
Копировать код
docker-compose up --build
This command will:

Build the Docker image for your Django application.
Start the PostgreSQL database.
Run Django migrations and collect static files.
Start the Django development server at http://localhost:8080.
4. Accessing the Application
Once the containers are running, you can access the application in your browser at:

arduino
Копировать код
http://localhost:8080
To access the Django admin panel, append /admin to the URL.

5. Running Management Commands
You can run Django management commands inside the Docker container using docker-compose exec. For example:

bash
Копировать код
docker-compose exec web python manage.py createsuperuser
6. Static and Media Files
Static and media files are mounted as volumes in the Docker container:

Static files are stored in the ./staticfiles/ directory.
Media uploads are stored in the ./media/ directory.
These directories are automatically synchronized between the local machine and the container.

7. Stopping the Application
To stop the containers, press Ctrl+C or run:

bash
Копировать код
docker-compose down
This will stop and remove the containers, but the data in the database will be preserved in the postgres_data volume.

8. Running in Production
If you're running this application in production, remember to:

Set DEBUG=0 in the .env file.
Use a strong, unique SECRET_KEY.
Properly configure the ALLOWED_HOSTS setting with your production domain.
Docker Configuration Details
Dockerfile
This project uses a multi-stage Dockerfile:

### dockerfile

```dockerfile

# Base image
FROM python:3.12-bullseye

# Set working directory
WORKDIR /usr/src/business_card_site

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt .
RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev pkg-config curl gettext && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove -y gcc pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .
```

### Docker Compose Configuration

The `docker-compose.yml` file defines two services: `web` and `db` (PostgreSQL):

```yml
services:
  web:
    build: .
    command: >
      bash -c "python manage.py makemigrations &&
              python manage.py migrate &&
              python manage.py collectstatic --noinput &&
              python manage.py runserver 0.0.0.0:8080"
    restart: always
    volumes:
      - ./media/:/usr/src/business_card_site/media/
      - ./staticfiles/:/usr/src/business_card_site/staticfiles/
    ports:
      - 8080:8080
    env_file:
      - ./.env
    depends_on:
      - db

  db:
    image: postgres:15-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    env_file:
      - .env.db
    ports:
      - 5432:5432

volumes:
  postgres_data:
```

## Useful Commands

- ***Start containers:*** `docker-compose up`
- ***Stop containers:*** `docker-compose down`
- ***Run Django management commands:*** `docker-compose exec web python manage.py` `<command>`
- ***Rebuild images:*** `docker-compose up --build`

## License

This project is licensed under the MIT License - see the LICENSE file for details.







