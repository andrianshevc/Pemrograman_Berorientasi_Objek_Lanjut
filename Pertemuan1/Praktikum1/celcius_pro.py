# Tugas Minggu 1
# NIM	: 210511071
# Nama	: ANDRIAN SHEVCHENKO # Kelas	: TIF21B (R2)

class KonversiSuhu: 
    @staticmethod
    def celsius1_to_fahrenheit(celsius): 
        return (9/5) * celsius1 + 32

    @staticmethod
    def celsius2_to_reamur(celsius): 
        return (4/5) * celsius2

    @staticmethod
    def celsius3_to_kelvin(celsius): 
        return celsius3 + 273.15


celsius1 = 75
celsius2 = 30
celsius3 = 60

fahrenheit = KonversiSuhu.celsius1_to_fahrenheit(celsius1) 
reamur = KonversiSuhu.celsius2_to_reamur(celsius2)
kelvin = KonversiSuhu.celsius3_to_kelvin(celsius3)

print("konversi",celsius1, "derajat celcius adalah ",fahrenheit, "derajat fahrenheit")
print("konversi",celsius2, "derajat celcius adalah ",reamur, "derajat Reamur")
print("konversi",celsius3, "derajat celcius adalah ",kelvin, "derajat Kelvin")
 
