from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from typing import Optional

router = APIRouter()

def generate_tracking_url(carrier: Optional[str], tracking_number: Optional[str]) -> Optional[str]:
    # 根据物流公司和运单号生成跟踪链接
    if carrier and tracking_number:
        if carrier.lower() == "example_express":
            return f"https://example-express.com/track?id={tracking_number}"
        # 添加其他物流公司的链接规则
    return None

@router.get("/orders/{order_number}/status", response_model=schemas.ShippingInfoResponse)
async def track_order(order_number: str, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.order_number == order_number).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if not order.shipping_info:
        return schemas.ShippingInfoResponse(order_number=order.order_number, order_status=order.order_status)
    tracking_url = generate_tracking_url(order.shipping_info.shipping_carrier, order.shipping_info.tracking_number)
    return schemas.ShippingInfoResponse(
        order_number=order.order_number,
        order_status=order.order_status,
        shipping_carrier=order.shipping_info.shipping_carrier,
        tracking_number=order.shipping_info.tracking_number,
        shipping_status=order.shipping_info.shipping_status,
        last_updated=order.shipping_info.last_updated,
        estimated_delivery=order.shipping_info.estimated_delivery,
        tracking_url=tracking_url
    )