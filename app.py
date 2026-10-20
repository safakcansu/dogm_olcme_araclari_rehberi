import streamlit as st
import pandas as pd
import os
import base64

# 1. Sayfa Yapılandırması
st.set_page_config(
    page_title="Ölçme ve Değerlendirme Araçları: Ders Kitabı ve Öğretim Materyali Örnekleri",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Dosya Yolları
GORSEL_KLASORU = os.path.join("assets", "images")
FON_GORSELI_JPG = os.path.join(GORSEL_KLASORU, "webfon.jpg")
FON_GORSELI_PNG = os.path.join(GORSEL_KLASORU, "webfon.png")
EXCEL_YOLU = os.path.join("data", "araclar.xlsx")
LOGO_YOLU = os.path.join(GORSEL_KLASORU, "DOGM_Logo_Yan_.png")

# Arka Plan Görselini Belirleme ve Base64 Formatına Çevirme
fon_yolu = FON_GORSELI_JPG if os.path.exists(FON_GORSELI_JPG) else FON_GORSELI_PNG

def arka_plan_css_olustur(gorsel_yolu):
    if os.path.exists(gorsel_yolu):
        ext = "jpeg" if gorsel_yolu.endswith((".jpg", ".jpeg")) else "png"
        with open(gorsel_yolu, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode()
        return f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(240, 244, 248, 0.88), rgba(240, 244, 248, 0.88)), url("data:image/{ext};base64,{encoded_string}");
            background-size: cover;
            background-position: center right;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """
    return ""

st.markdown(arka_plan_css_olustur(fon_yolu), unsafe_allow_html=True)

# 3. İri, Ultra Bold ve Renkli Sekme Butonları + İçerik Kartları CSS'i
CUSTOM_CSS = """
<style>
/* Sekme Buton Çubuğu */
div[data-testid="stTabs"] {
    gap: 12px !important;
    margin-top: 15px !important;
    margin-bottom: 25px !important;
}

/* Sekme Butonlarının Temel Tasarımı */
div[data-testid="stTabs"] button {
    border-radius: 12px !important;
    padding: 16px 26px !important;
    margin-right: 6px !important;
    border: 2px solid transparent !important;
    transition: all 0.25s ease-in-out !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04) !important;
    background-color: rgba(255, 255, 255, 0.85) !important;
    backdrop-filter: blur(6px) !important;
}

/* Sekme Butonu İçindeki Yazıyı Zorla Ultra Bold Yap */
div[data-testid="stTabs"] button p,
div[data-testid="stTabs"] button strong {
    font-size: 1.35rem !important;
    font-weight: 900 !important;
    letter-spacing: -0.3px !important;
    margin: 0 !important;
    line-height: 1.3 !important;
}

/* 1. SEKME: 1. TANITIM (Petrol Mavisi) */
div[data-testid="stTabs"] button:nth-of-type(1) {
    background-color: rgba(224, 242, 254, 0.85) !important;
    border-color: #bae6fd !important;
}
div[data-testid="stTabs"] button:nth-of-type(1) p,
div[data-testid="stTabs"] button:nth-of-type(1) strong {
    color: #0369a1 !important;
}
div[data-testid="stTabs"] button:nth-of-type(1)[aria-selected="true"] {
    background-color: #006064 !important;
    border-color: #004d40 !important;
    box-shadow: 0 6px 16px rgba(0, 96, 100, 0.35) !important;
}
div[data-testid="stTabs"] button:nth-of-type(1)[aria-selected="true"] p,
div[data-testid="stTabs"] button:nth-of-type(1)[aria-selected="true"] strong {
    color: #ffffff !important;
}

/* 2. SEKME: 2. HAZIRLARKEN DİKKAT EDİLECEK HUSUSLAR (Sıcak Turuncu) */
div[data-testid="stTabs"] button:nth-of-type(2) {
    background-color: rgba(255, 237, 213, 0.85) !important;
    border-color: #fed7aa !important;
}
div[data-testid="stTabs"] button:nth-of-type(2) p,
div[data-testid="stTabs"] button:nth-of-type(2) strong {
    color: #c2410c !important;
}
div[data-testid="stTabs"] button:nth-of-type(2)[aria-selected="true"] {
    background-color: #ea580c !important;
    border-color: #c2410c !important;
    box-shadow: 0 6px 16px rgba(234, 88, 12, 0.35) !important;
}
div[data-testid="stTabs"] button:nth-of-type(2)[aria-selected="true"] p,
div[data-testid="stTabs"] button:nth-of-type(2)[aria-selected="true"] strong {
    color: #ffffff !important;
}

