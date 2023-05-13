class BolaMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
# Tambahkan method untuk menghitung volume dan Luas Permukaan Persegi
        def Volume(cls, jari_jari):
            return (4/3) * 3.14 * jari_jari**3
        cls.Volume = classmethod(Volume)
        def Lpermukaan(cls, jari_jari):
            return 4 * 3.14 * jari_jari**2
        cls.Lpermukaan = classmethod(Lpermukaan)
class Bola(metaclass=BolaMeta):
    pass
s = Bola()
# Menghitung Volume bola dengan jari2 = 7
volume_bola = Bola.Volume(7)
print("Volume Bola :", volume_bola)
# Menghitung Lpermukaan bola dengan jari2 = 7
Lpermukaan_bola = Bola.Lpermukaan(7)
print("Lpermukaan Bola:", Lpermukaan_bola)