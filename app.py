# ==============================================================================
# [Script] Interactive Multilingual Syllabus Table (School System Layout)
# 【腳本】多語系互動課綱表格化網頁（仿學校教務系統 6 欄位設計）
# ==============================================================================

import streamlit as st
import pandas as pd

# 1. 頁面基本配置
st.set_page_config(
    page_title="Python AI Applications - Syllabus Table",
    layout="wide",
    page_icon="🎓"
)

# 2. 標題與副標題
st.title("🎓 Python AI Applications (Python AI 應用)")
st.caption("115 學期 四技經管系2丙 (3.0 學分 / 3.0 時數) | 互動式多語系課程進度表")

# 3. 語言定義與切換設定
LANG_CONFIG = {
    "tw": {"label": "繁體中文", "name": "🇹🇼 繁體中文 (Traditional Chinese)", "flag": "https://flagcdn.com/w40/tw.png"},
    "us": {"label": "English", "name": "🇺🇸 English (Official)", "flag": "https://flagcdn.com/w40/us.png"},
    "vn": {"label": "Tiếng Việt", "name": "🇻🇳 Vietnamese (Tiếng Việt)", "flag": "https://flagcdn.com/w40/vn.png"},
    "my": {"label": "B. Melayu", "name": "🇲🇾 Bahasa Melayu (Malay)", "flag": "https://flagcdn.com/w40/my.png"},
    "id": {"label": "B. Indonesia", "name": "🇮🇩 Bahasa Indonesia (Indonesian)", "flag": "https://flagcdn.com/w40/id.png"},
    "th": {"label": "ภาษาไทย", "name": "🇹🇭 Thai (ภาษาไทย)", "flag": "https://flagcdn.com/w40/th.png"},
    "fr": {"label": "Français", "name": "🇫🇷 French (Français)", "flag": "https://flagcdn.com/w40/fr.png"}
}

current_code = st.query_params.get("lang", "tw")
if current_code not in LANG_CONFIG:
    current_code = "tw"

current_info = LANG_CONFIG[current_code]

# 自訂 CSS：按鈕格線、防融色國旗外框與表格優化
st.markdown("""
<style>
.flag-btn-grid {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 10px;
    margin: 10px 0 18px 0;
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
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.flag-btn:hover {
    border-color: #ff4b4b;
    background-color: #fff5f5;
    color: #ff4b4b !important;
    transform: translateY(-1px);
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
    border: 1px solid #b0b4b9;
}
</style>
""", unsafe_allow_html=True)

st.markdown("**🌐 Select Parallel Language (點擊按鈕切換表格對照語言):**")

# 7 國語言按鈕列
btn_items = "".join([
    f'<a class="flag-btn {"active" if code == current_code else ""}" href="?lang={code}" target="_self"><img class="flag-img" src="{data["flag"]}" alt="{data["label"]}"><span>{data["label"]}</span></a>'
    for code, data in LANG_CONFIG.items()
])
st.markdown(f'<div class="flag-btn-grid">{btn_items}</div>', unsafe_allow_html=True)

st.info(f"💡 **Current Parallel View / 目前對照語言**: **{current_info['name']}**")

