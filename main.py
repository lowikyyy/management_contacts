##kalkulator bmi

print("PERHITUNGAN BMI (BODY MASS INDEX)")
print('-'*20)

berat_badan = int(input("Masukkan Berat Badan = "))
tinggi_badan = float(input("Masukkan Tinggi Badan = "))

bmi = berat_badan / (tinggi_badan ** 2)
berat_badan_ideal = dict()
berat_badan_ideal ['Min'] = 18.5 * (tinggi_badan**2)
berat_badan_ideal ['Max'] = 25 * (tinggi_badan**2)
print(f'nilai BMI anda adalah {bmi:.2f} kg/m^2')

x = bmi >= 18.5
y = bmi <= 25

if x:
    print("Berat anda sudah sesuai BMI")
elif y:
    print("Berat anda sudah sesuai BMI")
else:
    print("Berat anda masih belum sesuai nih:((")

print(f'Berat Ideal BMI Anda adalah dalam rentang {berat_badan_ideal ['Min']} Kg - {berat_badan_ideal ['Max']} Kg')
print ('Terima Kasih Sudah Menggunakan Program Ini :))))')
