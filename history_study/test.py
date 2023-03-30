import logging

# fmt = "%(name)s----->%(message)s----->%(asctime)s"
# logging.basicConfig(level="DEBUG",format=fmt)
# logging.debug("这是debug信息")
# logging.info('这是info信息')
# logging.warning('这是警告信息')
# logging.error('这是错误信息')
# logging.critical('这是cri信息')


logger = logging.getLogger('heihei') #默认的打印级别是WARNING，所以当跟控制台日志的打印级别不一样时，以打印级别最高的为准。
logger.setLevel('INFO')
console_handler = logging.StreamHandler()
#控制台的等级
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
console_handler.setLevel(level='INFO')
logger.addHandler(console_handler)

file_handler = logging.FileHandler('1.txt', encoding='utf-8', mode='a')
file_handler.setLevel('INFO')
logger.addHandler(file_handler)
logging.debug("这是debug信息")
logging.info('这是info信息')
logging.warning('这是警告信息')
logging.error('这是错误信息')
logging.critical('这是cri信息')

USER_AGENTS