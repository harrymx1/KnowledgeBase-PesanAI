# Panduan Konfigurasi Intent Taxonomy & Answer Memory PesanAI (UM Helpdesk)

Dokumen ini mencatat standarisasi konfigurasi pada platform PesanAI (C-iCare AI / Mekari Qontak) untuk Universitas Negeri Malang, memisahkan antara Knowledge Base, Intent Routing, dan Answer Memory.

---

## 1. Arsitektur Pemisahan Tanggung Jawab

| Komponen di PesanAI | Peran & Tanggung Jawab | Lokasi Menu |
| :--- | :--- | :--- |
| **Knowledge Base** | Dokumen sumber kebenaran (Ground Truth) faktual untuk retrieval RAG. | `/manual/knowledge` |
| **Intent Taxonomy** | Klasifikasi intensi percakapan dan perutean (*routing*) ke departemen/antrian. | `/manual/intents` |
| **Answer Memory** | Pasangan tanya-jawab standar terverifikasi (L1/L2 cache matching) untuk respon instan tanpa halusinasi LLM. | `/manual/answer-memory` |
| **Instruksi Tenant AI** | Persona, gaya bahasa (sapaan 'Kak'), batasan layanan. *Dilarang memasukkan fakta bisnis di sini.* | `/manual/ai-settings` |

---

## 2. Konfigurasi Answer Memory (Verified Q&A)

### Entri 1: Jadwal & Status Pengisian KRS
- **Canonical Question:** `Apakah hari ini masih bisa mengisi KRS?`
- **Variasi Pertanyaan (Alternative Phrases):**
  - `Apakah sekarang masih bisa KRS?`
  - `Kapan jadwal pengisian KRS?`
  - `Apakah portal KRS masih dibuka?`
  - `Batas akhir pengisian KRS kapan?`
- **Jawaban Terverifikasi (Verified Answer):**
  ```text
  Jadwal Pengisian KRS Universitas Negeri Malang (Tahun Akademik 2026/2027):

  • Semester Gasal: 14 – 18 Agustus 2026
  • Semester Genap: 15 – 19 Januari 2027

  Pengisian KRS dilakukan secara mandiri melalui portal SIAKAD (siakad.um.ac.id) pada rentang tanggal tersebut. Jika Anda terlambat atau mengalami kendala KRS di luar jadwal, silakan hubungi Subag Akademik Fakultas masing-masing.
  ```
- **Intent Terkait:** `academic_krs_schedule`
- **Status:** `Verified / Aktif`

---

### Entri 2: Jadwal Pembayaran UKT & Registrasi Administrasi
- **Canonical Question:** `Kapan batas pembayaran UKT semester ini?`
- **Variasi Pertanyaan (Alternative Phrases):**
  - `Batas akhir bayar UKT kapan?`
  - `Jadwal registrasi administrasi dan bayar UKT`
  - `Kapan terakhir bayar kuliah semester gasal?`
- **Jawaban Terverifikasi (Verified Answer):**
  ```text
  Jadwal Pembayaran UKT / Registrasi Administrasi UM (Tahun Akademik 2026/2027):

  • Semester Gasal: 1 – 12 Agustus 2026
  • Semester Genap: 2 – 13 Januari 2027

  Pembayaran dapat dilakukan melalui bank mitra resmi UM (BNI, BRI, BTN, Mandiri, Bank Jatim) dengan memasukkan nomor tagihan SIAKAD.
  ```
- **Intent Terkait:** `academic_calendar_general`
- **Status:** `Verified / Aktif`

---

## 3. Konfigurasi Intent Taxonomy

### 1. `academic_krs_schedule`
- **Nama Intent:** Jadwal dan Pengisian KRS
- **Department Routing:** `Akademik`
- **Training Phrases:**
  - `jadwal krs`
  - `kapan krs dibuka`
  - `apakah masih bisa krs`
  - `batas pengisian krs gasal 2026`

### 2. `academic_calendar_general`
- **Nama Intent:** Kalender Akademik dan UKT
- **Department Routing:** `Akademik`
- **Training Phrases:**
  - `jadwal kalender akademik 2026`
  - `batas bayar ukt`
  - `kapan mulai perkuliahan`
  - `jadwal uts uas 2026`

---

## 4. File Knowledge Base Terkait
- [Kalender_Akademik_Resmi_UM_2026_2027.md](file:///c:/Users/LOQ/Downloads/Knowledge%20Base%20(Unggah%20Mekari)-20260916T225534Z-1-001/Knowledge%20Base%20(Unggah%20Mekari)/Knowledge_Base_Clean_Categorized/03_Akademik_dan_SIAKAD/Kalender_Akademik_Resmi_UM_2026_2027.md)
