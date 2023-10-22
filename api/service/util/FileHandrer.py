import csv
import time

class fileHandler:
    data = None

    def __init__(self) -> None:
        # 初期化
        self.data = []
        pass

    def appender(self, line: list):
        self.data.append(line)
        return True

    def writer(self):
        path = 'param_' + str(time.time()) + '.tsv'
        with open(path, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(self.data)
        del self.data
        return True