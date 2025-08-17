from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import os
from dotenv import load_dotenv
import pandas as pd
import json

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Data Analyst Agent API",
    description="An API that uses LLMs to source, prepare, analyze, and visualize data",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class AnalysisRequest(BaseModel):
    data_source: str  # Can be a file path, URL, or raw data
    analysis_type: str
    parameters: Optional[Dict[str, Any]] = None

class VisualizationRequest(BaseModel):
    data: Any
    chart_type: str
    parameters: Optional[Dict[str, Any]] = None

# Routes
@app.get("/")
async def root():
    return {"message": "Welcome to Data Analyst Agent API"}

@app.post("/analyze")
async def analyze_data(request: AnalysisRequest):
    try:
        # This is a placeholder for the analysis logic
        # In a real implementation, you would process the data source
        # and perform the requested analysis
        return {
            "status": "success",
            "analysis_type": request.analysis_type,
            "results": "Analysis results will be returned here",
            "parameters": request.parameters
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/visualize")
async def create_visualization(request: VisualizationRequest):
    try:
        # This is a placeholder for the visualization logic
        return {
            "status": "success",
            "chart_type": request.chart_type,
            "parameters": request.parameters
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Read the file content
        contents = await file.read()
        
        # Process different file types
        if file.filename.endswith('.csv'):
            df = pd.read_csv(contents)
        elif file.filename.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(contents)
        elif file.filename.endswith('.json'):
            df = pd.read_json(contents)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file format")
        
        # Convert to JSON for response
        return {
            "status": "success",
            "filename": file.filename,
            "columns": df.columns.tolist(),
            "preview": df.head().to_dict(orient='records')
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
