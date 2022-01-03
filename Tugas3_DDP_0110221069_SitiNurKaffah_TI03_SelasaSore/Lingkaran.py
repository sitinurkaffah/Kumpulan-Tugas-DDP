import math
class Lingkaran:
    def __init__(self,jarijari):
        self.jarijari = jarijari

    def keliling(self):
        return 2 * math.pi * self.jarijari

    def luas(self):
        return math.pi * self.jarijari * self.jarijari