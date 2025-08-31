class m5logger:
    
  def read_logger(self,ser):
    import serial
    line01 = ser.readline()
    print(line01)
    while True:
      line01 = ser.readline()
      print(line01)
      try:
        line02=line01.strip().decode('utf-8')
        print(line02)
      except UnicodeDecodeError:
        continue
      data = [str(val) for val in line02.split(",")]
      data1=[]
      if len(data)==12:
        for i in range(0,11):
          try:
            if i==0:
              data1.append(data[0])
            else:
              fd=float(data[i+1])
              data1.append(fd)
          except:
            continue
        return data1
      else:
        continue
      print("b1")
#
  def close(self,ser):
    ser.close()
