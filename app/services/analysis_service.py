from typing import Dict, Any, Optional
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
import io
import base64

class AnalysisService:
    def __init__(self, openai_api_key: str):
        self.openai_api_key = openai_api_key

    async def analyze_data(self, data: Any, analysis_type: str, parameters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Perform analysis on the provided data
        
        Args:
            data: Input data (can be a file path, URL, or raw data)
            analysis_type: Type of analysis to perform
            parameters: Additional parameters for the analysis
            
        Returns:
            Dict containing analysis results
        """
        try:
            # Convert data to DataFrame if it's not already
            df = self._prepare_data(data)
            
            # Perform the requested analysis
            if analysis_type == "descriptive_stats":
                return self._descriptive_statistics(df, parameters)
            elif analysis_type == "correlation":
                return self._correlation_analysis(df, parameters)
            elif analysis_type == "time_series":
                return self._time_series_analysis(df, parameters)
            else:
                return {"error": f"Unsupported analysis type: {analysis_type}"}
                
        except Exception as e:
            return {"error": str(e)}

    def _prepare_data(self, data: Any) -> pd.DataFrame:
        """Convert input data to pandas DataFrame"""
        if isinstance(data, str):
            if data.endswith('.csv'):
                return pd.read_csv(data)
            elif data.endswith(('.xls', '.xlsx')):
                return pd.read_excel(data)
            elif data.endswith('.json'):
                return pd.read_json(data)
            else:
                # Assume it's a JSON string
                return pd.read_json(io.StringIO(data))
        elif isinstance(data, dict):
            return pd.DataFrame(data)
        elif isinstance(data, pd.DataFrame):
            return data
        else:
            raise ValueError("Unsupported data format")

    def _descriptive_statistics(self, df: pd.DataFrame, parameters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Calculate descriptive statistics for the data"""
        if parameters and 'columns' in parameters:
            df = df[parameters['columns']]
            
        return {
            "statistics": df.describe().to_dict(),
            "info": {
                "total_rows": len(df),
                "columns": list(df.columns),
                "missing_values": df.isnull().sum().to_dict()
            }
        }

    def _correlation_analysis(self, df: pd.DataFrame, parameters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Perform correlation analysis"""
        # Select only numeric columns for correlation
        numeric_df = df.select_dtypes(include=['number'])
        
        if len(numeric_df.columns) < 2:
            return {"error": "Not enough numeric columns for correlation analysis"}
            
        return {
            "correlation_matrix": numeric_df.corr().to_dict(),
            "columns": list(numeric_df.columns)
        }

    def _time_series_analysis(self, df: pd.DataFrame, parameters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Perform time series analysis"""
        # This is a placeholder - in a real implementation, you would add time series analysis logic
        return {
            "message": "Time series analysis results will be returned here",
            "parameters": parameters
        }

    def create_visualization(self, data: Any, chart_type: str, parameters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Create a visualization from the data
        
        Args:
            data: Input data
            chart_type: Type of chart to create
            parameters: Additional parameters for the visualization
            
        Returns:
            Dict containing the visualization data or path to the saved image
        """
        try:
            df = self._prepare_data(data)
            
            if chart_type == "scatter":
                fig = px.scatter(
                    df,
                    x=parameters.get('x'),
                    y=parameters.get('y'),
                    color=parameters.get('color'),
                    title=parameters.get('title', 'Scatter Plot')
                )
            elif chart_type == "bar":
                fig = px.bar(
                    df,
                    x=parameters.get('x'),
                    y=parameters.get('y'),
                    color=parameters.get('color'),
                    title=parameters.get('title', 'Bar Chart')
                )
            elif chart_type == "line":
                fig = px.line(
                    df,
                    x=parameters.get('x'),
                    y=parameters.get('y'),
                    color=parameters.get('color'),
                    title=parameters.get('title', 'Line Chart')
                )
            elif chart_type == "histogram":
                fig = px.histogram(
                    df,
                    x=parameters.get('x'),
                    nbins=parameters.get('nbins', 30),
                    title=parameters.get('title', 'Histogram')
                )
            else:
                return {"error": f"Unsupported chart type: {chart_type}"}
            
            # Convert the figure to a JSON-serializable format
            fig_json = fig.to_dict()
            
            # Generate HTML for embedding
            html = fig.to_html(full_html=False, include_plotlyjs='cdn')
            
            return {
                "chart_type": chart_type,
                "figure": fig_json,
                "html": html
            }
            
        except Exception as e:
            return {"error": str(e)}
