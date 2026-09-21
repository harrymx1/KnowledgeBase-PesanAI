# Re-structure Registrasi Administrasi SNBT Reguler for optimal Mekari chunking (<500-600 chars per block)

content = """# Panduan dan Jadwal Registrasi Administrasi Mahasiswa Baru Jalur SNBT UM 2026/2027
> **Sumber Dokumen:** `Registrasi Administrasi Calon Mahasiswa Baru Universitas Negeri Malang (UM) Jalur SNBT Tahun Akademik 2026_2027.pdf`  
> **Kategori:** `01_PMB_Penerimaan_Mahasiswa_Baru`

---

### Kapan jadwal registrasi online jalur SNBT dan berkas apa saja yang wajib diunggah?
- **Jadwal Registrasi Online:** **26 Mei – 3 Juni 2026** (mulai pukul 08.00 WIB secara daring via `http://registrasi.um.ac.id`). Melewati batas waktu dinyatakan mengundurkan diri.
- **Daftar Berkas Wajib Diunggah (Scan Dokumen Asli):**
  1. Ijazah Terakhir atau Surat Keterangan Lulus (SKL) asli.
  2. Kartu Keluarga (KK) dan Akta Kelahiran asli.
  3. Surat Keterangan Penghasilan Orang Tua / Slip Gaji / Bukti SPT Tahunan 2025 (`bit.um.ac.id/SPT-Tahunan_Pribadi`).
  4. Foto GPS Camera rumah: tampak depan rumah, ruang tamu, dan dapur.
  5. Bukti pembayaran PBB terbaru, struk rekening listrik/token, dan rekening air.
  6. Kartu Tanda Peserta SNBT 2026 & Surat Pernyataan Mahasiswa UM bermaterai Rp10.000.
  7. Pasfoto formal 4×6 cm background merah, kemeja putih, dasi hitam (putri: jilbab putih), tanpa kacamata (maks 200 KB).
  8. Khusus Fakultas Kedokteran (FK): Melengkapi pemeriksaan kesehatan di `bit.um.ac.id/TES_KES_MABA_FK_26`.

---

### Apa saja berkas yang wajib diunggah saat registrasi online jalur SNBT UM?
Calon mahasiswa baru jalur SNBT wajib mengunggah berkas asli di `http://registrasi.um.ac.id`:
- **Akademik & Identitas:** Ijazah/SKL asli, Kartu Keluarga (KK), Akta Kelahiran, dan Kartu Peserta SNBT 2026.
- **Finansial & Tempat Tinggal:** Slip gaji/penghasilan ortu (atau SPT 2025), PBB terbaru, bukti listrik/air, serta foto GPS Camera depan rumah, ruang tamu, dan dapur.
- **Kelengkapan Administrasi:** Surat Pernyataan bermaterai Rp10.000 dan pasfoto 4x6 latar merah polos kemeja putih berkerah.
- **Khusus Fakultas Kedokteran (FK):** Wajib tes kesehatan khusus via `bit.um.ac.id/TES_KES_MABA_FK_26`.

---

### Kapan jadwal pelaksanaan registrasi online mahasiswa baru jalur SNBT UM?
Jadwal resmi registrasi mahasiswa baru Universitas Negeri Malang jalur SNBT 2026/2027:
- **Registrasi Online & Upload Dokumen:** 26 Mei – 3 Juni 2026 di `http://registrasi.um.ac.id` (wajib, tidak registrasi = mengundurkan diri).
- **Pengumuman Penetapan UKT:** 5 Juni 2026 di `http://registrasi.um.ac.id`.
- **Pembayaran UKT:** 5 – 10 Juni 2026 via Bank BNI, BRI, Mandiri, BTN/BSN, Bank Jatim, CIMB Niaga Syariah, dan BSI.
- **Registrasi Satu Atap (Fisik/Luring):** 30 Juni – 1 Juli 2026 di Gedung Cakrawala UM.
- **Uji Kemampuan Bahasa Inggris (UKBIng):** 2 – 3 Juli 2026 (kartu diunduh di SIAKAD mulai 30 Juni 2026).
- **Pengenalan Kehidupan Kampus (PKKMB):** 10 – 14 Agustus 2026.
- **Awal Perkuliahan Gasal:** 24 Agustus 2026.

---

### Kapan pengumuman penetapan UKT dan pembayaran biaya pendidikan jalur SNBT?
1. **Pengumuman Penetapan UKT SNBT:** Tanggal **5 Juni 2026** di `http://registrasi.um.ac.id`.
2. **Pembayaran Biaya Pendidikan (UKT):** Tanggal **5 – 10 Juni 2026**.
   - Pembayaran menggunakan Kode Pembayaran unik dari sistem registrasi.
   - Bank mitra: Bank BNI, BRI, Mandiri, BTN/BSN, Bank Jatim, CIMB Niaga Syariah, dan BSI (`https://support.um.ac.id/topic/epayment/`).
   - Biaya yang telah dibayarkan tidak dapat ditarik kembali.

---

### Kapan dan bagaimana pelaksanaan Registrasi Satu Atap jalur SNBT?
- **Jadwal & Tempat:** **30 Juni – 1 Juli 2026** secara langsung/luring di **Gedung Cakrawala UM**.
- **Berkas Fisik yang Wajib Dibawa:**
  1. Cetak Biodata Mahasiswa dan Lembar Rincian Biaya Pendidikan (bisa dicetak mulai 26 Juni 2026 di laman registrasi).
  2. Cetak Kartu Tanda Peserta SNBT 2026.
  3. Bukti bayar biaya pendidikan / UKT yang sah dari bank mitra.

---

### Kontak Helpdesk Resmi Registrasi PMB UM
Jika mengalami kendala teknis dalam proses pendaftaran dan registrasi online:
- **WhatsApp Helpdesk PMB:** `0813-3344-400` (hanya melayani chat teks pada hari dan jam kerja).
- **Portal Registrasi:** `http://registrasi.um.ac.id`
- **Portal Seleksi UM:** `https://seleksi.um.ac.id`
"""

with open("Knowledge_Base_Clean_Categorized/01_PMB_Penerimaan_Mahasiswa_Baru/Registrasi Administrasi Calon Mahasiswa Baru Universitas Negeri Malang (UM) Jalur SNBT Tahun Akademik 2026_2027.md", "w", encoding="utf-8") as f:
    f.write(content)

print("File SNBT successfully updated with optimized chunks!")
