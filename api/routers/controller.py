from fastapi import APIRouter, HTTPException
from typing import List

import api.schemas.entity.observer.request as request_observer
import api.schemas.entity.observer.response as response_observer
import api.service.parameter_identification.motor.wave as wave_motor

router = APIRouter()


#waveMotor = wave_motor()

@router.post("/controller/observer/send/", response_model=List[response_observer.Response])
async def set_pwm_value_mortors(request: request_observer.Request):
    #global waveMotor
    session_id,counter,mode,stop_signal = wave_motor.Wave(request)
    return [request_observer.Request(session_id=session_id, counter=counter, mode=mode, stop_signal=stop_signal)]
