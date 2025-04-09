from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from datetime import datetime

router = APIRouter()

@router.get("/promotions", response_model=schemas.PromotionsResponse)
async def get_current_promotions(db: Session = Depends(get_db)):
    now = datetime.now()
    promotions = db.query(models.Promotion).filter(models.Promotion.start_date <= now, models.Promotion.end_date >= now).all()
    return schemas.PromotionsResponse(promotions=[schemas.PromotionInfo(**promo.__dict__) for promo in promotions])