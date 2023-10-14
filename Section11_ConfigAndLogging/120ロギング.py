# -*- coding: utf-8 -*-
"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""

# import logging as log

# log.basicConfig(filename='test.log', level=log.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

# log.critical('critical')
# log.error('error')
# log.warning('warning')
# log.info('info')
# log.debug('debug')



# コンソールにも出力する
import logging

# ロガーを定義
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# フォーマットを定義
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

#fileハンドラを生成する
file_handler = logging.FileHandler('test.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# コンソールハンドラを作成
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


logger.critical('critical')
logger.error('error')
logger.warning('warning')
logger.info('info')
logger.debug('debug')

