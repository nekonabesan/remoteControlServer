import time
import asyncio
import hashlib
import datetime
import api.schemas.entity.physical.request as request_physical
import api.service.util.FileHandrer as util_file_handler

class Parameter:
    def degrees(self, request: request_physical.Request, fileHandler: util_file_handler.fileHandler):
        print(request)
        delta = request.delta
        counter = request.counter
        session_id = request.session_id
        line = []
        line.append(str(delta))
        line.append(str(request.Rx_acc))
        line.append(str(request.Rx_velocity))
        line.append(str(request.Rx_degrees))
        line.append(str(request.Ry_acc))
        line.append(str(request.Ry_velocity))
        line.append(str(request.Ry_degrees))
        line.append(str(request.Rz_acc))
        line.append(str(request.Rz_velocity))
        line.append(str(request.Rz_degrees))
        if counter == 0:
            # ヘッダ行を追加
            fileHandler.appender(['delta', 'Rx_acc', 'Rx_velocity', 'Rx_degrees', 'Ry_acc', 'Ry_velocity', 'Rr_degrees', 'Rz_acc', 'Rz_velocity', 'Rz_degrees'])
        fileHandler.appender(line)
        # セッションIDが未定義の場合
        if session_id == None or session_id == '0':
            now = datetime.datetime.now()
            date = now.strftime('%Y%m%d%H%M%S')
            session_id  = hashlib.md5(date.encode()).hexdigest()
        # 繰り返し回数を超過した場合、停止コードを送信
        if request.counter == 100:
            fileHandler.writer()
            stop_signal = 1
        else:
            stop_signal = 0
        # カウンタをインクリメント
        #counter = counter + 1
        return session_id,counter,stop_signal,delta