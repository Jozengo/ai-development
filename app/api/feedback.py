from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter()

@router.post("/feedback", response_model=schemas.FeedbackResponse)
async def submit_feedback(request: schemas.FeedbackRequest, db: Session = Depends(get_db)):
    db_inquiry = models.Inquiry(
        channel=request.channel,
        user_identifier=request.user_identifier,
        inquiry_text=request.feedback_text
    )
    db.add(db_inquiry)
    db.commit()
    db.refresh(db_inquiry)
    return schemas.FeedbackResponse(message="您的反馈已收到，我们会认真处理。")