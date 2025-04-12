from typing import List, Optional, Dict, Any
from pydantic import BaseModel


class TextMemoryAddRequest(BaseModel):
    """添加文本到记忆体的请求模型"""
    text: str  # 要添加的文本内容
    user_id: Optional[str] = None  # 用户ID，如果提供则添加到用户私有记忆体
    is_public: bool = False  # 是否添加到公共记忆体
    metadata: Optional[Dict[str, Any]] = None  # 可选的元数据


class MemoryQueryRequest(BaseModel):
    """查询记忆体的请求模型"""
    query: str  # 查询文本
    user_id: Optional[str] = None  # 用户ID，如果提供则查询用户私有记忆体
    is_public: bool = False  # 是否查询公共记忆体
    limit: int = 5  # 返回结果数量限制


class MemoryQueryResponse(BaseModel):
    """记忆体查询响应模型"""
    results: List[Dict[str, Any]]  # 查询结果列表


class FileUploadResponse(BaseModel):
    """文件上传响应模型"""
    filename: str  # 文件名
    size: int  # 文件大小（字符数）
    content_preview: str  # 内容预览
    added_to_public: bool  # 是否添加到公共记忆体
    added_to_user: bool  # 是否添加到用户私有记忆体
    user_id: Optional[str] = None  # 用户ID