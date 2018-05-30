from texttable import Texttable
import xlrd
import random

def print_texttable(data_array):
    t=Texttable()
    t.add_rows(data_array)
    print(t.draw())

def data_dari_excel(nama_file):
    tabel=[]
    file_excel = xlrd.open_workbook(nama_file)
    sheet = file_excel.sheet_by_index(3)
    baris = sheet.nrows
    kolom = sheet.ncols

    for i in range(baris):
        data = []
        for j in range(kolom):
            data.append(sheet.cell_value(rowx=i, colx=j))
        tabel.append(data)
    return tabel

def hitung_jarak(a, b):
    hasil = pow(a, 2) + pow(b, 2)
    hasil = pow(hasil, 1/2)
    return hasil

def data_koordinat(koordinatKota):
    matrikJarak = []
    header = ["Kota"]
    for i in koordinatKota:
        header.append(i)
        konten = [i]
        for j in koordinatKota:
            kota1 = koordinatKota[i]
            kota2 = koordinatKota[j]
            x = kota2[0]-kota1[0]
            y = kota2[1]-kota1[1]
            jarak = hitung_jarak(x, y)
            konten.append(jarak)
        matrikJarak.append(konten)
    matrikJarak.insert(0, header)
    return matrikJarak

def nilai_hitung_eta(angka):
    if angka == 0:
        return 0
    else:
        return 1 / angka

def matrik_data_jarak(data):
    aray_data_jarak = []
    for i in range(len(data)):
        data_jarak = []
        for j in range(len(data[i])):
            if (i == 0):
                data_jarak.append(data[i][j])
            elif(j == 0):
                data_jarak.append(data[i][j])
            else:
                data_jarak.append(nilai_hitung_eta(data[i][j]))
        aray_data_jarak.append(data_jarak)
    return aray_data_jarak

def matrik_data_jarak_awal(data, tho):
    aray_data_jarak = []
    for i in range(len(data)):
        data_jarak = []
        for j in range(len(data[i])):
            if (i == 0):
                data_jarak.append(data[i][j])
            elif(j == 0):
                data_jarak.append(data[i][j])
            elif(i == j):
                data_jarak.append(0)
            else:
                data_jarak.append(tho)
        aray_data_jarak.append(data_jarak)
    return aray_data_jarak    

def nilai_penyebut_probabilitas(jalur, data_jarak, data_jarak_awal, alpha, beta):
    jumlah = 0
    jalur_terakhir = jalur.split("-")[-2]
    array_data_jarak = []
    array_data_jarak_awal = []
    for i in range(len(data_jarak)):
        if data_jarak[i][0] in jalur_terakhir:
            for j in range(1, len(data_jarak[i])):
                if data_jarak[0][j] not in jalur:
                    array_data_jarak.append(data_jarak[i][j])
                    array_data_jarak_awal.append(data_jarak_awal[i][j])
    for i in range(len(array_data_jarak)):
        jumlah+=(pow(array_data_jarak[i], alpha)*pow(array_data_jarak_awal[i], beta))
    return jumlah

def nilai_probabilitas(angka_jarak, angka_jarak_awal, alpha, beta, penyebut):
    return (pow(angka_jarak, alpha)*pow(angka_jarak_awal, beta))/penyebut

def array_komulatif(jalur, data_jarak, data_jarak_awal, alpha, beta):
    jalur_terakhir = jalur.split("-")[-2]
    aray_komulatif = []
    aray_nama_kota = []
    penyebut = nilai_penyebut_probabilitas(jalur, data_jarak, data_jarak_awal, alpha, beta)
    for i in range(len(data_jarak)):
        if data_jarak[i][0] in jalur_terakhir:
            for j in range(1, len(data_jarak[i])):
                if data_jarak[0][j] not in jalur:
                    aray_komulatif.append(nilai_probabilitas(data_jarak[i][j], data_jarak_awal[i][j], alpha, beta, penyebut))
                    aray_nama_kota.append(data_jarak[0][j])
    for i in range(1, len(aray_komulatif)):
        aray_komulatif[i] = aray_komulatif[i] + aray_komulatif[i-1]
    return {"nama_kota" : aray_nama_kota, "nilai_komulatif" : aray_komulatif}

def index_hasil_random(array_komulatif):
    acak = random.uniform(0, 1)
    for i in range(len(array_komulatif)):
        if acak <= array_komulatif[i]:
            return i

def pencarian_jalur_semut(data_jarak, data_jarak_awal, alpha, beta):
    jalur = data_jarak[0][1]+"-"
    for i in range(len(data_jarak)-3):
        komulatif = array_komulatif(jalur, data_jarak, data_jarak_awal, alpha, beta)
        index_random = index_hasil_random(komulatif["nilai_komulatif"])
        jalur_baru = komulatif["nama_kota"][index_random]
        jalur+=jalur_baru+"-"
    for i in range(1, len(data_jarak)):
        if data_jarak[0][i] not in jalur:
            jalur+=data_jarak[0][i]
    return jalur

