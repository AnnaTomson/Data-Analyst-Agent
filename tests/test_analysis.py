import os
import sys
import pytest
import pandas as pd

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.analysis_service import AnalysisService

@pytest.fixture
def analysis_service():
    return AnalysisService(openai_api_key="test_key")

import pytest

@pytest.mark.asyncio
async def test_descriptive_statistics(analysis_service):
    # Create test data
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)
    
    # Test analysis
    result = await analysis_service.analyze_data(df, "descriptive_stats")
    
    # Assert results
    assert 'statistics' in result
    assert 'info' in result
    assert result['info']['total_rows'] == 5
    assert 'A' in result['statistics']
    assert 'B' in result['statistics']

def test_visualization(analysis_service):
    # Create test data
    data = {
        'x': [1, 2, 3, 4, 5],
        'y': [5, 4, 3, 2, 1]
    }
    
    # Test visualization
    result = analysis_service.create_visualization(
        data,
        "scatter",
        {"x": "x", "y": "y", "title": "Test Scatter Plot"}
    )
    
    # Assert results
    assert 'figure' in result
    assert 'html' in result
    assert result['chart_type'] == "scatter"
