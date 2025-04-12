from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backends.mock.app.database import get_db
from backends.mock.app import models, schemas

router = APIRouter()

@router.post("/returns_exchanges", response_model=schemas.ReturnExchangeResponse)
async def create_return_exchange(request: schemas.ReturnExchangeRequest, db: Session = Depends(get_db)):
    order_item = db.query(models.OrderItem).filter(models.OrderItem.id == request.order_item_id).first()
    if not order_item:
        raise HTTPException(status_code=404, detail="Order item not found")

    # 在这里可以添加更复杂的退换货政策校验逻辑
    # 例如：检查是否在退换货期限内，商品状态是否符合要求

    db_return_exchange = models.ReturnsExchange(
        order_item_id=request.order_item_id,
        reason=request.reason,
        request_type=request.request_type
    )
    db.add(db_return_exchange)
    db.commit()
    db.refresh(db_return_exchange)
    return schemas.ReturnExchangeResponse(message="退换货申请已提交", return_exchange_id=db_return_exchange.id)