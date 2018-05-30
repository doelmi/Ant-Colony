from semut import Semut

ncmax = 1000000
m = 100
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


Semutku = Semut()

#data = Semutku.data_koordinat(koordinatKota)

data = Semutku.data_dari_excel("Data Jarak.xlsx")

ant_colony = Semutku.antcolony(ncmax, m, data)

print("\n-------------------- JALUR TERBAIK --------------------")
print(ant_colony["jalur"])
print("-------------------- JARAK --------------------")
print(ant_colony["jarak"])
print("-------------------- JUMLAH ITERASI --------------------")
print(ant_colony["iterasi"])