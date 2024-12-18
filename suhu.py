i = 1
while i<=3: 
            nama = input("Silahkan Masukkan Nama Anda:")
            print("Nama :",nama)
            tekanan_darah_sistolik = float(input("Masukkan Hasil Tekanan darah sistolik Anda(mmHg):"))
            print(" tekanan darah sistolik:",tekanan_darah_sistolik)
            tekanan_darah_diastolik = float(input(" Masukkan Hasil Tekanan darah diastolik Anda(mmHg):"))
            print(" tekanan darah diastolik:",tekanan_darah_diastolik)
            denyut_nadi = float(input("Masukkan Hasil Cek denyut nadi Anda(bpm):"))
            print(" Denyut Nadi:",denyut_nadi)

            # Mengecek tekanan darah sistolik dan diastolik
            if tekanan_darah_sistolik >180 or tekanan_darah_diastolik >120:
                print("Anda sedang mengalami Krisis Hipertensi segera mencari bantuan medis")
            elif tekanan_darah_sistolik >140 or tekanan_darah_diastolik >90:
                print("Disarankan untuk konsultasi dengan dokter mengenai hipertensi")
            elif 120<=tekanan_darah_sistolik<=139 or 80<=tekanan_darah_diastolik<=89:
                print("Anda berada di dalam kondisi prahipertensi")
            elif tekanan_darah_sistolik <120 and tekanan_darah_diastolik <80:
                print("Tekanan darah anda normal")

            #mengecek denyut nadi
            if denyut_nadi >100:
                print("Anda disarankan untuk memeriksa kondisi kesehatan jantung")
            elif denyut_nadi <60:
                print("Disarankan untuk diperiksa apakah ada gejala yang mengiringi bradikardia")
            elif 60<=denyut_nadi<=100:
                print("Denyut nadi Anda normal")
                i =+1