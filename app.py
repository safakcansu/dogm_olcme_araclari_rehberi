import streamlit as st
import pandas as pd
import os
import base64
import re

# ============================================================
# 1. Sayfa Yapılandırması
# ============================================================
st.set_page_config(
    page_title="Ölçme ve Değerlendirme Araçları: Ders Kitabı ve Öğretim Materyali Örnekleri",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# 2. Dosya Yolları
# ============================================================
GORSEL_KLASORU = os.path.join("assets", "images")
FON_GORSELI_PNG = os.path.join(GORSEL_KLASORU, "webfon.png")
FON_GORSELI_JPG = os.path.join(GORSEL_KLASORU, "webfon.jpg")
SOL_PANEL_GORSELI = os.path.join(GORSEL_KLASORU, "solpanel.png")
EXCEL_YOLU = os.path.join("data", "araclar.xlsx")
LOGO_YOLU = os.path.join(GORSEL_KLASORU, "DOGM_Logo_Yan_.png")

# Arka Plan Görselini Belirleme ve Base64 Formatına Çevirme
fon_yolu = FON_GORSELI_PNG if os.path.exists(FON_GORSELI_PNG) else FON_GORSELI_JPG

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

# ============================================================
# 3. Webfon Uyumlu Kurumsal CSS
# ============================================================
TYMM_CSS = """
<style>
/* Sol Kenar Çubuğu */
section[data-testid="stSidebar"] {
    background-color: rgba(241, 245, 249, 0.95) !important;
    border-right: 1px solid #CBD5E1 !important;
    backdrop-filter: blur(10px) !important;
}

section[data-testid="stSidebar"] h1, 
section[data-testid="stSidebar"] h2, 
section[data-testid="stSidebar"] h3, 
section[data-testid="stSidebar"] p, 
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] div {
    color: #0F172A !important;
}

section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {
    color: #475569 !important;
}

section[data-testid="stSidebar"] button {
    background-color: #FFFFFF !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 8px !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04) !important;
    transition: all 0.2s ease !important;
}
section[data-testid="stSidebar"] button * {
    color: #0F172A !important;
    font-weight: 700 !important;
}
section[data-testid="stSidebar"] button:hover {
    background-color: #0891B2 !important;
    border-color: #0891B2 !important;
}
section[data-testid="stSidebar"] button:hover * {
    color: #FFFFFF !important;
}

/* Kurumsal Banner */
.tymm-header-banner {
    background: linear-gradient(135deg, #0F172A 0%, #164E63 100%);
    border-radius: 16px;
    padding: 28px 36px;
    color: #FFFFFF;
    margin-bottom: 24px;
    box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.15);
    border-bottom: 4px solid #0891B2;
}
.tymm-header-banner h1 {
    color: #FFFFFF !important;
    font-size: 1.85rem !important;
    font-weight: 800 !important;
    margin-bottom: 8px !important;
}
.tymm-header-banner p {
    color: #BAE6FD !important;
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
    border-left: 5px solid #0891B2;
    padding-left: 12px;
}

/* Araç Butonları */
div[data-testid="stButton"] > button {
    background-color: rgba(255, 255, 255, 0.95) !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 12px !important;
    padding: 14px 18px !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04) !important;
    backdrop-filter: blur(6px) !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
}
div[data-testid="stButton"] > button * {
    color: #0F172A !important;
    font-weight: 700 !important;
    font-size: 0.98rem !important;
}
div[data-testid="stButton"] > button:hover {
    background-color: #0891B2 !important;
    border-color: #0891B2 !important;
    box-shadow: 0 8px 20px rgba(8, 145, 178, 0.35) !important;
    transform: translateY(-2px) !important;
}
div[data-testid="stButton"] > button:hover * {
    color: #FFFFFF !important;
}

/* Sekmeler */
div[data-testid="stTabs"] {
    gap: 12px !important;
    margin-top: 15px !important;
    margin-bottom: 25px !important;
}
div[data-testid="stTabs"] [data-baseweb="tab"] {
    background-color: rgba(255, 255, 255, 0.90) !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 10px !important;
    padding: 12px 22px !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04) !important;
    transition: all 0.2s ease !important;
}
div[data-testid="stTabs"] [data-baseweb="tab"] * {
    color: #334155 !important;
    font-size: 1.05rem !important;
    font-weight: 750 !important;
}
div[data-testid="stTabs"] [data-baseweb="tab"]:hover {
    background-color: #0891B2 !important;
    border-color: #0891B2 !important;
    box-shadow: 0 4px 12px rgba(8, 145, 178, 0.35) !important;
}
div[data-testid="stTabs"] [data-baseweb="tab"]:hover * {
    color: #FFFFFF !important;
}
div[data-testid="stTabs"] [data-baseweb="tab"][aria-selected="true"] {
    background-color: #0891B2 !important;
    border-color: #0891B2 !important;
    box-shadow: 0 6px 16px rgba(8, 145, 178, 0.45) !important;
}
div[data-testid="stTabs"] [data-baseweb="tab"][aria-selected="true"] * {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}
div[data-testid="stTabs"] [data-baseweb="tab-highlight"] {
    display: none !important;
}

/* Expander */
div[data-testid="stExpander"] {
    background-color: rgba(255, 255, 255, 0.94) !important;
    border: 1px solid #E2E8F0 !important;
    border-left: 6px solid #0891B2 !important;
    border-radius: 14px !important;
    margin-bottom: 24px !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04) !important;
    backdrop-filter: blur(8px) !important;
}
div[data-testid="stExpander"] details summary span p {
    font-size: 1.25rem !important;
    font-weight: 800 !important;
    color: #0F172A !important;
}

/* Kartlar */
.tymm-card {
    background-color: rgba(255, 255, 255, 0.94);
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 26px 30px;
    margin-top: 10px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04);
    backdrop-filter: blur(8px);
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
    background-color: #0891B2;
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

.tymm-img-container {
    background-color: rgba(255, 255, 255, 0.95);
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
    text-align: center;
}

.tymm-cikti-box {
    background-color: rgba(255, 255, 255, 0.94);
    border: 1px solid #E2E8F0;
    border-top: 4px solid #EA580C;
    border-radius: 14px;
    padding: 24px 26px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
    backdrop-filter: blur(8px);
    margin-bottom: 15px;
}
.tymm-cikti-box h5 {
    color: #9A3412;
    margin-bottom: 14px;
    font-size: 1.15rem;
    font-weight: 800;
}

/* Floating Buton */
.floating-back-link {
    text-decoration: none !important;
}

.floating-back-box {
    background-color: rgba(255, 255, 255, 0.95) !important;
    color: #0F172A !important;
    border: 1.5px solid #CBD5E1 !important;
    border-radius: 50px !important;
    padding: 10px 22px !important;
    font-weight: 800 !important;
    font-size: 0.95rem !important;
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
    box-shadow: 0 4px 16px rgba(15, 23, 42, 0.12) !important;
    backdrop-filter: blur(8px) !important;
    cursor: pointer !important;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

.floating-back-box span {
    color: #0F172A !important;
    transition: color 0.2s ease !important;
}

.floating-back-box:hover {
    background-color: #0891B2 !important;
    border-color: #0891B2 !important;
    box-shadow: 0 8px 24px rgba(8, 145, 178, 0.45) !important;
    transform: scale(1.05) translateY(-2px) !important;
}

.floating-back-box:hover span {
    color: #FFFFFF !important;
}

/* Footer Butonları */
div[data-testid="column"]:has(button[key^="nav_alt_"]) button {
    background-color: #FFFFFF !important;
    border: 1.5px solid #CBD5E1 !important;
    border-radius: 12px !important;
    padding: 14px 20px !important;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03) !important;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    text-align: center !important;
}

div[data-testid="column"]:has(button[key^="nav_alt_"]) button * {
    color: #0F172A !important;
    font-weight: 750 !important;
    font-size: 0.98rem !important;
}

div[data-testid="column"]:has(button[key^="nav_alt_"]) button:hover {
    background-color: #0891B2 !important;
    border-color: #0891B2 !important;
    box-shadow: 0 8px 20px rgba(8, 145, 178, 0.35) !important;
    transform: translateY(-3px) !important;
}

div[data-testid="column"]:has(button[key^="nav_alt_"]) button:hover * {
    color: #FFFFFF !important;
}
</style>
"""
st.markdown(TYMM_CSS, unsafe_allow_html=True)

# ============================================================
# 4. Süreç Bileşenlerini Biçimlendiren Fonksiyon
# ============================================================
def surec_bilesenlerini_bicimlendir(metin):
    if not metin or str(metin) == "nan":
        return "<p style='color: #64748b; font-size: 1rem;'>Bu örnek için özel bir alt süreç bileşeni belirtilmemiştir.</p>"
    
    metin = str(metin).strip()
    if "|" in metin:
        parcalar = [p.strip() for p in metin.split("|") if p.strip()]
        html_cikti = "<ul style='margin: 0; padding-left: 5px; list-style-type: none;'>"
        for madde in parcalar:
            html_cikti += f"""
            <li style='margin-bottom: 8px; color: #334155; font-size: 1rem; line-height: 1.6; display: flex; align-items: flex-start;'>
                <span style='margin-right: 8px; color: #EA580C; font-weight: 800;'>▪</span>
                <span>{madde}</span>
            </li>
            """
        html_cikti += "</ul>"
        return html_cikti
    
    return f"<p style='margin:0; font-size:1.05rem; line-height:1.7; color:#1E293B;'>{metin}</p>"

# ============================================================
# 5. Görsel Tarayıcı
# ============================================================
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

# ============================================================
# 6. Excel Verilerini Otomatik Yükleme (49 Araç + Beceri + Örnekler)
# ============================================================
@st.cache_data
def verileri_yukle(dosya_yolu, dosya_zamani):
    if not os.path.exists(dosya_yolu):
        return None, None, None
    try:
        xls = pd.ExcelFile(dosya_yolu)
        
        # 1. Sayfa: Araç Listesi
        sheet_arac = "Arac_Listesi" if "Arac_Listesi" in xls.sheet_names else xls.sheet_names[1] if len(xls.sheet_names) > 1 else xls.sheet_names[0]
        df_araclar = pd.read_excel(xls, sheet_name=sheet_arac)
        
        # Kolon standartlaştırma
        df_araclar.columns = [c.strip() for c in df_araclar.columns]
        rename_dict = {}
        for c in df_araclar.columns:
            if "No" in c: rename_dict[c] = "arac_id"
            elif "Adı" in c or "Adi" in c: rename_dict[c] = "arac_adi"
            elif "Sayfa" in c: rename_dict[c] = "sayfa_araligi"
            elif "Tanım" in c or "Tanim" in c: rename_dict[c] = "tanitim"
            elif "İlke" in c or "Ilke" in c or "Dikkat" in c: rename_dict[c] = "dikkat_edilecekler"
        df_araclar = df_araclar.rename(columns=rename_dict)
        df_araclar["arac_id"] = pd.to_numeric(df_araclar["arac_id"], errors="coerce")

        # Kategori ataması (Eğer sütun yoksa ID aralığına göre dinamik belirle)
        if "kategori" not in df_araclar.columns:
            def kategori_belirle(row_id):
                if row_id in [39, 40, 41]:
                    return "Puanlama Araçları"
                elif row_id in [42, 43, 44, 45]:
                    return "Değerlendirme Formları"
                elif row_id in [46, 47, 48, 49]:
                    return "Hızlı Değerlendirme Teknikleri"
                return "Ölçme ve Değerlendirme Araçları"
            df_araclar["kategori"] = df_araclar["arac_id"].apply(kategori_belirle)

        # 2. Sayfa: Beceri Matrisi
        df_beceriler = None
        if "Beceri_Matrisi" in xls.sheet_names:
            df_beceriler = pd.read_excel(xls, sheet_name="Beceri_Matrisi")
        elif len(xls.sheet_names) > 2:
            df_beceriler = pd.read_excel(xls, sheet_name=2)
            
        if df_beceriler is not None:
            df_beceriler.columns = [c.strip() for c in df_beceriler.columns]
            rename_b = {}
            for c in df_beceriler.columns:
                if "No" in c: rename_b[c] = "arac_id"
                elif "Adı" in c or "Adi" in c: rename_b[c] = "arac_adi"
                elif "Kodu" in c: rename_b[c] = "beceri_kodu"
                elif "Önerilen" in c or "Onerilen" in c: rename_b[c] = "onerilen_beceri"
                elif "Süreç" in c or "Surec" in c: rename_b[c] = "surec_bileseni"
            df_beceriler = df_beceriler.rename(columns=rename_b)
            df_beceriler["arac_id"] = pd.to_numeric(df_beceriler["arac_id"], errors="coerce")

        # 3. Sayfa: Örnek Uygulamalar
        df_ornekler = None
        if "Ornek_Uygulamalar" in xls.sheet_names:
            df_ornekler = pd.read_excel(xls, sheet_name="Ornek_Uygulamalar")
        elif len(xls.sheet_names) > 3:
            df_ornekler = pd.read_excel(xls, sheet_name=3)

        if df_ornekler is not None:
            df_ornekler.columns = [c.strip() for c in df_ornekler.columns]
            rename_o = {}
            for c in df_ornekler.columns:
                if "No" in c and "Araç" in c: rename_o[c] = "arac_id"
                elif "Örnek No" in c or "Ornek No" in c: rename_o[c] = "ornek_no"
                elif "Öğrenme" in c or "Ogrenme" in c or "Başlığı" in c: rename_o[c] = "ogrenme_ciktisi"
                elif "Detay" in c or "Notu" in c or "Süreç" in c: rename_o[c] = "surec_detay"
            df_ornekler = df_ornekler.rename(columns=rename_o)
            df_ornekler["arac_id"] = pd.to_numeric(df_ornekler["arac_id"], errors="coerce")

        return df_araclar, df_beceriler, df_ornekler
    except Exception as e:
        st.error(f"Excel okunurken hata oluştu: {e}")
        return None, None, None

dosya_zamani = os.path.getmtime(EXCEL_YOLU) if os.path.exists(EXCEL_YOLU) else 0
df, df_beceriler, df_ornekler = verileri_yukle(EXCEL_YOLU, dosya_zamani)

if df is None:
    st.error(f"`{EXCEL_YOLU}` dosyası bulunamadı! Lütfen Excel dosyasını `data` klasörüne ekleyin.")
    st.stop()

# ============================================================
# 7. Oturum Durumu ve Query Parametre Kontrolü
# ============================================================
if "secilen_arac" not in st.session_state:
    st.session_state.secilen_arac = None

if "aktif_gorunum" not in st.session_state:
    st.session_state.aktif_gorunum = "araclar"

if "action" in st.query_params and st.query_params["action"] == "geri":
    st.session_state.secilen_arac = None
    st.query_params.clear()
    st.rerun()

# ============================================================
# 8. Sol Kenar Çubuğu
# ============================================================
with st.sidebar:
    if os.path.exists(SOL_PANEL_GORSELI):
        st.markdown(f"""
        <div style="display: flex; justify-content: center; overflow: visible; margin-bottom: 12px;">
            <img src="data:image/png;base64,{base64.b64encode(open(SOL_PANEL_GORSELI, 'rb').read()).decode()}" 
                 style="width: 115%; max-width: 115%; border-radius: 8px;">
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### **TÜRKİYE YÜZYILI MAARİF MODELİ**")
    st.caption("Ölçme ve Değerlendirme Araçları Rehberi")
    
    if st.button("🏠 Ana Sayfa", use_container_width=True):
        st.session_state.secilen_arac = None
        st.session_state.aktif_gorunum = "araclar"
        st.rerun()

    st.markdown("---")
    
    mod_secim = st.radio(
        "Gezinme Yöntemi:",
        ["📋 Ölçme Araçları Listesi", "🎯 Beceriden Araca Ulaş"],
        index=0 if st.session_state.aktif_gorunum == "araclar" else 1
    )
    yeni_mod = "araclar" if "Ölçme" in mod_secim else "beceriler"
    if yeni_mod != st.session_state.aktif_gorunum:
        st.session_state.aktif_gorunum = yeni_mod
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

# ============================================================
# 9. GÖRÜNÜM 1: ANA SAYFA
# ============================================================
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

    # KURUMSAL TAKDİM
    with st.expander("📋 SUNUŞ VE METODOLOJİK ÇERÇEVE", expanded=False):
        takdim_icerik = """
        <div style="padding: 10px 6px;">
            <p style="color: #334155; font-size: 1.05rem; line-height: 1.8; margin-bottom: 16px; text-align: justify;">
                Bu rehber çalışma; <strong>Millî Eğitim Bakanlığı Din Öğretimi Genel Müdürlüğü Öğretim Programları ve Materyalleri Daire Başkanlığı</strong> bünyesinde yürütülen ders kitabı ve öğretim materyali yazım süreçlerinde görev alan komisyon üyelerine, ölçme ve değerlendirme araçlarının hazırlanması, yapılandırılması ve öğrenme çıktılarıyla tutarlı biçimde eşleştirilmesinde rehberlik etmek amacıyla <strong>Ölçme ve Değerlendirme Komisyonu</strong> tarafından hazırlanmıştır.
            </p>
            <div style="background-color: rgba(248, 250, 252, 0.85); border-radius: 10px; padding: 18px 22px; border: 1px solid #E2E8F0;">
                <h5 style="color: #0F172A; font-weight: 750; font-size: 1.05rem; margin-bottom: 10px;">📌 Örnek Uygulamaların Kapsamı ve Hazırlanış İlkeleri:</h5>
                <ul style="margin: 0; padding-left: 20px; color: #475569; font-size: 0.98rem; line-height: 1.75;">
                    <li style="margin-bottom: 6px;">
                        <strong>Doğrudan Alıntılanan Örnekler:</strong> Rehberde yer alan örneklerin öncelikli bölümü, Bakanlığımızca onaylanarak okullarımızda okutulan mevcut ders kitaplarından doğrudan seçilmiş olup <em>materyalin özgünlüğünü ve bağlamını korumak adına üzerlerinde hiçbir pedagojik veya biçimsel değişiklik yapılmamıştır</em>.
                    </li>
                    <li>
                        <strong>Uzman Geliştirmesi Örnekler:</strong> Ders kitaplarında doğrudan örneği bulunmayan veya yeni program yaklaşımıyla geliştirilmesine ihtiyaç duyulan ölçme araçları için örnekler, <em>ölçme ve değerlendirme uzmanları tarafından alana özgü ilkeler doğrultusunda sıfırdan hazırlanmıştır</em>.
                    </li>
                </ul>
            </div>
            <div style="margin-top: 14px; font-size: 0.88rem; color: #64748B; font-style: italic; border-top: 1px dashed #CBD5E1; padding-top: 10px;">
                - Bu rehber bağlayıcı bir mevzuat hükmü taşımamakta olup ders kitabı yazım komisyonlarının nitelikli, geçerli ve güvenilir ölçme-değerlendirme pratikleri geliştirmesini destekleyici bir referans kaynaktır.
            </div>
        </div>
        """
        st.markdown(takdim_icerik, unsafe_allow_html=True)

    # 1.A) BECERİDEN ARACA ULAŞMA MODU
    if st.session_state.aktif_gorunum == "beceriler":
        st.markdown('<div class="tymm-section-title">🎯 Becerilere Göre Ölçme Aracı Önerileri</div>', unsafe_allow_html=True)
        st.markdown("Öğretim programında yer alan beceriyi seçerek, bu beceriyi ölçmede kullanılabilecek önerilen araçları listeleyebilirsiniz.")
        
        st.warning("""
        ⚠️ **Önemli Not ve Sınırlılık:**  
        Burada sunulan eşleştirmeler ve araç listeleri **kesin bir kural veya doğrudan literatür bulgusuna dayalı bağlayıcı bir sınıflandırma niteliği taşımamakta olup**, kitap yazım sürecinde komisyon üyelerine fikir vermek amacıyla hazırlanmış **tavsiye ve öneri niteliğindedir**. 
        
        Ölçme aracının seçimi; ilgili öğrenme çıktısının derinliğine, dersin bağlamına, hedef kitleye ve öğretim materyalinin tasarım ilkelerine göre yazarın uzmanlık kararıyla belirlenmelidir.
        """)
        
        if df_beceriler is None or "onerilen_beceri" not in df_beceriler.columns:
            st.info("ℹ️ Beceri eşleme verisi bulunamadı.")
        else:
            # Filtre için geçerli beceri listesi
            gecerli_beceri_df = df_beceriler[df_beceriler["beceri_kodu"] != "-"].copy()
            beceri_listesi = ["--- Bir Beceri / Süreç Bileşeni Seçiniz ---"] + sorted(gecerli_beceri_df["onerilen_beceri"].dropna().unique().tolist())
            secilen_beceri = st.selectbox("İncelemek istediğiniz beceriyi seçiniz:", beceri_listesi)
            
            if secilen_beceri != "--- Bir Beceri / Süreç Bileşeni Seçiniz ---":
                eslesen_satirlar = df_beceriler[df_beceriler["onerilen_beceri"] == secilen_beceri]
                eslesen_arac_idleri = eslesen_satirlar["arac_id"].dropna().unique().tolist()
                onerilen_araclar_df = df[df["arac_id"].isin(eslesen_arac_idleri)].sort_values("arac_id")
                
                st.markdown(f"##### Bu Beceriyi Ölçmek İçin Önerilen Araçlar ({len(onerilen_araclar_df)} Araç)")
                cols = st.columns(3)
                for idx, (_, row) in enumerate(onerilen_araclar_df.iterrows()):
                    col_target = cols[idx % 3]
                    etiket = f"{int(row['arac_id'])}. {row['arac_adi']}"
                    if col_target.button(etiket, key=f"beceri_btn_{row['arac_id']}", use_container_width=True):
                        st.session_state.secilen_arac = row["arac_adi"]
                        st.rerun()

    # 1.B) MEVCUT 4 KATEGORİLİ LİSTE MODU
    else:
        kategoriler = [
            ("Ölçme ve Değerlendirme Araçları", "Ölçme ve Değerlendirme Araçları"),
            ("Puanlama Araçları", "Puanlama Araçları"),
            ("Değerlendirme Formları", "Değerlendirme Formları"),
            ("Hızlı Değerlendirme Teknikleri", "Hızlı Değerlendirme Teknikleri")
        ]

        for kat_baslik, kat_anahtar in kategoriler:
            st.markdown(f'<div class="tymm-section-title">{kat_baslik}</div>', unsafe_allow_html=True)
            kat_df = df[df["kategori"].astype(str).str.strip() == kat_anahtar]
            
            cols = st.columns(3)
            for idx, (_, row) in enumerate(kat_df.iterrows()):
                col_target = cols[idx % 3]
                etiket = f"{int(row['arac_id'])}. {row['arac_adi']}"
                if col_target.button(etiket, key=f"btn_{row['arac_id']}", use_container_width=True):
                    st.session_state.secilen_arac = row["arac_adi"]
                    st.rerun()

# ============================================================
# 10. GÖRÜNÜM 2: DETAY SAYFASI
# ============================================================
else:
    # Tüm araçların sıralı listesini al (ID sırasına göre)
    df_sirali = df.sort_values(by="arac_id").reset_index(drop=True)
    tum_arac_adlari = df_sirali["arac_adi"].tolist()
    
    secilen_index = tum_arac_adlari.index(st.session_state.secilen_arac)
    secilen_arac = df_sirali.iloc[secilen_index]
    arac_id = int(secilen_arac["arac_id"])

    # Önceki ve Sonraki Araç Bilgilerini Belirle
    onceki_arac_adi = None
    onceki_etiket = None
    if secilen_index > 0:
        onceki_satir = df_sirali.iloc[secilen_index - 1]
        onceki_arac_adi = onceki_satir["arac_adi"]
        onceki_etiket = f"⏮️ {int(onceki_satir['arac_id'])}. {onceki_arac_adi}"

    sonraki_arac_adi = None
    sonraki_etiket = None
    if secilen_index < len(df_sirali) - 1:
        sonraki_satir = df_sirali.iloc[secilen_index + 1]
        sonraki_arac_adi = sonraki_satir["arac_adi"]
        sonraki_etiket = f"{int(sonraki_satir['arac_id'])}. {sonraki_arac_adi} ⏭️"

    # SAĞ ÜSTTE SABİT GEZEN FLOATING BUTON
    st.markdown("""
    <div style="position: fixed; top: 75px; right: 35px; z-index: 9999999;">
        <a href="?action=geri" target="_self" class="floating-back-link">
            <div class="floating-back-box">
                <span>⬅️</span>
                <span>Geri Dön</span>
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Üst Başlık
    st.markdown(f"""
    <div style="margin-bottom: 20px;">
        <span style="background-color: #CCFBF1; color: #0F766E; font-size: 0.85rem; font-weight: 700; padding: 4px 10px; border-radius: 6px;">
            {secilen_arac.get('kategori', 'Ölçme Aracı')}
        </span>
        <span style="background-color: #E0F2FE; color: #0369A1; font-size: 0.85rem; font-weight: 700; padding: 4px 10px; border-radius: 6px; margin-left: 6px;">
            Sayfa: {secilen_arac.get('sayfa_araligi', '')}
        </span>
        <h2 style="color: #0F172A; font-size: 1.85rem; font-weight: 800; margin-top: 8px; margin-bottom: 0;">
            {arac_id}. {secilen_arac['arac_adi']}
        </h2>
    </div>
    """, unsafe_allow_html=True)

    # 4 Ana Sekme
    tab1, tab2, tab3, tab4 = st.tabs([
        "**1. Tanıtım & Kapsam**",
        "**2. Hazırlarken Dikkat Edilecek Hususlar**",
        "**3. Önerilen Beceriler (2 Sütun)**",
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
                temiz_satir = re.sub(r'^[✓✔•\-\*\s]+', '', satir).strip()
                if temiz_satir and not temiz_satir.startswith("Sürecinde Dikkat"):
                    li_icerik += f"<li>{temiz_satir}</li>"
        if not li_icerik:
            li_icerik = "<li>Belirtilen husus bulunamadı.</li>"

        st.markdown(f"""
        <div class="tymm-card">
            <div class="tymm-card-title">Hazırlık ve Yazım Sürecinde Dikkat Edilecek İlkeler</div>
            <ul>
                {li_icerik}
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # 3. Önerilen Beceriler (2 Sütunlu Temiz Tablo)
    with tab3:
        if df_beceriler is not None:
            arac_beceri_df = df_beceriler[df_beceriler["arac_id"] == arac_id].copy()
            if not arac_beceri_df.empty:
                st.markdown(f"""
                <div class="tymm-card" style="margin-bottom: 16px;">
                    <div class="tymm-card-title">Bu Araçla Ölçülmesi Önerilen Beceriler ve Süreç Bileşenleri</div>
                    <p>Aşağıdaki tabloda bu ölçme aracı ile yoklanması önerilen kavramsal beceriler, dinî alan becerileri ve süreç bileşenleri listelenmiştir.</p>
                </div>
                """, unsafe_allow_html=True)
                
                tablo_verisi = arac_beceri_df[["onerilen_beceri", "surec_bileseni"]].copy()
                tablo_verisi.columns = ["Önerilen Beceri", "Süreç Bileşenleri"]
                st.dataframe(tablo_verisi, use_container_width=True, hide_index=True)
            else:
                st.info("Bu araç için kayıtlı özel bir beceri eşleşmesi bulunmamaktadır.")
        else:
            st.warning("Beceri matrisi tablosu yüklenemedi.")

    # 4. Örnek Görseller ve Çıktı Eşleşmesi
    with tab4:
        st.write("")
        ornekler_listesi = tum_ornekleri_bul(arac_id)
        
        # Bu araca ait exceldeki örnekler
        ilgili_ornekler_df = pd.DataFrame()
        if df_ornekler is not None:
            ilgili_ornekler_df = df_ornekler[df_ornekler["arac_id"] == arac_id].copy()
        
        # Görsel varsa görsellerle birlikte göster
        if ornekler_listesi:
            for o_no, gorsel_yolu_bulunan, dosya_adi in ornekler_listesi:
                # Eşleşen öğrenme çıktısını bul
                cikti_metni = ""
                surec_metni = ""
                if not ilgili_ornekler_df.empty and len(ilgili_ornekler_df) >= o_no:
                    satir_ornek = ilgili_ornekler_df.iloc[o_no - 1]
                    cikti_metni = satir_ornek.get("ogrenme_ciktisi", "")
                    surec_metni = satir_ornek.get("surec_detay", "")

                bicimli_cikti = surec_bilesenlerini_bicimlendir(surec_metni)
                
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
                        <p style="font-weight:700; color:#0F172A; margin-bottom:8px;">{cikti_metni}</p>
                        {bicimli_cikti}
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("<hr style='border: 0; border-top: 1px solid #E2E8F0; margin: 30px 0;'>", unsafe_allow_html=True)
        else:
            # Görsel henüz yoksa exceldeki örnek metinlerini göster
            if not ilgili_ornekler_df.empty:
                for _, r_orn in ilgili_ornekler_df.iterrows():
                    o_sirasi = r_orn.get("ornek_no", "Örnek")
                    cikti_b = r_orn.get("ogrenme_ciktisi", "")
                    surec_d = r_orn.get("surec_detay", "")
                    bicimli_c = surec_bilesenlerini_bicimlendir(surec_d)
                    
                    st.markdown(f"""
                    <div class="tymm-cikti-box">
                        <h5>{o_sirasi} - {cikti_b}</h5>
                        {bicimli_c}
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="tymm-img-container">
                    <p style="color: #64748B; font-weight: 600; margin: 30px 0;">
                        Bu ölçme aracına ait örnek görsel bulunamadı.<br>
                        Beklenen dosya formatı: <code>assets/images/ornek{arac_id}_1.png / .jpg</code>
                    </p>
                </div>
                """, unsafe_allow_html=True)

    # ============================================================
    # Sayfa Altı Navigasyon (Footer)
    # ============================================================
    st.markdown('<div class="footer-nav-container">', unsafe_allow_html=True)
    st.write("")
    st.write("")
    col_alt_sol, col_alt_bosluk, col_alt_sag = st.columns([4, 2, 4])
    
    with col_alt_sol:
        if onceki_arac_adi:
            if st.button(onceki_etiket, key="nav_alt_onceki", use_container_width=True):
                st.session_state.secilen_arac = onceki_arac_adi
                st.rerun()
                
    with col_alt_sag:
        if sonraki_arac_adi:
            if st.button(sonraki_etiket, key="nav_alt_sonraki", use_container_width=True):
                st.session_state.secilen_arac = sonraki_arac_adi
                st.rerun()
