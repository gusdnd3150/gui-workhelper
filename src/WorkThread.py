
from PySide6.QtCore import QThread, Signal



class WorkThread(QThread):
    # 데이터를 수정하는 신호 정의
    updateConnList = Signal()  # row, column, data

    def __init__(self):
        super().__init__()

    def run(self): # 백그라운드 작업 실행
        self.updateConnList.emit()







