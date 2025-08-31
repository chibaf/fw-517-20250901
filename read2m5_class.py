class read2m5:
#
  def __init__(self):
    import serial
    #read serials#    from read_m5b_class import m5logger
    self.ser0=serial.Serial("/dev/ttyUSB0",115200)
    self.ser1=serial.Serial("/dev/ttyUSB1",115200)
#   
  def reads(self):
    import serial
    i=0
    while True:
      i=i+1
      line01 = self.ser0.readline()
      line02 = self.ser1.readline()
      try:
        line01s=line01.strip().decode('utf-8')
        line02s=line02.strip().decode('utf-8')
      except UnicodeDecodeError:
        continue
      data1s=line01s.split(",")
      data2s=line02s.split(",")
      if len(data1s)!=12 or len(data2s)!=12:
        continue
      data1=[]
      data2=[]
      for i in range(0,10):
        data1=data1+[data1s[i+2]]
        data2=data2+[data2s[i+2]]
      try:
        data1s = [float(val) for val in data1]
        data2s = [float(val) for val in data2]
      except Exception as e:
        continue
      break
    if data1s[0]=='03':
      array=data2s+data1s
    else:
      array=data1s+data2s
    return array
#    
  def close(self):
    import serial
    self.ser0.close()   
    self.ser1.close()   
