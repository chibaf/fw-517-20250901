import serial
from datetime import date
from read2m5_class import read2m5
import time
import matplotlib.pyplot as plt
import threading
import queue  # library for queu operation
import RPi.GPIO as GPIO
from thread_ssr_class import thread_ssr  # import thread body
#
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#
current_time = time.strftime("_H%H_M%M_S%S", time.localtime())
fn = "LR5-SSR_" + str(date.today()) + current_time + ".csv"
f=open(fn, 'w', encoding="utf-8")
start = time.time()
#
GPIO.setup(11, GPIO.OUT)  # side heater: : ssr11
GPIO.setup(12, GPIO.OUT)  # core heater: ssr12
GPIO.setup(13, GPIO.OUT)  # heater: ssr13
GPIO.setup(15, GPIO.OUT)  # pump: ssr15
GPIO.setup(16, GPIO.OUT)  # side heater: ssr16
GPIO.setup(18, GPIO.OUT)  # freezer: ssr18
GPIO.setup(19, GPIO.OUT)  # bottom heater: ssr19
#
data=[[0]*10]*10
loggers = read2m5()
plt.figure(100)
x = range(0, 10, 1)
#
GPIO.output(15, 1)  # pump always runs
#
it=0   # thread counter
q =queue.Queue()  # queue which stores a result of a thread
ssr=[0,0,0]
while True:
  try:
    # output data
    line0=loggers.reads()
    line=[]
    for i in range(0,10):
      line=line+[line0[i]]
    if len(line)<10:
      continue
    if it==0:  #when thread has not started
      it=it+1
      thread1=thread_ssr() #provide a thread
      q.put(line+[time.time()]+[time.time()])
      print(line+[time.time()]+[time.time()])
      th = threading.Thread(target=thread1.thread,args=(it,q),daemon=True)
      th.start()
    if th.is_alive()==False:  #when no thread
      it=it+1
      ssr=q.get()
      ssrtime1=ssr[2]
      ssrtime2=ssr[3]
      thread1=thread_ssr() #provide a thread
      q.put(line+[ssrtime1,ssrtime2])
      print(line+[ssrtime1,ssrtime2])
      th = threading.Thread(target=thread1.thread,args=(it,q),daemon=True)
      th.start()
    # set heaters ssr / ssr[0]==1: on;  ssr[0]==0: off
    GPIO.output(11,ssr[0])  # side heater: : ssr11
    GPIO.output(12,ssr[0])  # core heater: ssr12
    GPIO.output(13,ssr[0])  # heater: ssr13
    GPIO.output(16,ssr[0])  # side heater: ssr16
    GPIO.output(19,ssr[0])  # bottom heater: ssr19
    # set freezer on / ssr[1]==1: on;  ssr[1]==0: off
    GPIO.output(18,ssr[1])
    #
    st = time.strftime("%Y %b %d %H:%M:%S", time.localtime())
    ss = str(time.time() - int(time.time()))
    row=st + ss[1:5] + "," + str(round(time.time()-start, 2)) + ","
    for i in range(0,len(line)):
      row=row+str(line[i])+","
    row=row+str(ssr[0])+","+str(ssr[1])+"\n"
    f.write(row)
# plotting
    x = range(0, 10, 1)
    plt.clf()
    plt.ylim(-25,10)
    tl = [0] * 10
    hd = []
    data.pop(-1)
    data.insert(0,line)
    rez=[[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]  # transposing a matrix
    for i in range(0,len(rez)):
      tl[i], = plt.plot(x,rez[i], label="T" + str(i+1))
    for i in range(0,len(rez)):
      hd.append(tl[i])
      plt.legend(handles=hd)
    plt.pause(0.1)
  except KeyboardInterrupt:
    print("KeyboardInterrupt:")
    GPIO.output(11, False)
    GPIO.output(12, False)
    GPIO.output(13, False)
    GPIO.output(15, 1)    # pump keeps running
    GPIO.output(16, False)  
    GPIO.output(18, False)
    GPIO.output(19, False)
    loggers.close()
    f.close()
    exit()