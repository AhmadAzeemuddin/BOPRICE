jenis_papan = ['Papan lapis kayu keras', 'Papan lapis Laut', 'Papan lapis Teras Lumber', 'Papan Zarah', 'Papan Fiberboard Ketumpatan Sederhana', 'Papan Baltic Birch']
harga_papan = [10,20,40,15,12,5]
jumlah = [0,1,2,3,4,5,6]
a = int(input("Masukkan tempahan untuk lapis kayu keras: "))
b = int(input("Masukkan tempahan untuk lapis Laut: "))
c = int(input("Masukkan tempahan untuk lapis Teras Lumber: "))
d = int(input("Masukkan tempahan untuk Zarah: "))
e = int(input("Masukkan tempahan untuk Fiberboard Ketumpatan Sederhana: "))
f = int(input("Masukkan tempahan untuk Baltic Birch: "))
tempahan = [a,b,c,d,e,f]


for i in range(6):
    jumlah[i] = harga_papan[i] * tempahan[i]
 
def cetak () :
    print("\n\nTempahan anda ialah:")
    print(a,"papan",jenis_papan[0])
    print(b,"papan",jenis_papan[1])
    print(c,"papan",jenis_papan[2])
    print(d,"papan",jenis_papan[3])
    print(e,"papan",jenis_papan[4])
    print(f,"papan",jenis_papan[5])
    print("\nJumlah harga untuk tempahan ialah RM",sum(jumlah))
