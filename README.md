# Ant-Colony
Implementasi Ant Colony pada pencarian jalur terdekat di semua kecamatan di Bangkalan. Menggunakan bahasa Python 3

## Penggunaan

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
