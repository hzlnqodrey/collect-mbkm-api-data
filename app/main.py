import uvicorn
from typing import Union
from fastapi import FastAPI, Response, Request
from pydantic import BaseModel
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

from .helper import api_builder

app = FastAPI(debug=True)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

# Route
@app.get("/", status_code=200)
def status(response: Response):
    return api_builder.builder("hzlnqodrey - KampusmerdekaV4 Source Data API working!", response.status_code)

@app.get("/magang_data_api", status_code=200)
def status(response: Response):

    # Fetch Data
    data = pd.read_csv('./app/DATA/COMPACT/compact.csv')

    data = data.fillna('') # have to replace NaN values in the dataframe

    result = []

    for index, row in list(data.iterrows()):
        result.append(row)

    return api_builder.builder(result, response.status_code)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="800", reload=True)