import os
import sys
import traceback
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QColor, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView, QMessageBox
import logging
from conf.logconfig import logger
from ui.ui_main import Ui_MainWindow

from src.taps.IndoTap import IndoTap

# 네이밍
# 1. btn_?, popup_?, input_?,

class InitClass(QMainWindow):

    mainLayOut = None
    workThread = None # 실시간성 GUI 수정작업을 스레드를 통해 진행
    logThread = None
    IndoTap = None

    def __init__(self):
        super(InitClass, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        logger.info('application start')
        self.setWindowTitle('work helper (made by KHW)')

        self.IndoTap = IndoTap(self)

        # self.workThread = WorkThread()
        # self.workThread.updateConnList.connect(self.workUpdateConnList)
        # self.ui.btn_start.clicked.connect(self.start_sk)  # 시작버튼
        # self.ui.btn_stop.clicked.connect(self.stop_sk)   # 종료버튼

        # self.logThread = LogThread(self)
        # self.logThread.updateLog.connect(self.insertLog)

        # self.ui.log_btn_clear.clicked.connect(self.clickClear)
        # self.ui.btn_settings.clicked.connect(self.open_settings)
        # self.ui.btn_handler.clicked.connect(self.open_handler)
        # self.ui.btn_show_log.clicked.connect(self.open_logger)

        # self.bindData()


        # 설정팝업
        # self.popup = Settings(self.initData)
        # self.handlPop = Handler(self.initData)
        # self.utilityPop = Utility(self.initData)








    def bindData(self):
        print('')
        # list = moduleData.setCombos()
        # logger.info(f'combo init :: {list}')
        # for comKey in list.keys():
        #     if comKey == 'PKG_LIST':
        #         for item in list[comKey]:
        #             self.ui.combo_pkg.addItem(item['PKG_ID'])

        # for i in range(0, len(pkgCombo)):
        #     self.ui.combo_pkg.addItem(pkgCombo[i])



    def setGrid(self):
        self.ui.list_run_server.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.list_run_server.verticalHeader().setVisible(False)  # 행 번호 헤더 숨기기
        # self.ui.list_run_server.horizontalHeader().setVisible(False)  # 열 번호 헤더 숨기기
        self.ui.list_run_server.setRowCount(0)  # Table의 행을 설정, list의 길이
        self.ui.list_run_server.setColumnCount(9)
        self.ui.list_run_server.setHorizontalHeaderLabels(
            [
            'SK_ID',
            'SK_GROUP',
            'SK_TYPE',
            'SK_CLIENT_TYPE',
            'HD_ID',
            'SK_IP',
            'SK_PORT',
            'SK_DELIMIT_TYPE',
            'MAX_LENGTH'
             ]
        )

        self.ui.list_run_client.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.list_run_client.verticalHeader().setVisible(False)
        self.ui.list_run_client.setRowCount(0)  # Table의 행을 설정, list의 길이
        self.ui.list_run_client.setColumnCount(9)

        self.ui.list_run_client.setHorizontalHeaderLabels(
            [
                'SK_ID',
                'SK_GROUP',
                'SK_TYPE',
                'SK_CLIENT_TYPE',
                'HD_ID',
                'SK_IP',
                'SK_PORT',
                'SK_DELIMIT_TYPE',
                'MAX_LENGTH'
            ]
        )


        # self.ui.list_conn
        self.treeModel = QStandardItemModel()
        # self.treeModel.setHorizontalHeaderLabels(["Item", "Description"])
        self.treeModel.setHorizontalHeaderLabels(["Item"])
        self.root_node = self.treeModel.invisibleRootItem()







    def open_logger(self):
        # 열고 싶은 경로
        # path = r"../logs/"
        # current_path = os.getcwd()
        # logger.info(f'path : {current_path}')
        # # 경로 열기
        # os.startfile(f'{current_path}/logs')
        if self.logPop.isVisible():
            self.logPop.hide()
        else:
            self.logPop.show()



    @Slot()
    def workUpdateConnList(self):

        try:
            self.treeModel.clear()  # 모델의 모든 항목 제거
            # self.treeModel.setHorizontalHeaderLabels(["SK_ID", "Description"])  # 헤더 다시 설정
            self.treeModel.setHorizontalHeaderLabels(["connection Info"])  # 헤더 다시 설정
            self.root_node = self.treeModel.invisibleRootItem()
            for index, item in enumerate(moduleData.sokcetList):
                skItem = QStandardItem( item['SK_ID'] )
                description_item = QStandardItem( item['SK_CONN_TYPE'])
                for skId, client, thread in moduleData.runChannels:
                    if skId == item['SK_ID']:
                        # skItem.appendRow([QStandardItem(str(client)), QStandardItem(str(thread))])
                        skItem.appendRow([QStandardItem(f'{str(client)} -- {thread}')])
                # 루트 노드에 부모 항목 추가 (여러 열)
                # self.root_node.appendRow([skItem, description_item])
                self.root_node.appendRow([skItem])
            self.ui.list_conn.setModel(self.treeModel)
            self.ui.list_conn.expandAll()

        except:
            logger.error(f'updateConnList exception: {traceback.format_exc()}')

    @Slot(str)
    def insertLog(self,msg):
        try:
            if "recive_string" in msg:
                self.ui.log_text_log.append(f'<span style="color:blue">{msg} <span/>')
            elif "send_string" in msg:
                self.ui.log_text_log.append(f'<span style="color:green">{msg} <span/>')
            else:
                self.ui.log_text_log.append(f'<span>{msg} <span/>')
        except:
            logger.error(f'showLog error : {traceback.format_exc()}')