# 4. 課程表格資料庫（支援 7 國語言）
syllabus_data = [
    {
        "week": "Week 1",
        "date": "2026/09/10",
        "tw": {
            "progress": "課程導覽與自然語言編程",
            "homework": "Lab 0: 課堂趣味實作探索",
            "summary": "課程總覽；提示詞驅動 AI 編程與自然語言；Google Colab 設定；零語法負擔。",
            "remark": "實體上課"
        },
        "us": {
            "progress": "Course Onboarding & Vibe Coding",
            "homework": "Lab 0: In-class fun exploration",
            "summary": "Course overview; prompt-driven programming with natural language; Google Colab setup; zero syntax stress.",
            "remark": "In-person"
        },
        "vn": {
            "progress": "Khởi động khóa học & Vibe Coding",
            "homework": "Lab 0: Khám phá thú vị trên lớp",
            "summary": "Tổng quan khóa học; lập trình AI bằng ngôn ngữ tự nhiên; cài đặt Google Colab; không áp lực cú pháp.",
            "remark": "Trực tiếp"
        },
        "my": {
            "progress": "Orientasi Kursus & Vibe Coding",
            "homework": "Lab 0: Penerokaan seronok di kelas",
            "summary": "Gambaran keseluruhan kursus; pengaturcaraan dipacu prompt dengan bahasa asli; persediaan Google Colab.",
            "remark": "Semuka"
        },
        "id": {
            "progress": "Orientasi Kursus & Vibe Coding",
            "homework": "Lab 0: Eksplorasi menyenangkan",
            "summary": "Gambaran umum kursus; pemrograman dengan prompt bahasa alami; pengaturan Google Colab.",
            "remark": "Tatap muka"
        },
        "th": {
            "progress": "แนะนำรายวิชา & Vibe Coding",
            "homework": "Lab 0: สำรวจความสนุกในชั้นเรียน",
            "summary": "ภาพรวมรายวิชา การเขียนโปรแกรมด้วยภาษาธรรมชาติ การตั้งค่า Google Colab ปราศจากความเครียดเรื่องไวยากรณ์",
            "remark": "ในชั้นเรียน"
        },
        "fr": {
            "progress": "Présentation du cours & Vibe Coding",
            "homework": "Lab 0 : Exploration ludique",
            "summary": "Aperçu du cours ; programmation par invites en langage naturel ; configuration de Google Colab.",
            "remark": "En présentiel"
        }
    },
    {
        "week": "Week 2",
        "date": "2026/09/17",
        "tw": {
            "progress": "市場數據工程：台積電與蘋果",
            "homework": "課堂即時實作與練習",
            "summary": "加退選結束；透過 Python 擷取每日股價；繪製視覺化走勢圖；新手友善導覽。",
            "remark": "實體上課"
        },
        "us": {
            "progress": "Market Data Engineering: Apple & TSMC",
            "homework": "In-class live practice",
            "summary": "Add/drop period; fetching daily stock prices with Python; creating visual trend charts; friendly onboarding.",
            "remark": "In-person"
        },
        "vn": {
            "progress": "Kỹ thuật dữ liệu thị trường: Apple & TSMC",
            "homework": "Thực hành trực tiếp trên lớp",
            "summary": "Thu thập giá cổ phiếu hàng ngày với Python; vẽ biểu đồ xu hướng.",
            "remark": "Trực tiếp"
        },
        "my": {
            "progress": "Kejuruteraan Data Pasaran: Apple & TSMC",
            "homework": "Amali langsung di kelas",
            "summary": "Mendapatkan harga saham harian dengan Python; membina carta trend visual.",
            "remark": "Semuka"
        },
        "id": {
            "progress": "Rekayasa Data Pasar: Apple & TSMC",
            "homework": "Praktik langsung di kelas",
            "summary": "Mengambil harga saham harian dengan Python; membuat grafik tren visual.",
            "remark": "Tatap muka"
        },
        "th": {
            "progress": "วิศวกรรมข้อมูลตลาด: Apple & TSMC",
            "homework": "ปฏิบัติจริงในชั้นเรียน",
            "summary": "ดึงราคาหุ้นรายวันด้วย Python สร้างแผนภูมิแนวโน้มภาพ",
            "remark": "ในชั้นเรียน"
        },
        "fr": {
            "progress": "Ingénierie des données : Apple & TSMC",
            "homework": "Pratique en direct en classe",
            "summary": "Extraction des cours boursiers quotidiens avec Python ; graphiques de tendance.",
            "remark": "En présentiel"
        }
    },
    {
        "week": "Week 3",
        "date": "2026/09/24",
        "tw": {
            "progress": "全球電動車趨勢：Tesla 與全球車廠",
            "homework": "Lab 1: 電動車市場趨勢筆記本",
            "summary": "名單確認；對比全球電動車龍頭與供應鏈；計算日報酬率與基礎風險指標。",
            "remark": "實體上課"
        },
        "us": {
            "progress": "Global EV Trends: Tesla vs. Worldwide Leaders",
            "homework": "Lab 1: EV market trends notebook",
            "summary": "Roster finalized; comparing global EV leaders and key supply chain players; calculating daily returns.",
            "remark": "In-person"
        },
        "vn": {
            "progress": "Xu hướng xe điện toàn cầu: Tesla vs Các hãng lớn",
            "homework": "Lab 1: Sổ tay xu hướng xe điện",
            "summary": "So sánh các hãng xe điện hàng đầu và chuỗi cung ứng; tính tỷ suất sinh lời.",
            "remark": "Trực tiếp"
        },
        "my": {
            "progress": "Trend Kenderaan Elektrik Global: Tesla vs Peneraju Dunia",
            "homework": "Lab 1: Buku nota trend pasaran EV",
            "summary": "Membandingkan peneraju pasaran EV global; pengiraan pulangan harian.",
            "remark": "Semuka"
        },
        "id": {
            "progress": "Tren EV Global: Tesla vs Pemimpin Pasar",
            "homework": "Lab 1: Buku catatan tren pasar EV",
            "summary": "Membandingkan pemain utama EV global; menghitung return harian.",
            "remark": "Tatap muka"
        },
        "th": {
            "progress": "แนวโน้ม EV ระดับโลก: Tesla เทียบกับผู้นำตลาดโลก",
            "homework": "Lab 1: สมุดบันทึกแนวโน้มตลาด EV",
            "summary": "เปรียบเทียบผู้นำ EV ระดับโลกและห่วงโซ่อุปทาน คำนวณผลตอบแทนรายวัน",
            "remark": "ในชั้นเรียน"
        },
        "fr": {
            "progress": "Tendances mondiales du VE : Tesla vs Leaders",
            "homework": "Lab 1 : Cahier des tendances du marché VE",
            "summary": "Comparaison des leaders mondiaux du VE ; calcul des rendements quotidiens.",
            "remark": "En présentiel"
        }
    },
    {
        "week": "Week 4",
        "date": "2026/10/01",
        "tw": {
            "progress": "量化交易策略實戰",
            "homework": "Lab 2: 移動平均線策略報告",
            "summary": "移動平均線概念（20MA 與 60MA）；比較策略交易與買進持有；評估報酬與安全性。",
            "remark": "實體上課"
        },
        "us": {
            "progress": "Quantitative Trading Strategies",
            "homework": "Lab 2: Moving average strategy report",
            "summary": "Moving average concepts (20MA vs 60MA); comparing trading rules vs. Buy & Hold; evaluating returns and safety.",
            "remark": "In-person"
        },
        "vn": {
            "progress": "Chiến lược giao dịch định lượng",
            "homework": "Lab 2: Báo cáo chiến lược trung bình động",
            "summary": "Khái niệm đường trung bình động (MA20 vs MA60); so sánh giao dịch quy tắc với Mua & Giữ.",
            "remark": "Trực tiếp"
        },
        "my": {
            "progress": "Strategi Dagangan Kuantitatif",
            "homework": "Lab 2: Laporan strategi purata bergerak",
            "summary": "Konsep purata bergerak (20MA lwn 60MA); perbandingan peraturan dagangan lwn Buy & Hold.",
            "remark": "Semuka"
        },
        "id": {
            "progress": "Strategi Trading Kuantitatif",
            "homework": "Lab 2: Laporan strategi moving average",
            "summary": "Konsep rata-rata bergerak (20MA vs 60MA); membandingkan aturan trading vs Buy & Hold.",
            "remark": "Tatap muka"
        },
        "th": {
            "progress": "กลยุทธ์การเทรดเชิงปริมาณ",
            "homework": "Lab 2: รายงานกลยุทธ์ค่าเฉลี่ยเคลื่อนที่",
            "summary": "แนวคิดเส้นค่าเฉลี่ย (20MA vs 60MA) เปรียบเทียบกฎการเทรดกับการถือครอง",
            "remark": "ในชั้นเรียน"
        },
        "fr": {
            "progress": "Stratégies de trading quantitatif",
            "homework": "Lab 2 : Rapport sur la stratégie de moyenne mobile",
            "summary": "Concepts de moyenne mobile (20MA vs 60MA) ; comparaison règles vs Buy & Hold.",
            "remark": "En présentiel"
        }
    }
]

# 5. 組裝成 Pandas DataFrame
table_rows = []
for item in syllabus_data:
    lang_content = item.get(current_code, item["tw"])
    table_rows.append({
        "週次 (Week)": item["week"],
        "上課日期 (Date)": item["date"],
        "教學進度 (Progress)": lang_content["progress"],
        "作業進度 (Homework)": lang_content["homework"],
        "內容摘要 (Summary)": lang_content["summary"],
        "備註 (Remarks)": lang_content["remark"]
    })

df = pd.DataFrame(table_rows)

# 6. 以互動表格呈現
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)
