def hitung_probabilitas_pergerakan_ratu(papan_catur, posisi_ratu):
    def is_valid(x, y):
        return 0 <= x < 8 and 0 <= y < 8

    total_kemungkinan = 0

    # Daftar langkah yang bisa dilakukan oleh ratu catur
    langkahs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for langkah in langkahs:
        x, y = posisi_ratu
        dx, dy = langkah

        while True:
            x += dx
            y += dy

            if not is_valid(x, y):
                break

            total_kemungkinan += 1

            if papan_catur[x][y]:
                break

    return total_kemungkinan


# Contoh penggunaan program
if __name__ == "__main__":
    # Inisialisasi papan catur
    papan_catur = [[False for _ in range(8)] for _ in range(8)]

    # Contoh posisi ratu catur (misalnya pada baris 3, kolom 4)
    posisi_ratu = (3, 4)
    papan_catur[posisi_ratu[0]][posisi_ratu[1]] = True

    # Hitung probabilitas pergerakan ratu catur
    probabilitas = hitung_probabilitas_pergerakan_ratu(papan_catur, posisi_ratu)

    # Cetak hasil
    print(f"Probabilitas pergerakan pada ratu catur dari posisi {posisi_ratu} adalah {probabilitas}")
