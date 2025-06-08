# 🌾 Rice Leaf Disease Classifier

**Proyek Tugas Akhir - Mata Kuliah Pengenalan Pola**  
Menggunakan Deep Learning (ResNet50) untuk Klasifikasi Gambar Daun Padi

---

## 🧠 Deskripsi Proyek

Proyek ini mengimplementasikan **klasifikasi citra daun padi** menggunakan **Convolutional Neural Network (CNN)** berbasis arsitektur **ResNet50**. Aplikasi GUI elegan dibangun dengan `Tkinter`, yang memungkinkan pengguna memilih gambar daun dan mendapatkan prediksi jenis penyakit yang diderita tanaman.

> Proyek ini ditujukan untuk membantu deteksi dini penyakit pada tanaman padi secara otomatis berbasis visual, sebagai bagian dari pengaplikasian *pattern recognition* dalam bidang pertanian cerdas (*smart farming*).

---
## 📸 File .keras

(https://drive.google.com/file/d/12HdnkY9k2kQgG09OixVDsKLN2UW-fwx3/view?usp=sharing)



---

## 🔍 Kelas Penyakit yang Dideteksi

| Label                  | Penjelasan                                                                 |
|------------------------|---------------------------------------------------------------------------|
| **Bacterial leaf blight** | Penyakit akibat infeksi bakteri yang menyebabkan bercak coklat pada daun. |
| **Brown spot**         | Ditandai dengan munculnya bintik-bintik berwarna coklat pada permukaan daun. |
| **Leaf smut**          | Penyakit jamur yang memunculkan garis-garis atau bercak gelap memanjang.     |

---

## 🛠️ Teknologi yang Digunakan

- **TensorFlow / Keras** – Untuk pelatihan dan pemanggilan model deep learning.
- **Pillow (PIL)** – Untuk pemrosesan dan penampilan gambar.
- **Tkinter** – Untuk membangun GUI interaktif yang ringan dan portabel.
- **Python 3.9+**

---

## 🚀 Cara Menjalankan

1. Clone repositori ini:
    ```bash
    git clone https://github.com/el-rozi/classification-of-rice-diseases.git
    cd classification-of-rice-diseases
    ```

2. Install dependensi:
    ```bash
    pip install tensorflow pillow
    ```

3. Jalankan aplikasi GUI:
    ```bash
    python gui_app.py
    ```

---

## 📁 Struktur Folder

| File | Deskripsi |
|------|-----------|
| `best_resnet_model.keras` | Model deep learning hasil training (ResNet50) |
| `gui_app.py` | Aplikasi GUI berbasis Tkinter |
| `klasifikasi_penyakit_pada_tanaman_padi.ipynb` | Notebook eksplorasi awal & visualisasi |
| `README.md` | Dokumentasi proyek |



---

## 🎓 Kontribusi Mahasiswa

- **Nama**: Muhammad Fakhrur Rozi – **NIM**: 202351090  
- **Nama**: Iqbal Saiful Amri – **NIM**: 202351093  
- **Mata Kuliah**: Pengenalan Pola  
- **Dosen Pengampu**: Endang Supriyati, S.Kom., M.Kom.

---

## 📬 Lisensi

MIT License. Bebas digunakan untuk pembelajaran dan pengembangan lanjutan.

> _"Pattern Recognition bukan sekadar teori — ia dapat menyelamatkan hasil panen."_


