# Tugas Besar 2  

## IF3140 Manajemen Basis Data

### IMPLEMENTASI MEKANISME CONCURRENCY CONTROL

#### 1. Dasar Teori

ACID (Atomicity Consistency Isolation Durability) merupakan empat hal yang
perlu dijaga oleh sebuah basis data. Untuk menjamin konsistensi dari basis data,
dibutuhkan proses concurrency control untuk menjamin konsistensi perubahan
data. Concurrency control dapat dilakukan dengan berbagai protokol.
Protokol-protokol yang dapat diterapkan antara lain :
1. Lock-Based Protocols
2. Timestamp-Based Protocols
3. Validation-Based Protocols
4. Multiversion Schemes

#### 2. Spesifikasi

Pada tugas besar ini, peserta kelas diharapkan melakukan eksplorasi algoritma
concurrency control. Adapun ketentuan tugas ini adalah sebagai berikut :
1. Tugas ini dikerjakan secara berkelompok. Satu kelompok beranggotakan empat
sampai enam orang sesuai kelompok presentasi.
2. Setiap kelompok melakukan implementasi algoritma dari berbagai protokol yang
telah ditentukan, yaitu :
     - Simple Locking (exclusive locks only)
     - Serial Optimistic Concurrency Control (OCC)
     - Multiversion Timestamp Ordering Concurrency Control
3. Setiap algoritma protokol concurrency control harus dicoba dan
didokumentasikan ke dalam laporan.
4. Referensi pengerjaan tugas bisa dilihat pada
     - https://github.com/dhatch/database-concurrency-control.
     - https://www.geeksforgeeks.org/timestamp-based-concurrency-control/

#### 3. Deliverables

Peserta diharapkan mengumpulkan :

a. laporan dalam format PDF yang berisi:

    i.  Cover Laporan yang berisi kode mata kuliah, nama mata kuliah, judul
        tugas, logo ITB, nama dan NIM anggota kelompok.
    ii. Dasar teori untuk pengerjaan tugas. Peserta dilarang melakukan copy
        paste langsung dari referensi, tetapi menulis dasar teori sesuai dengan
        pemahaman dan gaya penulisan sendiri.
    iii.Untuk setiap algoritma, sertakan :
        1. Screenshot hasil percobaan
        2. Hasil analisis dari algoritma yang diterapkan
    iv. Hasil analisis perbandingan setiap algoritma dan cantumkan algoritma
        terbaik menurut kelompok.
    v.  Kesimpulan dan Saran.
    vi. Pembagian kerja dalam kelompok.
    vii.Referensi.
        
b. Kode Program

c. Petunjuk cara menjalankan program

#### 4. Teknis Pengumpulan

Hal-hal relevan yang kurang jelas ataupun tidak dicantumkan pada berkas soal ini dapat
ditanyakan melalui milis. Peserta dianjurkan untuk menggunakan milis agar seluruh
informasi dapat tersebar dengan merata ke seluruh pihak yang terlibat. Seluruh
deliverables disatukan di dalam satu **file .zip** diunggah ke: http://bit.ly/Tugas2IF3140
dengan format penamaan **IF3140-Tugas2-<NIM_TERKECIL>.zip**

#### 5. Referensi

https://github.com/dhatch/database-concurrency-control