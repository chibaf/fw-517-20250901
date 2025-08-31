class gagdet():

  def __init__(self): 
    self.tc=0.0  # tc initial value
    self.ssr1=0  # ssr initial value
    
  def set_gpio(self,ssr): # GPIO on/off
      self.ssr1=ssr
      
  def step(self,n):  # change Tc by time step
    import random
    r=random.randint(0,9)
    for i in range(0,n):
      if self.ssr1==1:  # if ssr on
        self.tc=self.tc+0.05*r*0.1
      else:  # if ssr off
        self.tc=self.tc-0.05*r*0.1
      
  def logger(self):  # values of logger
      return self.tc