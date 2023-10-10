from typing import Optional
from pydantic import BaseModel, Field

# 制御対象から受け取るパラメータ
class Request(BaseModel):
    session_id: Optional[str] = Field(None, description="制御対象+タスクを一意に特定するSession ID", example="000000000000")
    counter: Optional[int] = Field(None, description="有限回の繰り返し処理を行う場合に使用するカウンタ", example=0)
    mode: Optional[int] = Field(None, description="", example=0)
    speed: Optional[int] = Field(None, description="", example=0)
    degrees: Optional[int] = Field(None, description="", example=0)
    delta: Optional[float] = Field(None, description="", example=0)