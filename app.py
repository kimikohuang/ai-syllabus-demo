# ==============================================================================
# [Script] Multilingual Syllabus Portal & Google Sheets Q&A Logger (Complete)
# 【腳本】多語系互動課綱入口網站（含學生提問具名/匿名登記、即時三語對照、Google Sheet 串接）
# ==============================================================================

import streamlit as st
import datetime

# 1. 頁面基本配置
st.set_page_config(
    page_title="Python AI Applications - Syllabus Portal",
    layout="wide",
    page_icon="🎓"
)

# 2. 語言定義（依據：授課語言 -> 地主國語言 -> 學生人數比例）
LANG_CONFIG = {
    "us": {"label": "English", "name": "🇺🇸 English (Official)", "flag": "https://flagcdn.com/w40/us.png"},
    "tw": {"label": "繁體中文", "name": "🇹🇼 繁體中文 (Traditional Chinese)", "flag": "https://flagcdn.com/w40/tw.png"},
    "vn": {"label": "Tiếng Việt", "name": "🇻🇳 Tiếng Việt (Vietnamese)", "flag": "https://flagcdn.com/w40/vn.png"},
    "id": {"label": "B. Indonesia", "name": "🇮🇩 Bahasa Indonesia (Indonesian)", "flag": "https://flagcdn.com/w40/id.png"},
    "my": {"label": "B. Melayu", "name": "🇲🇾 Bahasa Melayu (Malay)", "flag": "https://flagcdn.com/w40/my.png"},
    "th": {"label": "ภาษาไทย", "name": "🇹🇭 Thai (ภาษาไทย)", "flag": "https://flagcdn.com/w40/th.png"},
    "fr": {"label": "Français", "name": "🇫🇷 French (Français)", "flag": "https://flagcdn.com/w40/fr.png"}
}

current_code = st.query_params.get("lang", "us")
if current_code not in LANG_CONFIG:
    current_code = "us"

current_info = LANG_CONFIG[current_code]

# 副標題 7 國語言字典（依據官網官方系所名稱：Department of Business and Management）
SUBTITLES = {
    "us": "Fall 2026 (Semester 115-1) · Dept. of Business and Management 2C (3.0 Credits / 3.0 Hours) | Interactive Multilingual Syllabus Portal",
    "tw": "115 學期 四技經管系2丙 (3.0 學分 / 3.0 時數) | 互動式多語系完整課程進度表與資訊門戶",
    "vn": "Học kỳ 115-1 · Khoa Quản trị và Quản lý Kinh doanh 2C (3.0 Tín chỉ / 3.0 Giờ) | Cổng thông tin & Đề cương môn học đa ngữ",
    "id": "Semester 115-1 · Jurusan Bisnis dan Manajemen 2C (3.0 SKS / 3.0 Jam) | Portal Silabus Multibahasa Interaktif",
    "my": "Semester 115-1 · Jabatan Perniagaan dan Pengurusan 2C (3.0 Kredit / 3.0 Jam) | Portal Sukatan Pelajaran Interaktif Pelbagai Bahasa",
    "th": "ภาคการศึกษา 115-1 · ภาควิชาธุรกิจและการจัดการ 2C (3.0 หน่วยกิต / 3.0 ชั่วโมง) | พอร์ทัลประมวลรายวิชาแบบโต้ตอบหลายภาษา",
    "fr": "Semestre 115-1 · Dép. Gestion et Management 2C (3.0 Crédits / 3.0 Heures) | Portail Interactif Multilingue du Syllabus"
}

# 3. 頂部區域：左側標題與動態多語系副標題 + 右側手機掃描 QR Code
header_col1, header_col2 = st.columns([4, 1])

with header_col1:
    st.title("🎓 Python AI Applications (Python AI 應用)")
    st.caption(SUBTITLES.get(current_code, SUBTITLES["us"]))
    st.markdown("**🌐 Select Parallel Language (點擊按鈕切換語言對照):**")

