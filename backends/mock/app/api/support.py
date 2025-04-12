from fastapi import APIRouter
from backends.mock.app import schemas

router = APIRouter()

@router.post("/request_human_support", response_model=schemas.HumanSupportResponse)
async def request_human_support(request: schemas.HumanSupportRequest):
    # 在实际应用中，这里需要处理转接逻辑，例如：
    # - 将请求放入人工客服队列
    # - 返回在线客服系统的链接
    # - 触发通知给人工客服

    return schemas.HumanSupportResponse(message="正在为您转接人工客服，请稍候。", support_link="[您的在线客服链接]")