# Data produk: id_produk -> harga
produk = {
    1: 12000000,
    2: 15000000,
    3: 1200000,
    4: 1800000,
    5: 90000,
    6: 75000,
    7: 25000000,
    8: 18000000,
    9: 199000,
    10: 3000000
}

id_pesanan_awal = 311
id_pesanan_maks = 7222

# Pola jumlah pembelian (berulang)
jumlah_pola = [2,1,3,1,2,3,1,2,1,2]

id_pesanan = id_pesanan_awal
rows = []

while id_pesanan <= id_pesanan_maks:
    for i, (id_produk, harga) in enumerate(produk.items()):
        if id_pesanan > id_pesanan_maks:
            break

        jumlah = jumlah_pola[i % len(jumlah_pola)]
        subtotal = harga * jumlah

        rows.append(
            f"({id_produk},{id_pesanan},{harga},{jumlah},{subtotal})"
        )
        id_pesanan += 1

# Tulis ke file .txt
with open("pesanan_item.txt", "w", encoding="utf-8") as file:
    file.write(
        "INSERT INTO pesanan_item "
        "(id_produk, id_pesanan, harga_saat_beli, jumlah, subtotal) VALUES\n"
    )
    file.write(",\n".join(rows))
    file.write(";")

print("File pesanan_item.txt berhasil dibuat")