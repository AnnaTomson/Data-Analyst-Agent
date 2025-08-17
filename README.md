# Data Analyst Agent API

A FastAPI-based API that uses LLMs to source, prepare, analyze, and visualize data.

## Features

- Upload and process various data formats (CSV, Excel, JSON)
- Perform data analysis using LLMs
- Generate visualizations
- RESTful API endpoints for easy integration

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add your environment variables:
   ```
   OPENAI_API_KEY=your_api_key_here
   ENVIRONMENT=production
   ```

## Running the API

### Development
```bash
uvicorn app.main:app --reload
```

### Production
```bash
gunicorn -c gunicorn_conf.py app.main:app
```

## Deployment

### Option 1: Heroku

1. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Login:
   ```bash
   heroku login
   ```
3. Create a new Heroku app:
   ```bash
   heroku create your-app-name
   ```
4. Set environment variables:
   ```bash
   heroku config:set OPENAI_API_KEY=your_api_key_here
   heroku config:set ENVIRONMENT=production
   ```
5. Deploy:
   ```bash
   git push heroku main
   ```

### Option 2: Docker

1. Build the image:
   ```bash
   docker build -t data-analyst-agent .
   ```
2. Run the container:
   ```bash
   docker run -d --name analyst-agent -p 8000:8000 --env-file .env data-analyst-agent
   ```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, visit:
- Interactive API docs: `http://localhost:8000/docs`
- Alternative API docs: `http://localhost:8000/redoc`

## Endpoints

- `POST /analyze`: Perform data analysis
- `POST /visualize`: Generate visualizations
- `POST /upload`: Upload data files

## Example Usage

### Upload a file
```bash
curl -X 'POST' \
  'http://localhost:8000/upload' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@your_data.csv;type=text/csv'
```

### Analyze data
```bash
curl -X 'POST' \
  'http://localhost:8000/analyze' \
  -H 'Content-Type: application/json' \
  -d '{
    "data_source": "path/to/your/data.csv",
    "analysis_type": "descriptive_statistics",
    "parameters": {"column": "price"}
  }'
```
