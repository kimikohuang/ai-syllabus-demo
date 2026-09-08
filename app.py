# 1. 讀取目前的語言參數（預設 us 英文）
current_code = st.query_params.get("lang", "us")
if current_code not in LANG_CONFIG:
    current_code = "us"

current_info = LANG_CONFIG[current_code]

# 2. 副標題多語系對照字典
SUBTITLES = {
    "us": "Fall 2026 (Semester 115-1) · Dept. of Business Administration 2C (3.0 Credits / 3.0 Hours) | Interactive Multilingual Syllabus Portal",
    "tw": "115 學期 四技經管系2丙 (3.0 學分 / 3.0 時數) | 互動式多語系完整課程進度表與資訊門戶",
    "vn": "Học kỳ 115-1 · Khoa Quản trị Kinh doanh 2C (3.0 Tín chỉ / 3.0 Giờ) | Cổng thông tin & Đề cương môn học đa ngữ",
    "id": "Semester 115-1 · Jurusan Administrasi Bisnis 2C (3.0 SKS / 3.0 Jam) | Portal Silabus Multibahasa Interaktif",
    "my": "Semester 115-1 · Jabatan Pengurusan Perniagaan 2C (3.0 Kredit / 3.0 Jam) | Portal Sukatan Pelajaran Interaktif Pelbagai Bahasa",
    "th": "ภาคการศึกษา 115-1 · ภาควิชาบริหารธุรกิจ 2C (3.0 หน่วยกิต / 3.0 ชั่วโมง) | พอร์ทัลประมวลรายวิชาแบบโต้ตอบหลายภาษา",
    "fr": "Semestre 115-1 · Dép. Gestion des Affaires 2C (3.0 Crédits / 3.0 Heures) | Portail Interactif Multilingue du Syllabus"
}

# 3. 渲染動態副標題
st.caption(SUBTITLES.get(current_code, SUBTITLES["us"]))
