# ==============================================================================
# [Script] Interactive Multilingual Syllabus Portal & Q&A Assistant
# 學生端多語系課綱門戶（含教室創506、必備筆電手機、4行Code快速複製、Colab/Gemini按鈕）
# ==============================================================================

import streamlit as st
import datetime
import requests

# 1. 頁面基本配置
st.set_page_config(
    page_title="Python AI Applications - Syllabus Portal",
    layout="wide",
    page_icon="🎓"
)

# 2. 語言定義
LANG_CONFIG = {
    "us": {"label": "English", "name": "🇺🇸 English (Official)", "flag": "https://flagcdn.com/w40/us.png"},
    "tw": {"label": "繁體中文", "name": "🇹🇼 繁體中文 (Traditional Chinese)", "flag": "https://flagcdn.com/w40/tw.png"},
    "vn": {"label": "Tiếng Việt", "name": "🇻🇳 Tiếng Việt (Vietnamese)", "flag": "https://flagcdn.com/w40/vn.png"},
    "id": {"label": "B. Indonesia", "name": "🇮🇩 Bahasa Indonesia (Indonesian)", "flag": "https://flagcdn.com/w40/id.png"},
    "my": {"label": "B. Melayu", "name": "🇲🇾 Bahasa Melayu (Malay)", "flag": "https://flagcdn.com/w40/my.png"},
    "th": {"label": "ภาษาไทย", "name": "🇹🇭 ภาษาไทย (Thai)", "flag": "https://flagcdn.com/w40/th.png"},
    "fr": {"label": "Français", "name": "🇫🇷 Français (French)", "flag": "https://flagcdn.com/w40/fr.png"}
}

current_code = st.query_params.get("lang", "us")
if current_code not in LANG_CONFIG:
    current_code = "us"

current_info = LANG_CONFIG[current_code]

# 多語系副標題
SUBTITLES = {
    "us": "Fall 2026 (Semester 115-1) · Instructor: Kimiko Kechun Huang (黃可羣) · Dept. of Business and Management 2C · Room: Innovation Bldg 506 (創506)",
    "tw": "115 學期 四技經管系2丙 · 授課教師：黃可羣 (Kimiko Kechun Huang) · 上課教室：創新大樓 506 教室 (創506) · 3.0 學分",
    "vn": "Học kỳ 115-1 · Giảng viên: Kimiko Kechun Huang (黃可羣) · Khoa Quản trị và Quản lý Kinh doanh 2C · Phòng: Tòa Đổi mới 506 (創506)",
    "id": "Semester 115-1 · Dosen: Kimiko Kechun Huang (黃可羣) · Jurusan Bisnis dan Manajemen 2C · Ruang: Gedung Inovasi 506 (創506)",
    "my": "Semester 115-1 · Pensyarah: Kimiko Kechun Huang (黃可羣) · Jabatan Perniagaan dan Pengurusan 2C · Bilik: Bangunan Inovasi 506 (創506)",
    "th": "ภาคการศึกษา 115-1 · ผู้สอน: Kimiko Kechun Huang (黃可羣) · ภาควิชาธุรกิจและการจัดการ 2C · ห้องเรียน: อาคารนวัตกรรม 506 (創506)",
    "fr": "Semestre 115-1 · Enseignant : Kimiko Kechun Huang (黃可羣) · Dép. Gestion et Management 2C · Salle : Bâtiment Innovation 506 (創506)"
}

LANG_SELECT_PROMPTS = {
    "us": "🌐 Select Parallel Language:",
    "tw": "🌐 點擊按鈕切換語言對照：",
    "vn": "🌐 Chọn ngôn ngữ song ngữ đối chiếu:",
    "id": "🌐 Pilih Bahasa Tampilan:",
    "my": "🌐 Pilih Bahasa Paparan:",
    "th": "🌐 เลือกภาษาเพื่อแสดงผล:",
    "fr": "🌐 Sélectionnez la langue d'affichage :"
}

# 3. 頂部區域：標題與 QR Codes
header_col1, header_col2, header_col3 = st.columns([3, 1, 1])

with header_col1:
    st.markdown("## 🎓 Python AI Applications (Python AI 應用)")
    st.caption(SUBTITLES.get(current_code, SUBTITLES["us"]))
    st.markdown(f"**{LANG_SELECT_PROMPTS.get(current_code, LANG_SELECT_PROMPTS['us'])}**")

with header_col2:
    app_url = "https://ai-syllabus.streamlit.app"
    qr_portal_url = f"https://api.qrserver.com/v1/create-qr-code/?size=110x110&margin=4&data={app_url}"
    st.markdown(
        f"""
        <div style="text-align: center; background: #ffffff; padding: 4px; border-radius: 8px; border: 1px solid #e5e7eb; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
            <img src="{qr_portal_url}" style="width: 70px; height: 70px; display: block; margin: 0 auto;">
            <span style="font-size: 11px; color: #1e3a8a; font-weight: 600; display: block; margin-top: 2px;">📱 Portal QR</span>
        </div>
        """,
        unsafe_allow_html=True
    )

