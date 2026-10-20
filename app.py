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
FON_GORSELI_PNG = os.path.join(GORSEL_KLASORU, "webfon.png")
FON_GORSELI_JPG = os.path.join(GORSEL_KLASORU, "webfon.jpg")
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

# 3. KESİN ÇÖZÜM: Dark/Light Mod Hover Çakışmasını Engelleyen CSS
TYMM_CSS = """
<style>
/* Sol Kenar Çubuğu */
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
}
section[data-testid="stSidebar"] button:hover {
    background-color: #0891B2 !important;
    border-color: #0891B2 !important;
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

/* ============================================================
   ARAÇ BUTONLARI (KARTLAR) İÇİN KESİN HOVER ÇÖZÜMÜ
   ============================================================ */

/* Normal Durum: Koyu zemin, net beyaz yazı */
div[data-testid="stButton"] > button {
    background-color: #0F172A !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
    padding: 14px 18px !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.06) !important;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

/* İçindeki yazılar normalde beyaz olsun */
div[data-testid="stButton"] > button p,
div[data-testid="stButton"] > button span,
div[data-testid="stButton"] > button div {
    color: #FFFFFF !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
}

/* HOVER (ÜZERİNE GELİNCE): Zemin Turkuaz Mavi, Yazı Parlak Beyaz */
div[data-testid="stButton"] > button:hover {
    background-color: #0891B2 !important;
    border-color: #0891B2 !important;
    box-shadow: 0 8px 20px rgba(8, 145, 178, 0.4) !important;
    transform: translateY(-2px) !important;
}

/* Hover anında TÜM alt etiketleri zorla beyaz yap */
div[data-testid="stButton"] > button:hover * {
    color: #FFFFFF !important;
    background-color: transparent !important;
}

/* ============================================================
   SEKME (TAB) BUTONLARI İÇİN KESİN HOVER ÇÖZÜMÜ
   ============================================================ */
div[data-testid="stTabs"] {
    gap: 10px !important;
    margin-top: 15px !important;
    margin-bottom: 25px !important;
}

/* Sekmeler Normal Durum */
div[data-testid="stTabs"] button[role="tab"] {
    background-color: #1E293B !important;
    border: 1px solid #334155 !important;
    border-radius: 10px !important;
    padding: 14px 22px !important;
    transition: all 0.2s ease !important;
}
div[data-testid="stTabs"] button[role="tab"] * {
    color: #F8FAFC !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
}

/* Sekmeler Hover Durumu */
div[data-testid="stTabs"] button[role="tab"]:hover {
    background-color: #0891B2 !important;
    border-color: #0891B2 !important;
}
div[data-testid="stTabs"] button[role="tab"]:hover * {
    color: #FFFFFF !important;
    background-color: transparent !important;
}

/* Sekmeler Seçili (Aktif) Durum */
div[data-testid="stTabs"] button[role="tab"][aria-selected="true"] {
    background-color: #0891B2 !important;
    border-color: #0891B2 !important;
    box-shadow: 0 4px 14px rgba(8, 145, 178, 0.4) !important;
}
div[data-testid="stTabs"] button[role="tab"][aria-selected="true"] * {
    color: #FFFFFF !important;
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

.tymm-badge-item {
    background-color: #F0FDFA;
    border: 1px solid #CCFBF1;
    padding: 12px 18px;
    border-radius: 10px;
    margin-bottom: 10px;
    color: #0F766E;
    font-size: 1.02rem;
    font-weight: 600;
    display: flex;
    align-items: center;
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
}
.tymm-cikti-box h5 {
    color: #9A3412;
    margin-bottom: 14px;
    font-size: 1.15rem;
    font-weight: 800;
}
</style>
"""
st.markdown(TYMM_CSS, unsafe_allow_html=True)

