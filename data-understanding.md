# Data Understanding

## 1. Deskripsi Dataset

Dataset yang digunakan adalah **Iris Dataset**, salah satu dataset klasik dalam machine learning untuk klasifikasi.

Dataset ini berisi **150 data bunga Iris** yang terbagi menjadi 3 spesies:

* Setosa
* Versicolor
* Virginica

Masing-masing spesies memiliki 50 data.

Dataset digunakan untuk menganalisis hubungan antar fitur morfologi bunga dan menentukan pola klasifikasi.

---

## 2. Sumber Data

Dataset diambil dari file:

```
IRIS.xlsx
```

Dianalisis menggunakan **Google Colab (Python)** dan divisualisasikan menggunakan:

* Pandas
* Matplotlib
* Seaborn

Notebook Colab:
[https://colab.research.google.com/drive/1jnM-gNHHCcz7odjE_hZMXnBusv0blv-J?usp=sharing](https://colab.research.google.com/drive/1jnM-gNHHCcz7odjE_hZMXnBusv0blv-J?usp=sharing)

---

## 3. Struktur Dataset

Dataset memiliki 5 atribut:

| No | Atribut      | Tipe Data | Keterangan                 |
| -- | ------------ | --------- | -------------------------- |
| 1  | sepal_length | float     | Panjang kelopak bunga (cm) |
| 2  | sepal_width  | float     | Lebar kelopak bunga (cm)   |
| 3  | petal_length | float     | Panjang mahkota bunga (cm) |
| 4  | petal_width  | float     | Lebar mahkota bunga (cm)   |
| 5  | species      | object    | Jenis spesies bunga        |

Jumlah data:

* 150 baris
* 5 kolom

---

## 4. Pemeriksaan Awal Data

### Membaca Data

```python
import pandas as pd

df = pd.read_excel('IRIS.xlsx')
df.head()
```

### Informasi Dataset

```python
df.info()
```

Hasil pemeriksaan menunjukkan:

* Tidak terdapat missing value
* Semua fitur numerik bertipe float
* Kolom species bertipe kategorikal

---

## 5. Statistik Deskriptif

```python
df.describe()
```

Ringkasan statistik:

* Rata-rata sepal_length ≈ 5.84 cm
* Rata-rata petal_length ≈ 3.76 cm
* Standar deviasi petal_length cukup tinggi
* Nilai minimum dan maksimum menunjukkan variasi yang signifikan antar spesies

Hal ini mengindikasikan bahwa fitur petal kemungkinan memiliki pengaruh besar dalam proses klasifikasi.

---

## 6. Distribusi Kelas

```python
df['species'].value_counts()
```

Hasil menunjukkan:

* Setosa = 50
* Versicolor = 50
* Virginica = 50

Dataset dalam kondisi **balanced**, sehingga tidak terjadi ketimpangan kelas.

---

## 7. Insight Awal

1. Dataset bersih dan siap dianalisis
2. Tidak ada data kosong
3. Distribusi kelas seimbang
4. Fitur petal_length dan petal_width memiliki variasi tinggi
5. Dataset cocok untuk:

   * Klasifikasi
   * Clustering
   * Analisis korelasi