with header_col3:
    line_group_url = "https://line.me/ti/g2/LUyGiu6JVuGP9MQ2leJRbjn7zhEj-G55qGiGog?utm_source=invitation&utm_medium=link_copy&utm_campaign=default"
    qr_line_url = f"https://api.qrserver.com/v1/create-qr-code/?size=110x110&margin=4&data={line_group_url}"
    st.markdown(
        f"""
        <div style="text-align: center; background: #ffffff; padding: 4px; border-radius: 8px; border: 1px solid #e5e7eb; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
            <img src="{qr_line_url}" style="width: 70px; height: 70px; display: block; margin: 0 auto;">
            <span style="font-size: 11px; color: #06c755; font-weight: 600; display: block; margin-top: 2px;">💬 LINE Chat</span>
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

status_labels = {
    "us": "Current Parallel View", "tw": "目前對照語言", "vn": "Chế độ xem song song hiện tại",
    "id": "Tampilan Bahasa Saat Ini", "my": "Paparan Bahasa Semasa", "th": "มุมมองภาษาปัจจุบัน", "fr": "Vue de langue actuelle"
}
st.info(f"💡 **{status_labels.get(current_code, status_labels['us'])}**: **{current_info['name']}**")

# 4. 四大卡片完整多語系資料庫
meta_cards = {
    "goal": {
        "title": {
            "us": "🎯 Objectives & Conductor Mindset", 
            "tw": "🎯 教學目標與指揮家思維", 
            "vn": "🎯 Mục tiêu môn học & Tư duy nhạc trưởng",
            "id": "🎯 Tujuan & Pola Pikir Konduktor", 
            "my": "🎯 Objektif & Minda Konduktor", 
            "th": "🎯 วัตถุประสงค์ & แนวคิดผู้นำคำสั่ง", 
            "fr": "🎯 Objectifs & Chef d'orchestre"
        },
        "content": {
            "us": "As future business managers, you do not need to memorize complex coding syntax! You are the **conductor**, and AI is your musician. Connect freshman Accounting & Economics with sophomore Statistics and Management to build interactive charts and launch web apps on your phone.\n\n*If you can ask a question, you can create with AI!*",
            "tw": "作為未來的商業經理人，你不需要死記複雜的程式語法！你是樂團的**指揮家**，AI 則是你的樂手。串聯大一會計與經濟學基礎，支援大二統計、行銷與管理課程，共同打造互動商業圖表並發布手機 Web App。\n\n*只要會提問，就能與 AI 共同創造！*",
            "vn": "Là nhà quản lý tương lai, bạn không cần ghi nhớ cú pháp code! Bạn là **nhạc trưởng**, AI là nhạc công. Kết nối Kế toán & Kinh tế năm nhất với Thống kê và Quản trị năm hai để xây dựng biểu đồ tương tác và phát hành Web App.\n\n*Chỉ cần biết đặt câu hỏi, bạn có thể sáng tạo cùng AI!*",
            "id": "Sebagai calon manajer bisnis, Anda tidak perlu menghafal sintaksis kode yang rumit! Anda adalah **konduktor**, dan AI adalah musisi Anda. Hubungkan Akuntansi & Ekonomi tingkat satu dengan Statistik dan Manajemen tingkat dua untuk membuat grafik interaktif dan web app di ponsel.\n\n*Jika Anda bisa bertanya, Anda bisa berkreasi dengan AI!*",
            "my": "Sebagai pengurus perniagaan masa depan, anda tidak perlu menghafal sintaks kod yang rumit! Anda adalah **konduktor**, dan AI adalah pemuzik anda. Hubungkan Perakaunan & Ekonomi tahun satu dengan Statistik dan Pengurusan tahun dua untuk membina carta interaktif dan aplikasi web.\n\n*Jika anda boleh bertanya, anda boleh mencipta dengan AI!*",
            "th": "ในฐานะผู้จัดการธุรกิจในอนาคต คุณไม่จำเป็นต้องท่องจำไวยากรณ์โค้ดที่ซับซ้อน! คุณคือ**ผู้นำวงคอนดักเตอร์** และ AI คือนักดนตรีของคุณ เชื่อมโยงบัญชีและเศรษฐศาสตร์ปี 1 สู่สถิติและการจัดการปี 2 เพื่อสร้างชาร์ตและเว็บแอปบนมือถือ\n\n*ขอแค่ถามเป็น คุณก็สร้างสรรค์ร่วมกับ AI ได้!*",
            "fr": "En tant que futurs managers, nul besoin d'apprendre par cœur le code complexe ! Vous êtes le **chef d'orchestre**, l'IA est votre musicien. Reliez la comptabilité et l'économie aux statistiques et à la gestion pour créer des applications web interactives sur smartphone.\n\n*Si vous savez poser des questions, vous savez créer avec l'IA !*"
        }
    },
    "grading": {
        "title": {
            "us": "📊 Grading Policy", 
            "tw": "📊 評量標準", 
            "vn": "📊 Tiêu chí đánh giá",
            "id": "📊 Kebijakan Penilaian", 
            "my": "📊 Dasar Pemarkahan", 
            "th": "📊 เกณฑ์การประเมินผล", 
            "fr": "📊 Barème d'évaluation"
        },
        "content": {
            "us": "**Weekly In-Class Fun Practice**: 50%  \n**Midterm Exam or Project (W9)**: 20%  \n**Final Project Report & Showcase (W16)**: 30%  \n*(Step-by-step guidance in class. Beginners are warmly welcome!)*",
            "tw": "**每週課堂趣味實作練習**：50%  \n**期中測驗或專題 (第 9 週)**：20%  \n**期末專案報告與成果發表 (第 16 週)**：30%  \n*(課堂手把手步驟引導，初學者友善！)*",
            "vn": "**Thực hành vui trên lớp hàng tuần**: 50%  \n**Thi giữa kỳ / Đồ án (Tuần 9)**: 20%  \n**Báo cáo & Trình bày đồ án (Tuần 16)**: 30%  \n*(Hướng dẫn chi tiết từng bước, chào đón người mới bắt đầu!)*",
            "id": "**Praktik Seru Mingguan di Kelas**: 50%  \n**Ujian Tengah Semester / Proyek (M9)**: 20%  \n**Laporan & Presentasi Proyek Akhir (M16)**: 30%  \n*(Panduan langkah demi langkah di kelas. Sangat ramah pemula!)*",
            "my": "**Latihan Amali Mingguan di Kelas**: 50%  \n**Peperiksaan Pertengahan Penggal / Projek (M9)**: 20%  \n**Laporan & Pembentangan Akhir (M16)**: 30%  \n*(Bimbingan langkah demi langkah dalam kelas. Mesra pemula!)*",
            "th": "**แบบฝึกหัดในชั้นเรียนรายสัปดาห์**: 50%  \n**สอบกลางภาคหรือโครงงาน (สัปดาห์ 9)**: 20%  \n**รายงานและการนำเสนอโครงงานปลายภาค (สัปดาห์ 16)**: 30%  \n*(มีคำแนะนำทีละขั้นตอนในชั้นเรียน เหมาะสำหรับผู้เริ่มต้นอย่างยิ่ง!)*",
            "fr": "**Pratiques interactives en classe**: 50%  \n**Examen partiel ou projet (Semaine 9)**: 20%  \n**Rapport final et soutenance (Semaine 16)**: 30%  \n*(Accompagnement pas à pas en classe. Débutants bienvenus !)*"
        }
    },
    "materials": {
        "title": {
            "us": "💻 Devices & Open Platforms", 
            "tw": "💻 上課設備與開放平台", 
            "vn": "💻 Thiết bị & Nền tảng mở",
            "id": "💻 Perangkat & Platform Terbuka", 
            "my": "💻 Peranti & Platform Terbuka", 
            "th": "💻 อุปกรณ์และแพลตฟอร์ม", 
            "fr": "💻 Appareils & Plateformes ouvertes"
        },
        "content": {
            "us": "**Bring to Class**:  \n1. 💻 **Laptop (Required)**: For cloud coding (Google Colab).  \n2. 📱 **Smartphone**: For LINE chat & web apps.  \n3. 🎧 **Transparency Earphones (Recommended)**: Best for voice-prompting AI while hearing classmates and lecture!  \n**Platforms**: Google Colab, Google AI Studio, Streamlit, FRED API.",
            "tw": "**每週必備設備**：  \n1. 💻 **筆記型電腦（必備）**：用於雲端 Colab 編程實作。  \n2. 📱 **智慧型手機**：用於 LINE 社群與 App 預覽。  \n3. 🎧 **透通式耳機/麥克風（強烈推薦）**：結合 AI 語音輸入神技，邊聽邊講且不漏接老師上課與同伴討論！  \n**雲端工具**：Google Colab、Google AI Studio、Streamlit、FRED 總經資料庫。",
            "vn": "**Mang theo khi lên lớp**:  \n1. 💻 **Laptop (Bắt buộc)**: Dùng để lập trình Google Colab.  \n2. 📱 **Điện thoại thông minh**: Dùng cho nhóm LINE và xem trước Web App.  \n3. 🎧 **Tai nghe xuyên âm (Được khuyến nghị)**: Giúp sử dụng giọng nói với AI mà vẫn nghe rõ bài giảng!  \n**Nền tảng**: Google Colab, Google AI Studio, Streamlit, FRED API.",
            "id": "**Bawa ke Kelas**:  \n1. 💻 **Laptop (Wajib)**: Untuk coding cloud Google Colab.  \n2. 📱 **Ponsel**: Untuk obrolan LINE & web app.  \n3. 🎧 **Earphone Transparan (Disarankan)**: Terbaik untuk perintah suara AI sambil mendengarkan kelas!  \n**Platform**: Google Colab, Google AI Studio, Streamlit, FRED API.",
            "my": "**Bawa ke Kelas**:  \n1. 💻 **Laptop (Wajib)**: Untuk pengaturcaraan Google Colab.  \n2. 📱 **Telefon Pintar**: Untuk sembang LINE & aplikasi web.  \n3. 🎧 **Earfon Telus (Disyorkan)**: Sesuai untuk arahan suara AI sambil mendengar kuliah!  \n**Platform**: Google Colab, Google AI Studio, Streamlit, FRED API.",
            "th": "**สิ่งที่ต้องนำมาเรียน**:  \n1. 💻 **แล็ปท็อป (จำเป็น)**: สำหรับ Google Colab  \n2. 📱 **สมาร์ทโฟน**: สำหรับ LINE และเว็บแอป  \n3. 🎧 **หูฟังโหมดโปร่งใส (แนะนำ)**: เหมาะที่สุดสำหรับการสั่งงานด้วยเสียง AI พร้อมฟังบรรยาย!  \n**แพลตฟอร์ม**: Google Colab, Google AI Studio, Streamlit, FRED API.",
            "fr": "**À apporter en cours**:  \n1. 💻 **Ordinateur portable (Requis)**: Pour Google Colab.  \n2. 📱 **Smartphone**: Pour le chat LINE et les web apps.  \n3. 🎧 **Écouteurs à transparence (Recommandé)**: Idéal pour dicter à l'IA tout en écoutant le cours !  \n**Plateformes**: Google Colab, Google AI Studio, Streamlit, FRED API."
        }
    },
    "office_hour": {
        "title": {
            "us": "🕒 Office Hours & Contact", 
            "tw": "🕒 諮詢時間與聯絡管道", 
            "vn": "🕒 Giờ tư vấn & Liên hệ",
            "id": "🕒 Jam Konsultasi & Kontak", 
            "my": "🕒 Waktu Konsultasi & Hubungan", 
            "th": "🕒 เวลาให้คำปรึกษา & การติดต่อ", 
            "fr": "🕒 Permanence & Contact"
        },
        "content": {
            "us": "**Instructor**: Kimiko Kechun Huang (黃可羣)  \n**Office Hour**: Talk directly right after class in Room 506, or message in our LINE group to set up a meeting on campus.  \n**Email**: `kimikohuang@mail.mcut.edu.tw`  \n**LINE Nickname**: Last 3 digits + Name (e.g. 205 Huy)",
            "tw": "**授課教師**：黃可羣 (Kimiko Kechun Huang)  \n**諮詢時間**：每週四下課後於 506 教室面談，或於 LINE 社群私訊預約校內諮詢。  \n**公務信箱**：`kimikohuang@mail.mcut.edu.tw`  \n**LINE 暱稱**：學號末三碼 + 名字（例如：205 Huy）",
            "vn": "**Giảng viên**: Kimiko Kechun Huang (黃可羣)  \n**Giờ tư vấn**: Trao đổi trực tiếp sau giờ học tại Phòng 506, hoặc nhắn trong nhóm LINE để hẹn lịch gặp tại trường.  \n**Email**: `kimikohuang@mail.mcut.edu.tw`  \n**Quy định LINE**: 3 số cuối mã SV + Tên (vd: 205 Huy)",
            "id": "**Dosen**: Kimiko Kechun Huang (黃可羣)  \n**Jam Konsultasi**: Konsultasi langsung setelah kelas di Ruang 506, atau buat janji temu via grup LINE.  \n**Email**: `kimikohuang@mail.mcut.edu.tw`  \n**Aturan LINE**: 3 Digit Akhir + Nama (cth: 205 Huy)",
            "my": "**Pensyarah**: Kimiko Kechun Huang (黃可羣)  \n**Waktu Konsultasi**: Berbincang terus selepas kelas di Bilik 506, atau mesej dalam grup LINE untuk janji temu.  \n**Emel**: `kimikohuang@mail.mcut.edu.tw`  \n**Peraturan LINE**: 3 Digit Terakhir + Nama (cth: 205 Huy)",
            "th": "**ผู้สอน**: Kimiko Kechun Huang (黃可羣)  \n**เวลาปรึกษา**: ปรึกษาได้ทันทีหลังเลิกเรียนที่ห้อง 506 หรือส่งข้อความนัดหมายในกลุ่ม LINE  \n**อีเมล**: `kimikohuang@mail.mcut.edu.tw`  \n**กฎ LINE**: เลขท้าย 3 ตัว + ชื่อ (เช่น 205 Huy)",
            "fr": "**Enseignant** : Kimiko Kechun Huang (黃可羣)  \n**Permanence** : Directement après le cours en salle 506, ou sur rendez-vous via le groupe LINE.  \n**Email** : `kimikohuang@mail.mcut.edu.tw`  \n**Règle LINE** : 3 derniers chiffres + Nom (ex: 205 Huy)"
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

# ==============================================================================
# 5. 【學期藍圖：置頂】18 週課程完整大表格（100% 精準對照學校進度表）
# ==============================================================================
st.markdown("---")
schedule_expander_titles = {
    "us": "🗓️ View Official 18-Week Syllabus Breakdown (Click to Expand)",
    "tw": "🗓️ 查看官方完整 18 週教學進度總表（點擊展開查閱）",
    "vn": "🗓️ Xem toàn bộ lịch trình 18 tuần chính thức (Bấm để mở rộng)",
    "id": "🗓️ Lihat Silabus Lengkap 18 Minggu Resmi (Klik untuk Memperluas)",
    "my": "🗓️ Lihat Sukatan Pelajaran Rasmi 18 Minggu (Klik untuk Buka)",
    "th": "🗓️ ดูแผนการสอนอย่างเป็นทางการ 18 สัปดาห์ (คลิกเพื่อขยาย)",
    "fr": "🗓️ Consulter le calendrier officiel sur 18 semaines (Cliquez pour dérouler)"
}

weeks_all = [
    {
        "week": "Week 1", "date": "2026/09/10",
        "us": {"prog": "Course Onboarding & Vibe Coding", "hw": "Lab 0: In-class fun exploration", "sum": "Course overview; prompt-driven programming with natural language; Google Colab setup; zero syntax stress.", "rem": "創506"},
        "tw": {"prog": "課程導覽與自然語言編程", "hw": "Lab 0: 課堂趣味實作探索", "sum": "課程總覽；自然語言提示詞編程；Google Colab 環境配置；零語法壓力。", "rem": "創506"},
        "vn": {"prog": "Khởi động khóa học & Vibe Coding", "hw": "Lab 0: Khám phá thú vị tại lớp", "sum": "Tổng quan môn học; lập trình bằng câu lệnh tự nhiên; cài đặt Colab; không áp lực cú pháp.", "rem": "創506"},
        "id": {"prog": "Pengenalan Kursus & Vibe Coding", "hw": "Lab 0: Eksplorasi seru di kelas", "sum": "Tinjauan kursus; pemrograman berbasis prompt bahasa alami; setup Colab; bebas stres sintaks.", "rem": "創506"},
        "my": {"prog": "Pengenalan Kursus & Vibe Coding", "hw": "Lab 0: Penerokaan menarik dalam kelas", "sum": "Gambaran keseluruhan kursus; pengaturcaraan bahasa semula jadi; persediaan Colab; sifar tekanan sintaks.", "rem": "創506"},
        "th": {"prog": "ปฐมนิเทศรายวิชา & Vibe Coding", "hw": "Lab 0: กิจกรรมสำรวจในชั้นเรียน", "sum": "ภาพรวมวิชา; เขียนโค้ดด้วยภาษาธรรมชาติผ่านข้อความพร้อมต์; ติดตั้ง Colab; ปราศจากความเครียดเรื่องไวยากรณ์", "rem": "創506"},
        "fr": {"prog": "Introduction au cours & Vibe Coding", "hw": "Lab 0 : Découverte pratique en classe", "sum": "Présentation du cours ; programmation en langage naturel ; configuration Colab ; zéro stress de syntaxe.", "rem": "創506"}
    },
    {
        "week": "Week 2", "date": "2026/09/17",
        "us": {"prog": "Market Data Engineering: Apple & TSMC", "hw": "In-class live practice", "sum": "Add/drop period; fetching daily stock prices with Python; creating visual trend charts; friendly onboarding.", "rem": "創506"},
        "tw": {"prog": "市場數據工程：台積電與蘋果", "hw": "課堂即時實作與練習", "sum": "加退選期間；Python 擷取每日股價；資料表 DataFrame 處理與繪製走勢圖；友善入門。", "rem": "創506"},
        "vn": {"prog": "Kỹ thuật dữ liệu thị trường: Apple & TSMC", "hw": "Thực hành trực tiếp trên lớp", "sum": "Giai đoạn thêm/hủy môn; lấy giá cổ phiếu hàng ngày; vẽ biểu đồ xu hướng trực quan; làm quen nhẹ nhàng.", "rem": "創506"},
        "id": {"prog": "Rekayasa Data Pasar: Apple & TSMC", "hw": "Latihan langsung di kelas", "sum": "Periode tambah/batal matkul; mengambil harga saham harian; grafik tren visual; onboarding ramah.", "rem": "創506"},
        "my": {"prog": "Kejuruteraan Data Pasaran: Apple & TSMC", "hw": "Latihan langsung dalam kelas", "sum": "Tempoh tambah/gugur kursus; mengambil data harga saham harian; carta trend visual; pengenalan mesra.", "rem": "創506"},
        "th": {"prog": "วิศวกรรมข้อมูลตลาด: Apple & TSMC", "hw": "ฝึกปฏิบัติตามสดในชั้นเรียน", "sum": "ช่วงเพิ่ม-ถอนรายวิชา; ดึงข้อมูลราคาหุ้นรายวันด้วย Python; สร้างกราฟแนวโน้ม; เริ่มต้นอย่างเป็นมิตร", "rem": "創506"},
        "fr": {"prog": "Ingénierie des données de marché : Apple & TSMC", "hw": "Exercice guidé en classe", "sum": "Période d'ajustement ; extraction de cours boursiers avec Python ; graphiques visuels ; onboarding doux.", "rem": "創506"}
    },
    {
        "week": "Week 3", "date": "2026/09/24",
        "us": {"prog": "Global EV Trends: Tesla vs. Worldwide Market Leaders", "hw": "Lab 1: EV market trends notebook", "sum": "Roster finalized; comparing global EV leaders and key supply chain players; calculating daily returns and simple risk metrics.", "rem": "創506"},
        "tw": {"prog": "全球電動車趨勢：Tesla 與全球車廠龍頭", "hw": "Lab 1: 電動車市場趨勢筆記本", "sum": "選課名單確定；全球電動車供應鏈與龍頭對比；計算日報酬率與簡易風險指標。", "rem": "創506"},
        "vn": {"prog": "Xu hướng xe điện toàn cầu: Tesla vs Các hãng lớn", "hw": "Lab 1: Vở bài tập xu hướng xe điện", "sum": "Chốt danh sách lớp; so sánh các hãng xe điện và chuỗi cung ứng; tính tỷ suất sinh lời và rủi ro cơ bản.", "rem": "創506"},
        "id": {"prog": "Tren EV Global: Tesla vs Pemimpin Industri Dunia", "hw": "Lab 1: Notebook tren pasar EV", "sum": "Daftar mahasiswa final; membandingkan produsen EV dan rantai pasok; menghitung return harian & risiko.", "rem": "創506"},
        "my": {"prog": "Trend EV Global: Tesla vs Peneraju Industri Global", "hw": "Lab 1: Buku nota trend pasaran EV", "sum": "Senarai kursus muktamad; analisis rantaian bekalan EV; pengiraan pulangan harian dan metrik risiko mudah.", "rem": "創506"},
        "th": {"prog": "แนวโน้มยานยนต์ไฟฟ้าโลก: Tesla เทียบผู้นำตลาดโลก", "hw": "Lab 1: สมุดโค้ดวิเคราะห์แนวโน้มตลาด EV", "sum": "สรุปรายชื่อลงทะเบียน; เปรียบเทียบผู้นำ EV และห่วงโซ่อุปทานหลัก; คำนวณผลตอบแทนรายวันและดัชนีความเสี่ยงเบื้องต้น", "rem": "創506"},
        "fr": {"prog": "Tendances mondiales des VE : Tesla vs Leaders mondiaux", "hw": "TP 1 : Notebook tendances du marché VE", "sum": "Inscriptions closes ; comparatif du secteur des VE ; calcul des rendements journaliers et métriques de risque simples.", "rem": "創506"}
    },
    {
        "week": "Week 4", "date": "2026/10/01",
        "us": {"prog": "Quantitative Trading Strategies", "hw": "Lab 2: Moving average strategy report", "sum": "Moving average concepts (20MA vs 60MA); comparing trading rules vs. Buy & Hold; evaluating returns and safety.", "rem": "創506"},
        "tw": {"prog": "量化交易策略實戰", "hw": "Lab 2: 移動平均線策略報告", "sum": "均線交叉法則（20MA vs 60MA）；規則化交易與買進持有對比；報酬率與安全性評估。", "rem": "創506"},
        "vn": {"prog": "Chiến lược giao dịch định lượng", "hw": "Lab 2: Báo cáo chiến lược đường trung bình", "sum": "Khái niệm đường trung bình MA (20MA vs 60MA); so sánh giao dịch theo quy tắc vs Mua & Nắm giữ; đánh giá lợi nhuận & an toàn.", "rem": "創506"},
        "id": {"prog": "Strategi Trading Kuantitatif", "hw": "Lab 2: Laporan strategi moving average", "sum": "Konsep Moving Average (20MA vs 60MA); membandingkan aturan trading vs Beli & Simpan; evaluasi return & keamanan.", "rem": "創506"},
        "my": {"prog": "Strategi Dagangan Kuantitatif", "hw": "Lab 2: Laporan strategi moving average", "sum": "Konsep purata bergerak (20MA vs 60MA); perbandingan strategi berasaskan peraturan vs Beli & Pegang; penilaian pulangan & keselamatan.", "rem": "創506"},
        "th": {"prog": "กลยุทธ์การซื้อขายเชิงปริมาณ", "hw": "Lab 2: รายงานกลยุทธ์เส้นค่าเฉลี่ยเคลื่อนที่", "sum": "แนวคิดเส้นค่าเฉลี่ย MA (20MA vs 60MA); เปรียบเทียบการเทรดตามกฎระเบียบ vs ซื้อถือยาว; ประเมินผลตอบแทนและความปลอดภัย", "rem": "創506"},
        "fr": {"prog": "Stratégies de trading quantitatif", "hw": "TP 2 : Rapport sur les moyennes mobiles", "sum": "Moyennes mobiles (20MA vs 60MA) ; règles de trading vs Buy & Hold ; évaluation des rendements et de la sécurité.", "rem": "創506"}
    },
    {
        "week": "Week 5", "date": "2026/10/08",
        "us": {"prog": "Macro Economy & Global Currencies", "hw": "Lab 3: Economic trends & FX report", "sum": "Connecting to FRED database; analyzing benchmark interest rates, inflation trends, and currency exchange rates.", "rem": "創506"},
        "tw": {"prog": "總體經濟指標與全球匯率觀測", "hw": "Lab 3: 總經趨勢與匯率觀測報告", "sum": "串接聖路易斯聯準會 FRED 資料庫；分析指標基準利率、通貨膨脹走勢與外匯匯率變動。", "rem": "創506"},
        "vn": {"prog": "Kinh tế vĩ mô & Tiền tệ toàn cầu", "hw": "Lab 3: Báo cáo xu hướng kinh tế & tỷ giá", "sum": "Kết nối cơ sở dữ liệu FRED; phân tích lãi suất chuẩn, xu hướng lạm phát và tỷ giá hối đoái ngoại tệ.", "rem": "創506"},
        "id": {"prog": "Ekonomi Makro & Mata Uang Global", "hw": "Lab 3: Laporan tren ekonomi & valas", "sum": "Menghubungkan database FRED; menganalisis suku bunga acuan, tren inflasi, dan nilai tukar mata uang.", "rem": "創506"},
        "my": {"prog": "Ekonomi Makro & Mata Wang Global", "hw": "Lab 3: Laporan trend ekonomi & pertukaran asing", "sum": "Menyambung ke pangkalan data FRED; menganalisis kadar faedah penanda aras, trend inflasi, dan kadar pertukaran wang.", "rem": "創506"},
        "th": {"prog": "เศรษฐกิจมหภาคและอัตราแลกเปลี่ยนโลก", "hw": "Lab 3: รายงานแนวโน้มเศรษฐกิจและอัตราแลกเปลี่ยน", "sum": "เชื่อมต่อฐานข้อมูล FRED; วิเคราะห์อัตราดอกเบี้ยนโยบาย แนวโน้มเงินเฟ้อ และอัตราแลกเปลี่ยนเงินตราต่างประเทศ", "rem": "創506"},
        "fr": {"prog": "Macroéconomie & Devises mondiales", "hw": "TP 3 : Rapport sur les tendances macro et le Forex", "sum": "Connexion à la base FRED ; analyse des taux d'intérêt directeurs, de l'inflation et des taux de change.", "rem": "創506"}
    },
    {
        "week": "Week 6", "date": "2026/10/15",
        "us": {"prog": "Corporate Health & Global Industry Champions", "hw": "Lab 4: Automated company health tool", "sum": "Reading financial statements; evaluating profitability, debt ratios, and DuPont ROE for global and regional market leaders.", "rem": "創506"},
        "tw": {"prog": "企業財務健康診斷與產業冠軍剖析", "hw": "Lab 4: 自動化企業健康診斷工具", "sum": "公開財務報表剖析；評估獲利能力、負債比率與杜邦 ROE 分析法，診斷國內外產業龍頭。", "rem": "創506"},
        "vn": {"prog": "Sức khỏe doanh nghiệp & Các nhà vô địch ngành", "hw": "Lab 4: Công cụ tự động đánh giá doanh nghiệp", "sum": "Đọc báo cáo tài chính; đánh giá khả năng sinh lời, tỷ lệ nợ và mô hình DuPont ROE cho các doanh nghiệp dẫn đầu.", "rem": "創506"},
        "id": {"prog": "Kesehatan Perusahaan & Juara Industri Global", "hw": "Lab 4: Alat otomatis kesehatan perusahaan", "sum": "Membaca laporan keuangan; evaluasi profitabilitas, rasio utang, dan analisis DuPont ROE bagi pemimpin pasar.", "rem": "創506"},
        "my": {"prog": "Kesihatan Korporat & Peneraju Industri Global", "hw": "Lab 4: Alat automatik kesihatan syarikat", "sum": "Membaca penyata kewangan; menilai keberuntungan, nisbah hutang, dan DuPont ROE untuk peneraju pasaran.", "rem": "創506"},
        "th": {"prog": "สุขภาพทางการเงินขององค์กรและผู้นำอุตสาหกรรมโลก", "hw": "Lab 4: เครื่องมือตรวจสุขภาพองค์กรอัตโนมัติ", "sum": "อ่านงบการเงิน; ประเมินความสามารถในการทำกำไร อัตราส่วนหนี้สิน และโมเดล DuPont ROE สำหรับบริษัทชั้นนำระดับโลก", "rem": "創506"},
        "fr": {"prog": "Santé d'entreprise & Champions industriels mondiaux", "hw": "TP 4 : Outil automatisé de santé financière", "sum": "Lecture des états financiers ; analyse de rentabilité, ratios d'endettement et modèle DuPont ROE.", "rem": "創506"}
    },
    {
        "week": "Week 7", "date": "2026/10/22",
        "us": {"prog": "Google AI Studio: Virtual Analyst", "hw": "Lab 5: AI prompt tuning practice", "sum": "Exploring Google AI Studio; configuring system instructions; building an AI copilot for business news summarization.", "rem": "創506"},
        "tw": {"prog": "Google AI Studio：虛擬商業分析師打造", "hw": "Lab 5: AI 提示詞微調實作練習", "sum": "探索 Google AI Studio 平臺；配置系統角色指令（System Instructions）；打造商業新聞摘要專屬 Copilot。", "rem": "創506"},
        "vn": {"prog": "Google AI Studio: Nhà phân tích ảo", "hw": "Lab 5: Thực hành tinh chỉnh prompt AI", "sum": "Khám phá Google AI Studio; cấu hình chỉ thị hệ thống; xây dựng trợ lý AI tóm tắt tin tức kinh doanh.", "rem": "創506"},
        "id": {"prog": "Google AI Studio: Analis Virtual", "hw": "Lab 5: Latihan tuning prompt AI", "sum": "Eksplorasi Google AI Studio; konfigurasi instruksi sistem; membangun AI copilot untuk ringkasan berita bisnis.", "rem": "創506"},
        "my": {"prog": "Google AI Studio: Penganalisis Maya", "hw": "Lab 5: Latihan penalaan prompt AI", "sum": "Meneroka Google AI Studio; mengkonfigurasi arahan sistem; membina copilot AI untuk meringkaskan berita perniagaan.", "rem": "創506"},
        "th": {"prog": "Google AI Studio: นักวิเคราะห์ธุรกิจเสมือนจริง", "hw": "Lab 5: ปฏิบัติการปรับแต่งคำสั่ง Prompt สำหรับ AI", "sum": "สำรวจ Google AI Studio; กำหนดคำสั่งระบบ (System Instructions); สร้าง AI Copilot สำหรับสรุปข่าวธุรกิจ", "rem": "創506"},
        "fr": {"prog": "Google AI Studio : Analyste virtuel", "hw": "TP 5 : Pratique de conception de prompts d'IA", "sum": "Découverte de Google AI Studio ; configuration des instructions système ; création d'un copilote d'analyse de presse.", "rem": "創506"}
    },
    {
        "week": "Week 8", "date": "2026/10/29",
        "us": {"prog": "Multilingual News Sentiment", "hw": "Lab 6: Market sentiment dashboard", "sum": "Using Gemini API; analyzing positive and negative market sentiment from financial news headlines and public comments.", "rem": "創506"},
        "tw": {"prog": "多語系財經新聞市場情緒分析", "hw": "Lab 6: 市場情緒即時監控儀表板", "sum": "串接 Gemini API；深度剖析多國語言財經新聞標題與大眾輿情正面/負面情緒指數。", "rem": "創506"},
        "vn": {"prog": "Phân tích tâm lý tin tức đa ngôn ngữ", "hw": "Lab 6: Bảng theo dõi tâm lý thị trường", "sum": "Sử dụng Gemini API; phân tích cảm xúc tích cực và tiêu cực từ tiêu đề tin tức tài chính và bình luận xã hội.", "rem": "創506"},
        "id": {"prog": "Sentimen Berita Pasar Multibahasa", "hw": "Lab 6: Dashboard sentimen pasar", "sum": "Menggunakan API Gemini; menganalisis sentimen pasar positif & negatif dari judul berita finansial dan opini publik.", "rem": "創506"},
        "my": {"prog": "Sentimen Berita Pasaran Pelbagai Bahasa", "hw": "Lab 6: Papan pemuka sentimen pasaran", "sum": "Menggunakan API Gemini; menganalisis sentimen positif dan negatif daripada tajuk berita kewangan dan ulasan awam.", "rem": "創506"},
        "th": {"prog": "วิเคราะห์ความรู้สึกจากข่าวการเงินหลายภาษา", "hw": "Lab 6: แดชบอร์ดติดตามความรู้สึกตลาด", "sum": "ใช้งาน Gemini API; วิเคราะห์ดัชนีความรู้สึกเชิงบวกและเชิงลบจากพาดหัวข่าวการเงินและความคิดเห็นสาธารณะ", "rem": "創506"},
        "fr": {"prog": "Analyse de sentiment d'actualités multilingues", "hw": "TP 6 : Tableau de bord de sentiment de marché", "sum": "Utilisation de l'API Gemini ; analyse des sentiments haussiers/baissiers à partir des flux d'actualités financières.", "rem": "創506"}
    },
    {
        "week": "Week 9", "date": "2026/11/05",
        "us": {"prog": "Midterm Examination Week", "hw": "Midterm Practical Review", "sum": "Official Midterm Exam Week; in-class hands-on assessment of core AI prompts and financial calculations.", "rem": "Midterm Exam"},
        "tw": {"prog": "【期中評量週】實作成果審查", "hw": "期中上機實務總複習與評量", "sum": "學校期中考週；課堂核心 AI 提示詞編程實作與商業財務指標計算上機評量。", "rem": "期中評量"},
        "vn": {"prog": "【Tuần thi giữa kỳ】Đánh giá thực hành", "hw": "Ôn tập và kiểm tra thực hành giữa kỳ", "sum": "Tuần thi giữa kỳ chính thức; đánh giá thực hành trên lớp về câu lệnh prompt AI và tính toán tài chính cốt lõi.", "rem": "Thi giữa kỳ"},
        "id": {"prog": "[Minggu UTS] Evaluasi Praktik", "hw": "Review dan Penilaian Praktik UTS", "sum": "Minggu UTS resmi; asesmen langsung di kelas mengenai prompt AI inti dan perhitungan finansial bisnis.", "rem": "Ujian Tengah Semester"},
        "my": {"prog": "[Minggu Peperiksaan Pertengahan Penggal]", "hw": "Semakan Amali Pertengahan Penggal", "sum": "Minggu Peperiksaan Pertengahan Penggal rasmi; penilaian amali dalam kelas melibatkan prompt AI dan pengiraan kewangan.", "rem": "Peperiksaan"},
        "th": {"prog": "【สัปดาห์สอบกลางภาค】การประเมินผลภาคปฏิบัติ", "hw": "ทบทวนและประเมินผลปฏิบัติการกลางภาค", "sum": "สัปดาห์สอบกลางภาคอย่างเป็นทางการ; การประเมินผลในชั้นเรียนเรื่องการสั่งการ AI และการคำนวณทางการเงิน", "rem": "สอบกลางภาค"},
        "fr": {"prog": "[Semaine des examens partiels]", "hw": "Évaluation pratique de mi-semestre", "sum": "Semaine officielle d'examens partiels ; évaluation pratique sur machine des prompts d'IA et calculs financiers.", "rem": "Examen"}
    },
    {
        "week": "Week 10", "date": "2026/11/12",
        "us": {"prog": "Interactive Web Apps with Streamlit", "hw": "Lab 7: Web app interface script", "sum": "Transforming Python scripts into interactive web applications; adding dropdown menus, sliders, and buttons.", "rem": "創506"},
        "tw": {"prog": "Streamlit 互動 Web 應用開發入門", "hw": "Lab 7: 互動網頁介面開發腳本", "sum": "將 Python 數據分析腳本轉化為互動式 Web 應用程式；加入下拉選單、數值滑桿與功能按鈕。", "rem": "創506"},
        "vn": {"prog": "Ứng dụng Web tương tác với Streamlit", "hw": "Lab 7: Kịch bản giao diện Web App", "sum": "Chuyển mã Python thành ứng dụng web tương tác; thêm menu thả xuống, thanh trượt và các nút bấm.", "rem": "創506"},
        "id": {"prog": "Aplikasi Web Interaktif dengan Streamlit", "hw": "Lab 7: Skrip antarmuka aplikasi web", "sum": "Mengubah skrip Python menjadi aplikasi web interaktif; menambahkan menu dropdown, slider, dan tombol.", "rem": "創506"},
        "my": {"prog": "Aplikasi Web Interaktif dengan Streamlit", "hw": "Lab 7: Skrip antara muka aplikasi web", "sum": "Menukar skrip Python kepada aplikasi web interaktif; menambah menu dropdown, slider, dan butang tindakan.", "rem": "創506"},
        "th": {"prog": "สร้างเว็บแอปพลิเคชันเชิงโต้ตอบด้วย Streamlit", "hw": "Lab 7: สคริปต์ส่วนติดต่อผู้ใช้ของเว็บแอป", "sum": "เปลี่ยนสคริปต์ Python ให้กลายเป็นเว็บแอปที่โต้ตอบได้; เพิ่มเมนูดรอปดาวน์ ตัวเลื่อนปรับค่า และปุ่มกด", "rem": "創506"},
        "fr": {"prog": "Applications web interactives avec Streamlit", "hw": "TP 7 : Script d'interface pour application web", "sum": "Transformation de scripts Python en applications web interactives ; ajout de menus déroulants, curseurs et boutons.", "rem": "創506"}
    },
    {
        "week": "Week 11", "date": "2026/11/19",
        "us": {"prog": "Cloud Deployment & Mobile UI", "hw": "Lab 8: Deploy app to the web", "sum": "Publishing web applications online for free; testing responsive layouts on smartphones; mobile accessibility check.", "rem": "創506"},
        "tw": {"prog": "雲端部署實戰與手機響應式介面優化", "hw": "Lab 8: 雲端 Web 應用正式發布上線", "sum": "將 Web 應用程式免費發布至雲端永久運行；在手機上實機測試響應式排版與跨螢幕無障礙體驗。", "rem": "創506"},
        "vn": {"prog": "Triển khai đám mây & Giao diện di động", "hw": "Lab 8: Phát hành ứng dụng lên web", "sum": "Xuất bản ứng dụng web lên mạng miễn phí; kiểm thử giao diện thích ứng trên điện thoại thông minh.", "rem": "創506"},
        "id": {"prog": "Deployment Cloud & UI Mobile", "hw": "Lab 8: Rilis aplikasi ke web publik", "sum": "Mempublikasikan aplikasi web online secara gratis; menguji tata letak responsif pada smartphone.", "rem": "創506"},
        "my": {"prog": "Penyebaran Awan & Antara Muka Mudah Alih", "hw": "Lab 8: Sebarkan aplikasi ke web secara langsung", "sum": "Menerbitkan aplikasi web atas talian secara percuma; menguji reka bentuk responsif pada telefon pintar.", "rem": "創506"},
        "th": {"prog": "การปรับใช้บนคลาวด์ & UI สำหรับสมาร์ทโฟน", "hw": "Lab 8: นำเว็บแอปขึ้นสู่อินเทอร์เน็ตสาธารณะ", "sum": "เผยแพร่เว็บแอปพลิเคชันออนไลน์ฟรี; ทดสอบการจัดหน้าจอแบบตอบสนองบนสมาร์ทโฟน", "rem": "創506"},
        "fr": {"prog": "Déploiement Cloud & Interface Mobile", "hw": "TP 8 : Mise en ligne de l'application", "sum": "Publication gratuite d'applications web ; tests de compatibilité et responsive design sur smartphones.", "rem": "創506"}
    },
    {
        "week": "Week 12", "date": "2026/11/26",
        "us": {"prog": "Earnings Call & Annual Report Reader", "hw": "Lab 9: Automated risk summary report", "sum": "Using AI to parse corporate quarterly filings and earnings call transcripts; extracting key risks and growth drivers in seconds.", "rem": "創506"},
        "tw": {"prog": "法說會逐字稿與財報風險智慧解析", "hw": "Lab 9: 自動化企業風險摘要報告", "sum": "運用 AI 秒速剖析企業季報與法說會逐字稿；精準萃取營運關鍵風險因子與未來成長驅動力。", "rem": "創506"},
        "vn": {"prog": "Phân tích cuộc họp báo tài chính & Báo cáo thường niên", "hw": "Lab 9: Báo cáo tóm tắt rủi ro tự động", "sum": "Dùng AI bóc tách hồ sơ quý và biên bản họp báo cáo tài chính; trích xuất rủi ro chính và động lực tăng trưởng trong vài giây.", "rem": "創506"},
        "id": {"prog": "Pembaca Laporan Tahunan & Earnings Call", "hw": "Lab 9: Laporan ringkasan risiko otomatis", "sum": "Memanfaatkan AI untuk membedah laporan kuartalan dan transkrip earnings call; ekstraksi risiko dan pendorong pertumbuhan.", "rem": "創506"},
        "my": {"prog": "Pembaca Panggilan Pendapatan & Laporan Tahunan", "hw": "Lab 9: Laporan ringkasan risiko automatik", "sum": "Menggunakan AI untuk menghurai pemfailan suku tahunan dan transkrip panggilan pendapatan; mengekstrak risiko utama.", "rem": "創506"},
        "th": {"prog": "ระบบอ่านรายงานประจำปีและการแถลงผลประกอบการ", "hw": "Lab 9: รายงานสรุปความเสี่ยงองค์กรอัตโนมัติ", "sum": "ใช้ AI แยกวิเคราะห์รายงานทางการเงินรายไตรมาสและการแถลงผลงาน; ดึงข้อมูลความเสี่ยงสำคัญและปัจจัยหนุนการเติบโต", "rem": "創506"},
        "fr": {"prog": "Lecteur d'Earnings Call & Rapports annuels", "hw": "TP 9 : Synthèse automatisée des risques", "sum": "Utilisation de l'IA pour analyser les rapports trimestriels et les conférences de résultats financiers.", "rem": "創506"}
    },
    {
        "week": "Week 13", "date": "2026/12/03",
        "us": {"prog": "Multimodal AI: Smart Receipt Scanner", "hw": "Lab 10: Receipt scanner project", "sum": "Gemini Vision; parsing invoices and receipts; auto-generating accounting entries and inbound inventory sorting logic.", "rem": "創506"},
        "tw": {"prog": "多模態 AI 影像辨識：智慧發票報帳助手", "hw": "Lab 10: 智慧單據辨識專題", "sum": "運用 Gemini Vision 多模態視覺能力；辨識發票與收據；自動生成會計分錄與進貨分類盤點邏輯。", "rem": "創506"},
        "vn": {"prog": "AI đa phương thức: Máy quét hóa đơn thông minh", "hw": "Lab 10: Dự án quét hóa đơn tự động", "sum": "Gemini Vision; phân tích hóa đơn và biên lai; tự động tạo bút toán kế toán và phân loại hàng tồn kho nhập kho.", "rem": "創506"},
        "id": {"prog": "AI Multimodal: Pemindai Struk & Faktur Cerdas", "hw": "Lab 10: Proyek pemindai struk belanja", "sum": "Gemini Vision; parsing invoice dan kuitansi; otomatis membuat jurnal akuntansi dan klasifikasi inventaris masuk.", "rem": "創506"},
        "my": {"prog": "AI Multimodal: Pengimbas Resit Pintar", "hw": "Lab 10: Projek pengimbas resit automatik", "sum": "Gemini Vision; menganalisis invois dan resit; menjana catatan perakaunan automatik dan pengisihan inventori.", "rem": "創506"},
        "th": {"prog": "AI หลายรูปแบบ: ระบบสแกนใบเสร็จอัจฉริยะ", "hw": "Lab 10: โครงงานสแกนใบเสร็จและใบแจ้งหนี้", "sum": "Gemini Vision; แยกแยะใบแจ้งหนี้และใบเสร็จ; สร้างบันทึกทางบัญชีอัตโนมัติและจัดหมวดหมู่สินค้าคงคลัง", "rem": "創506"},
        "fr": {"prog": "IA Multimodale : Scanner de reçus et factures", "hw": "TP 10 : Projet de numérisation de reçus", "sum": "Gemini Vision ; analyse de factures et tickets ; génération automatique d'écritures comptables et inventaire.", "rem": "創506"}
    },
    {
        "week": "Week 14", "date": "2026/12/10",
        "us": {"prog": "Dynamic Charts: Interactive Visuals", "hw": "Project Sprint: Pro candlestick charts", "sum": "Creating interactive financial charts; zooming, tooltips, and volume overlays; polishing mobile user interfaces.", "rem": "創506"},
        "tw": {"prog": "動態商業視覺化：互動專業 K 線圖", "hw": "專案衝刺：專業動態 K 線圖表", "sum": "打造互動式金融圖表；縮放檢視、懸浮數值資訊卡與成交量疊加分析；精修手機操作介面。", "rem": "創506"},
        "vn": {"prog": "Biểu đồ động: Trực quan hóa tương tác", "hw": "Tăng tốc dự án: Biểu đồ nến chuyên nghiệp", "sum": "Tạo biểu đồ tài chính tương tác; phóng to, xem tooltip và lớp phủ khối lượng; tối ưu giao diện di động.", "rem": "創506"},
        "id": {"prog": "Grafik Dinamis: Visualisasi Interaktif", "hw": "Sprint Proyek: Grafik candlestick pro", "sum": "Membuat grafik keuangan interaktif; fitur zoom, tooltip angka, dan overlay volume; memoles antarmuka ponsel.", "rem": "創506"},
        "my": {"prog": "Carta Dinamik: Visual Interaktif", "hw": "Pecutan Projek: Carta candlestick profesional", "sum": "Membina carta kewangan interaktif; zum, petua alat, dan tindanan volum; memperhalusi UI mudah alih.", "rem": "創506"},
        "th": {"prog": "แผนภูมิไดนามิก: การแสดงภาพเชิงโต้ตอบ", "hw": "สปรินต์โครงงาน: กราฟแท่งเทียนระดับมืออาชีพ", "sum": "สร้างแผนภูมิการเงินแบบอินเทอร์แอคทีฟ; ซูมเข้าออก กล่องข้อความเมื่อชี้เมาส์ และกราฟปริมาณซื้อขาย", "rem": "創506"},
        "fr": {"prog": "Graphiques dynamiques : Visuels interactifs", "hw": "Sprint Projet : Chandeliers boursiers pro", "sum": "Conception de graphiques financiers interactifs ; zoom, infobulles et volumes ; finition de l'interface mobile.", "rem": "創506"}
    },
    {
        "week": "Week 15", "date": "2026/12/17",
        "us": {"prog": "AI Ethics, Data Privacy & Security", "hw": "Lab 11: Prompt defense & key safety", "sum": "AI compliance and digital ethics; public vs. confidential data boundaries; API key protection; safe app deployment.", "rem": "創506"},
        "tw": {"prog": "AI 倫理、資料隱私與資安防護", "hw": "Lab 11: 提示詞防禦與金鑰資安實作", "sum": "AI 合規性與數位倫理；公開資訊與商業機密界線；API 金鑰環境變數隱藏安全；安全發布應用。", "rem": "創506"},
        "vn": {"prog": "Đạo đức AI, Quyền riêng tư & Bảo mật dữ liệu", "hw": "Lab 11: Phòng thủ câu lệnh & Bảo vệ khóa", "sum": "Tuân thủ AI và đạo đức kỹ thuật số; ranh giới dữ liệu bí mật kinh doanh; bảo vệ khóa API; triển khai an toàn.", "rem": "創506"},
        "id": {"prog": "Etika AI, Privasi Data & Keamanan Sistem", "hw": "Lab 11: Pertahanan prompt & keamanan kunci", "sum": "Kepatuhan AI dan etika digital; batas rahasia bisnis; perlindungan kunci API; penerapan web yang aman.", "rem": "創506"},
        "my": {"prog": "Etika AI, Privasi Data & Keselamatan", "hw": "Lab 11: Pertahanan prompt & kunci API selamat", "sum": "Pematuhan AI dan etika digital; sempadan rahsia perdagangan; perlindungan kunci API; penyebaran selamat.", "rem": "創506"},
        "th": {"prog": "จริยธรรม AI ความเป็นส่วนตัวและความปลอดภัยข้อมูล", "hw": "Lab 11: ป้องกันการแทรกคำสั่งและรักษาคีย์ API", "sum": "ความสอดคล้องทางกฎหมายและจริยธรรม AI; ขอบเขตความลับทางธุรกิจ; การเก็บรักษาคีย์ API อย่างปลอดภัย", "rem": "創506"},
        "fr": {"prog": "Éthique de l'IA, Données & Cybersécurité", "hw": "TP 11 : Défense de prompt & Clés sécurisées", "sum": "Conformité de l'IA et éthique numérique ; secret des affaires ; protection des clés d'API ; déploiement sécurisé.", "rem": "創506"}
    },
    {
        "week": "Week 16", "date": "2026/12/24",
        "us": {"prog": "Final Project Showcase", "hw": "Final Deliverable: Live Web App", "sum": "In-class project showcase; live demonstration of interactive FinTech web applications; peer feedback and evaluation.", "rem": "Final Demo Day"},
        "tw": {"prog": "【期末成果發表會】專題展示與互評", "hw": "期末交付成果：上線運作 Web App", "sum": "課堂現場專題成果發表會；學生上台現場展示可互動之金融科技 Web 應用程式；同儕互評與回饋交流。", "rem": "成果發表會"},
        "vn": {"prog": "【Báo cáo đồ án cuối kỳ】Trình diễn sản phẩm", "hw": "Sản phẩm bàn giao: Web App trực tuyến", "sum": "Trình bày đồ án trực tiếp trên lớp; demo trực tiếp ứng dụng FinTech có thể tương tác; nhận xét và đánh giá chéo.", "rem": "Demo Day"},
        "id": {"prog": "[Showcase Proyek Akhir] Demo Produk", "hw": "Pengumpulan Akhir: Live Web App", "sum": "Presentasi proyek akhir di kelas; demonstrasi langsung aplikasi web FinTech interaktif; evaluasi rekan sejawat.", "rem": "Demo Day"},
        "my": {"prog": "[Pameran Projek Akhir] Demonstrasi Langsung", "hw": "Penyerahan Akhir: Aplikasi Web Aktif", "sum": "Pembentangan projek akhir dalam kelas; demonstrasi langsung aplikasi web FinTech interaktif; maklum balas rakan sebaya.", "rem": "Hari Demo"},
        "th": {"prog": "【นำเสนอผลงานโครงงานปลายภาค】สาธิตสด", "hw": "ผลงานส่งมอบขั้นสุดท้าย: เว็บแอปที่ใช้งานได้จริง", "sum": "การนำเสนอโครงงานสดในชั้นเรียน; สาธิตการทำงานจริงของเว็บแอปพลิเคชัน FinTech แบบอินเทอร์แอคทีฟ; การประเมินผลโดยเพื่อนร่วมชั้น", "rem": "วันนำเสนอผลงาน"},
        "fr": {"prog": "[Showcase final des projets] Démonstration", "hw": "Livrable final : Application web en ligne", "sum": "Présentation des projets en direct en classe ; démonstrations d'applications FinTech interactives ; retours et évaluation.", "rem": "Demo Day"}
    },
    {
        "week": "Week 17", "date": "2026/12/31",
        "us": {"prog": "Independent Study: FinTech Multimedia", "hw": "Independent project enhancement", "sum": "Self-directed learning per school policy: viewing industry multimedia tutorials; refining code logic and mobile UI.", "rem": "Flexible Learning"},
        "tw": {"prog": "【自主學習活動】FinTech 多媒體研習", "hw": "自主專案程式優化與精進", "sum": "依學校自主學習規定：自主觀看業界多媒體影音教材；持續精進專案程式邏輯與手機排版體驗。", "rem": "自主學習週"},
        "vn": {"prog": "Học tập tự chủ: Đa phương tiện FinTech", "hw": "Nâng cấp dự án độc lập", "sum": "Tự học theo quy định của nhà trường: xem tài liệu video công nghệ tài chính; tinh chỉnh mã nguồn và giao diện di động.", "rem": "Học tập linh hoạt"},
        "id": {"prog": "Studi Mandiri: Multimedia FinTech", "hw": "Penyempurnaan proyek mandiri", "sum": "Pembelajaran mandiri sesuai kebijakan kampus: menonton tutorial video industri; menyempurnakan kode dan UI seluler.", "rem": "Studi Mandiri"},
        "my": {"prog": "Kajian Mandiri: Multimedia FinTech", "hw": "Penambahbaikan projek kendiri", "sum": "Pembelajaran kendiri mengikut dasar universiti: menonton tutorial multimedia industri; memperkemas kod dan UI mudah alih.", "rem": "Pembelajaran Fleksibel"},
        "th": {"prog": "กิจกรรมการเรียนรู้ด้วยตนเอง: มัลติมีเดีย FinTech", "hw": "การปรับปรุงโครงงานด้วยตนเอง", "sum": "การเรียนรู้ตามอัธยาศัยตามนโยบายมหาวิทยาลัย: ศึกษาสื่อมัลติมีเดียอุตสาหกรรม; ขัดเกลาตรรกะโค้ดและ UI มือถือ", "rem": "สัปดาห์เรียนรู้ยืดหยุ่น"},
        "fr": {"prog": "Étude autonome : Multimédia FinTech", "hw": "Amélioration autonome du projet", "sum": "Apprentissage autonome selon les directives de l'université : visionnage de tutoriels industriels ; perfectionnement du code.", "rem": "Apprentissage flexible"}
    },
    {
        "week": "Week 18", "date": "2027/01/07",
        "us": {"prog": "Independent Study: Case Studies & Portfolio", "hw": "Final portfolio submission", "sum": "Self-directed learning per school policy: reviewing AI case studies; submitting final project portfolio.", "rem": "Flexible Learning"},
        "tw": {"prog": "【自主學習活動】AI 商業案例與歷程彙整", "hw": "學期學習歷程檔案最終交付", "sum": "依學校自主學習規定：研讀國際 AI 商業應用案例；彙整並繳交全學期學習歷程檔案。", "rem": "自主學習週"},
        "vn": {"prog": "Học tập tự chủ: Tình huống AI & Hồ sơ", "hw": "Nộp hồ sơ học tập cuối kỳ", "sum": "Tự học theo quy chế: nghiên cứu tình huống kinh doanh AI; hoàn thiện và nộp hồ sơ học tập cả kỳ.", "rem": "Học tập linh hoạt"},
        "id": {"prog": "Studi Mandiri: Studi Kasus AI & Portofolio", "hw": "Pengumpulan portofolio akhir", "sum": "Pembelajaran mandiri sesuai kebijakan kampus: meninjau studi kasus AI; mengumpulkan portofolio belajar akhir.", "rem": "Studi Mandiri"},
        "my": {"prog": "Kajian Mandiri: Kajian Kes AI & Portfolio", "hw": "Penyerahan portfolio akhir", "sum": "Pembelajaran kendiri mengikut dasar: meneliti kajian kes perniagaan AI; mengumpul dan menyerahkan portfolio semester.", "rem": "Pembelajaran Fleksibel"},
        "th": {"prog": "กิจกรรมการเรียนรู้ด้วยตนเอง: กรณีศึกษา AI & พอร์ตโฟลิโอ", "hw": "ส่งแฟ้มสะสมผลงานฉบับสมบูรณ์", "sum": "การเรียนรู้ด้วยตนเองตามนโยบาย: ศึกษากรณีศึกษาทางธุรกิจ AI; รวบรวมและส่งแฟ้มสะสมงานการเรียนรู้ตลอดภาคเรียน", "rem": "สัปดาห์เรียนรู้ยืดหยุ่น"},
        "fr": {"prog": "Étude autonome : Études de cas d'IA & Portfolio", "hw": "Dépôt final du portfolio", "sum": "Apprentissage autonome : étude de cas concrets d'IA dans les affaires ; consolidation et dépôt du portfolio d'apprentissage.", "rem": "Apprentissage flexible"}
    }
]

def get_translated_row(item, code):
    if code in item:
        return item[code]
    return item["us"]

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

with st.expander(schedule_expander_titles.get(current_code, schedule_expander_titles["us"]), expanded=False):
    if hasattr(st, "html"):
        st.html(table_full)
    else:
        st.markdown(table_full, unsafe_allow_html=True)

# ==============================================================================
# 6. 【每週課堂步驟：下方】詳細操作抽屜（Week 1 預設展開 + 多語系健全 Fallback）
# ==============================================================================
st.markdown("---")
expand_section_titles = {
    "us": "🚀 In-Class Practice & Session Breakdown (Click week to expand)",
    "tw": "🚀 課堂實作步驟與上機指引（點擊展開各週）",
    "vn": "🚀 Hướng dẫn thực hành & Chi tiết tiết học (Bấm để mở rộng)",
    "id": "🚀 Panduan Praktik & Rincian Sesi (Klik untuk memperluas)",
    "my": "🚀 Panduan Amali & Pecahan Sesi (Klik untuk buka)",
    "th": "🚀 คำแนะนำการปฏิบัติการในชั้นเรียน (คลิกเพื่อขยาย)",
    "fr": "🚀 Guide de pratique en classe & Séances (Cliquez pour dérouler)"
}
st.markdown(f"### {expand_section_titles.get(current_code, expand_section_titles['us'])}")

# 第一週詳細內容（支援繁中與英文，其他語言自動 fallback 至英文確保零故障）
w1_details = {
    "us": """
    * **Part 1 (09:00 - 09:50) | Concept, Mindset & Portal Tour (Room 506)**
      1. Course orientation, grading policies, and portal overview.
      2. Device Requirements: Bring your **Laptop**, **Smartphone**, and **Transparency Earphones** (for voice prompting!).
      3. Introducing the **Conductor Mindset**: Lead AI with natural language prompts.
    * **Part 2 (10:00 - 10:50) | Cloud Setup, Voice Prompting & Live Demo**
      4. Launching **Google Colab** and testing **Voice Typing / Microphone** in Gemini (Micro-whisper technique).
      5. Instructor live coding: Fetching real-time TSMC (`2330.TW`) stock prices.
    * **Part 3 (11:00 - 11:50) | Lab 0 Milestone & Sidebar Check-in**
      6. **Core Milestone (Lab 0)**: Customize the script for `AAPL` or `SBUX`.
      7. **Mandatory Check-in**: Submit your ID and stock insight via the **sidebar AI Assistant**.
    """,
    "tw": """
    * **Part 1 (09:00 - 09:50) ｜ 觀念引導、指揮家思維與網頁導覽 (創新大樓 506 教室)**
      1. 課程總覽、評量標準（平常 50%、第9週期中 20%、第16週期末發表 30%）與多語系 AI 助教網頁導覽。
      2. 必備設備提醒：每週請務必攜帶 **筆記型電腦** 與 **智慧型手機**。
      3. 建立「指揮家思維 (Conductor Mindset)」：以自然語言提示詞指揮 AI。
    * **Part 2 (10:00 - 10:50) ｜ 雲端環境、鍵盤快捷鍵與台積電 Live Demo**
      4. 登入 **Google Colab** 雲端開發環境（未帶電腦者採兩人結對 Pair Programming）。
      5. 鍵盤快捷鍵暖身與 `Shift + Enter` 執行。
      6. 老師現場示範 4 行 Python 程式碼抓取台積電 (`2330.TW`) 股價。
    * **Part 3 (11:00 - 11:50) ｜ Lab 0 成就解鎖、加碼挑戰與側邊欄打卡**
      7. **核心成就解鎖 (Lab 0)**：成功跑出台積電或自選股票（如蘋果 `AAPL`、星巴克 `SBUX`）的走勢圖。
      8. **加碼挑戰**：嘗試 5 年長線趨勢 (`period="5y"`) 或詢問 Gemini 進行雙資產對比。
      9. **重要打卡 (Check-in)**：請務必將學號、股票代號與觀察心得透過 **左側側邊欄 AI 助教** 送出，作為今日出勤與實作完成證明！
    """
}

shortcuts_info = {
    "us": """
| Action (功能) | Windows | Mac | Description (說明) |
| :--- | :--- | :--- | :--- |
| **Copy (複製)** | `Ctrl + C` | `Cmd ⌘ + C` | Copy code or error message (複製代碼或錯誤訊息) |
| **Paste (貼上)** | `Ctrl + V` | `Cmd ⌘ + V` | Paste code into Gemini (貼入 AI 對話框) |
| **Undo (復原救命鍵)** | `Ctrl + Z` | `Cmd ⌘ + Z` | Undo mistake if code is deleted (手滑刪除代碼時的救命鍵) |
| **Run Cell (執行程式)** | `Shift + Enter` | `Shift + Enter` | Run current Colab block instantly (免按滑鼠直接執行) |
""",
    "tw": """
| 快捷鍵功能 | Windows | Mac | 課堂實戰用途 |
| :--- | :--- | :--- | :--- |
| **複製 (Copy)** | `Ctrl + C` | `Cmd ⌘ + C` | 快速複製 Colab 程式碼或紅字錯誤訊息 |
| **貼上 (Paste)** | `Ctrl + V` | `Cmd ⌘ + V` | 把代碼貼入 Gemini 詢問或貼回 Colab |
| **復原 (Undo 救命鍵)** | `Ctrl + Z` | `Cmd ⌘ + Z` | 不小心按錯或把代碼刪除時的一鍵還原！ |
| **Colab 執行 (Run)** | `Shift + Enter` | `Shift + Enter` | 免用滑鼠按播放鈕，直接執行並跳至下一格 |
"""
}

dual_track_info = {
    "us": """
1. **Primary Track (Colab AI)**: Use the built-in "Generate with AI" button directly inside your notebook cells for quick completion.
2. **Backup Track (Google Gemini)**: Keep `gemini.google.com` open in a second browser tab.
3. **When Colab limit is reached**: Press `Ctrl/Cmd + C` to copy your code & error, switch to Gemini with `Ctrl/Cmd + V`, and ask: *"Explain what went wrong and give me the corrected code."*
""",
    "tw": """
1. **第一軌（Colab 內建 AI）**：直接在儲存格旁邊點擊「使用 AI 產生代碼」，進行即時編寫與自動補齊。
2. **第二軌（Gemini 深度助教）**：在另一個瀏覽器分頁常駐開啟 `gemini.google.com`。
3. **當 Colab 額度用盡或報錯看不懂時**：按下 `Ctrl/Cmd + C` 複製報錯訊息，切換到 Gemini 貼上詢問：*「請幫我解釋這段錯誤並給我修正後的 Python 代碼」*。
"""
}

demo_prompts = {
    "us": {
        "title": "📈 Live Demo: TSMC 4-Line Python & Prompt (Copy to run)",
        "prompt_label": "**Natural Language Prompt (Copy to ask AI)**:",
        "prompt_text": "`Write a Python script using yfinance to download TSMC (2330.TW) stock prices for the past 1 year and plot a closing price line chart.`",
        "code_label": "**Python Code (Click copy icon in top-right / 點擊右上角一鍵複製)**:",
        "caption": "💡 **Execution Guide**: Copy code above ➔ Click Colab button below ➔ Paste (`Ctrl+V` / `Cmd+V`) ➔ Press `Shift + Enter` to run!"
    },
    "tw": {
        "title": "📈 現場 Live Demo：台積電 4 行 Python 程式碼與提示詞（一鍵複製）",
        "prompt_label": "**自然語言提示詞 (可直接複製問 AI)**：",
        "prompt_text": "`請用 Python 的 yfinance 套件，抓取台積電 (2330.TW) 過去一年的股價歷史資料，並畫出收盤價的折線圖。`",
        "code_label": "**Python 程式碼 (點擊右上角小圖示一鍵複製)**：",
        "caption": "💡 **操作步驟**：複製上方代碼 ➔ 點下方按鈕打開 Colab ➔ 貼上 (`Ctrl+V` / `Cmd+V`) ➔ 按下 `Shift + Enter` 立即執行！"
    }
}

# 多語系傳送門按鈕標籤
portal_btn_labels = {
    "us": ("🛠️ Quick Access Links (Week 1)", "🚀 Open Google Colab", "💡 Open Google Gemini (Backup AI)"),
    "tw": ("🛠️ 課堂實作快速傳送門 (第 1 週)", "🚀 打開 Google Colab (雲端筆記本)", "💡 開啟 Google Gemini (AI 助教備用分頁)"),
    "vn": ("🛠️ Đường dẫn truy cập nhanh (Tuần 1)", "🚀 Mở Google Colab", "💡 Mở Google Gemini (AI dự phòng)"),
    "id": ("🛠️ Tautan Akses Cepat (Minggu 1)", "🚀 Buka Google Colab", "💡 Buka Google Gemini (AI Cadangan)"),
    "my": ("🛠️ Pautan Akses Pantas (Minggu 1)", "🚀 Buka Google Colab", "💡 Buka Google Gemini (AI Sandaran)"),
    "th": ("🛠️ ทางลัดเข้าใช้งานด่วน (สัปดาห์ที่ 1)", "🚀 เปิด Google Colab", "💡 เปิด Google Gemini (AI สำรอง)"),
    "fr": ("🛠️ Liens d'accès rapide (Semaine 1)", "🚀 Ouvrir Google Colab", "💡 Ouvrir Google Gemini (IA relais)")
}
cur_btn_meta = portal_btn_labels.get(current_code, portal_btn_labels["us"])

for i in range(1, 19):
    week_title_map = {
        "us": f"Week {i} Detailed Agenda (3-Hour Breakdown)",
        "tw": f"第 {i} 週詳細三節課進行步驟與上機指引",
        "vn": f"Tuần {i} - Chi tiết 3 tiết học",
        "id": f"Minggu {i} - Rincian Sesi",
        "my": f"Minggu {i} - Butiran Sesi",
        "th": f"สัปดาห์ที่ {i} - รายละเอียดบทเรียน",
        "fr": f"Semaine {i} - Détail des séances"
    }
    w_title = week_title_map.get(current_code, week_title_map["us"])
    
    with st.expander(w_title, expanded=(i == 1)):
        if i == 1:
            # 【學習目標與能力清單】
            with st.container(border=True):
                st.markdown("##### 🎯 Week 1 Learning Objectives / 本週學習目標與能力清單")
                st.markdown("""
                By the end of today's session, you will be able to:
                1. 🤖 **Master the Conductor Mindset**: Lead AI with natural language prompts and voice-typing without memorizing syntax.
                2. 💻 **Launch Cloud Python**: Set up Google Colab, execute your first 4-line financial script, and handle keyboard shortcuts.
                3. 📈 **Fetch Real-World Data**: Pull real-time stock prices (TSMC / Apple) using `yfinance` and plot closing price trends.
                4. 🚀 **Complete Digital Check-in**: Submit your lab milestone and insights via the sidebar AI Assistant to record your attendance.
                
                *(🎯 Self-Check: Make sure you have completed all 4 items above and checked in via the sidebar!)*
                """)

            st.markdown("---")
            
            # 第一週詳細步驟
            st.markdown(w1_details.get(current_code, w1_details["us"]))
            
            # 1. 快捷鍵速查
            with st.expander("⚡ Keyboard Shortcuts Cheat Sheet (Windows & Mac 快捷鍵速查表)", expanded=False):
                st.markdown(shortcuts_info.get(current_code, shortcuts_info["us"]))
                
            # 2. 雙軌 AI 指引
            with st.expander("💡 Dual-Track AI Workflow Guide (雙軌 AI 實作工作流指引)", expanded=False):
                st.markdown(dual_track_info.get(current_code, dual_track_info["us"]))

            # 3. Live Demo 程式碼與 Prompt 快速複製區 (英文為主，中文為輔)
            with st.expander("📈 Live Demo: TSMC 4-Line Python & Prompt (台積電 Live Demo 程式碼與提示詞)", expanded=True):
                st.markdown("**Natural Language Prompt / 自然語言提示詞 (Copy to ask AI):**")
                st.code("Write a Python script using yfinance to download TSMC (2330.TW) stock prices for the past 1 year and plot a closing price line chart.", language="text")
                
                st.markdown("**Python Code / Python 程式碼 (Click copy icon in top-right / 點擊右上角一鍵複製):**")
                demo_code = """# 1. Install and import market data package
!pip install yfinance
import yfinance as yf

# 2. Download TSMC (2330.TW) 1-year historical prices and plot trend
df = yf.download("2330.TW", period="1y")
df['Close'].plot(title="TSMC (2330.TW) - 1 Year Trend", figsize=(10, 5), grid=True)
"""
                st.code(demo_code, language="python")
                st.caption("💡 **Execution Guide / 操作指引**: Copy code above ➔ Click Colab button below ➔ Paste (`Ctrl+V` / `Cmd+V`) ➔ Press `Shift + Enter` to run!")

            # 4. 商業與經濟延伸思考題 (Business & Economics Reflection)
            with st.expander("🧠 Business & Economics Thinking / 跨學科商業思考題 (結合經濟與會計)", expanded=False):
                reflection_markdown = (
                    "Run your code, observe the charts, and connect back to what you learned in freshman year:\n\n"
                    "* **Question 1 (Economics & Market Shock / 經濟學供需震撼)**:  \n"
                    "  *Look at the soaring trend of TSMC (2330.TW). How does the explosion of Generative AI create a massive structural **demand shock** in the global semiconductor supply chain?*  \n"
                    "  *(觀察台積電飆升的曲線：生成式 AI 爆發如何對全球半導體供應鏈帶來巨大的結構性供需衝擊？)*\n\n"
                    "* **Question 2 (Accounting & Business Models / 會計營收結構對比)**:  \n"
                    "  *Why does TSMC's B2B infrastructure business model (selling to tech giants) behave so differently from Apple or Starbucks' B2C model (selling to consumers facing inflation)?*  \n"
                    "  *(台積電面向科技巨頭的 B2B 資本支出模式，與蘋果、星巴克直接受通膨影響的 B2C 消費支出模式，在財報營收成長性上有何本質不同？)*\n\n"
                    "* **Question 3 (The Power of Pair Work / 人機與結對協作)**:  \n"
                    "  *Why is having a partner (Pair Programming) far more effective than coding alone when directing AI agents?*  \n"
                    "  *(在 AI 時代，為什麼一人負責商業邏輯、一人把關代碼的雙人協作，能大幅降低決策盲點？)*"
                )
                st.markdown(reflection_markdown)

            # 5. 一鍵推薦給同學 (Share with Classmates - English First & Open to All Majors/International Students)
            with st.expander("📢 Invite Classmates / Share Course (Open to ALL Majors & International Students)", expanded=False):
                st.markdown("**Copy and forward this message to your class or international student LINE groups:**")
                share_text = (
                    "🔥 [Elective Course Recommendation: Python AI Applications]\n"
                    "No complex coding syntax required! Learn how to direct AI with natural language prompts, fetch real-time TSMC & US stock data, and build mobile Web Apps!\n"
                    "• **Language**: English-taught (ideal for international students), with supplementary Chinese guidance (課程主要以英文講授，並輔以中文說明)。If you need support for any specific national language, please feel free to leave a message in the TA section (若有需要增加國家語言，也歡迎在助教區留言)。\n"
                    "• **Eligibility**: Open to ALL majors, year levels, and graduate/undergraduate students across the university—both local and international students are warmly welcomed!\n"
                    "• **Format**: Beginner-friendly with Pair Programming (teams of 1-3)\n"
                    "• **Required Gear**: Laptop and Smartphone (A headset with a microphone is recommended but optional).\n\n"
                    "📍 Time: Every Thursday 09:00 - 11:50 (Room 506, Innovation Bldg)\n"
                    "🔗 Syllabus Portal: https://ai-syllabus.streamlit.app/\n"
                    "💬 LINE Community Group:\n"
                    "https://line.me/ti/g2/LUyGiu6JVuGP9MQ2leJRbjn7zhEj-G55qGiGog\n"
                    "Join us during the Add/Drop week! 🚀"
                )
                st.code(share_text, language="text")
                st.caption("💡 Forward this text to your student group chats to invite friends from any department!")
                
            # 6. 【永遠保留】Google Colab 與 Gemini 快速傳送門按鈕
            st.markdown("---")
            st.markdown(f"#### {cur_btn_meta[0]}")
            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                st.link_button(cur_btn_meta[1], "https://colab.research.google.com/", use_container_width=True)
            with btn_col2:
                st.link_button(cur_btn_meta[2], "https://gemini.google.com/", use_container_width=True)
        else:
            placeholders = {
                "us": f"Detailed session breakdown for Week {i} is coming soon. Stay tuned!",
                "tw": f"第 {i} 週的詳細三節課 1-5 點操作指引正在準備中，敬請期待！",
                "vn": f"Chi tiết cho Tuần {i} sẽ sớm được cập nhật.",
                "id": f"Rincian untuk Minggu {i} akan segera hadir.",
                "my": f"Butiran untuk Minggu {i} akan dikemas kini.",
                "th": f"รายละเอียดของสัปดาห์ที่ {i} จะอัปเดตเร็วๆ นี้",
                "fr": f"Le détail de la semaine {i} sera bientôt disponible."
            }
            st.info(placeholders.get(current_code, placeholders["us"]))

# ==============================================================================
# 7. 側邊欄：多語系 AI 助教 + Google Sheets 自動同步
# ==============================================================================
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

    user_q = st.text_input(
        "💬 填寫今日成就與心得 (例如: 成功跑出 AAPL 走勢，最高價約 230):", 
        placeholder="請輸入你的股票代號與觀察心得..."
    )
    
    if st.button(ui_texts["btn_submit"].get(current_code, "🚀 Submit"), use_container_width=True):
        if user_q:
            now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            q_lower = user_q.lower()
            
            if any(k in q_lower for k in ["đồ án", "cuối kỳ", "báo cáo", "final", "project", "showcase", "期末", "專案", "tugas akhir", "projek akhir", "โครงงาน"]):
                category = "Final Project"
                local_answers = {
                    "us": "The Final Project Showcase takes place in **Week 16 (Dec 24)**. Weeks 17 & 18 are flexible independent learning. It counts for **30%** of your final grade.",
                    "tw": "期末專案成果發表將於 **第 16 週 (12/24)** 課堂舉行（第 17-18 週為學校彈性自主學習），佔學期總成績 **30%**。",
                    "vn": "Đồ án cuối kỳ sẽ báo cáo vào **Tuần 16 (24/12)** (Tuần 17-18 là tự học linh hoạt), chiếm **30%** tổng điểm môn học.",
                    "id": "Presentasi Proyek Akhir berlangsung pada **Minggu ke-16 (24 Des)**, berbobot **30%** dari nilai akhir.",
                    "my": "Pembentangan Projek Akhir diadakan pada **Minggu ke-16 (24 Dis)**, menyumbang **30%** markah akhir.",
                    "th": "การนำเสนอโครงงานปลายภาคจะมีขึ้นใน **สัปดาห์ที่ 16 (24 ธ.ค.)** โดยคิดเป็น **30%** ของเกรดรวม",
                    "fr": "La présentation des projets finaux aura lieu en **semaine 16 (24 déc.)** (30% de la note finale)."
                }
                zh_summary = "詢問期末專案發表時程與佔比"
                en_broadcast = "The Final Project Showcase is in Week 16 (Dec 24) (30% of total grade)."

            elif any(k in q_lower for k in ["điểm", "grade", "score", "tỷ lệ", "評分", "成績", "比重", "nilai", "markah", "เกณฑ์", "คะแนน", "note"]):
                category = "Grading"
                local_answers = {
                    "us": "Grading: Weekly in-class practice (50%), Midterm W9 (20%), Final showcase W16 (30%).",
                    "tw": "評量標準：每週課堂趣味實作 50%、期中考/專案 20%、第 16 週期末成果展示 30%。",
                    "vn": "Tiêu chí chấm điểm: Thực hành trên lớp 50%, Giữa kỳ 20%, Đồ án cuối kỳ 30%.",
                    "id": "Penilaian: Praktik mingguan 50%, UTS 20%, Proyek akhir 30%.",
                    "my": "Pemarkahan: Amali mingguan 50%, Pertengahan penggal 20%, Projek akhir 30%.",
                    "th": "เกณฑ์คะแนน: แบบฝึกหัดในชั้นเรียน 50%, กลางภาค 20%, โครงงานปลายภาค 30%",
                    "fr": "Évaluation : Pratique en classe 50%, Partiel 20%, Projet final 30%."
                }
                zh_summary = "詢問課程評分比重"
                en_broadcast = "Grading policy: 50% weekly practice, 20% midterm, 30% final showcase."

            elif any(k in q_lower for k in ["colab", "bắt đầu", "python", "lập trình", "cài đặt", "環境", "instalasi", "ติดตั้ง", "installation"]):
                category = "Environment / Tools"
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
                category = "General / Consultation"
                local_answers = {
                    "us": f"Your question has been noted: '{user_q}'. Feel free to discuss with the instructor right after class in Room 506!",
                    "tw": f"已收到您的提問：『{user_q}』。下課後可於 506 教室與老師進一步討論！",
                    "vn": f"Câu hỏi của bạn: '{user_q}' đã được ghi nhận. Bạn có thể trao đổi với giảng viên sau giờ học tại Phòng 506!",
                    "id": f"Pertanyaan Anda: '{user_q}' telah dicatat. Silakan berdiskusi di Ruang 506 setelah kelas!",
                    "my": f"Soalan anda: '{user_q}' telah direkodkan. Sila berbincang selepas kelas di Bilik 506!",
                    "th": f"บันทึกคำถามของคุณแล้ว: '{user_q}' สามารถสอบถามกับผู้สอนได้ที่ห้อง 506 หลังเลิกเรียน",
                    "fr": f"Votre question a bien été notée : '{user_q}'. N'hésitez pas à en parler en salle 506 après le cours !"
                }
                zh_summary = f"學生提問：{user_q}"
                en_broadcast = "Feel free to ask questions after class in Room 506 or in our class chat group."

            webhook_url = "https://script.google.com/macros/s/AKfycbyep8yXuTaNgnAxKsdRXgsqJvYKAeqCmDiF2GqvUkJWf-7sCztuQ4n7cbkpbzyyYod4/exec"
            payload = {
                "timestamp": now_str,
                "student": final_student_id,
                "language": LANG_CONFIG[current_code]["label"],
                "question": user_q,
                "summary": zh_summary,
                "category": category
            }

            try:
                requests.post(webhook_url, json=payload, timeout=5)
            except Exception:
                pass

            st.success("✅ Recorded! / 已記錄並同步至課堂試算表")
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