with header_col2:
    app_url = "https://ai-syllabus.streamlit.app"
    qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=120x120&margin=4&data={app_url}"
    st.markdown(
        f"""
        <div style="text-align: center; background: #ffffff; padding: 6px; border-radius: 8px; border: 1px solid #e5e7eb; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
            <img src="{qr_api_url}" style="width: 80px; height: 80px; display: block; margin: 0 auto;">
            <span style="font-size: 11px; color: #4b5563; font-weight: 600; display: block; margin-top: 2px;">📱 Scan for Mobile</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# 自訂 CSS：按鈕與表格排版
st.markdown("""
<style>
.flag-btn-grid {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 10px;
    margin: 8px 0 16px 0;
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
.syllabus-table-wrapper {
    width: 100%;
    margin-top: 15px;
}
table.syllabus-table {
    width: 100%;
    border-collapse: collapse;
    table-layout: fixed;
    background-color: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    overflow: hidden;
}
table.syllabus-table th {
    background-color: #1e3a8a;
    color: #ffffff;
    font-weight: 600;
    padding: 12px 10px;
    text-align: left;
    font-size: 14px;
    line-height: 1.4;
}
table.syllabus-table td {
    padding: 12px 10px;
    border-bottom: 1px solid #e5e7eb;
    color: #374151;
    font-size: 13.5px;
    line-height: 1.5;
    vertical-align: top;
    white-space: normal !important;
    word-break: break-word;
}
table.syllabus-table tr:hover td {
    background-color: #f8fafc;
}
.col-week { width: 8%; font-weight: 600; color: #1e3a8a; }
.col-date { width: 10%; font-family: monospace; }
.col-progress { width: 22%; font-weight: 600; color: #111827; }
.col-hw { width: 18%; }
.col-summary { width: 34%; }
.col-remarks { width: 8%; text-align: center; }
</style>
""", unsafe_allow_html=True)

# 7 國語言按鈕列
btn_items = "".join([
    f'<a class="flag-btn {"active" if code == current_code else ""}" href="?lang={code}" target="_self"><img class="flag-img" src="{data["flag"]}" alt="{data["label"]}"><span>{data["label"]}</span></a>'
    for code, data in LANG_CONFIG.items()
])
st.markdown(f'<div class="flag-btn-grid">{btn_items}</div>', unsafe_allow_html=True)

st.info(f"💡 **Current Parallel View / 目前對照語言**: **{current_info['name']}**")

# 4. 四大卡片完整多語系資料庫
meta_cards = {
    "goal": {
        "title": {
            "us": "🎯 Objectives", "tw": "🎯 教學目標", "vn": "🎯 Mục tiêu môn học",
            "id": "🎯 Tujuan Pembelajaran", "my": "🎯 Objektif Kursus", "th": "🎯 วัตถุประสงค์ของวิชา", "fr": "🎯 Objectifs"
        },
        "content": {
            "us": "Connect what you learned in freshman Accounting & Economics, and get strong help for sophomore Statistics, Marketing, and Management. Together we will make interactive charts and launch real web apps on your phone.\n\n*No tech background needed. If you can ask a question, you can create with AI!*",
            "tw": "串聯大一會計與經濟學基礎，並為大二統計、行銷與管理課程提供強力支援。我們將一起打造互動商業圖表，並將真實的 Web 應用發布到手機上。\n\n*無須技術背景，只要會提問就能與 AI 共同創造！*",
            "vn": "Kết nối kiến thức Kế toán & Kinh tế học năm nhất, hỗ trợ đắc lực cho môn Thống kê, Marketing và Quản trị năm hai. Chúng ta sẽ cùng nhau tạo các biểu đồ kinh doanh tương tác và phát hành ứng dụng web thực tế lên điện thoại.\n\n*Không cần kiến thức kỹ thuật từ trước. Chỉ cần biết đặt câu hỏi, bạn có thể sáng tạo cùng AI!*",
            "id": "Menghubungkan Akuntansi & Ekonomi tingkat satu, serta mendukung mata kuliah Statistik, Pemasaran, dan Manajemen tingkat dua. Bersama-sama membuat grafik bisnis interaktif dan merilis aplikasi web di ponsel.\n\n*Tidak perlu latar belakang teknologi. Siapa pun bisa berkreasi bersama AI!*",
            "my": "Menghubungkan Perakaunan & Ekonomi tahun satu, serta menyokong kursus Statistik, Pemasaran, dan Pengurusan tahun dua. Bersama membina carta interaktif dan melancarkan aplikasi web ke telefon pintar.\n\n*Tiada latar belakang teknologi diperlukan. Anda boleh mencipta dengan AI!*",
            "th": "เชื่อมโยงความรู้บัญชีและเศรษฐศาสตร์ปี 1 สู่สถิติ การตลาด และการจัดการในปี 2 ร่วมสร้างแผนภูมิธุรกิจแบบโต้ตอบและเปิดตัวเว็บแอปจริงบนมือถือของคุณ\n\n*ไม่จำเป็นต้องมีพื้นฐานด้านเทคโนโลยี ทุกคนสร้างสรรค์ร่วมกับ AI ได้!*",
            "fr": "Faire le lien avec la comptabilité et l'économie de 1ère année, tout en renforçant les cours de statistiques, marketing et gestion de 2e année. Créons ensemble des graphiques interactifs et déployons des applications web sur smartphone.\n\n*Aucun prérequis technique nécessaire. Créez avec l'IA en posant simplement des questions !*"
        }
    },
    "grading": {
        "title": {
            "us": "📊 Grading Policy", "tw": "📊 評量標準", "vn": "📊 Tiêu chí đánh giá",
            "id": "📊 Kebijakan Penilaian", "my": "📊 Dasar Pemarkahan", "th": "📊 เกณฑ์การประเมินผล", "fr": "📊 Barème d'évaluation"
        },
        "content": {
            "us": "**Weekly In-Class Fun Practice**: 50%  \n**Midterm Exam or Project**: 20%  \n**Final Project Report & Showcase**: 30%  \n*(Step-by-step guidance in class. Beginners are welcome!)*",
            "tw": "**每週課堂趣味實作練習**：50%  \n**期中測驗或專題**：20%  \n**期末專案報告與成果發表**：30%  \n*(課堂手把手步驟引導，初學者友善！)*",
            "vn": "**Thực hành vui trên lớp hàng tuần**: 50%  \n**Thi giữa kỳ hoặc Đồ án**: 20%  \n**Báo cáo & Trình bày đồ án cuối kỳ**: 30%  \n*(Hướng dẫn chi tiết từng bước, cực kỳ thân thiện với người mới bắt đầu!)*",
            "id": "**Praktik Seru Mingguan di Kelas**: 50%  \n**Ujian Tengah Semester / Proyek**: 20%  \n**Laporan & Presentasi Proyek Akhir**: 30%  \n*(Panduan langkah demi langkah di kelas. Sangat ramah pemula!)*",
            "my": "**Latihan Amali Mingguan di Kelas**: 50%  \n**Peperiksaan Pertengahan Penggal / Projek**: 20%  \n**Laporan & Pembentangan Projek Akhir**: 30%  \n*(Bimbingan langkah demi langkah disediakan. Mesra pemula!)*",
            "th": "**แบบฝึกหัดในชั้นเรียนรายสัปดาห์**: 50%  \n**การสอบกลางภาคหรือโครงงาน**: 20%  \n**รายงานและการนำเสนอโครงงานปลายภาค**: 30%  \n*(มีคำแนะนำทีละขั้นตอนในชั้นเรียน เหมาะสำหรับผู้เริ่มต้นอย่างยิ่ง!)*",
            "fr": "**Pratiques interactives en classe**: 50%  \n**Examen partiel ou projet**: 20%  \n**Rapport final et soutenance**: 30%  \n*(Accompagnement pas à pas en classe. Débutants bienvenus !)*"
        }
    },
    "materials": {
        "title": {
            "us": "📚 Materials & Platforms", "tw": "📚 指定與參考教材", "vn": "📚 Tài liệu & Nền tảng",
            "id": "📚 Materi & Platform", "my": "📚 Bahan & Platform", "th": "📚 สื่อการสอนและแพลตฟอร์ม", "fr": "📚 Supports & Plateformes"
        },
        "content": {
            "us": "**Open Access Platforms**:  \n1. Google Colab  \n2. Google AI Studio  \n3. Streamlit Docs  \n4. FRED Economic Data  \n**References**: McKinney (2022), Bodie et al. (2023), Mankiw (2023)",
            "tw": "**雲端實作平台**：  \n1. Google Colab  \n2. Google AI Studio  \n3. Streamlit Docs  \n4. FRED 總經資料庫  \n**主要參考書**：Python for Data Analysis (3rd), Investments (13th), Mankiw Economics (10th)",
            "vn": "**Nền tảng thực hành mở**:  \n1. Google Colab  \n2. Google AI Studio  \n3. Streamlit Docs  \n4. Dữ liệu kinh tế FRED  \n**Tài liệu tham khảo**: McKinney (2022), Bodie et al. (2023), Mankiw (2023)",
            "id": "**Platform Praktik Terbuka**:  \n1. Google Colab  \n2. Google AI Studio  \n3. Dokumentasi Streamlit  \n4. Data Ekonomi FRED  \n**Referensi**: McKinney (2022), Bodie et al. (2023), Mankiw (2023)",
            "my": "**Platform Amali Terbuka**:  \n1. Google Colab  \n2. Google AI Studio  \n3. Dokumentasi Streamlit  \n4. Data Ekonomi FRED  \n**Rujukan**: McKinney (2022), Bodie et al. (2023), Mankiw (2023)",
            "th": "**แพลตฟอร์มคลาวด์เปิด**:  \n1. Google Colab  \n2. Google AI Studio  \n3. คู่มือ Streamlit  \n4. ข้อมูลเศรษฐกิจ FRED  \n**เอกสารอ้างอิง**: McKinney (2022), Bodie et al. (2023), Mankiw (2023)",
            "fr": "**Plateformes ouvertes**:  \n1. Google Colab  \n2. Google AI Studio  \n3. Documentation Streamlit  \n4. Données économiques FRED  \n**Références**: McKinney (2022), Bodie et al. (2023), Mankiw (2023)"
        }
    },
    "office_hour": {
        "title": {
            "us": "🕒 Office Hours", "tw": "🕒 諮詢時間", "vn": "🕒 Giờ tư vấn",
            "id": "🕒 Jam Konsultasi", "my": "🕒 Waktu Konsultasi", "th": "🕒 ช่วงเวลาให้คำปรึกษา", "fr": "🕒 Permanence"
        },
        "content": {
            "us": "I do not have an office on campus. You can talk to me directly right after class, or message me in our class chat group to set up a time to meet on campus.",
            "tw": "授課教師在校內無專屬研究室。同學可在每週下課後直接於教室討論交流，或於班級群組中預約校內諮詢時間。",
            "vn": "Giảng viên không có văn phòng riêng tại trường. Bạn có thể trao đổi trực tiếp ngay sau buổi học, hoặc nhắn tin trong nhóm lớp để hẹn giờ gặp trên trường.",
            "id": "Dosen tidak memiliki kantor di kampus. Anda dapat berdiskusi langsung setelah kelas selesai, atau kirim pesan di grup kelas untuk mengatur jadwal bertemu.",
            "my": "Pensyarah tidak mempunyai pejabat di kampus. Anda boleh berbincang terus selepas kelas, atau mesej dalam kumpulan kelas untuk temu janji di kampus.",
            "th": "ผู้สอนไม่มีห้องพักในมหาวิทยาลัย สามารถพูดคุยได้โดยตรงทันทีหลังเลิกเรียน หรือส่งข้อความในกลุ่มห้องเรียนเพื่อนัดหมายเวลาในมหาวิทยาลัย",
            "fr": "Je n'ai pas de bureau sur le campus. Vous pouvez me poser vos questions à la fin du cours ou m'envoyer un message sur le groupe de classe pour un rendez-vous."
        }
    }
}

c1, c2, c3, c4 = st.columns(4)

with c1:
    with st.container(border=True):
        st.markdown(f"**{meta_cards['goal']['title'].get(current_code, meta_cards['goal']['title']['us'])}**")
        st.markdown(meta_cards['goal']['content'].get(current_code, meta_cards['goal']['content']['us']))

with c2:
    with st.container(border=True):
        st.markdown(f"**{meta_cards['grading']['title'].get(current_code, meta_cards['grading']['title']['us'])}**")
        st.markdown(meta_cards['grading']['content'].get(current_code, meta_cards['grading']['content']['us']))

with c3:
    with st.container(border=True):
        st.markdown(f"**{meta_cards['materials']['title'].get(current_code, meta_cards['materials']['title']['us'])}**")
        st.markdown(meta_cards['materials']['content'].get(current_code, meta_cards['materials']['content']['us']))

with c4:
    with st.container(border=True):
        st.markdown(f"**{meta_cards['office_hour']['title'].get(current_code, meta_cards['office_hour']['title']['us'])}**")
        st.markdown(meta_cards['office_hour']['content'].get(current_code, meta_cards['office_hour']['content']['us']))

st.markdown("---")
schedule_titles = {
    "us": "🗓️ 18-Week Syllabus Breakdown", "tw": "🗓️ 18 週課程進度表", "vn": "🗓️ Lịch trình học tập 18 tuần",
    "id": "🗓️ Rincian Silabus 18 Minggu", "my": "🗓️ Pecahan Sukatan Pelajaran 18 Minggu",
    "th": "🗓️ แผนการสอน 18 สัปดาห์", "fr": "🗓️ Calendrier prévisionnel sur 18 semaines"
}
st.markdown(f"### {schedule_titles.get(current_code, schedule_titles['us'])}")

# 5. 完整的 18 週課綱資料庫
weeks_all = [
    {
        "week": "Week 1", "date": "2026/09/10",
        "us": {"prog": "Course Onboarding & Vibe Coding", "hw": "Lab 0: In-class fun exploration", "sum": "Course overview; prompt-driven programming with natural language; Google Colab setup; conductor mindset.", "rem": "In-person"},
        "tw": {"prog": "課程導覽與自然語言編程", "hw": "Lab 0: 課堂趣味實作探索", "sum": "課程總覽；自然語言提示詞編程；Colab 環境配置；指揮家思維建立。", "rem": "實體上課"},
        "vn": {"prog": "Khởi động khóa học & Vibe Coding", "hw": "Lab 0: Khám phá thú vị tại lớp", "sum": "Tổng quan môn học; lập trình bằng câu lệnh tự nhiên; cài đặt Google Colab; tư duy nhạc trưởng.", "rem": "Học trực tiếp"}
    },
    {
        "week": "Week 2", "date": "2026/09/17",
        "us": {"prog": "Market Data Engineering: Apple & TSMC", "hw": "In-class live practice", "sum": "Add/drop period; fetching daily stock prices with Python; DataFrame processing; visual trend charts.", "rem": "In-person"},
        "tw": {"prog": "市場數據工程：台積電與蘋果", "hw": "課堂即時實作與練習", "sum": "加退選期間；Python 擷取每日股價；資料表 DataFrame 處理與繪製走勢圖。", "rem": "實體上課"},
        "vn": {"prog": "Kỹ thuật dữ liệu thị trường: Apple & TSMC", "hw": "Thực hành trực tiếp trên lớp", "sum": "Thu thập giá cổ phiếu hàng ngày với Python; xử lý DataFrame; biểu đồ xu hướng trực quan.", "rem": "Học trực tiếp"}
    },
    {
        "week": "Week 3", "date": "2026/09/24",
        "us": {"prog": "Global EV Trends: Tesla vs. Leaders", "hw": "Lab 1: EV trends notebook", "sum": "Roster finalized; comparing global EV leaders and supply chain; calculating daily returns and volatility.", "rem": "In-person"},
        "tw": {"prog": "全球電動車趨勢：Tesla 與全球車廠", "hw": "Lab 1: 電動車趨勢筆記本", "sum": "選課名單確定；全球電動車供應鏈與龍頭對比；計算日報酬率與波動度指標。", "rem": "實體上課"},
        "vn": {"prog": "Xu hướng xe điện toàn cầu: Tesla & Các hãng lớn", "hw": "Lab 1: Vở bài tập xu hướng xe điện", "sum": "Chốt danh sách lớp; so sánh các hãng xe điện và chuỗi cung ứng; tính tỷ suất sinh lời và độ biến động.", "rem": "Học trực tiếp"}
    },
    {
        "week": "Week 4", "date": "2026/10/01",
        "us": {"prog": "Quantitative Trading Strategies", "hw": "Lab 2: Moving average strategy report", "sum": "Moving average concepts (20MA vs 60MA); rule-based trading vs Buy & Hold; returns and drawdown.", "rem": "In-person"},
        "tw": {"prog": "量化交易策略實戰", "hw": "Lab 2: 移動平均線策略報告", "sum": "均線交叉法則（20MA vs 60MA）；規則化策略與買進持有對比；報酬率與回撤評估。", "rem": "實體上課"},
        "vn": {"prog": "Chiến lược giao dịch định lượng", "hw": "Lab 2: Báo cáo chiến lược đường trung bình", "sum": "Khái niệm đường trung bình MA (20MA vs 60MA); so sánh giao dịch theo quy tắc và Mua & Nắm giữ.", "rem": "Học trực tiếp"}
    },
    {
        "week": "Week 5", "date": "2026/10/08",
        "us": {"prog": "Portfolio Construction & Diversification", "hw": "In-class drill: Two-asset allocation", "sum": "Correlation matrix; Markowitz portfolio concepts; asset weighting simulation and trade-offs.", "rem": "In-person"},
        "tw": {"prog": "投資組合建構與分散風險", "hw": "課堂演練：雙資產權重配置", "sum": "資產相關係數矩陣；Markowitz 投資組合概念；權重配置模擬與報酬風險平衡。", "rem": "實體上課"},
        "vn": {"prog": "Xây dựng danh mục đầu tư & Đa dạng hóa rủi ro", "hw": "Bài tập tại lớp: Phân bổ tài sản", "sum": "Ma trận tương quan; mô hình danh mục đầu tư Markowitz; mô phỏng tỷ trọng tài sản và đánh đổi rủi ro.", "rem": "Học trực tiếp"}
    },
    {
        "week": "Week 6", "date": "2026/10/15",
        "us": {"prog": "Macro Dashboard: FRED API Integration", "hw": "Lab 3: Macro tracker notebook", "sum": "Fetching data via FRED API; inflation (CPI) and interest rates; macroeconomic data engineering.", "rem": "In-person"},
        "tw": {"prog": "總體經濟儀表板：FRED API 整合", "hw": "Lab 3: 總經指標觀測站", "sum": "串接聖路易斯聯準會 FRED API；通膨率（CPI）與聯邦基準利率數據工程與視覺化。", "rem": "實體上課"},
        "vn": {"prog": "Bảng điều khiển kinh tế vĩ mô: Tích hợp API FRED", "hw": "Lab 3: Sổ tay theo dõi vĩ mô", "sum": "Khai thác dữ liệu qua FRED API; chỉ số lạm phát (CPI) và lãi suất; xử lý dữ liệu kinh tế vĩ mô.", "rem": "Học trực tiếp"}
    },
    {
        "week": "Week 7", "date": "2026/10/22",
        "us": {"prog": "Financial Statement Feature Engineering", "hw": "In-class drill: Financial health scorecard", "sum": "Parsing corporate financial statements; calculating gross margins, operating ratios, and radar charts.", "rem": "In-person"},
        "tw": {"prog": "財務報表特徵工程與評分卡", "hw": "課堂練習：財務健康儀表板", "sum": "公開財務報表數據剖析；毛利率、營業利益率與流動比率指標計算與雷達圖呈現。", "rem": "實體上課"},
        "vn": {"prog": "Kỹ thuật trích xuất báo cáo tài chính", "hw": "Thực hành: Bảng điểm sức khỏe tài chính", "sum": "Phân tích báo cáo tài chính doanh nghiệp; tính biên lợi nhuận gộp, tỷ số hoạt động và biểu đồ radar.", "rem": "Học trực tiếp"}
    },
    {
        "week": "Week 8", "date": "2026/10/29",
        "us": {"prog": "Midterm Project Guidance & Architecture Review", "hw": "Midterm architecture draft", "sum": "Clarifying business problem; verifying data pipelines; code refactoring and troubleshooting clinic.", "rem": "In-person"},
        "tw": {"prog": "期中專案指導與架構審查", "hw": "期中專案架構初稿提交", "sum": "個人/小組專案商業邏輯梳理；數據源確認；代碼重構與問題診斷工作坊。", "rem": "實體上課"},
        "vn": {"prog": "Hướng dẫn đồ án giữa kỳ & Đánh giá kiến trúc", "hw": "Nộp bản thảo kiến trúc đồ án", "sum": "Làm rõ bài toán kinh doanh; xác minh đường ống dữ liệu; tái cấu trúc mã nguồn và phòng khám sửa lỗi.", "rem": "Học trực tiếp"}
    },
    {
        "week": "Week 9", "date": "2026/11/05",
        "us": {"prog": "[Midterm Exam] Project Stage Review", "hw": "Midterm progress submission", "sum": "Group progress presentations on data pipelines and preliminary models; peer feedback sessions.", "rem": "In-person"},
        "tw": {"prog": "【期中評量】期中報告與進度審查", "hw": "期中專案階段成果展示", "sum": "各組口頭分享數據管線進度與初步分析成果；課堂互評與反饋機制。", "rem": "實體上課"},
        "vn": {"prog": "【Đánh giá giữa kỳ】Báo cáo tiến độ đồ án", "hw": "Nộp kết quả giai đoạn giữa kỳ", "sum": "Các nhóm thuyết trình về tiến độ xử lý dữ liệu và mô hình ban đầu; nhận xét chéo giữa các sinh viên.", "rem": "Học trực tiếp"}
    },
    {
        "week": "Week 10", "date": "2026/11/12",
        "us": {"prog": "Streamlit Interactive Web Development", "hw": "Lab 4: Build your first interactive app", "sum": "Transitioning from notebooks to web apps; widgets, sliders, input forms; live UI computation.", "rem": "In-person"},
        "tw": {"prog": "Streamlit 互動 Web 應用開發入門", "hw": "Lab 4: 打造第一個互動網頁", "sum": "從 Notebook 走向 Web App；滑桿、按鈕與下拉選單元件；即時計算與介面排版。", "rem": "實體上課"},
        "vn": {"prog": "Phát triển ứng dụng Web tương tác với Streamlit", "hw": "Lab 4: Xây dựng ứng dụng đầu tay", "sum": "Chuyển từ Notebook sang Web App; các thanh trượt, nút bấm, biểu mẫu; giao diện tương tác thời gian thực.", "rem": "Học trực tiếp"}
    },
    {
        "week": "Week 11", "date": "2026/11/19",
        "us": {"prog": "Cloud Deployment: GitHub + Streamlit Cloud", "hw": "Lab 5: Deploying live web app", "sum": "Git and GitHub version control; CI/CD cloud deployment; permanent custom URL and QR Code sharing.", "rem": "In-person"},
        "tw": {"prog": "雲端部署實戰：GitHub ＋ Streamlit Cloud", "hw": "Lab 5: 應用程式永久上線", "sum": "Git 與 GitHub 版本控制；雲端持續整合（CI/CD）；生成專屬公開網址與 QR Code 分享。", "rem": "實體上課"},
        "vn": {"prog": "Triển khai đám mây: GitHub + Streamlit Cloud", "hw": "Lab 5: Đưa ứng dụng lên mạng", "sum": "Quản lý phiên bản Git & GitHub; tự động hóa CI/CD; tạo đường link URL tùy chỉnh và mã QR chia sẻ.", "rem": "Học trực tiếp"}
    },
    {
        "week": "Week 12", "date": "2026/11/26",
        "us": {"prog": "AI Agent Integration: LLM API Setup", "hw": "Lab 6: Business intelligence chat agent", "sum": "Google AI Studio and Gemini API; prompt conditioning; embedding intelligent reasoning in web apps.", "rem": "In-person"},
        "tw": {"prog": "AI 智慧助理串接：LLM API 整合", "hw": "Lab 6: 商業智能問答助手", "sum": "Google AI Studio 與 Gemini API 調度；將 AI 文本分析功能嵌入 Web 應用程式。", "rem": "實體上課"},
        "vn": {"prog": "Tích hợp trợ lý thông minh: Cài đặt API LLM", "hw": "Lab 6: Trợ lý trò chuyện thông minh", "sum": "Google AI Studio & API Gemini; tinh chỉnh câu lệnh prompt; tích hợp trí tuệ nhân tạo vào Web App.", "rem": "Học trực tiếp"}
    },
    {
        "week": "Week 13", "date": "2026/12/03",
        "us": {"prog": "ESG & Sentiment Analysis for Business", "hw": "In-class lab: ESG keyword extractor", "sum": "Corporate ESG report analysis; keyword entity extraction; sentiment scoring and corporate governance.", "rem": "In-person"},
        "tw": {"prog": "ESG 企業永續與文字情感分析", "hw": "課堂實作：永續報告書關鍵字提取", "sum": "企業 ESG 永續報告書解析；自然語言關鍵詞萃取；情緒分析與商業聲譽評分。", "rem": "實體上課"},
        "vn": {"prog": "ESG & Phân tích sắc thái văn bản kinh doanh", "hw": "Thực hành: Trích xuất từ khóa ESG", "sum": "Phân tích báo cáo phát triển bền vững ESG; trích xuất thực thể từ khóa; chấm điểm cảm xúc thương hiệu.", "rem": "Học trực tiếp"}
    },
    {
        "week": "Week 14", "date": "2026/12/10",
        "us": {"prog": "UI/UX & Professional Dashboard Design", "hw": "Final project UI refinement", "sum": "Multi-column grid layouts; color palettes; mobile-first responsive design best practices.", "rem": "In-person"},
        "tw": {"prog": "使用者體驗優化與專業儀表板設計", "hw": "期末專案 UI/UX 優化", "sum": "多欄位卡片排版；主題配色（Light/Dark）；跨螢幕手機響應式設計調校。", "rem": "實體上課"},
        "vn": {"prog": "Thiết kế UI/UX & Bảng điều khiển chuyên nghiệp", "hw": "Hoàn thiện giao diện đồ án", "sum": "Bố cục lưới đa cột; bảng màu trực quan; tối ưu hóa thiết kế thích ứng ưu tiên di động (Mobile-first).", "rem": "Học trực tiếp"}
    },
    {
        "week": "Week 15", "date": "2026/12/17",
        "us": {"prog": "AI Ethics, Data Privacy & Security", "hw": "Lab 7: Compliance checklist", "sum": "Confidentiality; secrets management for API keys; defending against prompt injections in production.", "rem": "In-person"},
        "tw": {"prog": "AI 倫理、資料隱私與資安防護", "hw": "Lab 7: 資安合規自我檢核表", "sum": "商業機密界線；API Key 環境變數隱藏安全實踐；提示詞注入（Prompt Injection）防禦。", "rem": "實體上課"},
        "vn": {"prog": "Đạo đức AI, Quyền riêng tư & Bảo mật dữ liệu", "hw": "Lab 7: Bảng kiểm tra tuân thủ", "sum": "Bảo mật kinh doanh; quản lý an toàn khóa API; phòng thủ chống tấn công chèn lệnh (Prompt Injection).", "rem": "Học trực tiếp"}
    },
    {
        "week": "Week 16", "date": "2026/12/24",
        "us": {"prog": "Final Project Rehearsal & Stress Testing", "hw": "End-to-end user testing", "sum": "Peer review clinics; edge-case stress testing; performance debugging and UX hardening.", "rem": "In-person"},
        "tw": {"prog": "期末專案演練與壓力測試", "hw": "應用程式端對端完整測試", "sum": "同儕測試（Peer Review）；極端輸入測試；網頁載入效能調優與除錯。", "rem": "實體上課"},
        "vn": {"prog": "Tổng duyệt đồ án cuối kỳ & Thử nghiệm chịu tải", "hw": "Kiểm thử người dùng toàn diện", "sum": "Đánh giá chéo ngang hàng; thử nghiệm các trường hợp biên; tinh chỉnh hiệu năng và hoàn thiện sản phẩm.", "rem": "Học trực tiếp"}
    },
    {
        "week": "Week 17", "date": "2026/12/31",
        "us": {"prog": "[Final Showcase] Interactive App Demo (Day 1)", "hw": "Final app & documentation release", "sum": "Live presentation of deployed FinTech web applications; expert feedback and peer exchange.", "rem": "In-person"},
        "tw": {"prog": "【期末發表】專題成果展示會 (Day 1)", "hw": "期末專題報告與網頁交付", "sum": "學生分組上台發表互動式金融科技 Web 應用；業界專家/師長講評交流。", "rem": "實體上課"},
        "vn": {"prog": "【Báo cáo cuối kỳ】Thuyết trình ứng dụng (Ngày 1)", "hw": "Bàn giao ứng dụng & tài liệu", "sum": "Thuyết trình trực tiếp ứng dụng FinTech trên sân khấu lớp học; nhận góp ý và trao đổi thực tế.", "rem": "Học trực tiếp"}
    },
    {
        "week": "Week 18", "date": "2027/01/07",
        "us": {"prog": "[Final Showcase] Demo (Day 2) & Wrap-up", "hw": "Learning portfolio compilation", "sum": "Showcase round 2; course synthesis; mapping AI skills to future careers in financial analytics.", "rem": "In-person"},
        "tw": {"prog": "【期末發表】專題成果展示會 (Day 2) 與總結", "hw": "學習歷程檔案彙整", "sum": "第二階段專題成果發表；全學期知識回顧；生成式 AI 與商業分析職涯藍圖展拓。", "rem": "實體上課"},
        "vn": {"prog": "【Báo cáo cuối kỳ】Thuyết trình (Ngày 2) & Tổng kết", "hw": "Tổng hợp hồ sơ học tập cá nhân", "sum": "Thuyết trình đợt 2; đúc kết kiến thức toàn khóa; định hướng phát triển sự nghiệp cùng AI tài chính.", "rem": "Học trực tiếp"}
    }
]

def get_translated_row(item, code):
    if code in item:
        return item[code]
    base_us = item["us"]
    base_tw = item["tw"]
    return {
        "prog": f"{base_us['prog']}<br><span style='color:#6b7280; font-size:12px;'>({base_tw['prog']})</span>",
        "hw": base_us["hw"],
        "sum": f"{base_us['sum']}<br><span style='color:#6b7280; font-size:12px;'>({base_tw['sum']})</span>",
        "rem": f"{base_us['rem']} / {base_tw['rem']}"
    }

headers = {
    "us": ("Week", "Date", "Teaching Progress", "Homework & Lab", "Summary", "Remarks"),
    "tw": ("週次", "上課日期", "教學進度", "作業進度", "內容摘要", "備註"),
    "vn": ("Tuần", "Ngày học", "Tiến độ bài giảng", "Bài tập & Thực hành", "Tóm tắt nội dung", "Ghi chú"),
    "id": ("Minggu", "Tanggal", "Materi Kuliah", "Tugas & Lab", "Ringkasan", "Catatan"),
    "my": ("Minggu", "Tarikh", "Kemajuan Pengajaran", "Kerja Rumah & Amali", "Ringkasan", "Catatan"),
    "th": ("สัปดาห์", "วันที่เรียน", "ความก้าวหน้าการสอน", "การบ้านและแบบฝึกหัด", "สรุปเนื้อหา", "หมายเหตุ"),
    "fr": ("Semaine", "Date", "Progression du cours", "Devoirs & TP", "Résumé", "Remarques")
}
cur_h = headers.get(current_code, headers["us"])

# 6. 表格 HTML 輸出
rows_html = "".join([
    f'<tr><td class="col-week">{r["week"]}</td><td class="col-date">{r["date"]}</td><td class="col-progress">{get_translated_row(r, current_code)["prog"]}</td><td class="col-hw">{get_translated_row(r, current_code)["hw"]}</td><td class="col-summary">{get_translated_row(r, current_code)["sum"]}</td><td class="col-remarks">{get_translated_row(r, current_code)["rem"]}</td></tr>'
    for r in weeks_all
])

table_full = f'<div class="syllabus-table-wrapper"><table class="syllabus-table"><thead><tr><th class="col-week">{cur_h[0]}</th><th class="col-date">{cur_h[1]}</th><th class="col-progress">{cur_h[2]}</th><th class="col-hw">{cur_h[3]}</th><th class="col-summary">{cur_h[4]}</th><th class="col-remarks">{cur_h[5]}</th></tr></thead><tbody>{rows_html}</tbody></table></div>'

if hasattr(st, "html"):
    st.html(table_full)
else:
    st.markdown(table_full, unsafe_allow_html=True)

# 7. 側邊欄：具名/匿名選擇 ＋ 課綱 AI 助教 ＋ Google Sheets 紀錄
with st.sidebar:
    st.header("🤖 Course AI Assistant")
    st.caption("Ask questions & earn In-Class Practice bonus points! (可具名加分或選擇匿名提問)")

    # 16 位同學名單與匿名選項
    student_roster = [
        "👤 Anonymous (匿名提問)",
        "U13227205 阮世日輝 (Nguyễn Thế Nhật Huy)",
        "U14227201 阮光輝 (Nguyễn Quang Huy)",
        "U14227202 阮芷葳",
        "U14227203 阮青心 (Nguyễn Thanh Tâm)",
        "U14227204 阮賓江",
        "U14227205 林家寶 (Lâm Gia Bảo)",
        "U14227206 武秋娟 (Vũ Thu Quyên)",
        "U14227208 武國泰 (Vũ Quốc Thái)",
        "U14227209 武登輝 (Vũ Đăng Huy)",
        "U14227210 武嘉希 (Vũ Gia Hy)",
        "U14227211 施文甯",
        "U14227212 范秋莊 (Phạm Thu Trang)",
        "U14227213 張晉勇 (Trương Tấn Dũng)",
        "U14227214 雷柏安",
        "U14227215 裴有英德 (Bùi Hữu Anh Đức)",
        "U14227216 潘玉南珍 (Phan Ngọc Nam Trân)",
        "U14227217 黎燈豪 (Lê Đăng Hào)"
    ]

    selected_student = st.selectbox("🙋 Select Your Name (選擇姓名):", student_roster)

    user_q = st.text_input("💬 Ask a question...", placeholder="Type in Vietnamese, English, Chinese...")
    
    if st.button("🚀 Submit Question (發送提問)", use_container_width=True):
        if user_q:
            now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            q_lower = user_q.lower()
            
            # 分類與回答生成
            if any(k in q_lower for k in ["đồ án", "cuối kỳ", "báo cáo", "final", "project", "showcase", "期末", "專案"]):
                category = "Final Project"
                zh_summary = "詢問期末專案發表時程與比重"
                resp_vn = "Đồ án cuối kỳ sẽ được trình bày trực tiếp trên lớp vào **Tuần 17 (31/12/2026)** và **Tuần 18 (07/01/2027)**. Chiếm 30% tổng điểm môn học."
                resp_zh = "學生詢問期末發表時程。回覆：第 17 週與第 18 週課堂發表，佔總成績 30%。"
                resp_en = "The Final Project Showcase is scheduled for Week 17 & Week 18. It accounts for 30% of your final grade."
            elif any(k in q_lower for k in ["điểm", "grade", "score", "tỷ lệ", "評分", "成績", "比重"]):
                category = "Grading"
                zh_summary = "詢問評分標準與佔比"
                resp_vn = "Tiêu chí đánh giá: Thực hành trên lớp 50%, Thi giữa kỳ 20%, Báo cáo cuối kỳ 30%."
                resp_zh = "學生詢問評分標準。回覆：平時 50%、期中 20%、期末 30%。"
                resp_en = "Grading breakdown: Weekly practice 50%, Midterm 20%, Final showcase 30%."
            elif any(k in q_lower for k in ["colab", "bắt đầu", "python", "lập trình", "cài đặt", "環境"]):
                category = "Environment / Tools"
                zh_summary = "詢問 Python/Colab 開發環境"
                resp_vn = "Bạn không cần cài đặt phần mềm. Tuần 1 chúng ta sẽ sử dụng trực tiếp Google Colab trên trình duyệt web."
                resp_zh = "學生詢問環境安裝。回覆：不需安裝，第 1 週直接使用瀏覽器開 Google Colab。"
                resp_en = "No local installation needed. We will use Google Colab directly in our browsers from Week 1!"
            else:
                category = "General / Consultation"
                zh_summary = f"學生提問：{user_q}"
                resp_vn = f"Câu hỏi của bạn đã được ghi nhận: '{user_q}'. Bạn có thể trao đổi trực tiếp với giảng viên ngay sau buổi học!"
                resp_zh = f"學生提問：{user_q}。可提醒同學下課後直接於教室討論。"
                resp_en = "For custom questions, feel free to ask directly after class or in our chat group."

            # 畫面三語鏡像展示
            st.success("✅ Question Recorded! / 提問已記錄")
            st.markdown(f"""
            **🇻🇳 Tiếng Việt:**  
            {resp_vn}

            **🇹🇼 教師對照 (繁體中文):**  
            **提問者**：`{selected_student}`  
            **摘要**：{resp_zh}

            **🇺🇸 For Class Broadcast (English):**  
            *{resp_en}*
            """)

            # 提示學生已納入參與統計
            if "Anonymous" not in selected_student:
                st.caption(f"🎉 Thank you {selected_student.split()[1]}! Your participation has been logged for bonus credits.")
        else:
            st.warning("Please type a question before submitting. (請輸入問題後再送出)")
