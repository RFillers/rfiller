# FastAPI Backend

## Overview

This is a FastAPI backend project that uses:
- **Supabase** as the primary database.
- **OpenAI API** for embedding.
- **Qdrant** as a vector database.

Follow the steps below to set up your environment, install dependencies, and run the server.

---

## Prerequisites

- **Python**: Ensure you have Python 3.8 or later installed. You can check your version with:
  ```bash
  python --version

Virtual Environment: It’s recommended to use a virtual environment to manage dependencies.

# Project Setup

## 1. Set Up Environment Variables
Copy .env.example file in the project root and add the following environment variables:

```bash
  # Supabase Database
  DATABASE_URL=<your_supabase_url>
  SUPABASE_API_KEY=<your_supabase_key>

  # OpenAI API for embedding
  OPENAI_API_KEY=<your_openai_api_key>
```

Replace <your_supabase_url> and <your_supabase_key> with your actual Supabase project URL and API key.
Replace <your_openai_api_key> with your OpenAI API key.
Replace <your_qdrant_url> and <your_qdrant_api_key> with your Qdrant endpoint URL and API key, if required.

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