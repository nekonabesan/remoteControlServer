import time
import hashlib
import datetime
#import numpy as np
import api.schemas.entity.observer.request as request_observer

class Wave():
    NONE = -1
    RUN_FOR_DEGREES = 0
    RUN_FOR_ROTATIONS = 1
    RUN_FOR_SECONDS = 2
    RUN_TO_POSITION = 3

    #def __init__(self) -> None:
    #    # 初期化
    #    pass

    def calc(self, request: request_observer.Request):
        print(request)
        session_id = request.session_id
        counter = request.counter
        mode = request.mode
        degrees = request.degrees
        speed = request.speed
        delta = request.delta
        print(str(delta) + "\t" + str(degrees) + "\t" + str(speed))
        # mode 
        if mode == self.NONE:
            mode = self.RUN_TO_POSITION
        # セッションIDが未定義の場合
        if session_id == None or session_id == '0':
            now = datetime.datetime.now()
            date = now.strftime('%Y%m%d%H%M%S')
            session_id  = hashlib.md5(date.encode()).hexdigest()
        # 繰り返し回数を超過した場合、停止コードを送信
        if request.counter == 10:
            stop_signal = 1
        else:
            stop_signal = 0
        # カウンタをインクリメント
        counter = counter + 1
        # delta
        return session_id,counter,mode,stop_signal,delta
