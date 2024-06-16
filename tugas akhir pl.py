import datetime

class Peminjam:
    def __init__(self, nama_peminjam, alamat_peminjam, no_telepon_peminjam):
        self.nama_peminjam = nama_peminjam
        self.alamat_peminjam = alamat_peminjam
        self.no_telepon_peminjam = no_telepon_peminjam

class Buku:
    def __init__(self, nama_buku, pengarang_buku, tahun_terbit_buku, jumlah_buku):
        self.nama_buku = nama_buku
        self.pengarang_buku = pengarang_buku
        self.tahun_terbit_buku = tahun_terbit_buku
        self.jumlah_buku = jumlah_buku

class Peminjaman:
    def __init__(self, peminjam, buku, tanggal_peminjaman):
        self.peminjam = peminjam
        self.buku = buku
        self.tanggal_peminjaman = tanggal_peminjaman
        self.tanggal_pengembalian = None
        self.biaya_keterlambatan = 0

    def kembali_buku(self, tanggal_pengembalian):
        self.tanggal_pengembalian = tanggal_pengembalian
        keterlambatan = (tanggal_pengembalian - self.tanggal_peminjaman).days
        if keterlambatan > 7:
            self.biaya_keterlambatan = 500 * (keterlambatan - 7)
        elif keterlambatan > 14:
            self.biaya_keterlambatan = 1000 * (keterlambatan - 14)

class Perpustakaan:
    def __init__(self):
        self.peminjam = []
        self.buku = []
        self.peminjaman = []

    def tambah_peminjam(self, nama_peminjam, alamat_peminjam, no_telepon_peminjam):
        peminjam = Peminjam(nama_peminjam, alamat_peminjam, no_telepon_peminjam)
        self.peminjam.append(peminjam)

    def tambah_buku(self, nama_buku, pengarang_buku, tahun_terbit_buku, jumlah_buku):
        buku = Buku(nama_buku, pengarang_buku, tahun_terbit_buku, jumlah_buku)
        self.buku.append(buku)

    def pinjam_buku(self, peminjam, buku, tanggal_peminjaman):
        peminjaman = Peminjaman(peminjam, buku, tanggal_peminjaman)
        self.peminjaman.append(peminjaman)

    def kembali_buku(self, peminjaman, tanggal_pengembalian):
        peminjaman.kembali_buku(tanggal_pengembalian)

    def tampilkan_peminjaman(self):
        for peminjaman in self.peminjaman:
            print(f"Nama Peminjam: {peminjaman.peminjam.nama_peminjam}")
            print(f"Nama Buku: {peminjaman.buku.nama_buku}")
            print(f"Tanggal Peminjaman: {peminjaman.tanggal_peminjaman}")
            print(f"Tanggal Pengembalian: {peminjaman.tanggal_pengembalian}")
            print(f"Biaya Keterlambatan: {peminjaman.biaya_keterlambatan}")
            print("")

perpustakaan = Perpustakaan()

while True:
    print("Menu:")
    print("1. Tambah Peminjam")
    print("2. Tambah Buku")
    print("3. Pinjam Buku")
    print("4. Kembali Buku")
    print("5. Tampilkan Peminjaman")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama_peminjam = input("Nama Peminjam: ")
        alamat_peminjam = input("Alamat Peminjam: ")
        no_telepon_peminjam = input("No. Telepon Peminjam: ")
        perpustakaan.tambah_peminjam(nama_peminjam, alamat_peminjam, no_telepon_peminjam)
    elif pilihan == "2":
        nama_buku = input("Nama Buku: ")
        pengarang_buku = input("Pengarang Buku: ")
        tahun_terbit_buku = int(input("Tahun Terbit Buku: "))
        jumlah_buku = int(input("Jumlah Buku: "))
        perpustakaan.tambah_buku(nama_buku,pengarang_buku, tahun_terbit_buku, jumlah_buku)
    elif pilihan == "3":
        nama_peminjam = input("Nama Peminjam: ")
        nama_buku = input("Nama Buku: ")
        tanggal_peminjaman = datetime.date.today()
        peminjam = next((p for p in perpustakaan.peminjam if p.nama_peminjam == nama_peminjam), None)
        buku = next((b for b in perpustakaan.buku if b.nama_buku == nama_buku), None)
        if peminjam and buku:
            perpustakaan.pinjam_buku(peminjam, buku, tanggal_peminjaman)
        else:
            print("Peminjam atau buku tidak ditemukan!")
    elif pilihan == "4":
        nama_peminjam = input("Nama Peminjam: ")
        nama_buku = input("Nama Buku: ")
        tanggal_pengembalian = datetime.date.today()
        peminjaman = next((p for p in perpustakaan.peminjaman if p.peminjam.nama_peminjam == nama_peminjam and p.buku.nama_buku == nama_buku), None)
        if peminjaman:
            perpustakaan.kembali_buku(peminjaman, tanggal_pengembalian)
        else:
            print("Peminjaman tidak ditemukan!")
    elif pilihan == "5":
        perpustakaan.tampilkan_peminjaman()
    elif pilihan == "6":
        break
    else:
        print("Menu tidak tersedia!")