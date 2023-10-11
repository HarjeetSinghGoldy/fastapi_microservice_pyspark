# fastapi_microservice_pyspark
The simple structure and working dokcer containerized python fast api supporting pysparks

RUN
dokcer-compose up --build

Two api's will be availble on
GET - localhost:8000/data/health

POST - localhost:8000/data/process
body - {"data":"The text need for word count"}