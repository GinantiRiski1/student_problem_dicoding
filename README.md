# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya-Jaya Institut

## 🧠 Business Understanding

**Jaya Jaya Institut** merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan telah mencetak banyak lulusan berkualitas. Namun, mereka menghadapi permasalahan serius berupa **tingginya angka siswa yang dropout** (tidak menyelesaikan studinya). Hal ini berdampak pada reputasi institusi dan efektivitas operasional pendidikan.

### ❗ Permasalahan Bisnis

Berikut adalah daftar permasalahan bisnis yang ingin diselesaikan melalui proyek ini:
1.	Berapa total jumlah mahasiswa yang terdaftar?
2.	Berapa jumlah mahasiswa yang telah dropout?
3.	Berapa persentase dropout dibandingkan total mahasiswa?
4.	Jurusan apa yang memiliki angka dropout tertinggi?
5.	Bagaimana sebaran dropout berdasarkan pekerjaan orang tua (ayah dan ibu)?
6.	Apakah tingkat pendidikan orang tua berpengaruh terhadap risiko dropout?
7.	Apakah mode pendaftaran tertentu (Application_mode) cenderung menghasilkan lebih banyak dropout?
8.	Apakah nilai masuk (Admission_grade) memengaruhi kemungkinan dropout?
9.	Bagaimana hubungan antara jumlah mata kuliah yang disetujui/diulang dengan status dropout?
10.	Apakah jumlah evaluasi atau nilai semester pertama/kedua memengaruhi dropout?
11.	Apakah tingkat pengangguran (Unemployment_rate) berkorelasi dengan dropout?
12.	Apakah GDP turut memengaruhi tingkat dropout mahasiswa?
13.	Apakah inflasi nasional turut memengaruhi tingkat dropout mahasiswa?


### 🔍 Cakupan Proyek

Proyek ini mencakup beberapa tahap dan deliverables berikut:

- Data preparation dan data cleaning awal untuk memastikan kualitas data yang akan dianalisis.
- Membangun model machine learning menggunakan algoritma Random Forest untuk memprediksi status siswa (dropout, enrolled, graduated) berdasarkan berbagai faktor yang tersedia.
- Analisis feature importance dari model yang telah dilatih untuk menentukan variabel-variabel paling berpengaruh dalam prediksi status mahasiswa.
- Exploratory Data Analysis (EDA) untuk memahami lebih dalam pola dropout dan faktor-faktor penyebab melalui visualisasi data di Metabase.
- Membuat business dashboard di Metabase untuk menyajikan insight dari hasil analisis secara visual dan interaktif.
- Deployment model machine learning ke dalam aplikasi berbasis web menggunakan Streamlit yang dapat digunakan untuk memprediksi status mahasiswa.
- Penyusunan insight dan rekomendasi berbasis data untuk membantu manajemen institusi dalam pengambilan keputusan strategis.
- Pembuatan laporan presentasi dan video berdurasi 4 menit untuk menyampaikan hasil analisis kepada stakeholder secara ringkas dan informatif.


---

## ⚙️ Persiapan

### Preparation

