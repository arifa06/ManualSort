def manualSort(item):                                           # membuat fungsi
    angka = []                                                  # menampung nilai sementara
    for i in range (item):                                      # membuat perulangan dengan for untuk input angka
        num = int(input('Angka ke -{}: '.format(i+1)))          # input angka sejumlah nilai item
        angka.append(num)                                       # menambahkan angka
    angka.sort()                                                # sorting dari urutan terkecil hingga terbesar
    print('Hasil sort :',angka)                                 # cetak hasil

while True:                                                     # membuat perulangan dengan while
    try:                                                        # try & except untuk filter data sesuai kriteria
        item = int(input('Masukkan jumlah inputan : '))         # input jumlah item secara manual
        if 1 < item < 100:                                      # kriteria sesuai, memanggil fungsi
            manualSort(item)                               
        elif item > 100:                                        # kriteria tidak sesuai
            print('Invalid Input!')
        elif 0 < item < 1:                                      # kriteria tidak sesuai
            print('Invalid Input!')
        elif item < 0:                                          # kriteria tidak sesuai
            print('Invalid Input!')                                                     
    except:                                                     # kriteria tidak sesuai
        print('Invalid Input!') 
