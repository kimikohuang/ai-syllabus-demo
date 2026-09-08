# ==============================================================================
# [Script] Interactive Multilingual Syllabus Portal & Full AI Assistant
# ==============================================================================

import streamlit as st
import datetime

# 1. 頁面基本配置
st.set_page_config(
    page_title="Python AI Applications - Syllabus Portal",
    layout="wide",
    page_icon="🎓"
)

# 2. 語言定義（授課語言 -> 地主國語言 -> 學生人數比例）
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

SUBTITLES = {
    "us": "Fall 2026 (Semester 115-1) · Dept. of Business and Management 2C (3.0 Credits / 3.0 Hours) | Interactive Multilingual Syllabus Portal",
    "tw": "115 學期 四技經管系2丙 (3.0 學分 / 3.0 時數) | 互動式多語系完整課程進度表與資訊門戶",
    "vn": "Học kỳ 115-1 · Khoa Quản trị và Quản lý Kinh doanh 2C (3.0 Tín chỉ / 3.0 Giờ) | Cổng thông tin & Đề cương môn học đa ngữ",
    "id": "Semester 115-1 · Jurusan Bisnis dan Manajemen 2C (3.0 SKS / 3.0 Jam) | Portal Silabus Multibahasa Interaktif",
    "my": "Semester 115-1 · Jabatan Perniagaan dan Pengurusan 2C (3.0 Kredit / 3.0 Jam) | Portal Sukatan Pelajaran Interaktif Pelbagai Bahasa",
    "th": "ภาคการศึกษา 115-1 · ภาควิชาธุรกิจและการจัดการ 2C (3.0 หน่วยกิต / 3.0 ชั่วโมง) | พอร์ทัลประมวลรายวิชาแบบโต้ตอบหลายภาษา",
    "fr": "Semestre 115-1 · Dép. Gestion et Management 2C (3.0 Crédits / 3.0 Heures) | Portail Interactif Multilingue du Syllabus"
}

# 3. 頂部區域：標題、副標題與手機掃描 QR Code
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

# 5. 18 週課綱資料庫
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

rows_html = "".join([
    f'<tr><td class="col-week">{r["week"]}</td><td class="col-date">{r["date"]}</td><td class="col-progress">{get_translated_row(r, current_code)["prog"]}</td><td class="col-hw">{get_translated_row(r, current_code)["hw"]}</td><td class="col-summary">{get_translated_row(r, current_code)["sum"]}</td><td class="col-remarks">{get_translated_row(r, current_code)["rem"]}</td></tr>'
    for r in weeks_all
])

table_full = f'<div class="syllabus-table-wrapper"><table class="syllabus-table"><thead><tr><th class="col-week">{cur_h[0]}</th><th class="col-date">{cur_h[1]}</th><th class="col-progress">{cur_h[2]}</th><th class="col-hw">{cur_h[3]}</th><th class="col-summary">{cur_h[4]}</th><th class="col-remarks">{cur_h[5]}</th></tr></thead><tbody>{rows_html}</tbody></table></div>'

if hasattr(st, "html"):
    st.html(table_full)
else:
    st.markdown(table_full, unsafe_allow_html=True)

