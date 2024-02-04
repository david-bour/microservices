import random
from fastapi import FastAPI
from pydantic import BaseModel

class CouponLength(BaseModel):
    length: int

app = FastAPI()

@app.post("/")
def random_generator(coupon_length: CouponLength):
    if not coupon_length:
        coupon_length.length = 6
    coupon = "".join([chr(random.randrange(33, 126)) for _ in range(coupon_length.length)])
    return {"result": coupon}

@app.get("/health")
def health():
    return {"result": "healthy"}