def nilai_jarak_antar_dua_kota(kota1, kota2, data):
    for i in range(len(data)):
        if data[i][0] in kota1:
            for j in range(len(data[i])):
                if data[0][j] in kota2:
                    return data[i][j]

def nilai_jumlah_jarak_jalur(jalur, data):
    kota = jalur.split("-")
    jumlah = 0
    for i in range(len(kota)-1):
        jumlah+=nilai_jarak_antar_dua_kota(kota[i], kota[i+1], data)
    return jumlah

def iterasi_setiap_semut(jumlah_semut, data, data_jarak, data_jarak_awal, alpha, beta, Q):
    semut = []
    header = ["Semut ke", "Jalur", "Jumlah Jarak", "Delta"]
    semut.append(header)
    
    for i in range(jumlah_semut):
        jalur = pencarian_jalur_semut(data_jarak, data_jarak_awal, alpha, beta)
        jarak = nilai_jumlah_jarak_jalur(jalur, data)
        semutke = [i+1, jalur, jarak, Q/jarak]
        semut.append(semutke)
    
    return semut

def nilai_pheromon_update(rho, nilai):
    return (1-rho)*nilai

def matrik_pheromon_baru(rho, data_jarak_awal):
    matrik_pheromon = []
    for i in range(len(data_jarak_awal)):
        array_pheromon = []
        for j in range(len(data_jarak_awal[i])):
            if (i == 0):
                array_pheromon.append(data_jarak_awal[i][j])
            elif(j == 0):
                array_pheromon.append(data_jarak_awal[i][j])
            else:
                array_pheromon.append(nilai_pheromon_update(rho, data_jarak_awal[i][j]))
        matrik_pheromon.append(array_pheromon)
    return matrik_pheromon

def update_pheromon_tertentu(data_jarak_awal, jalur_semut):
    data_kota = []
    for i in range(1, len(data_jarak_awal)):
        data_kota.append(data_jarak_awal[0][i])
    
    counter_jalur = []
    
    for i in range(len(data_kota)):
        for j in range(len(data_kota)):
            if i != j :
                index = []
                dua_jalur = data_kota[i]+"-"+data_kota[j]
                for k in range(1, len(jalur_semut)):
                    if dua_jalur in jalur_semut[k][1]:
                        index.append(k)
                counter_jalur.append([dua_jalur, index])
    
    for i in range(len(counter_jalur)):
        kota = counter_jalur[i][0].split("-")
        jumlah_delta = 0
        for j in range(len(counter_jalur[i][1])):
            jumlah_delta+=jalur_semut[counter_jalur[i][1][j]][3]
        
        for j in range(len(data_jarak_awal)):
            if data_jarak_awal[j][0] in kota[0]:
                for k in range(len(data_jarak_awal[j])):
                    if data_jarak_awal[0][k] in kota[1]:
                        data_jarak_awal[j][k] += jumlah_delta
                
    return data_jarak_awal

def kondisi_cek_jalur(jalur_semut):
    for i in range(1, len(jalur_semut)-1):
        if jalur_semut[i][1] not in jalur_semut[i+1][1]:
            return True
    return False

def index_terbaik(jalur_semut):
    jarak_terkecil = jalur_semut[1][2]
    index = 1
    for i in range(1, len(jalur_semut)):
        if jalur_semut[i][2] < jarak_terkecil:
            index = i
            jarak_terkecil = jalur_semut[i][2]
    return index

def start_ant_colony(jumlah_iterasi, banyak_semut, data, alpha = 1, beta = 1, rho = 0.5, tho = 0.01, Q = 1, cetak = True):

    data_jarak = matrik_data_jarak(data)
    
    data_jarak_awal = matrik_data_jarak_awal(data, tho)
    
    if cetak:
        print ('DATA JARAK')
        print_texttable(data)
        
        print ('DATA JARAK ETA')
        print_texttable(data_jarak)
        
        print ('DATA JARAK AWAL THO')
        print_texttable(data_jarak_awal)
    
    counter = 1
    
    lanjut = True
    
    while counter <= jumlah_iterasi and lanjut:
        jalur_semut = iterasi_setiap_semut(banyak_semut, data, data_jarak, data_jarak_awal, alpha, beta, Q)
        data_jarak_awal = matrik_pheromon_baru(rho, data_jarak_awal)
        data_jarak_awal = update_pheromon_tertentu(data_jarak_awal, jalur_semut)
        
        if cetak:
            print("\n---------- ITERASI KE-", counter , " ----------")
            print ('JALUR YANG DILEWATI MASING-MASING SEMUT')
            print_texttable(jalur_semut)
            print ('DATA JARAK AWAL THO (EVAPORASI)')
            print_texttable(data_jarak_awal)
            print ('DATA JARAK AWAL THO (UPDATED PHEROMON)')
            print_texttable(data_jarak_awal)
        
        counter+=1
        
        lanjut = kondisi_cek_jalur(jalur_semut)
    
    index_baik = index_terbaik(jalur_semut)
    
    return {"jalur" : jalur_semut[index_baik][1], "jarak" : jalur_semut[index_baik][2], "iterasi" : counter-1}