# ==============================================================================
# [Script] Interactive Multilingual Syllabus Web Application (Embedded Flags)
# 【腳本】多語系互動課綱網頁應用（真·國旗鑲嵌於按鈕內 + 防融色微邊框修正版）
# ==============================================================================

import streamlit as st

# 1. 頁面基本配置
st.set_page_config(
    page_title="Python AI Applications - Syllabus",
    layout="wide",
    page_icon="🎓"
)

# 2. 標題與簡介
st.title("🎓 Python AI Applications (Python AI 應用)")
st.caption("18-Week Interactive Syllabus & Parallel Multilingual Companion | 18 週互動課綱與多語系對照")

# 3. 語言定義（含 FlagCDN 高畫質圖片、名稱、對照鍵值）
LANG_CONFIG = {
    "tw": {"label": "繁體中文", "name": "🇹🇼 繁體中文 (Traditional Chinese)", "flag": "https://flagcdn.com/w40/tw.png"},
    "us": {"label": "English", "name": "🇺🇸 English (Official)", "flag": "https://flagcdn.com/w40/us.png"},
    "vn": {"label": "Tiếng Việt", "name": "🇻🇳 Tiếng Việt (Vietnamese)", "flag": "https://flagcdn.com/w40/vn.png"},
    "my": {"label": "B. Melayu", "name": "🇲🇾 Bahasa Melayu (Malay)", "flag": "https://flagcdn.com/w40/my.png"},
    "id": {"label": "B. Indonesia", "name": "🇮🇩 Bahasa Indonesia (Indonesian)", "flag": "https://flagcdn.com/w40/id.png"},
    "th": {"label": "ภาษาไทย", "name": "🇹🇭 ภาษาไทย (Thai)", "flag": "https://flagcdn.com/w40/th.png"},
    "fr": {"label": "Français", "name": "🇫🇷 Français (French)", "flag": "https://flagcdn.com/w40/fr.png"}
}

# 讀取 URL 參數中的語言，若無則預設為繁體中文 (tw)
current_code = st.query_params.get("lang", "tw")
if current_code not in LANG_CONFIG:
    current_code = "tw"

current_info = LANG_CONFIG[current_code]

st.markdown("**🌐 Select Parallel Language (點擊按鈕切換右欄對照語言):**")

# 自訂按鈕 CSS：含背景底色、邊框、陰影、懸停反饋，以及國旗防融色微灰邊
st.markdown("""
<style>
.flag-btn-grid {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 10px;
    margin: 12px 0 20px 0;
}
.flag-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 9px 8px;
    background-color: #f7f9fb;
    border: 1px solid #dcdfe6;
    border-radius: 8px;
    text-decoration: none !important;
    color: #2c3e50 !important;
    font-size: 14px;
    font-weight: 500;
    transition: all 0.2s ease-in-out;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
}
.flag-btn:hover {
    border-color: #ff4b4b;
    background-color: #fff5f5;
    color: #ff4b4b !important;
    transform: translateY(-1px);
    box-shadow: 0 3px 6px rgba(255,75,75,0.15);
}
.flag-btn.active {
    border-color: #ff4b4b;
    background-color: #ffeaea;
    color: #d93838 !important;
    font-weight: 700;
    box-shadow: inset 0 0 0 1px #ff4b4b;
}
.flag-img {
    width: 22px;
    height: 15px;
    object-fit: cover;
    border-radius: 2px;
    border: 1px solid #b0b4b9; /* 明確外框：法國、印尼的白色區塊絕對不會被背景吃掉 */
}
</style>
""", unsafe_allow_html=True)

# 緊湊無縮排字串，避免觸發 Markdown 的程式碼縮排規則
btn_items = "".join([
    f'<a class="flag-btn {"active" if code == current_code else ""}" href="?lang={code}" target="_self"><img class="flag-img" src="{data["flag"]}" alt="{data["label"]}"><span>{data["label"]}</span></a>'
    for code, data in LANG_CONFIG.items()
])
st.markdown(f'<div class="flag-btn-grid">{btn_items}</div>', unsafe_allow_html=True)