/* 3. SEKME: 3. ÖNERİLEN BECERİLER / SÜREÇ BİLEŞENLERİ (Turkuaz/Zümrüt) */
div[data-testid="stTabs"] button:nth-of-type(3) {
    background-color: rgba(204, 251, 241, 0.85) !important;
    border-color: #99f6e4 !important;
}
div[data-testid="stTabs"] button:nth-of-type(3) p,
div[data-testid="stTabs"] button:nth-of-type(3) strong {
    color: #0f766e !important;
}
div[data-testid="stTabs"] button:nth-of-type(3)[aria-selected="true"] {
    background-color: #0d9488 !important;
    border-color: #0f766e !important;
    box-shadow: 0 6px 16px rgba(13, 148, 136, 0.35) !important;
}
div[data-testid="stTabs"] button:nth-of-type(3)[aria-selected="true"] p,
div[data-testid="stTabs"] button:nth-of-type(3)[aria-selected="true"] strong {
    color: #ffffff !important;
}

/* 4. SEKME: 4. ÖRNEK & ÇIKTI EŞLEŞMESİ (Altın / Kehribar) */
div[data-testid="stTabs"] button:nth-of-type(4) {
    background-color: rgba(254, 243, 199, 0.85) !important;
    border-color: #fde68a !important;
}
div[data-testid="stTabs"] button:nth-of-type(4) p,
div[data-testid="stTabs"] button:nth-of-type(4) strong {
    color: #b45309 !important;
}
div[data-testid="stTabs"] button:nth-of-type(4)[aria-selected="true"] {
    background-color: #b45309 !important;
    border-color: #92400e !important;
    box-shadow: 0 6px 16px rgba(180, 83, 9, 0.35) !important;
}
div[data-testid="stTabs"] button:nth-of-type(4)[aria-selected="true"] p,
div[data-testid="stTabs"] button:nth-of-type(4)[aria-selected="true"] strong {
    color: #ffffff !important;
}

/* İçerik Kartları */
.box-tanitim {
    background-color: rgba(255, 255, 255, 0.92) !important;
    border-left: 6px solid #00838f;
    padding: 26px 30px;
    border-radius: 14px;
    margin-top: 15px;
    box-shadow: 0 4px 15px rgba(0, 96, 100, 0.08);
    backdrop-filter: blur(8px);
}
.box-tanitim h4 {
    color: #006064;
    margin-bottom: 14px;
    font-size: 1.3rem;
    font-weight: 750;
}
.box-tanitim p {
    color: #1e293b;
    font-size: 1.15rem;
    line-height: 1.8;
}

.box-dikkat {
    background-color: rgba(255, 255, 255, 0.92) !important;
    border-left: 6px solid #ea580c;
    padding: 26px 30px;
    border-radius: 14px;
    margin-top: 15px;
    box-shadow: 0 4px 15px rgba(234, 88, 12, 0.08);
    backdrop-filter: blur(8px);
}
.box-dikkat h4 {
    color: #9a3412;
    margin-bottom: 14px;
    font-size: 1.3rem;
    font-weight: 750;
}
.box-dikkat ul {
    margin-bottom: 0;
    padding-left: 20px;
}
.box-dikkat li {
    color: #334155;
    font-size: 1.1rem;
    line-height: 1.85;
    margin-bottom: 8px;
}

