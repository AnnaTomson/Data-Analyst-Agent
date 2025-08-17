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
4. Create a `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Running the API

```
uvicorn app.main:app --reload
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
