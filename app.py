# ==============================================================================
# [Script] Interactive Multilingual Syllabus & Course Info Web Application
# 【腳本】多語系互動課綱與完整課程資訊（含教務系統目標、評分、教材、Office Hour）
# ==============================================================================

import streamlit as st

# 1. 頁面基本配置
st.set_page_config(
    page_title="Python AI Applications - Syllabus",
    layout="wide",
    page_icon="🎓"
)

# 2. 標題與副標題
st.title("🎓 Python AI Applications (Python AI 應用)")
st.caption("115 學期 四技經管系2丙 (3.0 學分 / 3.0 時數) | Interactive Syllabus & Parallel Multilingual Companion")

# 3. 語言定義與切換設定
LANG_CONFIG = {
    "tw": {"label": "繁體中文", "name": "🇹🇼 繁體中文 (Traditional Chinese)", "flag": "https://flagcdn.com/w40/tw.png"},
    "us": {"label": "English", "name": "🇺🇸 English (Official)", "flag": "https://flagcdn.com/w40/us.png"},
    "vn": {"label": "Tiếng Việt", "name": "🇻🇳 Tiếng Việt (Vietnamese)", "flag": "https://flagcdn.com/w40/vn.png"},
    "my": {"label": "B. Melayu", "name": "🇲🇾 Bahasa Melayu (Malay)", "flag": "https://flagcdn.com/w40/my.png"},
    "id": {"label": "B. Indonesia", "name": "🇮🇩 Bahasa Indonesia (Indonesian)", "flag": "https://flagcdn.com/w40/id.png"},
    "th": {"label": "ภาษาไทย", "name": "🇹🇭 ภาษาไทย (Thai)", "flag": "https://flagcdn.com/w40/th.png"},
    "fr": {"label": "Français", "name": "🇫🇷 Français (French)", "flag": "https://flagcdn.com/w40/fr.png"}
}

current_code = st.query_params.get("lang", "tw")
if current_code not in LANG_CONFIG:
    current_code = "tw"

current_info = LANG_CONFIG[current_code]

# 自訂 CSS：按鈕底色、微陰影、國旗防融色微灰外框
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

st.markdown("**🌐 Select Parallel Language (點擊按鈕切換右欄對照語言):**")

# 7 國語言按鈕列
btn_items = "".join([
    f'<a class="flag-btn {"active" if code == current_code else ""}" href="?lang={code}" target="_self"><img class="flag-img" src="{data["flag"]}" alt="{data["label"]}"><span>{data["label"]}</span></a>'
    for code, data in LANG_CONFIG.items()
])
st.markdown(f'<div class="flag-btn-grid">{btn_items}</div>', unsafe_allow_html=True)

st.info(f"💡 **Current Parallel View / 目前對照語言**: **{current_info['name']}**  \n*(Conductor's Note: Built with Python & Streamlit in under 120 lines. You will build and deploy apps like this in Week 10!)*")