# 6. 側邊欄：多語系切換 AI 助教
with st.sidebar:
    ui_texts = {
        "title": {
            "us": "🤖 Course AI Assistant", "tw": "🤖 課程 AI 助教", "vn": "🤖 Trợ lý AI Khóa học",
            "id": "🤖 Asisten AI Kursus", "my": "🤖 Pembantu AI Kursus", "th": "🤖 ผู้ช่วย AI ประจำวิชา", "fr": "🤖 Assistant IA du Cours"
        },
        "caption": {
            "us": "Ask questions to earn in-class engagement bonus! (Anonymous available)",
            "tw": "提出問題可獲得課堂平時參與加分！（亦可自由選擇匿名）",
            "vn": "Đặt câu hỏi để nhận điểm cộng tích cực trên lớp! (Có thể ẩn danh)",
            "id": "Ajukan pertanyaan untuk bonus keaktifan kelas! (Bisa anonim)",
            "my": "Kemukakan soalan untuk bonus penyertaan kelas! (Boleh tanpa nama)",
            "th": "ถามคำถามเพื่อรับคะแนนการมีส่วนร่วมในชั้นเรียน! (ไม่เปิดเผยตัวตนได้)",
            "fr": "Posez des questions pour gagner des points de participation ! (Anonymat possible)"
        },
        "select_label": {
            "us": "🙋 Select ID:", "tw": "🙋 選擇身分:", "vn": "🙋 Chọn danh tính:",
            "id": "🙋 Pilih Identitas:", "my": "🙋 Pilih Identiti:", "th": "🙋 เลือกตัวตนของคุณ:", "fr": "🙋 Choisissez votre identifiant:"
        },
        "placeholder": {
            "us": "Type your question...", "tw": "請輸入您的問題...", "vn": "Nhập câu hỏi của bạn...",
            "id": "Ketik pertanyaan Anda...", "my": "Tulis soalan anda...", "th": "พิมพ์คำถามของคุณ...", "fr": "Posez votre question..."
        },
        "btn_submit": {
            "us": "🚀 Submit Question", "tw": "🚀 送出問題", "vn": "🚀 Gửi câu hỏi",
            "id": "🚀 Kirim Pertanyaan", "my": "🚀 Hantar Soalan", "th": "🚀 ส่งคำถาม", "fr": "🚀 Poser la question"
        }
    }

    st.header(ui_texts["title"].get(current_code, ui_texts["title"]["us"]))
    st.caption(ui_texts["caption"].get(current_code, ui_texts["caption"]["us"]))

    student_roster = [
        "👤 Anonymous (匿名提問)",
        "***205 · 輝 (Huy)",
        "***201 · 輝 (Huy)",
        "***202 · 葳",
        "***203 · 心 (Tâm)",
        "***204 · 江",
        "***205 · 寶 (Bảo)",
        "***206 · 娟 (Quyên)",
        "***208 · 泰 (Thái)",
        "***209 · 輝 (Huy)",
        "***210 · 希 (Hy)",
        "***211 · 甯",
        "***212 · 莊 (Trang)",
        "***213 · 勇 (Dũng)",
        "***214 · 安",
        "***215 · 德 (Đức)",
        "***216 · 珍 (Trân)",
        "***217 · 豪 (Hào)",
        "➕ Other / Guest (旁聽／加選生自填)"
    ]

    selected_choice = st.selectbox(ui_texts["select_label"].get(current_code, "🙋 Select ID:"), student_roster)

    if selected_choice == "➕ Other / Guest (旁聽／加選生自填)":
        custom_name = st.text_input("📝 Enter ID / Nickname (輸入暱稱或學號):", placeholder="e.g. Guest 301 Alex")
        final_student_id = f"Guest: {custom_name}" if custom_name.strip() else "Guest"
    else:
        final_student_id = selected_choice

    user_q = st.text_input("💬", placeholder=ui_texts["placeholder"].get(current_code, "Type your question..."))
    
    if st.button(ui_texts["btn_submit"].get(current_code, "🚀 Submit"), use_container_width=True):
        if user_q:
            now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            q_lower = user_q.lower()
            
            if any(k in q_lower for k in ["đồ án", "cuối kỳ", "báo cáo", "final", "project", "showcase", "期末", "專案"]):
                local_answers = {
                    "us": "The Final Project Showcase takes place in **Week 17 & Week 18**. It counts for **30%** of your final grade.",
                    "tw": "期末專案成果發表將於 **第 17 週與第 18 週** 課堂進行，佔學期總成績 **30%**。",
                    "vn": "Đồ án cuối kỳ sẽ báo cáo trực tiếp vào **Tuần 17 & Tuần 18**, chiếm **30%** tổng điểm môn học.",
                    "id": "Presentasi Proyek Akhir berlangsung pada **Minggu ke-17 & 18**, berbobot **30%** dari nilai akhir.",
                    "my": "Pembentangan Projek Akhir diadakan pada **Minggu ke-17 & 18**, menyumbang **30%** daripada markah akhir.",
                    "th": "การนำเสนอโครงงานปลายภาคจะมีขึ้นใน **สัปดาห์ที่ 17 และ 18** โดยคิดเป็น **30%** ของเกรดรวม",
                    "fr": "La présentation des projets finaux aura lieu lors des **semaines 17 et 18** (30% de la note finale)."
                }
                zh_summary = "詢問期末專案發表時程與佔比"
                en_broadcast = "The Final Project Showcase is in Week 17 & 18 (30% of total grade)."

            elif any(k in q_lower for k in ["điểm", "grade", "score", "tỷ lệ", "評分", "成績", "比重"]):
                local_answers = {
                    "us": "Grading: Weekly in-class practice (50%), Midterm (20%), Final showcase (30%).",
                    "tw": "評量標準：每週課堂趣味實作 50%、期中考/專案 20%、期末成果展示 30%。",
                    "vn": "Tiêu chí chấm điểm: Thực hành trên lớp 50%, Giữa kỳ 20%, Đồ án cuối kỳ 30%.",
                    "id": "Penilaian: Praktik mingguan 50%, UTS 20%, Proyek akhir 30%.",
                    "my": "Pemarkahan: Amali mingguan 50%, Pertengahan penggal 20%, Projek akhir 30%.",
                    "th": "เกณฑ์คะแนน: แบบฝึกหัดในชั้นเรียน 50%, กลางภาค 20%, โครงงานปลายภาค 30%",
                    "fr": "Évaluation : Pratique en classe 50%, Partiel 20%, Projet final 30%."
                }
                zh_summary = "詢問課程評分比重"
                en_broadcast = "Grading policy: 50% weekly practice, 20% midterm, 30% final showcase."

            elif any(k in q_lower for k in ["colab", "bắt đầu", "python", "lập trình", "cài đặt", "環境"]):
                local_answers = {
                    "us": "No complex setup needed. We will code using **Google Colab** directly inside your web browser starting Week 1.",
                    "tw": "無須在個人電腦安裝繁瑣環境，第 1 週起直接使用瀏覽器開啟 **Google Colab** 實作。",
                    "vn": "Không cần cài đặt phức tạp. Chúng ta sẽ dùng **Google Colab** trực tiếp trên trình duyệt từ Tuần 1.",
                    "id": "Tidak perlu instalasi rumit. Kita menggunakan **Google Colab** langsung di browser mulai Minggu 1.",
                    "my": "Tiada pemasangan rumit diperlukan. Kita akan gunakan **Google Colab** terus di pelayar bermula Minggu 1.",
                    "th": "ไม่ต้องติดตั้งโปรแกรมให้ยุ่งยาก เราจะเขียนโค้ดด้วย **Google Colab** บนเบราว์เซอร์ตั้งแต่สัปดาห์ที่ 1",
                    "fr": "Aucune installation requise. Nous utiliserons **Google Colab** directement dans le navigateur dès la semaine 1."
                }
                zh_summary = "詢問開發環境安裝"
                en_broadcast = "No local installation needed; we use Google Colab in browsers from Week 1."

            else:
                local_answers = {
                    "us": f"Your question has been noted: '{user_q}'. Feel free to discuss with the instructor right after class!",
                    "tw": f"已收到您的提問：『{user_q}』。下課後可隨時於教室與老師進一步討論！",
                    "vn": f"Câu hỏi của bạn: '{user_q}' đã được ghi nhận. Bạn có thể trao đổi thêm với giảng viên sau giờ học!",
                    "id": f"Pertanyaan Anda: '{user_q}' telah dicatat. Silakan berdiskusi dengan dosen setelah kelas!",
                    "my": f"Soalan anda: '{user_q}' telah direkodkan. Sila berbincang dengan pensyarah selepas kelas!",
                    "th": f"บันทึกคำถามของคุณแล้ว: '{user_q}' สามารถสอบถามเพิ่มเติมกับผู้สอนได้ทันทีหลังเลิกเรียน",
                    "fr": f"Votre question a bien été notée : '{user_q}'. N'hésitez pas à en parler à la fin du cours !"
                }
                zh_summary = f"學生提問：{user_q}"
                en_broadcast = "Feel free to ask questions after class or in our class chat group."

            st.success("✅ Recorded! / 已記錄")
            current_flag = LANG_CONFIG[current_code]["name"]
            st.markdown(f"**{current_flag}:**\n\n{local_answers.get(current_code, local_answers['us'])}")
            
            if current_code != "tw":
                st.markdown(f"**🇹🇼 教師對照 (繁體中文):**\n- 提問者: `{final_student_id}`\n- 核心摘要: {zh_summary}")
                
            if current_code != "us":
                st.markdown(f"**🇺🇸 For Class Broadcast (English):**\n*{en_broadcast}*")

            if "Anonymous" not in final_student_id:
                st.caption(f"🎉 Participation logged for `{final_student_id}`.")
        else:
            st.warning("Please type a question. (請輸入問題)")
