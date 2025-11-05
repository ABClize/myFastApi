import math
from datetime import date
from typing import List

from fastapi import FastAPI
from fastapi.responses import PydanticJSONResponse
from fastapi.testclient import TestClient
from pydantic import BaseModel

from .utils import needs_pydanticv2

app = FastAPI(default_response_class=PydanticJSONResponse)


class Response(BaseModel):
    today: date
    numbers: List[float]


@app.get("/basic_response")
def get_basic_response() -> Response:
    return Response(
        today=date(2025, 11, 1),
        # pydantic converts inf/nan to None by default
        numbers=[3.14, math.inf, math.nan, 2.72],
    )


client = TestClient(app)


@needs_pydanticv2
def test_basic_response():
    with client:
        response = client.get("/basic_response")
    assert response.json() == {
        "today": "2025-11-01",
        "numbers": [3.14, None, None, 2.72],
    }
