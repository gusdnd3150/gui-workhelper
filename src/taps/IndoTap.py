
from conf.logconfig import *
from conf.initData import *
import traceback
from src.taps.infoTapDt.JobSetting import JobSetting

class IndoTap():

    mainLayout = None
    jobSetting = None

    def __init__(self, mainLayout):
        logger.info(f'IndoTap init')
        self.mainLayout = mainLayout
        self.setEvent()
        self.jobSetting = JobSetting(mainLayout)

    def setEvent(self):
        try:
            logger.info('IndoTap setEvent')
        except:
            traceback.print_exception()



