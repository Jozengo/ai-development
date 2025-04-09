from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from typing import Optional

router = APIRouter()

@router.get("/products/{product_identifier}", response_model=schemas.ProductDetailsResponse)
async def get_product_details(product_identifier: str, db: Session = Depends(get_db), query_type: str = Query(default="name", enum=["name", "model", "id"]), user_needs: Optional[str] = None):
    if query_type == "id":
        product = db.query(models.Product).filter(models.Product.id == product_identifier).first()
    elif query_type == "name":
        product = db.query(models.Product).filter(models.Product.name.ilike(f"%{product_identifier}%")).first()
    elif query_type == "model":
        product = db.query(models.Product).filter(models.Product.model == product_identifier).first()
    else:
        raise HTTPException(status_code=400, detail="Invalid query_type")

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    recommendations = []
    if user_needs:
        # 这里需要实现更复杂的推荐逻辑，例如基于产品知识库、用户偏好等
        # 这里仅为示例，随机推荐两款其他产品
        other_products = db.query(models.Product).filter(models.Product.id != product.id).limit(2).all()
        for p in other_products:
            recommendations.append(
                schemas.ProductRecommendation(id=p.id, name=p.name, price=float(p.price), image_url=p.image_url, reason=f"根据您的需求 '{user_needs}' 推荐"))

    return schemas.ProductDetailsResponse(product=schemas.ProductInfo(**product.__dict__), recommendations=recommendations if user_needs else None)