from operator import index

from conf.logconfig import *
import conf.initData as initData
import traceback

class JobSetting():

    mainLayOut = None

    def __init__(self, mainLayOut):
        logger.info('JobSetting init')
        self.mainLayOut = mainLayOut
        self.setEvent()

    def setEvent(self):
        try:
            self.mainLayOut.ui.useYnCombo.addItems(initData.uesYn)
            self.mainLayOut.ui.carTyCombo.addItems(initData.indoCarTy)
            self.mainLayOut.ui.bt_create.clicked.connect(self.createInsert)
            self.mainLayOut.ui.bt_clear.clicked.connect(self.clear)
            logger.info('JobSetting setEvent')
        except:
            traceback.print_exception()


    def clear(self):
        self.mainLayOut.ui.output.clear()

    def createInsert(self):
        try:

            toolId = self.mainLayOut.ui.toolId.text()
            jobGrp = int(toolId[len(toolId)-4:])
            procCd = self.mainLayOut.ui.procCd.text()
            carTy = self.mainLayOut.ui.carTyCombo.currentText()
            useYn = self.mainLayOut.ui.useYnCombo.currentText()
            jobId = self.mainLayOut.ui.jobId.text()
            keeperToolId = self.mainLayOut.ui.keeperToolId.text()
            keeperJobId = self.mainLayOut.ui.keeperJobId.text()
            jobGrp1 = []
            jobGrp2 = []
            jobGrp3 = []
            jobGrp4 = []
            jobGrp5 = []
            jobGrp6 = []
            if self.mainLayOut.ui.jobGrp1.text() != '':
                jobGrp1 = self.mainLayOut.ui.jobGrp1.text().split(',')
            if self.mainLayOut.ui.jobGrp2.text() != '':
                jobGrp2 = self.mainLayOut.ui.jobGrp2.text().split(',')
            if self.mainLayOut.ui.jobGrp3.text() != '':
                jobGrp3 = self.mainLayOut.ui.jobGrp3.text().split(',')
            if self.mainLayOut.ui.jobGrp4.text() != '':
                jobGrp4 = self.mainLayOut.ui.jobGrp4.text().split(',')
            if self.mainLayOut.ui.jobGrp5.text() != '':
                jobGrp5 = self.mainLayOut.ui.jobGrp5.text().split(',')
            if self.mainLayOut.ui.jobGrp6.text() != '':
                jobGrp6 = self.mainLayOut.ui.jobGrp6.text().split(',')

            insertStat = []
            for car in initData.indoCarCd:
                jobGrpTemp = 1
                if car.get(carTy) is not None:
                    carCd = car[carTy]

                    for idex, item in enumerate(jobGrp1):
                        jobSeq = (idex+1)
                        jogGrpSeq = f'{jobGrp}-{jobGrpTemp}'
                        colNo = item.split('/')[0]
                        colVal = item.split('/')[1]
                        # print(f'carCd:{carCd},jogGrpSeq:{jogGrpSeq},keyMap:{item}, jobSeq:{jobSeq}')
                        insert = (
                            f"INSERT INTO TB_BI_TOOL_JOB (TOOL_ID, PROC_CD, CAR_CD, JOB_SEQ, COL_NO, COL_VAL, JOB_ID, JOB_GRP, KEEPER_JOB_ID, KEEPER_TOOL_ID, USE_YN, JOB_MAP_KEY) "
                            f"VALUES('{toolId}', '{procCd}', '{carCd}', {jobSeq}, {colNo}, '{colVal}', {jobId}, '{jogGrpSeq}', {keeperJobId}, '{keeperToolId}', '{useYn}', '{item}')"
                        )
                        insertStat.append(insert)
                    if  (len(jobGrp1) > 0):
                        jobGrpTemp += 1

                    for idex, item in enumerate(jobGrp2):
                        jobSeq = (idex+1)
                        jogGrpSeq = f'{jobGrp}-{jobGrpTemp}'
                        colNo = item.split('/')[0]
                        colVal = item.split('/')[1]
                        # print(f'carCd:{carCd},jogGrpSeq:{jogGrpSeq},keyMap:{item}, jobSeq:{jobSeq}')
                        insert = (
                            f"INSERT INTO TB_BI_TOOL_JOB (TOOL_ID, PROC_CD, CAR_CD, JOB_SEQ, COL_NO, COL_VAL, JOB_ID, JOB_GRP, KEEPER_JOB_ID, KEEPER_TOOL_ID, USE_YN, JOB_MAP_KEY) "
                            f"VALUES('{toolId}', '{procCd}', '{carCd}', {jobSeq}, {colNo}, '{colVal}', {jobId}, '{jogGrpSeq}', {keeperJobId}, '{keeperToolId}', '{useYn}', '{item}')"
                        )
                        insertStat.append(insert)
                    if  (len(jobGrp2) > 0):
                        jobGrpTemp += 1

                    for idex, item in enumerate(jobGrp3):
                        jobSeq = (idex+1)
                        jogGrpSeq = f'{jobGrp}-{jobGrpTemp}'
                        colNo = item.split('/')[0]
                        colVal = item.split('/')[1]
                        # print(f'carCd:{carCd},jogGrpSeq:{jogGrpSeq},keyMap:{item}, jobSeq:{jobSeq}')
                        insert = (
                            f"INSERT INTO TB_BI_TOOL_JOB (TOOL_ID, PROC_CD, CAR_CD, JOB_SEQ, COL_NO, COL_VAL, JOB_ID, JOB_GRP, KEEPER_JOB_ID, KEEPER_TOOL_ID, USE_YN, JOB_MAP_KEY) "
                            f"VALUES('{toolId}', '{procCd}', '{carCd}', {jobSeq}, {colNo}, '{colVal}', {jobId}, '{jogGrpSeq}', {keeperJobId}, '{keeperToolId}', '{useYn}', '{item}')"
                        )
                        insertStat.append(insert)
                    if  (len(jobGrp3) > 0):
                        jobGrpTemp += 1

                    for idex, item in enumerate(jobGrp4):
                        jobSeq = (idex+1)
                        jogGrpSeq = f'{jobGrp}-{jobGrpTemp}'
                        colNo = item.split('/')[0]
                        colVal = item.split('/')[1]
                        # print(f'carCd:{carCd},jogGrpSeq:{jogGrpSeq},keyMap:{item}, jobSeq:{jobSeq}')
                        insert = (
                            f"INSERT INTO TB_BI_TOOL_JOB (TOOL_ID, PROC_CD, CAR_CD, JOB_SEQ, COL_NO, COL_VAL, JOB_ID, JOB_GRP, KEEPER_JOB_ID, KEEPER_TOOL_ID, USE_YN, JOB_MAP_KEY) "
                            f"VALUES('{toolId}', '{procCd}', '{carCd}', {jobSeq}, {colNo}, '{colVal}', {jobId}, '{jogGrpSeq}', {keeperJobId}, '{keeperToolId}', '{useYn}', '{item}')"
                        )
                        insertStat.append(insert)
                    if  (len(jobGrp4) > 0):
                        jobGrpTemp += 1

                    for idex, item in enumerate(jobGrp5):
                        jobSeq = (idex+1)
                        jogGrpSeq = f'{jobGrp}-{jobGrpTemp}'
                        colNo = item.split('/')[0]
                        colVal = item.split('/')[1]
                        # print(f'carCd:{carCd},jogGrpSeq:{jogGrpSeq},keyMap:{item}, jobSeq:{jobSeq}')
                        insert = (
                            f"INSERT INTO TB_BI_TOOL_JOB (TOOL_ID, PROC_CD, CAR_CD, JOB_SEQ, COL_NO, COL_VAL, JOB_ID, JOB_GRP, KEEPER_JOB_ID, KEEPER_TOOL_ID, USE_YN, JOB_MAP_KEY) "
                            f"VALUES('{toolId}', '{procCd}', '{carCd}', {jobSeq}, {colNo}, '{colVal}', {jobId}, '{jogGrpSeq}', {keeperJobId}, '{keeperToolId}', '{useYn}', '{item}')"
                        )
                        insertStat.append(insert)
                    if  (len(jobGrp5) > 0):
                        jobGrpTemp += 1

                    for idex, item in enumerate(jobGrp6):
                        jobSeq = (idex+1)
                        jogGrpSeq = f'{jobGrp}-{jobGrpTemp}'
                        colNo = item.split('/')[0]
                        colVal = item.split('/')[1]
                        # print(f'carCd:{carCd},jogGrpSeq:{jogGrpSeq},keyMap:{item}, jobSeq:{jobSeq}')
                        insert = (
                            f"INSERT INTO TB_BI_TOOL_JOB (TOOL_ID, PROC_CD, CAR_CD, JOB_SEQ, COL_NO, COL_VAL, JOB_ID, JOB_GRP, KEEPER_JOB_ID, KEEPER_TOOL_ID, USE_YN, JOB_MAP_KEY) "
                            f"VALUES('{toolId}', '{procCd}', '{carCd}', {jobSeq}, {colNo}, '{colVal}', {jobId}, '{jogGrpSeq}', {keeperJobId}, '{keeperToolId}', '{useYn}', '{item}')"
                        )
                        insertStat.append(insert)
                    if  (len(jobGrp6) > 0):
                        jobGrpTemp += 1




            log_str = (
                f'toolId: {toolId}\n'
                f'procCd: {procCd}\n'
                f'carTy: {carTy}\n'
                f'useYn: {useYn}\n'
                f'jobId: {jobId}\n'
                f'keeperToolId: {keeperToolId}\n'
                f'keeperJobId: {keeperJobId}\n'
                f'jobGrp: {jobGrp}\n'
                f'jobGrp1: {jobGrp1}\n'
                f'jobGrp2: {jobGrp2}\n'
                f'jobGrp3: {jobGrp3}\n'
                f'jobGrp4: {jobGrp4}\n'
                f'jobGrp5: {jobGrp5}\n'
                f'jobGrp6: {jobGrp6}'
            )
            self.mainLayOut.ui.output.setText(log_str)
            self.mainLayOut.ui.output.setText(';\n\r'.join(insertStat))


        except:
            self.mainLayOut.ui.output.setText(traceback.format_exc())
