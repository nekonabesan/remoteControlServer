from typing import Optional
from pydantic import BaseModel, Field

# 制御対象へ返すパラメータ
class ResponseBase(BaseModel):
    session_id: Optional[str] = Field(None, description="制御対象+タスクを一意に特定するSession ID", example="000000000000")
    counter: Optional[int] = Field(None, description="有限回の繰り返し処理を行う場合に使用するカウンタ", example=0)
    mode: Optional[int] = Field(None, description="モータの動作モード", example=0)
    stop_signal: Optional[int] = Field(None, description="", example=0)
    plimit: Optional[float] = Field(None, description="", example=0.1, ge=0.0, le=1.0)
    pwmv: Optional[float] = Field(None, description="", example=0, ge=-1, le=1)
    pwmthresh: Optional[float] = Field(None, description="", example=0.1, ge=0.0, le=1.0)
    minpwm: Optional[float] = Field(None, description="", example=0.1, ge=0.0, le=1.0)
    seconds: Optional[int] = Field(None, description="", example=0)
    rotations: Optional[int] = Field(None, description="", example=0)
    speed: Optional[int] = Field(None, description="", example=0)
    degrees: Optional[int] = Field(None, description="", example=0)
    blocking: Optional[int] = Field(None, description="", example=0)
    direction: Optional[str] = Field(None, description="", example="shortest/clockwise/anticlockwise")
    delta: Optional[float] = Field(None, description="", example=0)

class Response(ResponseBase):
    done: bool = Field(False, description="完了フラグ")