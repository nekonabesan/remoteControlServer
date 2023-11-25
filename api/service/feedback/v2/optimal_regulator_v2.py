import time
import hashlib
import datetime
import api.schemas.entity.feedback.optimal_regulator.request as request_optimal_regulator
import api.service.util.FileHandrer as util_file_handler
from decimal import *

class optimalRegulator():
    NONE = -1
    U_MAX = 100
    U_MIN = 0
    SPEED = 0
    OFFSET = 34
    FWD = 1
    BCK = 0

    K1 = Decimal(str(236.86507498))
    K2 = Decimal(str(28.46595518))
    K3 = Decimal(str(4.11073668))
    K4 = Decimal(str(4.33681214))

    def op_sign(self, value):
        return (value > 0) - (value < 0)

    def calc(self, request: request_optimal_regulator.Request, fileHandler: util_file_handler.fileHandler):
        print(request)
        # Requestパラメータ取得
        session_id = request.session_id
        counter = request.counter
        mode = request.mode
        angle_y = Decimal(str(round(request.angle_y)))
        prev_angle_y = Decimal(str(round(request.prev_angle_y)))
        rt_a_counter = Decimal(str(request.rt_a_counter))
        rt_d_counter = Decimal(str(request.rt_d_counter))
        before_count_a = Decimal(str(request.before_count_a))
        before_count_d = Decimal(str(request.before_count_d))
        rotation_a = request.rotation_a
        rotation_d = request.rotation_d
        delta_time = Decimal(str(request.delta))
        line = []
        # パラメータ初期化
        delta_angle_y = Decimal(angle_y - prev_angle_y)
        delta_theta_a = Decimal(abs(abs(rt_a_counter) - abs(before_count_a)))
        delta_theta_d = Decimal(abs(abs(rt_d_counter) - abs(before_count_d)))

        if rotation_a == self.BCK:
            delta_theta_a = -delta_theta_a
        if rotation_d == self.BCK:
            delta_theta_d = -delta_theta_d
        # motorの振子に対する角度
        motor_a_angle = delta_theta_a - delta_angle_y
        motor_d_angle = delta_theta_d - delta_angle_y
        '''
        if self.op_sign(delta_theta_a) == self.op_sign(delta_angle_y):
            motor_a_angle = delta_theta_a - delta_angle_y
        else:
            motor_a_angle = delta_angle_y - delta_theta_a
        if self.op_sign(delta_theta_d) == self.op_sign(delta_angle_y):
            motor_d_angle = delta_theta_d - delta_angle_y
        else:
            motor_d_angle = delta_angle_y - delta_theta_d
        '''
        # 振子の角速度
        if delta_angle_y == 0 or delta_time == 0:
            angular_velocity_y = Decimal(0)
        else:
            angular_velocity_y = Decimal(delta_angle_y/delta_time)
        # モータの角速度
        if delta_time != 0:
            velocity_a = Decimal(delta_theta_a/delta_time)
        else:
            velocity_a = 0
        if delta_time!= 0:
            velocity_d = Decimal(delta_theta_d/delta_time)
        else:
            velocity_d = 0

        # U(t)を導出
        ua = ((angle_y * self.K1) + (angular_velocity_y * self.K2) + (motor_a_angle * self.K3) + (velocity_a * self.K4))
        ud = ((angle_y * self.K1) + (angular_velocity_y * self.K2) + (motor_d_angle * self.K3) + (velocity_d * self.K4))

        # 回転方向を設定
        if ua < 0:
            direction_a = self.BCK
        else:
            direction_a = self.FWD

        if ud < 0:
            direction_d = self.BCK
        else:
            direction_d = self.FWD
        ua = abs(ua)
        ud = abs(ud)

        # 系に対してPWMデューティ比として与える制御入力をスケーリング
        if ua != self.U_MIN:
            ua = round(Decimal(0.015) * ua)
        if ud != self.U_MIN:
            ud = round(Decimal(0.015) * ud)

        if ua > self.U_MAX:
            ua = self.U_MAX
        if ud > self.U_MAX:
            ud = self.U_MAX
        
        line.append(str(request.angle_y))
        line.append(str(request.rt_a_counter))
        line.append(str(request.rt_d_counter))
        line.append(str(direction_a))
        line.append(str(direction_d))
        line.append(str(ua))
        line.append(str(ud))
        line.append(str(request.delta))
        #if counter == 0:
            # ヘッダ行を追加
        #    fileHandler.appender(['angle_y', 'rt_a_counter', 'rt_d_counter', 'direction_a', 'direction_d', 'ua', 'ud', 'delta'])
        #fileHandler.appender(line)
        # mode 
        if mode == self.NONE:
            mode = self.FWD
        # セッションIDが未定義の場合
        if session_id == None or session_id == '0':
            now = datetime.datetime.now()
            date = now.strftime('%Y%m%d%H%M%S')
            session_id  = hashlib.md5(date.encode()).hexdigest()
        # 繰り返し回数を超過した場合、停止コードを送信
        stop_signal = 0
        #if request.counter == 300:
        #    fileHandler.writer()
        #    stop_signal = 1
        #else:
        #    stop_signal = 0
        # カウンタをインクリメント
        #counter = counter + 1
        return session_id,counter,mode,stop_signal,ua,ud,direction_a,direction_d,delta_time