**Data source:**
[Students' Performance data](https://doi.org/10.24432/C5MC89 'UCI Machine Learning - Predict Students Dropout and Academic Success')

**Setup environment:**

1. Clone this Repository
   ```bash
   git clone https://github.com/GinantiRiski1/student_problem.git
   ```

2. Create Python Virtual Environment
   ```bash
   virtualenv venv
   ```

2. Activate the Environment
   ```bash
   venv\Scripts\activate
   ```

4. Install All the Requirements Inside "requirements.txt"
   ```bash
   pip install -r requirements.txt
   ```

---

## 📊 Business Dashboard

## Business Dashboard

Dashboard bisnis yang dibuat bertujuan untuk memberikan gambaran menyeluruh tentang performa mahasiswa di Jaya-Jaya Institut, dengan fokus utama pada analisis dropout. Dashboard ini dibuat menggunakan Metabase dan dirancang agar dapat diakses dan dipahami dengan mudah oleh stakeholder non-teknis.

![WhatsApp Image 2025-05-08 at 16 59 39_ec76b1aa](https://github.com/user-attachments/assets/770babd3-6cb2-478e-9c0b-c164d6cc4d18)

![WhatsApp Image 2025-05-08 at 16 59 40_b4a0198c](https://github.com/user-attachments/assets/8e28520e-adaf-4440-b035-fa0154963b76)

Dashboard mencakup beberapa komponen visual utama, antara lain:

- **Jumlah total mahasiswa, jumlah dropout, dan persentase dropout.**
- **Distribusi dropout berdasarkan jurusan, jalur pendaftaran, dan pekerjaan orang tua.**
- **Hubungan antara nilai masuk, nilai semester, dan dropout.**
- **Pengaruh faktor eksternal seperti GDP, tingkat pengangguran, dan inflasi terhadap dropout.**

Dashboard ini membantu pihak manajemen untuk:

- Mengidentifikasi jurusan atau jalur masuk dengan tingkat risiko dropout tertinggi.
- Mengenali pengaruh latar belakang keluarga dan kondisi ekonomi terhadap keberhasilan studi.
- Merancang kebijakan atau intervensi berbasis data untuk menurunkan angka dropout.

📊 [Klik untuk melihat dashboard](http://localhost:3000/public/dashboard/23cfb2c0-bc07-47cc-a407-fa5259df11e1)

> *Catatan: Link di atas hanya dapat diakses di lingkungan lokal/metabase host terkait.*

> [!NOTE]
> Video singkat penjelasan business dashboard dan kesimpulannya dapat dilihat pada tautan [YouTube ini](https://youtu.be/FcmiS-Oo1xc 'Jaya Jaya Institute Students Dashboard').

---

## 🤖 Menjalankan Sistem Machine Learning

Sistem machine learning dibangun menggunakan pendekatan **supervised classification** dengan model **Random Forest Classifier**.  

### 💻 Cara menjalankan prototype:
```bash
# Pastikan dependencies sudah terinstal
streamlit run app.py
```
## 🤖 Link Prototype yang Dapat Diakses

✅ [https://jaya-edutech-predictor.streamlit.app](https://jaya-edutech-predictor.streamlit.app)  
_(Ganti dengan URL asli jika sudah kamu hosting di Streamlit Cloud)_

---

## Conclusion

Melalui analisis data mahasiswa Jaya-Jaya Institut dan visualisasi dalam dashboard interaktif, kami berhasil menjawab 13 pertanyaan utama terkait dropout mahasiswa. Berikut kesimpulan dari tiap permasalahan:

1. **Total mahasiswa terdaftar** adalah 4.424 orang.
2. **Jumlah mahasiswa dropout** tercatat sebanyak 1.421 orang.
3. **Persentase dropout** dari keseluruhan mahasiswa adalah 32,12%.
4. **Jurusan dengan angka dropout tertinggi** adalah Management (evening attendance), diikuti oleh Informatics Engineering dan Management reguler.
5. **Dropout berdasarkan pekerjaan orang tua** menunjukkan distribusi yang tinggi pada jenis pekerjaan tertentu dengan penghasilan tidak tetap.
6. **Tingkat pendidikan orang tua** yang rendah (dasar dan menengah) cenderung berkorelasi dengan risiko dropout yang lebih tinggi.
7. **Mode pendaftaran** tertentu seperti "1st phase - general contingent" dan "Over 23 years old" memiliki angka dropout tertinggi.
8. **Nilai masuk (Admission Grade)** yang rendah terlihat pada mahasiswa dengan status dropout dibandingkan dengan yang lulus atau masih terdaftar.
9. **Jumlah mata kuliah yang disetujui atau diulang** memiliki hubungan kuat terhadap status dropout; mahasiswa dropout cenderung gagal di lebih banyak mata kuliah.
10. **Nilai rata-rata semester pertama dan kedua** mahasiswa dropout secara signifikan lebih rendah dibandingkan yang masih aktif atau telah lulus.
11. **Tingkat pengangguran** menunjukkan tren peningkatan dropout seiring naiknya angka pengangguran.
12. **GDP** yang rendah berkorelasi dengan peningkatan dropout, kemungkinan disebabkan oleh tekanan ekonomi.
13. **Inflasi** yang tinggi juga menunjukkan hubungan dengan kenaikan jumlah mahasiswa yang dropout.

Temuan-temuan ini menunjukkan bahwa dropout tidak hanya dipengaruhi oleh faktor akademik internal, tetapi juga oleh faktor sosial-ekonomi mahasiswa. Analisis ini memberikan landasan kuat untuk strategi pencegahan dropout berbasis data.

### Rekomendasi Action Items

Berikut beberapa rekomendasi tindakan yang dapat dilakukan oleh pihak institusi:

- **Identifikasi dan dukung mahasiswa berisiko** melalui program mentoring atau bimbingan belajar sejak awal perkuliahan.
- **Optimalkan jalur penerimaan mahasiswa** dengan melakukan evaluasi pada mode pendaftaran yang menunjukkan dropout tinggi.
- **Perkuat keterlibatan orang tua** terutama pada latar belakang dengan pendidikan rendah untuk mendukung keberlangsungan studi anaknya.
- **Manfaatkan sistem prediksi dropout** sebagai alat bantu dalam proses konseling akademik dan manajemen risiko.
- **Bangun skema dukungan keuangan** dan kebijakan adaptif untuk menghadapi dampak ekonomi eksternal seperti inflasi dan pengangguran.

---

link akses metabase :
- username : ginantiriski@gmail.com
- password : Aaaaa10&25
