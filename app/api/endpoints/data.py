# app/api/endpoints/data.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.errors import DataNotFoundError, handle_data_not_found_error, handle_internal_server_error
from app.data_processing.spark_processor import process_data


router = APIRouter()

class InputData(BaseModel):
    data: str

@router.post("/process")
async def process_data_endpoint(data: InputData):
    try:
        processed_data = process_data(data.data)
        return {"result": processed_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/health")
async def health_check():
    return {"status": "OK"}

@router.get("/data/{data_id}")
async def read_data(data_id: int):
    try:
        # Simulate data retrieval, but raise DataNotFoundError if not found
        if data_id == 1:
            return {"data_id": data_id, "value": "some data"}
        else:
            raise DataNotFoundError(data_id)
    except DataNotFoundError as e:
        return handle_data_not_found_error(e.data_id)
    except Exception as e:
        return handle_internal_server_error()

@router.get("/wordcount")
def wordcount(text: str):
    spark = SparkSession.builder.appName("WordCount").getOrCreate()
    words = text.split()
    word_count = spark.createDataFrame([(word,) for word in words], ["word"])
    result = word_count.groupBy("word").count().collect()
    spark.stop()
    return result