# 4. 教務系統基本資訊（支援 7 國語言對照）
meta_info = {
    "goal": {
        "en": "**Course Objectives**  \nConnect what you learned in freshman Accounting and Economics, and get strong help for your sophomore Statistics, Marketing, and Management classes. Together, we will make interactive business charts and launch real web apps on your phone.\n\n*No tech background needed. If you can ask a question, you can create with AI. Everyone is warmly welcome!*",
        "tw": "**教學目標**  \n串聯大一所學的會計與經濟學基礎，並為大二的統計、行銷與管理課程提供強力支援。我們將一起打造互動商業圖表，並將真實的 Web 應用程式發布到您的手機上。\n\n*無須任何技術背景。只要您會提問，就能與 AI 共同創造。誠摯歡迎每位同學！*",
        "vn": "**Mục tiêu môn học**  \nKết nối kiến thức Kế toán và Kinh tế học năm nhất, hỗ trợ đắc lực cho các môn Thống kê, Marketing và Quản trị năm hai. Chúng ta sẽ cùng nhau tạo các biểu đồ kinh doanh tương tác và triển khai ứng dụng web thực tế ngay trên điện thoại.\n\n*Không yêu cầu nền tảng kỹ thuật. Chỉ cần biết đặt câu hỏi, bạn có thể sáng tạo cùng AI!*",
        "ms": "**Objektif Kursus**  \nMenghubungkan apa yang dipelajari dalam Perakaunan dan Ekonomi tahun pertama, serta menyokong kursus Statistik, Pemasaran, dan Pengurusan tahun kedua. Bersama-sama, kita akan membina carta perniagaan interaktif dan melancarkan aplikasi web terus pada telefon pintar anda.\n\n*Tiada latar belakang teknologi diperlukan. Jika anda boleh bertanya soalan, anda boleh mencipta dengan AI!*",
        "id": "**Tujuan Pembelajaran**  \nMenghubungkan Akuntansi dan Ekonomi tingkat satu, serta mendukung mata kuliah Statistik, Pemasaran, dan Manajemen tingkat dua. Bersama-sama, kita akan membuat grafik bisnis interaktif dan merilis aplikasi web nyata langsung di ponsel Anda.\n\n*Tidak memerlukan latar belakang teknis. Jika Anda bisa bertanya, Anda bisa berkreasi dengan AI!*",
        "th": "**วัตถุประสงค์ของรายวิชา**  \nเชื่อมโยงความรู้พื้นฐานด้านบัญชีและเศรษฐศาสตร์ปี 1 และสนับสนุนวิชาสถิติ การตลาด และการจัดการในปี 2 เราจะร่วมกันสร้างแผนภูมิธุรกิจแบบอินเทอร์แอคทีฟและเปิดตัวเว็บแอปพลิเคชันจริงบนสมาร์ตโฟนของคุณ\n\n*ไม่จำเป็นต้องมีพื้นฐานด้านเทคโนโลยี เพียงแค่ตั้งคำถาม คุณก็สร้างสรรค์ผลงานร่วมกับ AI ได้!*",
        "fr": "**Objectifs pédagogiques**  \nFaire le pont avec la comptabilité et l'économie de 1ère année, tout en renforçant vos acquis pour les cours de statistiques, marketing et gestion de 2e année. Ensemble, nous créerons des graphiques interactifs et déploierons de réelles applications web accessibles sur votre smartphone.\n\n*Aucun prérequis technique nécessaire. Si vous savez poser une question, vous pouvez créer avec l'IA !*"
    },
    "grading": {
        "en": "**Grading Policy**  \n* **Weekly In-Class Fun Practice**: 50%\n* **Midterm Exam or Project**: 20%\n* **Final Project Report & Showcase**: 30%  \n*(Step-by-step guidance in class. Beginners are welcome!)*",
        "tw": "**成績評量標準**  \n* **每週課堂趣味實作練習**：50%\n* **期中測驗或專題**：20%\n* **期末專案報告與成果發表**：30%  \n*(課堂提供步驟引導，無基礎者亦可安心參與！)*",
        "vn": "**Tiêu chí đánh giá**  \n* **Thực hành vui trên lớp hàng tuần**: 50%\n* **Thi giữa kỳ hoặc Đồ án**: 20%\n* **Báo cáo và Trình bày Đồ án cuối kỳ**: 30%  \n*(Có hướng dẫn chi tiết từng bước, hoàn toàn phù hợp với người mới bắt đầu!)*",
        "ms": "**Dasar Pemarkahan**  \n* **Latihan Amali Mingguan di Kelas**: 50%\n* **Peperiksaan Pertengahan Semester / Projek**: 20%\n* **Laporan & Pembentangan Projek Akhir**: 30%  \n*(Panduan langkah demi langkah disediakan. Sangat mesra pemula!)*",
        "id": "**Kebijakan Penilaian**  \n* **Praktik Menyenangkan Mingguan di Kelas**: 50%\n* **Ujian Tengah Semester / Proyek**: 20%\n* **Laporan & Presentasi Proyek Akhir**: 30%  \n*(Bimbingan langkah demi langkah di kelas. Sangat ramah pemula!)*",
        "th": "**เกณฑ์การประเมินผล**  \n* **แบบฝึกหัดในชั้นเรียนรายสัปดาห์**: 50%\n* **การสอบกลางภาคหรือโครงงาน**: 20%\n* **รายงานโครงงานปลายภาคและการนำเสนอ**: 30%  \n*(มีการชี้แนะทีละขั้นตอนในชั้นเรียน ยินดีต้อนรับผู้เริ่มต้นอย่างอบอุ่น!)*",
        "fr": "**Modalités d'évaluation**  \n* **Exercices pratiques hebdomadaires en classe** : 50%\n* **Examen ou projet de mi-semestre** : 20%\n* **Rapport et soutenance du projet final** : 30%  \n*(Accompagnement pas à pas en classe. Débutants les bienvenus !)*"
    },
    "office_hour": {
        "en": "**Office Hours**  \nI do not have an office on campus. You can talk to me directly right after class, or message me in our class chat group to set up a time to meet on campus.",
        "tw": "**課業輔導時間 (Office Hour)**  \n授課教師在校內無專屬研究室。同學可在每週下課後直接於教室討論交流，或於班級聯絡群組中預約校內諮詢時間。",
        "vn": "**Giờ tư vấn (Office Hours)**  \nGiảng viên không có văn phòng cố định trong khuôn viên trường. Sinh viên có thể trao đổi trực tiếp ngay sau giờ học, hoặc nhắn tin trong nhóm lớp để hẹn thời gian gặp gỡ trên trường.",
        "ms": "**Waktu Konsultasi (Office Hours)**  \nPensyarah tidak mempunyai pejabat di kampus. Pelajar boleh berbincang terus selepas kelas tamat, atau menghantar mesej dalam kumpulan perbualan kelas untuk menetapkan masa pertemuan.",
        "id": "**Jam Konsultasi (Office Hours)**  \nDosen tidak memiliki ruang kerja pribadi di kampus. Mahasiswa dapat berdiskusi langsung setelah kelas selesai, atau mengirim pesan melalui grup kelas untuk mengatur jadwal pertemuan di kampus.",
        "th": "**ช่วงเวลาให้คำปรึกษา (Office Hours)**  \nผู้สอนไม่มีห้องพักส่วนตัวในมหาวิทยาลัย นักศึกษาสามารถพูดคุยได้โดยตรงทันทีหลังเลิกเรียน หรือส่งข้อความนัดหมายเวลาในกลุ่มสนทนาของชั้นเรียน",
        "fr": "**Heures de permanence (Office Hours)**  \nJe ne dispose pas de bureau dédié sur le campus. Vous pouvez échanger avec moi directement à la fin de chaque cours, ou m'envoyer un message sur le groupe de classe pour convenir d'un rendez-vous sur le campus."
    },
    "materials": {
        "en": "**Textbooks & Open Resources**  \n* **Open Access Materials & Platforms**:\n  1. Google Colab (`colab.research.google.com`)\n  2. Google AI Studio (`aistudio.google.com`)\n  3. Streamlit Documentation (`docs.streamlit.io`)\n  4. FRED Economic Data (`fred.stlouisfed.org`)\n* **References**:\n  1. McKinney, W., *Python for Data Analysis*, 3rd ed., O'Reilly Media, 2022.\n  2. Bodie, Z., Kane, A., & Marcus, A., *Investments*, 13th ed., McGraw-Hill, 2023.\n  3. Mankiw, N. G., *Principles of Economics*, 10th ed., Cengage Learning, 2023.",
        "tw": "**教材與實用雲端平台**  \n* **開放實作平台與資源**：\n  1. Google Colab 雲端開發環境\n  2. Google AI Studio 模型調度平台\n  3. Streamlit 官方開發文件\n  4. FRED 聖路易斯聯邦準備銀行總體經濟資料庫\n* **重要參考書籍**：\n  1. McKinney, W., *Python for Data Analysis*, 3rd ed. (2022)\n  2. Bodie, Kane, Marcus, *Investments*, 13th ed. (2023)\n  3. Mankiw, N. G., *Principles of Economics*, 10th ed. (2023)",
        "vn": "**Tài liệu & Nền tảng thực hành mở**  \n* **Nền tảng mở**:\n  1. Google Colab | 2. Google AI Studio | 3. Streamlit Docs | 4. Dữ liệu kinh tế FRED\n* **Sách tham khảo**:\n  1. McKinney, *Python for Data Analysis*, 3rd ed. (2022)\n  2. Bodie et al., *Investments*, 13th ed. (2023)\n  3. Mankiw, *Principles of Economics*, 10th ed. (2023)",
        "ms": "**Bahan Kursus & Platform Terbuka**  \n* **Platform Terbuka**:\n  1. Google Colab | 2. Google AI Studio | 3. Dokumentasi Streamlit | 4. Data Ekonomi FRED\n* **Rujukan**:\n  1. McKinney, *Python for Data Analysis*, 3rd ed. (2022)\n  2. Bodie et al., *Investments*, 13th ed. (2023)\n  3. Mankiw, *Principles of Economics*, 10th ed. (2023)",
        "id": "**Materi Kuliah & Platform Terbuka**  \n* **Platform Terbuka**:\n  1. Google Colab | 2. Google AI Studio | 3. Dokumentasi Streamlit | 4. Data Ekonomi FRED\n* **Referensi**:\n  1. McKinney, *Python for Data Analysis*, 3rd ed. (2022)\n  2. Bodie et al., *Investments*, 13th ed. (2023)\n  3. Mankiw, *Principles of Economics*, 10th ed. (2023)",
        "th": "**สื่อการสอนและแพลตฟอร์มคลาวด์แบบเปิด**  \n* **แพลตฟอร์มที่ใช้**:\n  1. Google Colab | 2. Google AI Studio | 3. เอกสาร Streamlit | 4. ฐานข้อมูลเศรษฐกิจ FRED\n* **หนังสืออ้างอิง**:\n  1. McKinney, *Python for Data Analysis*, 3rd ed. (2022)\n  2. Bodie et al., *Investments*, 13th ed. (2023)\n  3. Mankiw, *Principles of Economics*, 10th ed. (2023)",
        "fr": "**Supports et Plateformes Ouvertes**  \n* **Plateformes pratiques** :\n  1. Google Colab | 2. Google AI Studio | 3. Documentation Streamlit | 4. Données économiques FRED\n* **Ouvrages de référence** :\n  1. McKinney, *Python for Data Analysis*, 3e éd. (2022)\n  2. Bodie et al., *Investments*, 13e éd. (2023)\n  3. Mankiw, *Principles of Economics*, 10e éd. (2023)"
    }
}