.box-beceriler {
    background-color: rgba(255, 255, 255, 0.92) !important;
    border-left: 6px solid #0d9488;
    padding: 26px 30px;
    border-radius: 14px;
    margin-top: 15px;
    box-shadow: 0 4px 15px rgba(13, 148, 136, 0.08);
    backdrop-filter: blur(8px);
}
.box-beceriler h4 {
    color: #115e59;
    margin-bottom: 16px;
    font-size: 1.3rem;
    font-weight: 750;
}
.box-beceriler .badge-item {
    background-color: #f0fdfa;
    border: 1px solid #99f6e4;
    padding: 14px 20px;
    border-radius: 10px;
    margin-bottom: 10px;
    color: #0f766e;
    font-size: 1.1rem;
    font-weight: 650;
    box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}

.gorsel-kapsayici {
    background-color: rgba(255, 255, 255, 0.95) !important;
    border: 2px solid #e2e8f0;
    border-radius: 16px;
    padding: 22px;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.06);
    text-align: center;
}

.box-ornek-cikti {
    background-color: rgba(255, 255, 255, 0.92) !important;
    border-left: 6px solid #b45309;
    padding: 24px 26px;
    border-radius: 14px;
    box-shadow: 0 4px 15px rgba(180, 83, 9, 0.08);
    backdrop-filter: blur(8px);
}
.box-ornek-cikti h5 {
    color: #92400e;
    margin-bottom: 12px;
    font-size: 1.25rem;
    font-weight: 750;
}
.box-ornek-cikti p {
    color: #1e293b;
    font-size: 1.1rem;
    line-height: 1.7;
    margin-bottom: 0;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# 4. Dinamik Çoklu Görsel Tarayıcı Fonksiyonu
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

# 5. Excel Verisini Yükleme
@st.cache_data
def veriyi_yukle(dosya_yolu):
    if not os.path.exists(dosya_yolu):
        return None
    return pd.read_excel(dosya_yolu)

df = veriyi_yukle(EXCEL_YOLU)

if df is None:
    st.error(f"`{EXCEL_YOLU}` dosyası bulunamadı! Lütfen Excel dosyasını `data` klasörüne ekleyin.")
    st.stop()

# 6. Oturum Durumu Yönetimi
if "secilen_arac" not in st.session_state:
    st.session_state.secilen_arac = None

# 7. Sol Kenar Çubuğu (Sidebar)
with st.sidebar:
    st.title("📋 Rehber Gezgini")
    
    if st.button("🏠 Ana Listeye Dön", use_container_width=True):
        st.session_state.secilen_arac = None
        st.rerun()

    st.markdown("---")
    arac_listesi = ["--- Bir Araç Seçiniz ---"] + df["arac_adi"].dropna().tolist()
    
    mevcut_index = 0
    if st.session_state.secilen_arac in arac_listesi:
        mevcut_index = arac_listesi.index(st.session_state.secilen_arac)
        
    secim = st.selectbox("Hızlı Araç Seçimi:", arac_listesi, index=mevcut_index)
    if secim != "--- Bir Araç Seçiniz ---" and secim != st.session_state.secilen_arac:
        st.session_state.secilen_arac = secim
        st.rerun()

# ----------------------------------------------------
# 8. GÖRÜNÜM 1: ANA KATEGORİ LİSTESİ
# ----------------------------------------------------
if st.session_state.secilen_arac is None:
    col_baslik, col_logo = st.columns([4, 1.2], vertical_alignment="center")
    
    with col_baslik:
        st.title("📚 Ölçme ve Değerlendirme Araçları: Ders Kitabı ve Öğretim Materyali Örnekleri")
        st.markdown("İncelemek istediğiniz aracın kartına tıklayarak teknik ilkelere, becerilere ve örnek uygulamalara erişebilirsiniz.")
    
    with col_logo:
        if os.path.exists(LOGO_YOLU):
            st.image(LOGO_YOLU, use_container_width=True)
        else:
            st.caption(f"Logo dosyası bulunamadı: `{LOGO_YOLU}`")

    st.divider()

    kategoriler = [
        ("📌 Ölçme ve Değerlendirme Araçları", "Ölçme ve Değerlendirme Araçları"),
        ("⚖️ Puanlama Araçları", "Puanlama Araçları"),
        ("📝 Değerlendirme Formları", "Değerlendirme Formları"),
        ("⚡ Hızlı Değerlendirme Teknikleri", "Hızlı Değerlendirme Teknikleri")
    ]

    for kat_baslik, kat_anahtar in kategoriler:
        st.subheader(kat_baslik)
        kat_df = df[df["kategori"].astype(str).str.strip() == kat_anahtar] if "kategori" in df.columns else df
        
        cols = st.columns(3)
        for idx, (_, row) in enumerate(kat_df.iterrows()):
            col_target = cols[idx % 3]
            etiket = f"{int(row['arac_id'])}. {row['arac_adi']}"
            if col_target.button(etiket, key=f"btn_{row['arac_id']}", use_container_width=True):
                st.session_state.secilen_arac = row["arac_adi"]
                st.rerun()
        st.write("")

# ----------------------------------------------------
# 9. GÖRÜNÜM 2: DETAY SAYFASI (İKONSUZ & BOLD SEKMELER)
# ----------------------------------------------------
else:
    secilen_arac = df[df["arac_adi"] == st.session_state.secilen_arac].iloc[0]
    arac_id = int(secilen_arac["arac_id"])

    # Üst Başlık ve Geri Dön Butonu
    col_baslik, col_geri = st.columns([5, 1], vertical_alignment="center")
    with col_baslik:
        st.title(f"{arac_id}. {secilen_arac['arac_adi']}")
        if "kategori" in secilen_arac and pd.notna(secilen_arac["kategori"]):
            st.caption(f"📁 {secilen_arac['kategori']}")
    with col_geri:
        if st.button("⬅️ Geri Dön", use_container_width=True):
            st.session_state.secilen_arac = None
            st.rerun()

    # İkonsuz ve Doğrudan Bold Tanımlanmış 4 Ana Sekme
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
        <div class="box-tanitim">
            <h4>1. Ölçme Aracının Tanımı ve Kapsamı</h4>
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
        <div class="box-dikkat">
            <h4>2. Hazırlık ve Yazım Sürecinde Dikkat Edilecek İlkeler</h4>
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
                rozetler_html += f'<div class="badge-item">✔ {temiz}</div>'
        else:
            rozetler_html = '<div class="badge-item">Kayıtlı önerilen beceri bulunamadı.</div>'

        st.markdown(f"""
        <div class="box-beceriler">
            <h4>3. Bu Araçla Ölçülmesi Önerilen Beceriler ve Süreç Bileşenleri</h4>
            {rozetler_html}
        </div>
        """, unsafe_allow_html=True)

    # 4. Örnek Görseller ve Çıktı Eşleşmeleri
    with tab4:
        st.write("")
        ornekler_listesi = tum_ornekleri_bul(arac_id)
        
        if not ornekler_listesi:
            st.markdown(f"""
            <div class="gorsel-kapsayici">
                <p style="color: #64748b; font-weight: 600; margin: 30px 0;">
                    ⚠️ Bu ölçme aracına ait örnek görsel bulunamadı.<br>
                    Beklenen dosya formatı: <code>assets/images/ornek{arac_id}_1.png / .jpg</code>
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            for o_no, gorsel_yolu_bulunan, dosya_adi in ornekler_listesi:
                cikti_sutun_adi = f"ornek{o_no}_cikti"
                cikti_degeri = secilen_arac.get(cikti_sutun_adi) if cikti_sutun_adi in secilen_arac else None
                
                cikti_metni = str(cikti_degeri) if pd.notna(cikti_degeri) else "Bu örnek için Excel'de henüz özel bir öğrenme çıktısı tanımlanmamış."
                
                st.markdown(f"### Örnek {arac_id}.{o_no}")
                col_img, col_info = st.columns([3, 2], gap="large")
                
                with col_img:
                    st.markdown('<div class="gorsel-kapsayici">', unsafe_allow_html=True)
                    st.image(gorsel_yolu_bulunan, caption=f"Örnek {arac_id}.{o_no} ({dosya_adi})", use_container_width=True)
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with col_info:
                    st.markdown(f"""
                    <div class="box-ornek-cikti">
                        <h5>Örneğe Ait Öğrenme Çıktısı / Süreç Bileşeni</h5>
                        <p>{cikti_metni}</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("<hr style='border: 1px dashed #cbd5e1; margin: 35px 0;'>", unsafe_allow_html=True)