from datetime import datetime
from enum import Enum
from typing import List, Optional

from fastapi import FastAPI, status, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationError
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Trading App"
)


# info about error instead "Internal Server Error"
@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


fake_user = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
    {"id": 4, "role": "trader", "name": "Matt", "degree": [
        {"id": 1, "create_at": "2020-01-05T00:00:00", "type_degree": "expert"}
    ]},
]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 2, "currency": "BTC", "side": "sell", "price": 456, "amount": 2.12}
]


class DegreeType(Enum):
    newbie = "newbie"
    expert = "expert"


class Degree(BaseModel):
    id: int
    create_at: datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = []


@app.get("/user/{user_id}", response_model=List[User])
async def get_user(user_id: int):
    return [user for user in fake_user if user.get("id") == user_id]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    amount: float


@app.post("/trade")
async def add_trades(trade: List[Trade]):
    fake_trades.extend(trade)
    return {"status": 200, "data": fake_trades}