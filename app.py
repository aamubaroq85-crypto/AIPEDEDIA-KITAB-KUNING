import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="AIPEDIA Kitab Kuning - Zuhri Formalism",
    page_icon="📖",
    layout="wide"
)

# Judul Utama
st.title("📖 AIPEDIA Kitab Kuning: Zuhri Formalism Edition")
st.markdown("Sistem Navigasi & Eksplorasi Kitab Klasik Berbasis Kerangka Formalisme Zuhri.")

# Sidebar Navigasi Kategori
st.sidebar.header("🗂️ Direktori Kitab")
kategori = st.sidebar.selectbox(
    "Pilih Tingkatan / Kategori:",
    ["Dashboard Utama", "1. Kitab Syarat & Dasar (Ilmu Alat & Ibtida')", "2. Kitab Syarah & Menengah (Fiqih & Ushul)", "3. Kitab Tasawuf & Akhlak (Suluk)"]
)

# Database Simulasi Kitab Berdasarkan Formalisme
database_kitab = {
    "1. Kitab Syarat & Dasar (Ilmu Alat & Ibtida')": [
        {"nama": "Al-Jurumiyah", "penulis": "Imam Ash-Shanhaji", "bidang": "Nahwu", "deskripsi": "Kitab fondasi tata bahasa Arab untuk membaca kitab kuning."},
        {"nama": "Matan Al-Ghayah wat-Taqrib", "penulis": "Al-Qadhi Abu Syuja'", "bidang": "Fiqih Syafi'i", "deskripsi": "Ringkasan hukum fiqih ibadah dan muamalah dasar."}
    ],
    "2. Kitab Syarah & Menengah (Fiqih & Ushul)": [
        {"nama": "Fathul Qarib Al-Mujib", "penulis": "Ibnu Qasim Al-Ghazi", "bidang": "Fiqih", "deskripsi": "Syarah dari Matan Taqrib yang menjelaskan detail hukum secara komprehensif."},
        {"nama": "Lathaiful Minan", "penulis": "Ibnu Atha'illah", "bidang": "Ushul & Tasawuf", "deskripsi": "Penjelasan mengenai kaidah spiritual dan adab kepada Allah."}
    ],
    "3. Kitab Tasawuf & Akhlak (Suluk)": [
        {"nama": "Al-Hikam", "penulis": "Ibn Atha'illah As-Sakandari", "bidang": "Tasawuf", "deskripsi": "Mutiara hikmah pembersihan jiwa dan makrifatullah."},
        {"nama": "Bidayatul Hidayah", "penulis": "Imam Al-Ghazali", "bidang": "Akhlak", "deskripsi": "Panduan praktis ibadah harian dan pembentukan akhlak mulia."}
    ]
}

# Tampilan Konten Berdasarkan Pilihan
if kategori == "Dashboard Utama":
    st.subheader("Selamat Datang di Portal AI-Pedia Zuhri Formalism")
    st.write("Gunakan menu di sebelah kiri untuk menjelajahi tingkatan kitab kuning dari tingkat dasar hingga tasawuf.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**Level 1: Syarat & Dasar**\n\nFokus pada tata bahasa dan dasar syariat.")
    with col2:
        st.warning("**Level 2: Syarah & Fiqih**\n\nFokus pada penjabaran hukum dan dalil.")
    with col3:
        st.success("**Level 3: Tasawuf**\n\nFokus pada penyucian hati dan kedekatan Ilahi.")

else:
    st.subheader(f"📂 Kategori: {kategori}")
    st.markdown("---")
    
    daftar_kitab = database_kitab.get(kategori, [])
    
    for kitab in daftar_kitab:
        with st.expander(f"📚 {kitab['nama']} — ({kitab['bidang']})"):
            st.write(**Penulis:** {kitab['penulis']})
            st.write(f"**Deskripsi Formalisme:** {kitab['deskripsi']}")
            
            # Simulasi Fitur Analisis AI / Ekstraksi Zuhri Formalism
            if st.button(f"Analisis Struktur: {kitab['nama']}", key=kitab['nama']):
                st.success(f"Menjalankan ekstraksi Zuhri Formalism untuk {kitab['nama']}...")
                st.markdown("> **Hasil Analisis:** Pemetaan matan, identifikasi illat hukum, dan sinkronisasi teks dengan konteks kontemporer berhasil dimuat.")

# Footer
st.markdown("---")
st.caption("AIPEDIA Kitab Kuning | Dikembangkan dengan pendekatan Zuhri Formalism.")
