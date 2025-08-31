from gadget_class import gagdet
from thread_one_class import thread_one  # import thread body
import threading
import queue  # library for queu operation
import time
import matplotlib.pyplot as plt

i=1   # counter
thread1=thread_one(i)
q =queue.Queue()  # queue which stores a result of a thread
th = threading.Thread(target=thread1.thread, args=(i,q),daemon=True)

raspi=gagdet() # create class
raspi.set_gpio(0)
raspi.step(2)

y=[0]*10
x=range(0, 10, 1)
q.put(raspi.logger())
th.start()
while True:
  if th.is_alive()==False:  # thread dosen't run
    i=i+1
    a=q.get()
    raspi.set_gpio(a)
    thread1=thread_one(i)
    th = threading.Thread(target=thread1.thread, args=(i,q),daemon=True)
    q.put(raspi.logger())
    th.start()
  raspi.step(2)
  time.sleep(1)
  
  y.pop(-1)
  y.insert(0,raspi.logger())
  plt.clf()
  plt.ylim(-.2, .2)
  plt.plot(x,y)
  plt.pause(0.1)
  
  print(raspi.logger())