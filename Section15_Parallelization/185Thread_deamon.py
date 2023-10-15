import logging
import threading
import time
import random

def worker1(arg1 = None, arg2= 0):
    logging.debug("start")
    time.sleep(5)    
    logging.debug("end")


def worker2(x, y=1):
    logging.debug("start")
    time.sleep(1)
    logging.debug("end")

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG, 
        # 日時も表示する
        format='%(asctime)s %(threadName)s: %(message)s '
        # format='%(threadName)s: %(message)s'
    )

    logging.debug("start")

    t1 = threading.Thread(target=worker1, name="t1", args=(99, 98))
    # t1の処理を終了させる
    t1.setDaemon(True)

    t2 = threading.Thread(target=worker2, name="t2", args=(100,), kwargs={'y': 200})
    t1.start()
    t2.start()

    # 1/2の確率でt1を強制終了するif文を追加
    if random.randint(0, 1):
        # t1を強制終了
        t1.join(1)
    else:
        # t1, t2の処理が終わるまで待つ(5s)
        t1.join()

    logging.debug("end")

