### Jarak untuk **Atribut Campuran**

**Gower Distance versi manual**

Secara teori:

$d(i,j) = \frac{\sum_{f=1}^{p} \delta^{(f)}*{ij} ; d^{(f)}*{ij}}
{\sum_{f=1}^{p} \delta^{(f)}_{ij}}$

* (f) = atribut ke-f
* ($\delta^{(f)}_{ij}$) = bobot (biasanya 1 jika tidak missing)
* ($d^{(f)}_{ij}$) = jarak atribut ke-f

---

#### Persiapan: Definisi Tipe Atribut

```python
import pandas as pd
import numpy as np

df = pd.read_csv("data/College-Distance-Data.csv")

num_cols = ['score','unemp','wage','distance','tuition','education']
binary_cols = ['gender','ethnicity','fcollege','mcollege','home','urban']
ordinal_cols = ['income']
nominal_cols = ['region']
```

---

#### Normalisasi Numerik

```python
df_num_norm = df[num_cols].copy()
for col in num_cols:
    df_num_norm[col] = (
        df[col] - df[col].min()
    ) / (df[col].max() - df[col].min())
```
---

#### Ordinal → Ranking → Skala Interval

Sesuai slide:
$z_{if} = \frac{r_{if}-1}{M_f - 1}$

```python
income_order = ['low', 'middle', 'high']
df['income_rank'] = df['income'].apply(lambda x: income_order.index(x) + 1)

M = len(income_order)
df['income_norm'] = (df['income_rank'] - 1) / (M - 1)
```

---

#### Biner & Nominal → Matching Distance

```python
def binary_nominal_distance(x, y):
    return 0 if x == y else 1
```

---

## Fungsi **Jarak Atribut Campuran**

```python
def mixed_distance(df, i, j):
    num_dist = 0
    bin_dist = 0
    ord_dist = 0
    nom_dist = 0
    
    w_num = w_bin = w_ord = w_nom = 0

    # Numerik
    for col in num_cols:
        num_dist += abs(df_num_norm.loc[i, col] - df_num_norm.loc[j, col])
        w_num += 1

    # Biner
    for col in binary_cols:
        bin_dist += binary_nominal_distance(df.loc[i, col], df.loc[j, col])
        w_bin += 1

    # Ordinal
    ord_dist = abs(df.loc[i, 'income_norm'] - df.loc[j, 'income_norm'])
    w_ord = 1

    # Nominal
    for col in nominal_cols:
        nom_dist += binary_nominal_distance(df.loc[i, col], df.loc[j, col])
        w_nom += 1

    total_dist = num_dist + bin_dist + ord_dist + nom_dist
    total_weight = w_num + w_bin + w_ord + w_nom

    return total_dist / total_weight
```

---

## Contoh Perhitungan (Objek 0 dan 4)

```python
d_04 = mixed_distance(df, 0, 4)
print("Mixed Attribute Distance (0,4):", d_04)
```