# 5. 課表週次資料庫
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

# 6. 雙欄並列呈現完整資訊
col_en, col_trans = st.columns(2)

# 左欄：官方英文
with col_en:
    st.subheader("🇺🇸 Official English")
    
    with st.container(border=True):
        st.markdown("### 🎯 Course Objectives")
        st.markdown(meta_info["goal"]["en"])
        
    with st.container(border=True):
        st.markdown("### 📊 Grading Policy")
        st.markdown(meta_info["grading"]["en"])
        
    with st.container(border=True):
        st.markdown("### 📚 Textbooks & Cloud Platforms")
        st.markdown(meta_info["materials"]["en"])
        
    with st.container(border=True):
        st.markdown("### 🕒 Office Hours")
        st.markdown(meta_info["office_hour"]["en"])
        
    st.markdown("---")
    st.markdown("### 🗓️ Weekly Syllabus Breakdown")
    for item in weeks_data:
        with st.container(border=True):
            st.markdown(f"**{item['wk']}**")
            st.markdown(item["en"])

# 右欄：選取的對照語言
with col_trans:
    st.subheader(f"{current_info['name']}")
    
    with st.container(border=True):
        st.markdown("### 🎯 教學目標 / Course Objectives")
        st.markdown(meta_info["goal"].get(current_code, meta_info["goal"]["tw"]))
        
    with st.container(border=True):
        st.markdown("### 📊 評量標準 / Grading Policy")
        st.markdown(meta_info["grading"].get(current_code, meta_info["grading"]["tw"]))
        
    with st.container(border=True):
        st.markdown("### 📚 教材與開放資源 / Materials")
        st.markdown(meta_info["materials"].get(current_code, meta_info["materials"]["tw"]))
        
    with st.container(border=True):
        st.markdown("### 🕒 課業輔導時間 / Office Hours")
        st.markdown(meta_info["office_hour"].get(current_code, meta_info["office_hour"]["tw"]))
        
    st.markdown("---")
    st.markdown("### 🗓️ 週次課綱對照 / Weekly Schedule")
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
            st.markdown(f"**{item['wk']} (對照)**")
            st.markdown(trans_text)
