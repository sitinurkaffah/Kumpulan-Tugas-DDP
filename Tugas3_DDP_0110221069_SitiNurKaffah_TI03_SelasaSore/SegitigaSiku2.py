import math
class SegitigaSikuSiku:
  def __init__(self,alas,tinggi,miring):
    self.alas = alas
    self.tinggi = tinggi
    self.miring = miring
  
  def keliling(self):
    return self.alas + self.tinggi + self.miring

  def luas(self):
    return 0.5 * self.alas * self.tinggi

