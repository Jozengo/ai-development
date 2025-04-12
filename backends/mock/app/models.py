from sqlalchemy import Column, Integer, String, Numeric, DateTime, TEXT, JSON, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# 产品表
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    model = Column(String(100))
    description = Column(TEXT)
    specifications = Column(JSON)
    material = Column(String(100))
    size_guide = Column(TEXT)
    price = Column(Numeric(10, 2), nullable=False)
    stock_quantity = Column(Integer, nullable=False, default=0)
    image_url = Column(String(255))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)

# 促销活动表
class Promotion(Base):
    __tablename__ = "promotions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(TEXT)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    discount_type = Column(String(50))
    discount_value = Column(Numeric(10, 2))
    min_order_amount = Column(Numeric(10, 2))
    coupon_code = Column(String(50), unique=True)
    usage_limit = Column(Integer)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)

# 订单表
class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    order_number = Column(String(100), unique=True, nullable=False)
    user_id = Column(Integer)  # 可以关联用户表（如果需要用户系统）
    order_date = Column(DateTime, default=datetime.now())
    total_amount = Column(Numeric(10, 2), nullable=False)
    order_status = Column(String(50))
    shipping_address = Column(JSON)
    billing_address = Column(JSON)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)
    shipping_info = relationship("ShippingInfo", back_populates="order", uselist=False)
    order_items = relationship("OrderItem", back_populates="order")

# 订单项表
class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id")) # 暂时删除 ondelete
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)
    order = relationship("Order", back_populates="order_items")
    returns_exchange = relationship("ReturnsExchange", back_populates="order_item")

# 物流信息表
class ShippingInfo(Base):
    __tablename__ = "shipping_info"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), unique=True)
    shipping_carrier = Column(String(100))
    tracking_number = Column(String(100))
    shipping_status = Column(String(100))
    last_updated = Column(DateTime)
    estimated_delivery = Column(DateTime)
    order = relationship("Order", back_populates="shipping_info")

# 退换货申请表
class ReturnsExchange(Base):
    __tablename__ = "returns_exchanges"
    id = Column(Integer, primary_key=True, index=True)
    order_item_id = Column(Integer, ForeignKey("order_items.id")) # 暂时删除 ondelete
    reason = Column(TEXT, nullable=False)
    request_type = Column(String(50))
    status = Column(String(50), default='pending')
    application_date = Column(DateTime, default=datetime.now())
    processed_date = Column(DateTime)
    comments = Column(TEXT)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)
    order_item = relationship("OrderItem", back_populates="returns_exchange")

# 咨询记录表 (用于记录用户的咨询内容，可选，如果需要更精细的分析)
class Inquiry(Base):
    __tablename__ = "inquiries"
    id = Column(Integer, primary_key=True, index=True)
    channel = Column(String(50))
    user_identifier = Column(String(255))
    product_id = Column(Integer, ForeignKey("products.id"))
    inquiry_text = Column(TEXT, nullable=False)
    response_text = Column(TEXT)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)

# 知识库表 (用于存储产品信息、常见问题等)
class KnowledgeBase(Base):
    __tablename__ = "knowledge_base"
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(100), nullable=False)
    question = Column(TEXT, nullable=False)
    answer = Column(TEXT, nullable=False)
    keywords = Column(TEXT)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)