import logging
import logging.handlers
import os

# 로그 파일 경로 설정
log_file = './logs/appslog.log'

# 로그 파일 크기 제한 (100 메가바이트)
max_log_size = 100 * 1024 * 1024

def setup_sk_logger(skId):
    loggingLevl = logging.INFO

    # 로거 생성
    logger = logging.getLogger(skId)
    logger.setLevel(loggingLevl)

    # 로그 포맷 설정
    # log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(threadName)s - %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setLevel(loggingLevl)
    logger.addHandler(console_handler)

    # 파일 핸들러 생성
    file_handler = logging.handlers.RotatingFileHandler(f'./logs/{skId}', maxBytes=max_log_size, backupCount=2)
    file_handler.setFormatter(log_format)
    # 로거에 파일 핸들러 추가
    logger.addHandler(file_handler)
    return logger


def setup_global_logger():
    loggingLevl = logging.INFO

    # 로거 생성
    logger = logging.getLogger('my_logger')
    logger.setLevel(loggingLevl)

    # 로그 포맷 설정
    # log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(threadName)s - %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setLevel(loggingLevl)
    logger.addHandler(console_handler)

    # 파일 핸들러 생성
    file_handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=max_log_size, backupCount=1)
    file_handler.setFormatter(log_format)
    # 로거에 파일 핸들러 추가
    logger.addHandler(file_handler)
    return logger

# 전역 로거 설정
# 로그 파일 이동
os.makedirs('./logs', exist_ok=True)
logger = setup_global_logger()

# 예시로 로그 출력
# logger.debug('This is a debug message')
logger.info('application start')
# logger.warning('This is a warning message')
# logger.error('This is an error message')


if os.path.getsize(log_file) > max_log_size:
    old_logs_folder = './logs/old'
    os.makedirs(old_logs_folder, exist_ok=True)
    os.rename(log_file, os.path.join(old_logs_folder, os.path.basename(log_file)))