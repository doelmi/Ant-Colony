# AntColony
Implementasi Ant Colony pada pencarian jalur terdekat di semua kecamatan di Bangkalan. Menggunakan bahasa Python 3

## Penggunaan

### Instal dependency
Instal terlebih dahulu library 'texttable'
```
pip install texttable
```

Lalu library 'xlrd'
```
pip install xlrd
```

### Penempatan
Tempatkan file semut.py di dalam folder project kamu.

### Pemanggilan
Pertama, impor dulu file semut.py ke dalam file kamu dengan menggunakan 
```
from semut import Semut
```

Setelah itu, inisialisasi sebuah variabel dan isikan fungsi Semut()
```
Semutku = Semut()
```

Fungsi Semut() memiliki parameter-parameter berikut namun bernilai default: <br>
<ul>
<li>rho = 0.5</li>
<li>tho = 0.01</li>
<li>alpha = 1</li>
<li>beta = 1</li>
<li>Q = 1</li>
<li>cetak = True</li>
</ul>

Jika kamu ingin mengganti salah satunya
```
Semutku = Semut(tho = 0.02)
```

Jika mengganti lebih dari satu
```
Semutku = Semut(alpha = 3, beta = 3, rho = 0.6)
```

Maksud dari parameter cetak adalah apabila bernilai True maka seluruh nilai setiap iterasi akan dicetak. Akan sebaliknya jika bernilai False.

### Inisialisasi Data
#### Data dari file Excel
Jika kamu ingin menggunakan dari file excel, maka gunakan format yang telah disediakan. File 'Data Jarak.xlsx'. Cara menggunakannya adalah
```
nama_file = "Data Jarak.xlsx"
data = Semutku.data_dari_excel(nama_file)
```

Default index yang digunakan adalah index ke 0, namun bisa juga mengeset index sheet spesifik
```
nama_file = "Data Jarak.xlsx"
sheet_index = 2
data = Semutku.data_dari_excel(nama_file, sheet_index)
```

#### Data dari koordinat
Data dari koordinat harus sesuai dengan format berikut
```
koordinatKota = {"A" : [10, 0],
                 "B" : [9, 9],
                 "C" : [0, 0],
                 "D" : [5, 5],
                 "E" : [2, 3]}
```

Kemudian panggil fungsi untuk mem-parse data koordinat tersebut ke dalam format yang diterima program ini.

```
data = Semutku.data_koordinat(koordinatKota)
```

### Memanggil Fungsi Utama
Fungsi utama ini memiliki parameter : <br>
<ul>
<li>jumlah_iterasi</li>
<li>banyak_semut</li>
<li>data</li>
</ul>

Cara memanggilnya yaitu
```
jumlah_iterasi = 100
banyak_semut = 10

ant_colony = Semutku.antcolony(jumlah_iterasi, banyak_semut, data)
```

Memiliki nilai kembalian 
<ul>
<li>Jalur Terbaik -> ant_colony["jalur"]</li>
<li>Jarak Terpendek -> ant_colony["jarak"]</li>
<li>Jumlah Iterasi yang dilakukan -> ant_colony["iterasi"]</li>
</ul>

## Penerapan
### Contoh kode simpel untuk data dari koordinat
```
from semut import Semut
koordinatKota = {"A" : [10, 0],
                 "B" : [9, 9],
                 "C" : [0, 0],
                 "D" : [5, 5],
                 "E" : [2, 3]}
Semutku = Semut()
data = Semutku.data_koordinat(koordinatKota)
ant_colony = Semutku.antcolony(100, 10, data)
```

### Contoh kode simpel data dari file
```
from semut import Semut
Semutku = Semut()
data = Semutku.data_dari_excel("Data Jarak.xlsx")
ant_colony = Semutku.antcolony(100, 10, data)
```

## Hasil Running

Hasil Running apabila dicetak dengan
```
print("\n-------------------- JALUR TERBAIK --------------------")
print(ant_colony["jalur"])
print("-------------------- JARAK --------------------")
print(ant_colony["jarak"])
print("-------------------- JUMLAH ITERASI --------------------")
print(ant_colony["iterasi"])
```

maka dihasilkan
````
-------------------- JALUR TERBAIK --------------------
Kamal-Socah-Bangkalan-Burneh-Tragah-Kwanyar-Labang-Tanah Merah-Galis-Blega-Modung-Konang-Kokop-Tanjung Bumi-Sepuluh-Klampis-Arosbaya-Geger
-------------------- JARAK --------------------
194.0
-------------------- JUMLAH ITERASI --------------------
46
````
