from fastapi import APIRouter, HTTPException
from typing import List

import api.schemas.entity.observer.request as request_observer
import api.schemas.entity.observer.response as response_observer
import api.service.parameter_identification.motor.wave as wave_motor

router = APIRouter()


#waveMotor = wave_motor()

@router.post("/controller/observer/send/", response_model=List[response_observer.Response])
async def observer(request: request_observer.Request):
    print(type(request))
    wave = wave_motor.Wave()
    session_id,counter,mode,stop_signal = wave.calc(request)
    return [response_observer.Response(session_id=session_id, counter=counter, mode=mode, stop_signal=stop_signal)]
    #return [response_observer.Response(session_id=str(00000000), counter=1, mode=1, stop_signal=1)]
