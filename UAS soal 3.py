def hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja):
    lembur = max(0, jam_kerja_per_hari - 8) * tarif_per_jam * 1.5
    normal = min(8, jam_kerja_per_hari) * tarif_per_jam
    return hari_kerja * (normal + lembur)

try:
    tarif = float(input("Masukkan tarif gaji per jam: "))
    jam_per_hari = float(input("Masukkan rata-rata jam kerja per hari: "))
    hari = int(input("Masukkan jumlah hari kerja dalam sebulan: "))
    print(f"Total gaji bulanan Anda adalah: Rp {hitung_gaji(tarif, jam_per_hari, hari):,.2f}")
except ValueError:
    print("Harap masukkan input yang valid!")
