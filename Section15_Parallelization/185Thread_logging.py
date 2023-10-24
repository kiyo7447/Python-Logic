import logging
import threading
import time

def worker1(arg1, arg2):
    logging.debug("start")
    logging.debug(f"arg1: {arg1}, arg2: {arg2}")
    time.sleep(3)    
    logging.debug("end")


def worker2(x, y=1):
    logging.debug("start")
    logging.debug(f"x: {x}, y: {y}")
    time.sleep(5)
    logging.debug("end")

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG, 
        # 日時も表示する
        format='%(asctime)s %(threadName)s: %(message)s '
        # format='%(threadName)s: %(message)s'
    )

    logging.debug("start")
    # args, kwargsを指定する。kwargsはDictionary型で指定する。
    t1 = threading.Thread(target=worker1, name="t1", args=(99, 98))
    t2 = threading.Thread(target=worker2, name="t2", args=(100,), kwargs={'y': 200})
    t1.start()
    t2.start()

    logging.debug("end")