# 4. Süreç Bileşenlerini Biçimlendiren Fonksiyon
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
                <span style='margin-right: 8px; color: #EA580C; font-weight: 800;'>▪</span>
                <span><strong style='color: #0F172A;'>{etiket}</strong> {icerik}</span>
            </li>
            """
        else:
            html_cikti += f"""
            <li style='margin-bottom: 10px; color: #334155; font-size: 1rem; line-height: 1.6; display: flex; align-items: flex-start;'>
                <span style='margin-right: 8px; color: #EA580C; font-weight: 800;'>▪</span>
                <span>{madde}</span>
            </li>
            """
    html_cikti += "</ul>"
    return html_cikti

# 5. Görsel Tarayıcı
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

# 6. Excel Verilerini Yükleme
@st.cache_data
def verileri_yukle(dosya_yolu):
    if not os.path.exists(dosya_yolu):
        return None, None
    try:
        xls = pd.ExcelFile(dosya_yolu)
        df_araclar = pd.read_excel(xls, sheet_name=0)
        
        df_beceriler = None
        if "beceri_eslesme" in xls.sheet_names:
            df_beceriler = pd.read_excel(xls, sheet_name="beceri_eslesme")
        elif len(xls.sheet_names) > 1:
            df_beceriler = pd.read_excel(xls, sheet_name=1)
            
        return df_araclar, df_beceriler
    except Exception as e:
        return None, None

df, df_beceriler = verileri_yukle(EXCEL_YOLU)

if df is None:
    st.error(f"`{EXCEL_YOLU}` dosyası bulunamadı! Lütfen Excel dosyasını `data` klasörüne ekleyin.")
    st.stop()

# 7. Oturum Durumu
if "secilen_arac" not in st.session_state:
    st.session_state.secilen_arac = None

if "aktif_gorunum" not in st.session_state:
    st.session_state.aktif_gorunum = "araclar"

# 8. Sol Kenar Çubuğu
with st.sidebar:
    st.markdown("### 📘 Maarif Modeli")
    st.caption("Ölçme ve Değerlendirme Rehberi")
    
    if st.button("🏠 Ana Sayfaya Dön", use_container_width=True):
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

# ----------------------------------------------------
# 9. GÖRÜNÜM 1: ANA SAYFA
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

    # KURUMSAL TAKDİM (Açılır-Kapanır Başlık)
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
        st.markdown("Öğretim programında yer alan beceri veya süreç bileşenini seçerek, bu çıktıyı ölçmede kullanılabilecek araç önerilerini listeleyebilirsiniz.")
        
        st.warning("""
        ⚠️ **Önemli Not ve Sınırlılık:**  
        Burada sunulan eşleştirmeler ve araç listeleri **kesin bir kural veya doğrudan literatür bulgusuna dayalı bağlayıcı bir sınıflandırma niteliği taşımamakta olup**, kitap yazım sürecinde komisyon üyelerine fikir vermek amacıyla hazırlanmış **tavsiye ve öneri niteliğindedir**. 
        
        Ölçme aracının seçimi; ilgili öğrenme çıktısının derinliğine, dersin bağlamına, hedef kitleye ve öğretim materyalinin tasarım ilkelerine göre yazarın uzmanlık kararıyla belirlenmelidir.
        """)
        
        if df_beceriler is None or "beceri_adi" not in df_beceriler.columns:
            st.info("ℹ️ **Beceri Eşleştirme Modülü Hazırlık Aşamasındadır.**\n\n`araclar.xlsx` dosyanıza `beceri_eslesme` sayfası eklendiğinde önerilen araçlar otomatik olarak bu alanda listelenecektir.")
        else:
            beceri_listesi = ["--- Bir Beceri / Süreç Bileşeni Seçiniz ---"] + df_beceriler["beceri_adi"].dropna().tolist()
            secilen_beceri = st.selectbox("İncelemek istediğiniz beceriyi seçiniz:", beceri_listesi)
            
            if secilen_beceri != "--- Bir Beceri / Süreç Bileşeni Seçiniz ---":
                secilen_satir = df_beceriler[df_beceriler["beceri_adi"] == secilen_beceri].iloc[0]
                
                if "aciklama" in secilen_satir and pd.notna(secilen_satir["aciklama"]):
                    st.markdown(f"""
                    <div class="tymm-card" style="margin-bottom: 20px;">
                        <div class="tymm-card-title">Ölçme Yaklaşımı ve Rehber Not</div>
                        <p>{secilen_satir['aciklama']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                id_metni = str(secilen_satir.get("uygun_arac_idleri", ""))
                if id_metni and id_metni != "nan":
                    id_listesi = [int(s.strip()) for s in re.findall(r'\d+', id_metni)]
                    onerilen_araclar_df = df[df["arac_id"].isin(id_listesi)]
                    
                    st.markdown(f"##### Bu Beceriyi Ölçmek İçin Önerilen Araçlar ({len(onerilen_araclar_df)} Araç)")
                    cols = st.columns(3)
                    for idx, (_, row) in enumerate(onerilen_araclar_df.iterrows()):
                        col_target = cols[idx % 3]
                        etiket = f"{int(row['arac_id'])}. {row['arac_adi']}"
                        if col_target.button(etiket, key=f"beceri_btn_{row['arac_id']}", use_container_width=True):
                            st.session_state.secilen_arac = row["arac_adi"]
                            st.rerun()
                else:
                    st.warning("Bu beceri için henüz eşleştirilmiş araç ID'si girilmemiş.")

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

    col_baslik, col_geri = st.columns([5, 1], vertical_alignment="center")
    with col_baslik:
        st.markdown(f"""
        <div style="margin-bottom: 10px;">
            <span style="background-color: #CCFBF1; color: #0F766E; font-size: 0.85rem; font-weight: 700; padding: 4px 10px; border-radius: 6px;">
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
            satirlar =
