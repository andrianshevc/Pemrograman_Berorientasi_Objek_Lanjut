class KubusMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
# Tambahkan method untuk menghitung volume dan Luas Permukaan Persegi
        def Volume(cls, sisi):
            return sisi ** 3
        cls.Volume = classmethod(Volume)
        def Lpermukaan(cls, sisi):
            return 6 * sisi ** 2
        cls.Lpermukaan = classmethod(Lpermukaan)
class Kubus(metaclass=KubusMeta):
    pass
s = Kubus()
# Menghitung Volume kubus dengan sisi = 4
volume_kubus = Kubus.Volume(4)
print("Volume Kubus :", volume_kubus)
# Menghitung Lpermukaan kubus dengan sisi = 4
Lpermukaan_kubus = Kubus.Lpermukaan(4)
print("Lpermukaan Kubus:", Lpermukaan_kubus)