import threading
import time

def worker1():
    print(f"thread name: {threading.current_thread().name}", "start")
    time.sleep(3)    
    print(f"thread name: {threading.current_thread().name}", "end")


def worker2():
    print(f"thread name: {threading.current_thread().name}", "start")
    time.sleep(5)
    print(f"thread name: {threading.current_thread().name}", "end")

if __name__ == '__main__':
    print(f"thread name: {threading.current_thread().name}", "start")
    
    t1 = threading.Thread(target=worker1)
    t2 = threading.Thread(target=worker2)
    t1.start()
    t2.start()

    print(f"thread name: {threading.current_thread().name}", "end")    

