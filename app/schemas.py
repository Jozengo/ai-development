from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import datetime

class ProductInfo(BaseModel):
    id: int
    name: str
    model: Optional[str]
    description: Optional[str]
    specifications: Optional[Dict]
    material: Optional[str]
    size_guide: Optional[str]
    price: float
    stock_quantity: int
    image_url: Optional[str]

class ProductRecommendation(BaseModel):
    id: int
    name: str
    price: float
    image_url: Optional[str]
    reason: str # 推荐理由

class ProductDetailsResponse(BaseModel):
    product: Optional[ProductInfo]
    recommendations: Optional[List[ProductRecommendation]]

class PromotionInfo(BaseModel):
    id: int
    name: str
    description: Optional[str]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    discount_type: Optional[str]
    discount_value: Optional[float]
    min_order_amount: Optional[float]
    coupon_code: Optional[str]
    usage_limit: Optional[int]

class PromotionsResponse(BaseModel):
    promotions: List[PromotionInfo]

class ShippingInfoResponse(BaseModel):
    order_number: str
    order_status: str
    shipping_carrier: Optional[str]
    tracking_number: Optional[str]
    shipping_status: Optional[str]
    last_updated: Optional[datetime]
    estimated_delivery: Optional[datetime]
    tracking_url: Optional[str] # 可以根据物流公司和运单号生成

class ReturnExchangeRequest(BaseModel):
    order_item_id: int
    reason: str
    request_type: str  # 'return' 或 'exchange'

class ReturnExchangeResponse(BaseModel):
    message: str
    return_exchange_id: Optional[int]

class FeedbackRequest(BaseModel):
    channel: str  # 例如：chat, email
    user_identifier: Optional[str]
    feedback_text: str

class FeedbackResponse(BaseModel):
    message: str

class HumanSupportRequest(BaseModel):
    channel: str
    user_identifier: Optional[str]
    reason: Optional[str]

class HumanSupportResponse(BaseModel):
    message: str
    support_link: Optional[str]  # 如果有在线客服链接