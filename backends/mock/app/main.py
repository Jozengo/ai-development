import uvicorn
from fastapi import FastAPI
from api import products, promotions, orders, returns, feedback, support
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(products.router)
app.include_router(promotions.router)
app.include_router(orders.router)
app.include_router(returns.router)
app.include_router(feedback.router)
app.include_router(support.router)

if __name__ == '__main__':
    # uvicorn app.main:app --reload
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