st.info(f"💡 **Current Parallel View / 目前對照語言**: **{current_info['name']}**  \n*(Conductor's Note: Built with Python & Streamlit in under 95 lines. You will build and deploy apps like this in Week 10!)*")

# 4. 課程多語系資料庫
weeks_data = [
    {
        "wk": "Week 1",
        "en": "**Course Onboarding & Vibe Coding**  \nGoogle Colab setup, prompt-driven AI coding, orchestra conductor mindset.",
        "zh": "**課程導覽與自然語言編程**  \nGoogle Colab 設定、提示詞驅動 AI 編程、建立指揮家思維。",
        "vi": "**Khởi động khóa học & Vibe Coding**  \nCài đặt Google Colab, lập trình AI bằng câu lệnh tự nhiên, tư duy chỉ huy.",
        "ms": "**Orientasi Kursus & Vibe Coding**  \nPersediaan Google Colab, pengaturcaraan AI pacuan prompt, minda konduktor orkestra.",
        "id": "**Orientasi Kursus & Vibe Coding**  \nPengaturan Google Colab, coding AI dengan prompt alami, pola pikir konduktor.",
        "th": "**แนะนำรายวิชา & Vibe Coding**  \nตั้งค่า Google Colab, เขียนโค้ด AI ด้วยภาษาธรรมชาติ, แนวคิดวาทยกร",
        "fr": "**Présentation du cours & Vibe Coding**  \nConfiguration de Google Colab, programmation par invites, posture de chef d'orchestre."
    },
    {
        "wk": "Week 2",
        "en": "**Market Data Engineering: Apple & TSMC**  \nFetching daily stock prices, working with dataframes, plotting trend charts.",
        "zh": "**市場數據工程：台積電與蘋果**  \n每日股價數據擷取、資料表處理、繪製股價走勢圖。",
        "vi": "**Kỹ thuật dữ liệu thị trường: Apple & TSMC**  \nThu thập giá cổ phiếu hàng ngày, xử lý dataframe, vẽ biểu đồ xu hướng.",
        "ms": "**Kejuruteraan Data Pasaran: Apple & TSMC**  \nMendapatkan harga saham harian, memproses dataframe, membina carta trend harga.",
        "id": "**Rekayasa Data Pasar: Apple & TSMC**  \nMengambil data harga saham harian, tabel data, visualisasi tren.",
        "th": "**วิศวกรรมข้อมูลตลาด: Apple & TSMC**  \nดึงราคาหุ้นรายวัน, จัดการข้อมูล, สร้างแผนภูมิแนวโน้ม",
        "fr": "**Ingénierie des données de marché : Apple & TSMC**  \nExtraction des cours quotidiens, manipulation de tableaux, graphiques de tendance."
    },
    {
        "wk": "Week 3",
        "en": "**Global EV Trends: Tesla vs. Worldwide Leaders**  \nComparing EV leaders, calculating daily returns, basic risk metrics.",
        "zh": "**全球電動車趨勢：Tesla 與全球車廠**  \n電動車龍頭指標比對、日報酬率計算與基礎風險指標評估。",
        "vi": "**Xu hướng xe điện toàn cầu: Tesla vs Các hãng lớn**  \nSo sánh các hãng xe điện hàng đầu, tính tỷ suất sinh lời hàng ngày.",
        "ms": "**Trend Kenderaan Elektrik Global: Tesla vs Peneraju Dunia**  \nMembandingkan peneraju pasaran EV, pengiraan pulangan harian, metrik risiko asas.",
        "id": "**Tren EV Global: Tesla vs Pemimpin Pasar**  \nMembandingkan pemain utama EV, return harian, metrik risiko dasar.",
        "th": "**แนวโน้ม EV ระดับโลก: Tesla เทียบกับผู้นำตลาดโลก**  \nเปรียบเทียบผู้ผลิต EV ชั้นนำ, อัตราผลตอบแทนรายวัน, ตัวชี้วัดความเสี่ยง",
        "fr": "**Tendances mondiales du VE : Tesla vs Leaders mondiaux**  \nComparaison des acteurs majeurs, rendements quotidiens, métriques de risque."
    },
    {
        "wk": "Week 4",
        "en": "**Quantitative Trading Strategies**  \nMoving averages (20MA vs 60MA), rule-based trading vs Buy & Hold backtesting.",
        "zh": "**量化交易策略實戰**  \n均線交叉法則（20MA vs 60MA）、策略交易與買進持有對比、回測概念。",
        "vi": "**Chiến lược giao dịch định lượng**  \nĐường trung bình MA20 vs MA60, chiến lược quy tắc so với Buy & Hold.",
        "ms": "**Strategi Dagangan Kuantitatif**  \nPurata bergerak (20MA vs 60MA), dagangan berasaskan peraturan lwn Buy & Hold.",
        "id": "**Strategi Trading Kuantitatif**  \nRata-rata bergerak 20MA vs 60MA, perbandingan aturan trading vs Buy & Hold.",
        "th": "**กลยุทธ์การเทรดเชิงปริมาณ**  \nแนวคิดเส้นค่าเฉลี่ย 20MA vs 60MA, การเทรดตามกฎเทียบกับการถือครอง",
        "fr": "**Stratégies de trading quantitatif**  \nMoyennes mobiles 20MA vs 60MA, trading basé sur des règles vs Buy & Hold."
    },
    {
        "wk": "Week 15",
        "en": "**AI Ethics, Data Privacy & Security**  \nConfidentiality boundaries, API key protection, prompt injection defense.",
        "zh": "**AI 倫理、資料隱私與資安防護**  \n商業個資與機密界線、API 金鑰安全管理、提示詞注入防禦。",
        "vi": "**Đạo đức AI, Quyền riêng tư & Bảo mật dữ liệu**  \nRanh giới dữ liệu, bảo mật khóa API, phòng thủ prompt.",
        "ms": "**Etika AI, Privasi Data & Keselamatan**  \nBatasan kerahsiaan data, perlindungan kunci API, pertahanan suntikan prompt.",
        "id": "**Etika AI, Privasi Data & Keamanan**  \nBatasan data rahasia, keamanan API key, pertahanan prompt.",
        "th": "**จริยธรรม AI ความเป็นส่วนตัวและความปลอดภัยของข้อมูล**  \nการจัดการความลับ, การปกป้อง API Key, การป้องกัน Prompt",
        "fr": "**Éthique de l'IA, Confidentialité et Sécurité**  \nFrontières des données, protection des clés API, défense contre les invites."
    },
    {
        "wk": "Week 16",
        "en": "**Final Project Showcase**  \nIn-class live demonstration of interactive FinTech web applications.",
        "zh": "**【期末發表】專題成果展示會**  \n課堂現場發表互動式金融科技 Web 應用與實務成果交流。",
        "vi": "**Báo cáo đồ án cuối kỳ**  \nTrình bày trực tiếp ứng dụng web FinTech tương tác trước lớp.",
        "ms": "**Pembentangan Projek Akhir**  \nDemonstrasi langsung aplikasi web FinTech interaktif di dalam kelas.",
        "id": "**Presentasi Proyek Akhir**  \nDemonstrasi langsung aplikasi web FinTech interaktif di kelas.",
        "th": "**การนำเสนอโครงงานปลายภาค**  \nสาธิตเว็บแอปพลิเคชัน FinTech แบบอินเทอร์แอคทีฟในชั้นเรียน",
        "fr": "**Présentation du projet final**  \nDémonstration en direct d'applications web FinTech interactives en classe."
    }
]

# 5. 雙欄並列呈現
col_en, col_trans = st.columns(2)

with col_en:
    st.subheader("🇺🇸 Official English Syllabus")
    for item in weeks_data:
        with st.container(border=True):
            st.markdown(f"### {item['wk']}")
            st.markdown(item["en"])

with col_trans:
    st.subheader(f"{current_info['name']}")
    for item in weeks_data:
        lang_mapping = {
            "tw": item["zh"],
            "us": item["en"],
            "vn": item["vi"],
            "my": item["ms"],
            "id": item["id"],
            "th": item["th"],
            "fr": item["fr"]
        }
        trans_text = lang_mapping.get(current_code, item["zh"])

        with st.container(border=True):
            st.markdown(f"### {item['wk']} (對照)")
            st.markdown(trans_text)
