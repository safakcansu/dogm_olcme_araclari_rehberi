import streamlit as st
import pandas as pd
import os
import base64
import re

# 1. Sayfa Yapılandırması
st.set_page_config(
    page_title="Ölçme ve Değerlendirme Araçları: Ders Kitabı ve Öğretim Materyali Örnekleri",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Dosya Yolları
GORSEL_KLASORU = os.path.join("assets", "images")
EXCEL_YOLU = os.path.join("data", "araclar.xlsx")
LOGO_YOLU = os.path.join(GORSEL_KLASORU, "DOGM_Logo_Yan_.png")

# 3. Maarif Modeli (tymm.meb.gov.tr) Özel CSS Teması
TYMM_CSS = """
<style>
/* Genel Gövde ve Arka Plan */
.stApp {
    background-color: #F8FAFC !important;
    background-image: none !important;
    color: #1E293B !important;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
}

/* Sol Kenar Çubuğu (Sidebar) */
section[data-testid="stSidebar"] {
    background-color: #0F172A !important;
    color: #F8FAFC !important;
}
section[data-testid="stSidebar"] h1, 
section[data-testid="stSidebar"] p, 
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span {
    color: #F8FAFC !important;
}
section[data-testid="stSidebar"] button {
    background-color: #1E293B !important;
    color: #F8FAFC !important;
    border: 1px solid #334155 !important;
    border-radius: 8px !important;
    transition: all 0.2s ease !important;
}
section[data-testid="stSidebar"] button:hover {
    background-color: #C91D24 !important;
    border-color: #C91D24 !important;
    color: #FFFFFF !important;
}

/* Maarif Modeli Kurumsal Banner / Üst Panel */
.tymm-header-banner {
    background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
    border-radius: 16px;
    padding: 28px 36px;
    color: #FFFFFF;
    margin-bottom: 24px;
    box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.15);
    border-bottom: 4px solid #C91D24;
}
.tymm-header-banner h1 {
    color: #FFFFFF !important;
    font-size: 1.85rem !important;
    font-weight: 800 !important;
    margin-bottom: 8px !important;
}
.tymm-header-banner p {
    color: #94A3B8 !important;
    font-size: 1.05rem !important;
    margin-bottom: 0 !important;
}

/* Kategori Başlıkları */
.tymm-section-title {
    color: #0F172A;
    font-size: 1.3rem;
    font-weight: 800;
    margin-top: 24px;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    border-left: 5px solid #C91D24;
    padding-left: 12px;
}

/* Araç Butonları (Grid Kartları) */
div[data-testid="column"] button {
    background-color: #FFFFFF !important;
    color: #0F172A !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 12px !important;
    padding: 14px 18px !important;
    font-weight: 650 !important;
    font-size: 0.98rem !important;
    text-align: left !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04) !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
}
div[data-testid="column"] button:hover {
    border-color: #C91D24 !important;
    color: #C91D24 !important;
    background-color: #FFFFFF !important;
    box-shadow: 0 6px 16px rgba(201, 29, 36, 0.12) !important;
    transform: translateY(-2px) !important;
}

/* Sekmeler (Tabs - Maarif Modeli Hap Buton Yapısı) */
div[data-testid="stTabs"] {
    gap: 10px !important;
    margin-top: 15px !important;
    margin-bottom: 25px !important;
}
div[data-testid="stTabs"] button {
    background-color: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 10px !important;
    padding: 14px 22px !important;
    transition: all 0.2s ease !important;
}
div[data-testid="stTabs"] button p,
div[data-testid="stTabs"] button strong {
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    color: #475569 !important;
}
div[data-testid="stTabs"] button:hover {
    border-color: #94A3B8 !important;
}
div[data-testid="stTabs"] button[aria-selected="true"] {
    background-color: #0F172A !important;
    border-color: #0F172A !important;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.2) !important;
}
div[data-testid="stTabs"] button[aria-selected="true"] p,
div[data-testid="stTabs"] button[aria-selected="true"] strong {
    color: #FFFFFF !important;
}

/* İçerik Kartları */
.tymm-card {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 26px 30px;
    margin-top: 10px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}
.tymm-card-title {
    color: #0F172A;
    font-size: 1.25rem;
    font-weight: 800;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
}
.tymm-card-title::before {
    content: "";
    display: inline-block;
    width: 4px;
    height: 18px;
    background-color: #C91D24;
    margin-right: 10px;
    border-radius: 2px;
}
.tymm-card p {
    color: #334155;
    font-size: 1.05rem;
    line-height: 1.75;
}
.tymm-card ul {
    margin-bottom: 0;
    padding-left: 20px;
}
.tymm-card li {
    color: #334155;
    font-size: 1.05rem;
    line-height: 1.8;
    margin-bottom: 8px;
}

/* Rozet Maddeleri (Beceriler) */
.tymm-badge-item {
    background-color: #F8FAFC;
    border: 1px solid #E2E8F0;
    padding: 12px 18px;
    border-radius: 10px;
    margin-bottom: 10px;
    color: #0F172A;
    font-size: 1.02rem;
    font-weight: 600;
    display: flex;
    align-items: center;
}

/* Görsel Kapsayıcı */
.tymm-img-container {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
    text-align: center;
}

/* Örnek Çıktı Kartı */
.tymm-cikti-box {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-top: 4px solid #C91D24;
    border-radius: 14px;
    padding: 24px 26px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
}
.tymm-cikti-box h5 {
    color: #0F172A;
    margin-bottom: 14px;
    font-size: 1.15rem;
    font-weight: 800;
}
</style>
"""
st.markdown(TYMM_CSS, unsafe_allow_html=True)

# 4. Süreç Bileşenlerini Hatasız Ayrıştıran Fonksiyon
def surec_bilesenlerini_bicimlendir(metin):
    if not metin or str(metin) == "nan":
        return "<p style='color: #64748b; font-size: 1rem;'>Bu örnek için Excel'de henüz özel bir öğrenme çıktısı tanımlanmamış.</p>"
    
    metin = str(metin).strip()
    
    if "*" not in metin:
        return f"<p style='margin:0; font-size:1.05rem; line-height:1.7; color:#1E293B;'>{metin}</p>"
    
    parcalar = [p.strip() for p in metin.split("*") if p.strip()]
    
    ana_cikti = parcalar[0]
    html_cikti = f"<div style='font-size: 1.1rem; font-weight: 750; margin-bottom: 12px; color: #0F172A; line-height: 1.6;'>{ana_cikti}</div>"
    html_cikti += "<ul style='margin: 0; padding-left: 5px; list-style-type: none;'>"
    
    for madde in parcalar[1:]:
        kapanis = madde.find(")")
        if kapanis != -1:
            etiket = madde[:kapanis+1].strip()
            icerik = madde[kapanis+1:].strip()
            html_cikti += f"""
            <li style='margin-bottom: 10px; color: #334155; font-size: 1rem; line-height: 1.6; display: flex; align-items: flex-start;'>
                <span style='margin-right: 8px; color: #C91D24; font-weight: 800;'>▪</span>
                <span><strong style='color: #0F172A;'>{etiket}</strong> {icerik}</span>
            </li>
            """
        else:
            html_cikti += f"""
            <li style='margin-bottom: 10px; color: #334155; font-size: 1rem; line-height: 1.6; display: flex; align-items: flex-start;'>
                <span style='margin-right: 8px; color: #C91D24; font-weight: 800;'>▪</span>
                <span>{madde}</span>
            </li>
            """
            
    html_cikti += "</ul>"
    return html_cikti

# 5. Dinamik Çoklu Görsel Tarayıcı
def tum_ornekleri_bul(arac_id):
    uzantilar = [".png", ".jpg", ".jpeg", ".PNG", ".JPG"]
    bulunan_ornekler = []
    ornek_no = 1
    
    while True:
        bulundu = False
        for ext in uzantilar:
            dosya_adi = f"ornek{arac_id}_{ornek_no}{ext}"
            yol = os.path.join(GORSEL_KLASORU, dosya_adi)
            if os.path.exists(yol):
                bulunan_ornekler.append((ornek_no, yol, dosya_adi))
                bulundu = True
                break
        if not bulundu:
            break
        ornek_no += 1
        
    return bulunan_ornekler

# 6. Excel Verisini Yükleme
@st.cache_data
def veriyi_yukle(dosya_yolu):
    if not os.path.exists(dosya_yolu):
        return None
    return pd.read_excel(dosya_yolu)

df = veriyi_yukle(EXCEL_YOLU)

if df is None:
    st.error(f"`{EXCEL_YOLU}` dosyası bulunamadı! Lütfen Excel dosyasını `data` klasörüne ekleyin.")
    st.stop()

# 7. Oturum Durumu Yönetimi
if "secilen_arac" not in st.session_state:
    st.session_state.secilen_arac = None

# 8. Sol Kenar Çubuğu (Sidebar)
with st.sidebar:
    st.markdown("### 📘 Maarif Modeli")
    st.caption("Ölçme ve Değerlendirme Rehberi")
    
    if st.button("🏠 Ana Listeye Dön", use_container_width=True):
        st.session_state.secilen_arac = None
        st.rerun()

    st.markdown("---")
    arac_listesi = ["--- Bir Araç Seçiniz ---"] + df["arac_adi"].dropna().tolist()
    
    mevcut_index = 0
    if st.session_state.secilen_arac in arac_listesi:
        mevcut_index = arac_listesi.index(st.session_state.secilen_arac)
        
    secim = st.selectbox("Hızlı Araç Gezgini:", arac_listesi, index=mevcut_index)
    if secim != "--- Bir Araç Seçiniz ---" and secim != st.session_state.secilen_arac:
        st.session_state.secilen_arac = secim
        st.rerun()

# ----------------------------------------------------
# 9. GÖRÜNÜM 1: MAARİF MODELİ ANA KATEGORİ LİSTESİ
# ----------------------------------------------------
if st.session_state.secilen_arac is None:
    col_banner, col_logo = st.columns([4.2, 1.2], vertical_alignment="center")
    
    with col_banner:
        st.markdown("""
        <div class="tymm-header-banner">
            <h1>Ölçme ve Değerlendirme Araçları</h1>
            <p>Türkiye Yüzyılı Maarif Modeli: Ders Kitabı ve Öğretim Materyali Örnekleri</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_logo:
        if os.path.exists(LOGO_YOLU):
            st.image(LOGO_YOLU, use_container_width=True)

    kategoriler = [
        ("Ölçme ve Değerlendirme Araçları", "Ölçme ve Değerlendirme Araçları"),
        ("Puanlama Araçları", "Puanlama Araçları"),
        ("Değerlendirme Formları", "Değerlendirme Formları"),
        ("Hızlı Değerlendirme Teknikleri", "Hızlı Değerlendirme Teknikleri")
    ]

    for kat_baslik, kat_anahtar in kategoriler:
        st.markdown(f'<div class="tymm-section-title">{kat_baslik}</div>', unsafe_allow_html=True)
        kat_df = df[df["kategori"].astype(str).str.strip() == kat_anahtar] if "kategori" in df.columns else df
        
        cols = st.columns(3)
        for idx, (_, row) in enumerate(kat_df.iterrows()):
            col_target = cols[idx % 3]
            etiket = f"{int(row['arac_id'])}. {row['arac_adi']}"
            if col_target.button(etiket, key=f"btn_{row['arac_id']}", use_container_width=True):
                st.session_state.secilen_arac = row["arac_adi"]
                st.rerun()

# ----------------------------------------------------
# 10. GÖRÜNÜM 2: DETAY SAYFASI
# ----------------------------------------------------
else:
    secilen_arac = df[df["arac_adi"] == st.session_state.secilen_arac].iloc[0]
    arac_id = int(secilen_arac["arac_id"])

    # Üst Başlık ve Geri Butonu
    col_baslik, col_geri = st.columns([5, 1], vertical_alignment="center")
    with col_baslik:
        st.markdown(f"""
        <div style="margin-bottom: 10px;">
            <span style="background-color: #E2E8F0; color: #475569; font-size: 0.85rem; font-weight: 700; padding: 4px 10px; border-radius: 6px;">
                {secilen_arac.get('kategori', 'Ölçme Aracı')}
            </span>
            <h2 style="color: #0F172A; font-size: 1.85rem; font-weight: 800; margin-top: 8px; margin-bottom: 0;">
                {arac_id}. {secilen_arac['arac_adi']}
            </h2>
        </div>
        """, unsafe_allow_html=True)
    with col_geri:
        if st.button("⬅️ Geri Dön", use_container_width=True):
            st.session_state.secilen_arac = None
            st.rerun()

    # Maarif Modeli Sekmeleri
    tab1, tab2, tab3, tab4 = st.tabs([
        "**1. Tanıtım**",
        "**2. Hazırlarken Dikkat Edilecek Hususlar**",
        "**3. Önerilen Beceriler / Süreç Bileşenleri**",
        "**4. Örnek & Çıktı Eşleşmesi**"
    ])

    # 1. Tanıtım
    with tab1:
        tanitim_metni = str(secilen_arac.get("tanitim", "Tanıtım bilgisi bulunmuyor."))
        st.markdown(f"""
        <div class="tymm-card">
            <div class="tymm-card-title">Ölçme Aracının Tanımı ve Kapsamı</div>
            <p>{tanitim_metni}</p>
        </div>
        """, unsafe_allow_html=True)

    # 2. Dikkat Edilecekler
    with tab2:
        metin = str(secilen_arac.get("dikkat_edilecekler", ""))
        li_icerik = ""
        if metin and metin != "nan":
            satirlar = [s.strip() for s in metin.split("\n") if s.strip()]
            for satir in satirlar:
                li_icerik += f"<li>{satir.lstrip('•-* ')}</li>"
        else:
            li_icerik = "<li>Belirtilen husus bulunamadı.</li>"

        st.markdown(f"""
        <div class="tymm-card">
            <div class="tymm-card-title">Hazırlık ve Yazım Sürecinde Dikkat Edilecek İlkeler</div>
            <ul>
                {li_icerik}
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # 3. Önerilen Beceriler
    with tab3:
        beceriler = str(secilen_arac.get("onerilen_beceriler", ""))
        rozetler_html = ""
        if beceriler and beceriler != "nan":
            satirlar = [s.strip() for s in beceriler.split("\n") if s.strip()]
            for satir in satirlar:
                temiz = satir.lstrip('•-* ')
                rozetler_html += f'<div class="tymm-badge-item"><span style="color:#C91D24; margin-right:8px; font-weight:800;">✓</span> {temiz}</div>'
        else:
            rozetler_html = '<div class="tymm-badge-item">Kayıtlı önerilen beceri bulunamadı.</div>'

        st.markdown(f"""
        <div class="tymm-card">
            <div class="tymm-card-title">Bu Araçla Ölçülmesi Önerilen Beceriler ve Süreç Bileşenleri</div>
            {rozetler_html}
        </div>
        """, unsafe_allow_html=True)

    # 4. Örnek Görseller ve Çıktı Eşleşmesi
    with tab4:
        st.write("")
        ornekler_listesi = tum_ornekleri_bul(arac_id)
        
        if not ornekler_listesi:
            st.markdown(f"""
            <div class="tymm-img-container">
                <p style="color: #64748B; font-weight: 600; margin: 30px 0;">
                    Bu ölçme aracına ait örnek görsel bulunamadı.<br>
                    Beklenen dosya formatı: <code>assets/images/ornek{arac_id}_1.png / .jpg</code>
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            for o_no, gorsel_yolu_bulunan, dosya_adi in ornekler_listesi:
                cikti_sutun_adi = f"ornek{o_no}_cikti"
                cikti_degeri = secilen_arac.get(cikti_sutun_adi) if cikti_sutun_adi in secilen_arac else None
                
                bicimli_cikti = surec_bilesenlerini_bicimlendir(cikti_degeri)
                
                st.markdown(f"<h4 style='color:#0F172A; font-weight:800; margin-top:20px;'>Örnek {arac_id}.{o_no}</h4>", unsafe_allow_html=True)
                col_img, col_info = st.columns([3, 2], gap="large")
                
                with col_img:
                    st.markdown('<div class="tymm-img-container">', unsafe_allow_html=True)
                    st.image(gorsel_yolu_bulunan, caption=f"Örnek {arac_id}.{o_no} ({dosya_adi})", use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with col_info:
                    st.markdown(f"""
                    <div class="tymm-cikti-box">
                        <h5>Örneğe Ait Öğrenme Çıktısı / Süreç Bileşeni</h5>
                        {bicimli_cikti}
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("<hr style='border: 0; border-top: 1px solid #E2E8F0; margin: 30px 0;'>", unsafe_allow_html=True)
