import time
import asyncio
import hashlib
import datetime
import api.schemas.entity.observer.request as request_observer
import api.service.util.FileHandrer as util_file_handler

class Wave():
    NONE = -1
    RUN_FOR_DEGREES = 0
    RUN_FOR_ROTATIONS = 1
    RUN_FOR_SECONDS = 2
    RUN_TO_POSITION = 3

    #def __init__(self) -> None:
    #    # 初期化
    #    pass

    def calc(self, request: request_observer.Request, fileHandler: util_file_handler.fileHandler):
        print(request)
        session_id = request.session_id
        counter = request.counter
        mode = request.mode
        a_speed = request.a_speed
        a_position = request.a_position
        a_aposition = request.a_aposition
        delta_theta_a = request.delta_theta_a
        d_speed = request.d_speed
        d_position = request.d_position
        d_aposition = request.d_aposition
        delta_theta_d = request.delta_theta_d
        delta = request.delta
        line = []
        line.append(str(delta))
        line.append(str(a_speed))
        line.append(str(a_position))
        line.append(str(delta_theta_a))
        line.append(str(d_speed))
        line.append(str(d_position))
        line.append(str(delta_theta_d))
        if counter == 0:
            # ヘッダ行を追加
            fileHandler.appender(['delta', 'a_speed', 'a_position', 'delta_theta_a', 'd_speed', 'd_position', 'delta_theta_d'])
        fileHandler.appender(line)
        # mode 
        if mode == self.NONE:
            mode = self.RUN_TO_POSITION
        # セッションIDが未定義の場合
        if session_id == None or session_id == '0':
            now = datetime.datetime.now()
            date = now.strftime('%Y%m%d%H%M%S')
            session_id  = hashlib.md5(date.encode()).hexdigest()
        # 繰り返し回数を超過した場合、停止コードを送信
        if request.counter == 300:
            fileHandler.writer()
            stop_signal = 1
        else:
            stop_signal = 0
        # カウンタをインクリメント
        #counter = counter + 1
        return session_id,counter,mode,stop_signal,delta
