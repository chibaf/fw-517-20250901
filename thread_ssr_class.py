class thread_ssr:

  def __init__(self):   # initial action
    return
  def thread(self,it,q): # class body
    import time
    a=q.get()   # get Tc temp
#
    if time.time()-a[10]>=1800.: # freezer on/off
      a[10]=time.time()
      ssr18=0
    elif 0<time.time()-a[10]<=1500.:
      if a[0]<-10.0:
        ssr18=0
      else:
        ssr18=1 # 1->on, 0->off
    else:
      ssr18=0     
    if time.time()-a[11]>=40000.:
      a[10]=time.time()
    if 0<=time.time()-a[11]<=20000.: # temp on/off threshold
      temp=-0.5
    else:
      temp=0.5
    av=sum(a[1:9])/9. # heater
    if av>temp:  # threshold of ssr switching  # 0.5 -> 0.0 24/JUl/2025 # 0.0->0.5 20250725
      ssr1=0   # ssr off
    else:
      ssr1=1   # ssr on
    print([ssr1,ssr18,a[10],a[11]])
    q.put([ssr1,ssr18,a[10],a[11]])   # set ssr value to queu
    return
