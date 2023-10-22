from typing import Optional
from pydantic import BaseModel, Field

# 制御対象へ返すパラメータ
class ResponseBase(BaseModel):
    session_id: Optional[str] = Field(None, description="制御対象+タスクを一意に特定するSession ID", example="000000000000")
    counter: Optional[int] = Field(None, description="有限回の繰り返し処理を行う場合に使用するカウンタ", example=0)
    mode: Optional[int] = Field(None, description="モータの動作モード", example=0)
    stop_signal: Optional[int] = Field(None, description="", example=0)
    # モータAに対する指示パラメータ
    #a_plimit: Optional[float] = Field(None, description="", example=0.1, ge=0.0, le=1.0)
    #a_pwmv: Optional[float] = Field(None, description="", example=0, ge=-1, le=1)
    #a_pwmthresh: Optional[float] = Field(None, description="", example=0.1, ge=0.0, le=1.0)
    #a_minpwm: Optional[float] = Field(None, description="", example=0.1, ge=0.0, le=1.0)
    a_seconds: Optional[int] = Field(None, description="モータAに対する指示回転時間", example=0)
    #a_rotations: Optional[int] = Field(None, description="モータAに対する指示回転数", example=0)
    a_speed: Optional[int] = Field(None, description="モータAに対する指示速度", example=0)
    a_degrees: Optional[int] = Field(None, description="モータAに対する指示角度", example=0)
    a_blocking: Optional[int] = Field(None, description="モータAのブロッキング設定", example=0)
    # モータBに対する指示パラメータ
    #b_plimit: Optional[float] = Field(None, description="", example=0.1, ge=0.0, le=1.0)
    #b_pwmv: Optional[float] = Field(None, description="", example=0, ge=-1, le=1)
    #b_pwmthresh: Optional[float] = Field(None, description="", example=0.1, ge=0.0, le=1.0)
    #b_minpwm: Optional[float] = Field(None, description="", example=0.1, ge=0.0, le=1.0)
    b_seconds: Optional[int] = Field(None, description="モータBに対する指示回転時間", example=0)
    #b_rotations: Optional[int] = Field(None, description="モータBに対する指示回転数", example=0)
    b_speed: Optional[int] = Field(None, description="モータBに対する指示速度", example=0)
    b_degrees: Optional[int] = Field(None, description="モータBに対する指示角度", example=0)
    b_blocking: Optional[int] = Field(None, description="モータBのブロッキング設定", example=0)
    #
    direction: Optional[str] = Field(None, description="", example="shortest/clockwise/anticlockwise")
    delta: Optional[float] = Field(None, description="RTT", example=0)

class Response(ResponseBase):
    done: bool = Field(False, description="完了フラグ")