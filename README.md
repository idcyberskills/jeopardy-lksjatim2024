# Repositori LKS Jawa Timur CTF 2024

---

## Struktur Template
**Untuk pembuat soal**

Disediakan *template* pada folder `template/` agar memudahkan pembuatan soal. Silakan *copy* ke dalam folder kategori masing-masing dan diberi nama folder `judul-soal`. Strukturnya adalah sebagai berikut:
```
judul-soal/
 ├─ public/
 ├─ src/
 ├─ writeup/
 │   └─ README.md
 ├─ Dockerfile
 ├─ docker-compose.yml
 └─ README.md
```

Keterangan:
- `public/` 		: Seluruh file di folder ini akan di-zip dan menjadi attachment untuk peserta
- `src/`    		: Berisi file-file yang menjadi soal
- `writeup/`		: Berisi file-file yang menunjukkan solusi/PoC dari soal
- `Dockerfile` dan docker-compose.yml hanya untuk soal yang butuh di-*deploy*
- Update `README.md`


---

### Contoh README.md

---

# NAMASOAL

by nama_problem_setter

---

## Flag

```
LKSJATIM{str1n9s_4l4y_at4u_h4sh_a23b456d7f8a9f000001020bf5f6}
```

## Description
Deskripsi SOAL disini

(Optional)File : https://mega.nz/file/a2oixaib#Y7hu00KLlvhqVV43BzYYKcqxy8hEkUbZ1iL2rDg2wCM

## Difficulty
easy/medium/hard

## Hints
* Hint Pertama
* Hint Kedua
* Hint Ketiga
* Hint ke-n (max)

## Tags
tag soal (optional)
