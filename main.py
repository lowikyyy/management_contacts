##kalkulator bmi

print("PERHITUNGAN BMI (BODY MASS INDEX)")
print('-'*20)

berat_badan = int(input("Masukkan Berat Badan = "))
tinggi_badan = float(input("Masukkan Tinggi Badan = "))

bmi = berat_badan / (tinggi_badan ** 2)
berat_badan_ideal = dict()
berat_badan_ideal ['Min'] = 18.5 * (tinggi_badan**2)
berat_badan_ideal ['Max'] = 25 * (tinggi_badan**2)


if bmi< 18.5:
    hasil = "Berat kamu masih kurang nihh"
elif bmi < 25:
    hasil = "Berat kamuu udah sesuai nihhh"
elif bmi < 30:
    hasil = " Kayaknyaa kamu harus sedikit diet deh"
else:
    hasil = "Kamu terlalu berisi hahahaha"

print(f'\nnilai BMI anda adalah {bmi:.2f} kg/m^2')
print(hasil)
print(f"Berat badan ideal anda adalah dalam rentang"
      f"{berat_badan_ideal['Min']} Kg {berat_badan_ideal['Max']} Kg")
print ('Terima Kasih Sudah Menggunakan Program Ini :))))')
