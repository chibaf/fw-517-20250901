import threading
import queue  # library for queu operation
import time
from thread_one_class import thread_one  # import thread body
import random
#
i=1   # counter
thread1=thread_one(i) #provide a thread
q =queue.Queue()  # queue which stores a result of a thread
th = threading.Thread(target=thread1.thread, args=(i,q),daemon=True)
# setting of thread
a=[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]
q.put(a)
th.start() # start thread
while True:  # infinite loop
  if th.is_alive()==False:  #when thread ends
    result = q.get()  # take queu values
    print("thread: "+str(i)+" "+str(result))
    i=i+1
    if i>5:  # execute total five thread 
      break;  # exit loop
    thread1=thread_one(i) #proivide the next thread
    a=[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]
    q.put(a)
    th = threading.Thread(target=thread1.thread, args=(i,q),daemon=True)
    # setting the next thread
    th.start() # start thread
  time.sleep(2)  #do other tasks

exit()
