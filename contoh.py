from KoloniSemut import Semut

ncmax = 1000000 #jumlah iterasi
m = 100 #banyak semut
rho = 0.5
tho = 0.01
alpha = 1
beta = 1
Q = 1

koordinatKota = {"A" : [10, 0],
                 "B" : [9, 9],
                 "C" : [0, 0],
                 "D" : [5, 5],
                 "E" : [2, 3]}

#data = Semut.data_dari_excel("Data Jarak.xlsx")

data = Semut.data_koordinat(koordinatKota)

ant_colony = Semut.start_ant_colony(ncmax, m, data, alpha, beta, rho, tho, Q, cetak = True)

print("\n-------------------- JALUR TERBAIK --------------------")
print(ant_colony["jalur"])
print("-------------------- JARAK --------------------")
print(ant_colony["jarak"])
print("-------------------- JUMLAH ITERASI --------------------")
print(ant_colony["iterasi"])