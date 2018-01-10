nama = []
nim = []
kelas = []
jurusan = []

def tambahdata():
    a = int(input("Jumlah Entry Data : "))
    b = 1
    for i in range(int(a)):
        print("data ke- :"+ str(b))
        na = input("Masukkan Nama   :")
        ni = input("masukkan NIM    :")
        ke = input("Masukkan Kelas  :")
        ju = input("Masukkan Jurusan:")
        b += 1
        nama.append(na)
        nim.append(ni)
        kelas.append(ke)
        jurusan.append((ju))

def tampil():
    print("Nama     : ",nama)
    print("NIM      : ",nim)
    print("Kelas    : ",kelas)
    print("Jurusan  : ",jurusan)

tambahdata()
a = input("tampilkan data ? y/n")
if a == 'y':
    tampil()
else:
    print("exit program")

