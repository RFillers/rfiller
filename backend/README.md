# FastAPI Backend

## Overview

This is a FastAPI backend project that uses:
- **PostgreSQL** as the primary database.
- **OpenAI API** for embedding.
- **Qdrant** as a vector database.

Follow the steps below to set up your environment, install dependencies, and run the server.

---

## Prerequisites

- **Python**: Ensure you have Python 3.12 or later installed. You can check your version with:
  ```bash
  python --version

Virtual Environment: It’s recommended to use a virtual environment to manage dependencies.

# Project Setup

## 1. Set Up Environment Variables
Copy .env.example file in the project root and add the following environment variables:

```bash
  # OpenAI API for embedding
  OPENAI_API_KEY=<your_openai_api_key>
```

Replace <your_openai_api_key> with your OpenAI API key.

## 2. Install Dependencies
Create and activate a virtual environment, then install dependencies:

```bash
  # Create a virtual environment
  python -m venv venv

  # Activate the virtual environment
  # On Windows
  venv\Scripts\activate
  # On macOS/Linux
  source venv/bin/activate

  # Install dependencies
  pip install -r requirements.txt
```

## 3. Start the FastAPI Server
Run the FastAPI server locally with:

```bash
  uvicorn main:app --reload
```

## 4. Use the DB model

Upgrade the local DB from the migration files
```bash
  alembic upgrade head
```

Upgrade the migration files and the local DB from the migration files
```bash
  alembic revision --autogenerate -m "YOUR_COMMIT_MESSAGE"
  alembic upgrade head
```

## 5. Push the last docker image

```bash
  aws ecr get-login-password --region eu-west-3 | docker login --username AWS --password-stdin 767397667909.dkr.ecr.eu-west-3.amazonaws.com
  docker build -t rfiller:latest .
  docker tag rfiller:latest 767397667909.dkr.ecr.eu-west-3.amazonaws.com/rfiller:latest
  docker push 767397667909.dkr.ecr.eu-west-3.amazonaws.com/rfiller:latest
```
