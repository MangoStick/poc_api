import random
from fastapi import FastAPI, Request, Response
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=0)
app.max_request_size = 500 * 1024 * 1024  # 500 MB in bytes
app.max_response_size = 500 * 1024 * 1024  # 500 MB in bytes

def generate_random_numeric_json_records():
    records = []

    for _ in range(150000):
        record = {}
        for field_num in range(1, 50 + 1):
            field_name = f"field{field_num}"
            value = random.uniform(-1000, 1000) if random.choice([True, False]) else random.randint(-1000, 1000)
            record[field_name] = value
        records.append(record)

    return records


from app_2 import sql

@app.get("/")
def root(request: Request):
    # json_records = generate_random_numeric_json_records()

    # json_length = len(json_records)

    # print(f"JSON Length: {json_length} characters")

    json_records = sql()

    return JSONResponse(content=json_records)