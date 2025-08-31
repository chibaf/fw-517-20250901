class thread_one:

  def __init__(self,i):   # initial action
    print(" start "+str(i))

  def thread(self,i,q): # class body
    import time
    import random
    a=q.get()   # get Tc temp
    if a<0.0:
      ssr=1   # ssr on
    else:
      ssr=0   # ssr off
    q.put(ssr)   # set ssr value to queu
    return
