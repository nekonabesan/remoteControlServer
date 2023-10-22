from fastapi import APIRouter, HTTPException
from typing import List

import api.schemas.entity.observer.request as request_observer
import api.schemas.entity.observer.response as response_observer
import api.schemas.entity.physical.request as request_physical
import api.schemas.entity.physical.response as response_physical
import api.service.parameter_identification.motor.wave as wave_motor
import api.service.parameter_identification.sensor.parameter as parameter_sensor
import api.service.util.FileHandrer as util_file_handler

router = APIRouter()
fileHandler = util_file_handler.fileHandler()

@router.post("/controller/observer/send/", response_model=List[response_observer.Response])
async def observer(request: request_observer.Request):
    print(type(request))
    global fileHandler
    if fileHandler.data == None:
        fileHandler = util_file_handler.fileHandler()
    wave = wave_motor.Wave()
    session_id,counter,mode,stop_signal,delta = wave.calc(request, fileHandler)
    return [response_observer.Response(session_id=session_id, counter=counter, mode=mode, stop_signal=stop_signal, delta=delta)]

@router.post("/controller/observer/physical/", response_model=List[response_physical.Response])
async def observer(request: request_physical.Request):
    print(type(request))
    global fileHandler
    if fileHandler.data == None:
        fileHandler = util_file_handler.fileHandler()
    degrees = parameter_sensor.Parameter()
    session_id,counter,stop_signal,delta = degrees.degrees(request, fileHandler)
    return [response_physical.Response(session_id=session_id, counter=counter, stop_signal=stop_signal, delta=delta)]
