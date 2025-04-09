from fastapi import FastAPI
from .api import products, promotions, orders, returns, feedback, support
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(products.router)
app.include_router(promotions.router)
app.include_router(orders.router)
app.include_router(returns.router)
app.include_router(feedback.router)
app.include_router(support.router)

# uvicorn app.main:app --reload
