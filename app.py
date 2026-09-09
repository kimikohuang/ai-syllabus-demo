# ==============================================================================
# 6. 【學期藍圖】18 週課程完整大表格（摺疊收納版）
# ==============================================================================
st.markdown("---")
schedule_expander_titles = {
    "us": "🗓️ View Full 18-Week Syllabus Breakdown (Click to Expand)",
    "tw": "🗓️ 查看完整 18 週課程進度總表（點擊展開查閱）",
    "vn": "🗓️ Xem toàn bộ lịch trình 18 tuần (Bấm để mở rộng)",
    "id": "🗓️ Lihat Silabus Lengkap 18 Minggu (Klik untuk Memperluas)",
    "my": "🗓️ Lihat Sukatan Pelajaran Penuh 18 Minggu (Klik untuk Buka)",
    "th": "🗓️ ดูแผนการสอนฉบับสมบูรณ์ 18 สัปดาห์ (คลิกเพื่อขยาย)",
    "fr": "🗓️ Consulter le calendrier complet sur 18 semaines (Cliquez pour dérouler)"
}

weeks_all = [
    {
        "week": "Week 1", "date": "2026/09/10",
        "us": {"prog": "Course Onboarding & Vibe Coding", "hw": "Lab 0: In-class fun exploration", "sum": "Course overview; prompt-driven programming with natural language; Google Colab setup; conductor mindset.", "rem": "In-person"},
        "tw": {"prog": "課程導覽與自然語言編程", "hw": "Lab 0: 課堂趣味實作探索", "sum": "課程總覽；自然語言提示詞編程；Colab 環境配置；指揮家思維建立。", "rem": "實體上課"},
        "vn": {"prog": "Khởi động khóa học & Vibe Coding", "hw": "Lab 0: Khám phá thú vị tại lớp", "sum": "Tổng quan môn học; lập trình bằng câu lệnh tự nhiên; cài đặt Google Colab; tư duy nhạc trưởng.", "rem": "Học trực tiếp"},
        "id": {"prog": "Pengenalan Kursus & Vibe Coding", "hw": "Lab 0: Eksplorasi seru di kelas", "sum": "Tinjauan kursus; pemrograman berbasis prompt bahasa alami; pengaturan Colab; pola pikir konduktor.", "rem": "Tatap muka"},
        "my": {"prog": "Pengenalan Kursus & Vibe Coding", "hw": "Lab 0: Penerokaan menarik dalam kelas", "sum": "Gambaran keseluruhan kursus; pengaturcaraan bahasa semula jadi; persediaan Colab; minda konduktor.", "rem": "Bersemuka"},
        "th": {"prog": "ปฐมนิเทศรายวิชา & Vibe Coding", "hw": "Lab 0: กิจกรรมสำรวจในชั้นเรียน", "sum": "ภาพรวมวิชา; การเขียนโค้ดด้วยภาษาธรรมชาติผ่านข้อความพร้อมต์; ติดตั้ง Colab; ปลูกฝังแนวคิดผู้นำคำสั่ง", "rem": "เรียนในชั้น"},
        "fr": {"prog": "Introduction au cours & Vibe Coding", "hw": "Lab 0 : Découverte pratique en classe", "sum": "Présentation générale ; programmation en langage naturel ; configuration Colab ; posture de chef d'orchestre.", "rem": "Présentiel"}
    },
    {
        "week": "Week 2", "date": "2026/09/17",
        "us": {"prog": "Market Data Engineering: Apple & TSMC", "hw": "In-class live practice", "sum": "Add/drop period; fetching daily stock prices with Python; DataFrame processing; visual trend charts.", "rem": "In-person"},
        "tw": {"prog": "市場數據工程：台積電與蘋果", "hw": "課堂即時實作與練習", "sum": "加退選期間；Python 擷取每日股價；資料表 DataFrame 處理與繪製走勢圖。", "rem": "實體上課"},
        "vn": {"prog": "Kỹ thuật dữ liệu thị trường: Apple & TSMC", "hw": "Thực hành trực tiếp trên lớp", "sum": "Thu thập giá cổ phiếu hàng ngày với Python; xử lý DataFrame; biểu đồ xu hướng trực quan.", "rem": "Học trực tiếp"},
        "id": {"prog": "Rekayasa Data Pasar: Apple & TSMC", "hw": "Latihan langsung di kelas", "sum": "Periode tambah/batal matkul; mengambil harga saham harian dengan Python; manipulasi DataFrame; grafik tren visual.", "rem": "Tatap muka"},
        "my": {"prog": "Kejuruteraan Data Pasaran: Apple & TSMC", "hw": "Latihan langsung dalam kelas", "sum": "Tempoh tambah/gugur kursus; mengambil data harga saham harian; manipulasi DataFrame; carta trend visual.", "rem": "Bersemuka"},
        "th": {"prog": "วิศวกรรมข้อมูลตลาด: Apple & TSMC", "hw": "ฝึกปฏิบัติตามสดในชั้นเรียน", "sum": "ช่วงเพิ่ม-ถอนรายวิชา; ดึงข้อมูลราคาหุ้นรายวันด้วย Python; ประมวลผลตาราง DataFrame; แผนภูมิแนวโน้ม", "rem": "เรียนในชั้น"},
        "fr": {"prog": "Ingénierie des données de marché : Apple & TSMC", "hw": "Exercice guidé en classe", "sum": "Période d'ajustement ; extraction de cours boursiers avec Python ; manipulation de DataFrame ; graphiques.", "rem": "Présentiel"}
    },
    {
        "week": "Week 3", "date": "2026/09/24",
        "us": {"prog": "Global EV Trends: Tesla vs. Leaders", "hw": "Lab 1: EV trends notebook", "sum": "Roster finalized; comparing global EV leaders and supply chain; calculating daily returns and volatility.", "rem": "In-person"},
        "tw": {"prog": "全球電動車趨勢：Tesla 與全球車廠", "hw": "Lab 1: 電動車趨勢筆記本", "sum": "選課名單確定；全球電動車供應鏈與龍頭對比；計算日報酬率與波動度指標。", "rem": "實體上課"},
        "vn": {"prog": "Xu hướng xe điện toàn cầu: Tesla & Các hãng lớn", "hw": "Lab 1: Vở bài tập xu hướng xe điện", "sum": "Chốt danh sách lớp; so sánh các hãng xe điện và chuỗi cung ứng; tính tỷ suất sinh lời và độ biến động.", "rem": "Học trực tiếp"},
        "id": {"prog": "Tren EV Global: Tesla vs Pemimpin Industri", "hw": "Lab 1: Notebook tren EV", "sum": "Daftar mahasiswa final; membandingkan produsen EV dan rantai pasok; menghitung return harian & volatilitas.", "rem": "Tatap muka"},
        "my": {"prog": "Trend EV Global: Tesla vs Peneraju Industri", "hw": "Lab 1: Buku nota trend EV", "sum": "Senarai kursus muktamad; analisis rantaian bekalan EV; pengiraan pulangan harian dan turun naik pasaran.", "rem": "Bersemuka"},
        "th": {"prog": "แนวโน้มยานยนต์ไฟฟ้าโลก: Tesla เทียบผู้นำตลาด", "hw": "Lab 1: สมุดโค้ดวิเคราะห์แนวโน้ม EV", "sum": "สรุปรายชื่อผู้ลงทะเบียน; เปรียบเทียบห่วงโซ่อุปทาน EV; คำนวณผลตอบแทนรายวันและความผันผวน", "rem": "เรียนในชั้น"},
        "fr": {"prog": "Tendances mondiales des VE : Tesla vs Leaders", "hw": "TP 1 : Notebook tendances VE", "sum": "Inscriptions closes ; analyse comparative du secteur des VE ; calcul des rendements journaliers et volatilité.", "rem": "Présentiel"}
    },
    {
        "week": "Week 4", "date": "2026/10/01",
        "us": {"prog": "Quantitative Trading Strategies", "hw": "Lab 2: Moving average strategy report", "sum": "Moving average concepts (20MA vs 60MA); rule-based trading vs Buy & Hold; returns and drawdown.", "rem": "In-person"},
        "tw": {"prog": "量化交易策略實戰", "hw": "Lab 2: 移動平均線策略報告", "sum": "均線交叉法則（20MA vs 60MA）；規則化策略與買進持有對比；報酬率與回撤評估。", "rem": "實體上課"},
        "vn": {"prog": "Chiến lược giao dịch định lượng", "hw": "Lab 2: Báo cáo chiến lược đường trung bình", "sum": "Khái niệm đường trung bình MA (20MA vs 60MA); so sánh giao dịch theo quy tắc và Mua & Nắm giữ.", "rem": "Học trực tiếp"},
        "id": {"prog": "Strategi Trading Kuantitatif", "hw": "Lab 2: Laporan strategi moving average", "sum": "Konsep Moving Average (20MA vs 60MA); strategi berbasis aturan vs Beli & Simpan; evaluasi return & drawdown.", "rem": "Tatap muka"},
        "my": {"prog": "Strategi Dagangan Kuantitatif", "hw": "Lab 2: Laporan strategi moving average", "sum": "Konsep purata bergerak (20MA vs 60MA); perbandingan strategi berasaskan peraturan vs Beli & Pegang.", "rem": "Bersemuka"},
        "th": {"prog": "กลยุทธ์การซื้อขายเชิงปริมาณ", "hw": "Lab 2: รายงานกลยุทธ์เส้นค่าเฉลี่ยเคลื่อนที่", "sum": "แนวคิดเส้นค่าเฉลี่ย MA (20MA vs 60MA); การเทรดตามกฎระเบียบเทียบกับซื้อถือยาว; การวิเคราะห์ Drawdown", "rem": "เรียนในชั้น"},
        "fr": {"prog": "Stratégies de trading quantitatif", "hw": "TP 2 : Rapport sur les moyennes mobiles", "sum": "Moyennes mobiles (20MA vs 60MA) ; trading systématique vs Buy & Hold ; rendements et drawdown.", "rem": "Présentiel"}
    },
    {
        "week": "Week 5", "date": "2026/10/08",
        "us": {"prog": "Portfolio Construction & Diversification", "hw": "In-class drill: Two-asset allocation", "sum": "Correlation matrix; Markowitz portfolio concepts; asset weighting simulation and trade-offs.", "rem": "In-person"},
        "tw": {"prog": "投資組合建構與分散風險", "hw": "課堂演練：雙資產權重配置", "sum": "資產相關係數矩陣；Markowitz 投資組合概念；權重配置模擬與報酬風險平衡。", "rem": "實體上課"},
        "vn": {"prog": "Xây dựng danh mục đầu tư & Đa dạng hóa rủi ro", "hw": "Bài tập tại lớp: Phân bổ tài sản", "sum": "Ma trận tương quan; mô hình danh mục đầu tư Markowitz; mô phỏng tỷ trọng tài sản và đánh đổi rủi ro.", "rem": "Học trực tiếp"},
        "id": {"prog": "Konstruksi Portofolio & Diversifikasi", "hw": "Latihan kelas: Alokasi dua aset", "sum": "Matriks korelasi; dasar portofolio Markowitz; simulasi bobot aset dan trade-off return-risiko.", "rem": "Tatap muka"},
        "my": {"prog": "Pembinaan Portfolio & Kepelbagaian Risiko", "hw": "Latihan kelas: Peruntukan dua aset", "sum": "Matriks korelasi; konsep portfolio Markowitz; simulasi wajaran aset serta pertukaran risiko-pulangan.", "rem": "Bersemuka"},
        "th": {"prog": "การจัดพอร์ตการลงทุนและการกระจายความเสี่ยง", "hw": "แบบฝึกหัดในชั้น: จัดสรรสัดส่วน 2 สินทรัพย์", "sum": "เมทริกซ์สหสัมพันธ์; แนวคิดพอร์ตมาร์โควิทซ์; แบบจำลองการถ่วงน้ำหนักสินทรัพย์และผลตอบแทนความเสี่ยง", "rem": "เรียนในชั้น"},
        "fr": {"prog": "Construction de portefeuille & Diversification", "hw": "Exercice : Allocation bi-actifs", "sum": "Matrice de corrélation ; théorie moderne de Markowitz ; simulation d'arbitrage risque-rendement.", "rem": "Présentiel"}
    },
    {
        "week": "Week 6", "date": "2026/10/15",
        "us": {"prog": "Macro Dashboard: FRED API Integration", "hw": "Lab 3: Macro tracker notebook", "sum": "Fetching data via FRED API; inflation (CPI) and interest rates; macroeconomic data engineering.", "rem": "In-person"},
        "tw": {"prog": "總體經濟儀表板：FRED API 整合", "hw": "Lab 3: 總經指標觀測站", "sum": "串接聖路易斯聯準會 FRED API；通膨率（CPI）與聯邦基準利率數據工程與視覺化。", "rem": "實體上課"},
        "vn": {"prog": "Bảng điều khiển kinh tế vĩ mô: Tích hợp API FRED", "hw": "Lab 3: Sổ tay theo dõi vĩ mô", "sum": "Khai thác dữ liệu qua FRED API; chỉ số lạm phát (CPI) và lãi suất; xử lý dữ liệu kinh tế vĩ mô.", "rem": "Học trực tiếp"},
        "id": {"prog": "Dashboard Makroekonomi: Integrasi API FRED", "hw": "Lab 3: Notebook pemantau makro", "sum": "Mengambil data via API FRED; inflasi (CPI) dan suku bunga acuan; visualisasi indikator ekonomi.", "rem": "Tatap muka"},
        "my": {"prog": "Papan Pemuka Makroekonomi: Integrasi API FRED", "hw": "Lab 3: Buku nota penjejak makro", "sum": "Penyepaduan API FRED; analisis inflasi (CPI) dan kadar faedah; visualisasi data ekonomi makro.", "rem": "Bersemuka"},
        "th": {"prog": "แดชบอร์ดเศรษฐกิจมหภาค: เชื่อมต่อ API FRED", "hw": "Lab 3: สมุดโค้ดติดตามดัชนีมหภาค", "sum": "เชื่อมต่อ FRED API; วิเคราะห์อัตราเงินเฟ้อ (CPI) และอัตราดอกเบี้ย; การจัดการข้อมูลเศรษฐกิจ", "rem": "เรียนในชั้น"},
        "fr": {"prog": "Tableau de bord macro : API FRED", "hw": "TP 3 : Notebook de suivi macro", "sum": "Intégration de l'API de la FRED ; taux d'inflation (CPI) et taux d'intérêt ; pipeline de données macro.", "rem": "Présentiel"}
    },
    {
        "week": "Week 7", "date": "2026/10/22",
        "us": {"prog": "Financial Statement Feature Engineering", "hw": "In-class drill: Financial health scorecard", "sum": "Parsing corporate financial statements; calculating gross margins, operating ratios, and radar charts.", "rem": "In-person"},
        "tw": {"prog": "財務報表特徵工程與評分卡", "hw": "課堂練習：財務健康儀表板", "sum": "公開財務報表數據剖析；毛利率、營業利益率與流動比率指標計算與雷達圖呈現。", "rem": "實體上課"},
        "vn": {"prog": "Kỹ thuật trích xuất báo cáo tài chính", "hw": "Thực hành: Bảng điểm sức khỏe tài chính", "sum": "Phân tích báo cáo tài chính doanh nghiệp; tính biên lợi nhuận gộp, tỷ số hoạt động và biểu đồ radar.", "rem": "Học trực tiếp"},
        "id": {"prog": "Rekayasa Fitur Laporan Keuangan", "hw": "Latihan: Scorecard kesehatan finansial", "sum": "Parsing laporan keuangan; menghitung margin kotor, rasio likuiditas dan visualisasi grafik radar.", "rem": "Tatap muka"},
        "my": {"prog": "Kejuruteraan Ciri Penyata Kewangan", "hw": "Latihan: Kad skor kesihatan kewangan", "sum": "Analisis penyata kewangan syarikat; pengiraan margin kasar dan nisbah kecairan; paparan carta radar.", "rem": "Bersemuka"},
        "th": {"prog": "วิศวกรรมฟีเจอร์งบการเงินและการให้คะแนน", "hw": "แบบฝึกหัด: ดัชนีวัดสุขภาพการเงิน", "sum": "แยกข้อมูลรายงานทางการเงิน; คำนวณอัตรากำไรขั้นต้น อัตราส่วนสภาพคล่อง และพล็อตชาร์ตเรดาร์", "rem": "เรียนในชั้น"},
        "fr": {"prog": "Ingénierie financière & Scorecard", "hw": "Exercice : Tableau de santé financière", "sum": "Extraction des états financiers ; calcul des marges brutes, ratios de liquidité et graphiques radar.", "rem": "Présentiel"}
    },
    {
        "week": "Week 8", "date": "2026/10/29",
        "us": {"prog": "Midterm Project Guidance & Architecture Review", "hw": "Midterm architecture draft", "sum": "Clarifying business problem; verifying data pipelines; code refactoring and troubleshooting clinic.", "rem": "In-person"},
        "tw": {"prog": "期中專案指導與架構審查", "hw": "期中專案架構初稿提交", "sum": "個人/小組專案商業邏輯梳理；數據源確認；代碼重構與問題診斷工作坊。", "rem": "實體上課"},
        "vn": {"prog": "Hướng dẫn đồ án giữa kỳ & Đánh giá kiến trúc", "hw": "Nộp bản thảo kiến trúc đồ án", "sum": "Làm rõ bài toán kinh doanh; xác minh đường ống dữ liệu; tái cấu trúc mã nguồn và phòng khám sửa lỗi.", "rem": "Học trực tiếp"},
        "id": {"prog": "Bimbingan Proyek UTS & Review Arsitektur", "hw": "Pengumpulan draf arsitektur proyek", "sum": "Klarifikasi masalah bisnis; verifikasi alur data; refactoring kode dan klinik pemecahan masalah.", "rem": "Tatap muka"},
        "my": {"prog": "Bimbingan Projek Pertengahan Penggal", "hw": "Draf reka bentuk seni bina projek", "sum": "Penerangan model perniagaan; pengesahan saluran data; penambahbaikan kod dan sesi klinik nyahpepijat.", "rem": "Bersemuka"},
        "th": {"prog": "ให้คำปรึกษาโครงงานกลางภาค & ตรวจสถาปัตยกรรมระบบ", "hw": "ส่งร่างโครงสร้างระบบโครงงาน", "sum": "ปรับแต่งตรรกะทางธุรกิจ; ตรวจสอบความถูกต้องของข้อมูล; คลินิกให้คำแนะนำและแก้ปัญหาโค้ด", "rem": "เรียนในชั้น"},
        "fr": {"prog": "Orientation du projet partiel & Revue technique", "hw": "Ébauche de l'architecture du projet", "sum": "Clarification de la valeur métier ; validation des flux de données ; atelier de refactorisation.", "rem": "Présentiel"}
    },
    {
        "week": "Week 9", "date": "2026/11/05",
        "us": {"prog": "[Midterm Exam] Project Stage Review", "hw": "Midterm progress submission", "sum": "Group progress presentations on data pipelines and preliminary models; peer feedback sessions.", "rem": "In-person"},
        "tw": {"prog": "【期中評量】期中報告與進度審查", "hw": "期中專案階段成果展示", "sum": "各組口頭分享數據管線進度與初步分析成果；課堂互評與反饋機制。", "rem": "實體上課"},
        "vn": {"prog": "【Đánh giá giữa kỳ】Báo cáo tiến độ đồ án", "hw": "Nộp kết quả giai đoạn giữa kỳ", "sum": "Các nhóm thuyết trình về tiến độ xử lý dữ liệu và mô hình ban đầu; nhận xét chéo giữa các sinh viên.", "rem": "Học trực tiếp"},
        "id": {"prog": "[UTS] Review Progres Tahap Proyek", "hw": "Pengumpulan laporan kemajuan UTS", "sum": "Presentasi kelompok mengenai pipeline data dan model awal; sesi umpan balik antar rekan mahasiswa.", "rem": "Tatap muka"},
        "my": {"prog": "[Peperiksaan Pertengahan Penggal] Semakan Projek", "hw": "Penyerahan kemajuan pertengahan penggal", "sum": "Pembentangan kumpulan mengenai saluran data dan model awal; sesi maklum balas rakan sebaya.", "rem": "Bersemuka"},
        "th": {"prog": "【สอบกลางภาค】การนำเสนอความก้าวหน้าโครงงาน", "hw": "ส่งรายงานความคืบหน้ารอบกลางภาค", "sum": "แต่ละกลุ่มนำเสนอไปป์ไลน์ข้อมูลและโมเดลเบื้องต้น; กิจกรรมให้คำวิจารณ์เชิงสร้างสรรค์ระหว่างเพื่อนร่วมชั้น", "rem": "เรียนในชั้น"},
        "fr": {"prog": "[Examen partiel] Revue d'avancement du projet", "hw": "Dépôt d'étape du projet partiel", "sum": "Présentations des pipelines de données et premières modélisations ; retours entre pairs.", "rem": "Présentiel"}
    },
    {
        "week": "Week 10", "date": "2026/11/12",
        "us": {"prog": "Streamlit Interactive Web Development", "hw": "Lab 4: Build your first interactive app", "sum": "Transitioning from notebooks to web apps; widgets, sliders, input forms; live UI computation.", "rem": "In-person"},
        "tw": {"prog": "Streamlit 互動 Web 應用開發入門", "hw": "Lab 4: 打造第一個互動網頁", "sum": "從 Notebook 走向 Web App；滑桿、按鈕與下拉選單元件；即時計算與介面排版。", "rem": "實體上課"},
        "vn": {"prog": "Phát triển ứng dụng Web tương tác với Streamlit", "hw": "Lab 4: Xây dựng ứng dụng đầu tay", "sum": "Chuyển từ Notebook sang Web App; các thanh trượt, nút bấm, biểu mẫu; giao diện tương tác thời gian thực.", "rem": "Học trực tiếp"},
        "id": {"prog": "Pengembangan Web Interaktif Streamlit", "hw": "Lab 4: Bangun web interaktif pertama", "sum": "Transisi dari notebook ke aplikasi web; komponen slider, tombol, formulir input; kalkulasi UI langsung.", "rem": "Tatap muka"},
        "my": {"prog": "Pembangunan Web Interaktif Streamlit", "hw": "Lab 4: Bina aplikasi web interaktif pertama", "sum": "Peralihan daripada notebook ke aplikasi web; widget slider, butang borang; paparan masa nyata.", "rem": "Bersemuka"},
        "th": {"prog": "พัฒนาเว็บแอปพลิเคชันเชิงโต้ตอบด้วย Streamlit", "hw": "Lab 4: สร้างเว็บอินเทอร์แอคทีฟแรกของคุณ", "sum": "ก้าวข้ามจากสมุดโค้ดสู่เว็บแอป; วิดเจ็ต ตัวเลื่อน ปุ่มกด ฟอร์มกรอกข้อมูล; การคำนวณแบบสดบนหน้าเว็บ", "rem": "เรียนในชั้น"},
        "fr": {"prog": "Développement web interactif avec Streamlit", "hw": "TP 4 : Créez votre première application web", "sum": "Du notebook à l'application web ; composants interactifs, curseurs, formulaires ; calculs en direct.", "rem": "Présentiel"}
    },
    {
        "week": "Week 11", "date": "2026/11/19",
        "us": {"prog": "Cloud Deployment: GitHub + Streamlit Cloud", "hw": "Lab 5: Deploying live web app", "sum": "Git and GitHub version control; CI/CD cloud deployment; permanent custom URL and QR Code sharing.", "rem": "In-person"},
        "tw": {"prog": "雲端部署實戰：GitHub ＋ Streamlit Cloud", "hw": "Lab 5: 應用程式永久上線", "sum": "Git 與 GitHub 版本控制；雲端持續整合（CI/CD）；生成專屬公開網址與 QR Code 分享。", "rem": "實體上課"},
        "vn": {"prog": "Triển khai đám mây: GitHub + Streamlit Cloud", "hw": "Lab 5: Đưa ứng dụng lên mạng", "sum": "Quản lý phiên bản Git & GitHub; tự động hóa CI/CD; tạo đường link URL tùy chỉnh và mã QR chia sẻ.", "rem": "Học trực tiếp"},
        "id": {"prog": "Deployment Cloud: GitHub + Streamlit Cloud", "hw": "Lab 5: Rilis aplikasi web aktif", "sum": "Kontrol versi Git & GitHub; alur otomatisasi CI/CD cloud; bagikan link URL permanen dan kode QR.", "rem": "Tatap muka"},
        "my": {"prog": "Penyebaran Awan: GitHub + Streamlit Cloud", "hw": "Lab 5: Pelancaran aplikasi web secara langsung", "sum": "Kawalan versi Git dan GitHub; automasi CI/CD awan; pautan URL kekal dan perkongsian Kod QR.", "rem": "Bersemuka"},
        "th": {"prog": "การปรับใช้บนคลาวด์: GitHub + Streamlit Cloud", "hw": "Lab 5: เผยแพร่เว็บแอปสู่สาธารณะ", "sum": "ระบบควบคุมเวอร์ชัน Git & GitHub; กระบวนการ CI/CD คลาวด์; แชร์ลิงก์ถาวรและ QR Code สำหรับมือถือ", "rem": "เรียนในชั้น"},
        "fr": {"prog": "Déploiement Cloud : GitHub + Streamlit Cloud", "hw": "TP 5 : Mise en ligne de l'application", "sum": "Gestion de versions avec Git & GitHub ; intégration CI/CD ; partage via URL dédiée et QR Code.", "rem": "Présentiel"}
    },
    {
        "week": "Week 12", "date": "2026/11/26",
        "us": {"prog": "AI Agent Integration: LLM API Setup", "hw": "Lab 6: Business intelligence chat agent", "sum": "Google AI Studio and Gemini API; prompt conditioning; embedding intelligent reasoning in web apps.", "rem": "In-person"},
        "tw": {"prog": "AI 智慧助理串接：LLM API 整合", "hw": "Lab 6: 商業智能問答助手", "sum": "Google AI Studio 與 Gemini API 調度；將 AI 文本分析功能嵌入 Web 應用程式。", "rem": "實體上課"},
        "vn": {"prog": "Tích hợp trợ lý thông minh: Cài đặt API LLM", "hw": "Lab 6: Trợ lý trò chuyện thông minh", "sum": "Google AI Studio & API Gemini; tinh chỉnh câu lệnh prompt; tích hợp trí tuệ nhân tạo vào Web App.", "rem": "Học trực tiếp"},
        "id": {"prog": "Integrasi Asisten AI: Setup API LLM", "hw": "Lab 6: Asisten obrolan analitik bisnis", "sum": "Google AI Studio & API Gemini; prompt engineering terarah; menanamkan nalar cerdas ke aplikasi web.", "rem": "Tatap muka"},
        "my": {"prog": "Integrasi Ejen AI: Konfigurasi API LLM", "hw": "Lab 6: Ejen sembang kecerdasan perniagaan", "sum": "Google AI Studio dan API Gemini; kejuruteraan prompt; membenamkan penaakulan pintar ke dalam aplikasi.", "rem": "Bersemuka"},
        "th": {"prog": "การเชื่อมต่อเอเจนต์ AI: ตั้งค่า API ของ LLM", "hw": "Lab 6: บอทถามตอบอัจฉริยะทางธุรกิจ", "sum": "Google AI Studio และ Gemini API; การวางข้อกำหนดคำสั่ง Prompt; นำการประมวลผลอัจฉริยะลงสู่เว็บ", "rem": "เรียนในชั้น"},
        "fr": {"prog": "Intégration d'Agent IA : API de LLM", "hw": "TP 6 : Assistant conversationnel d'affaires", "sum": "Google AI Studio et API Gemini ; conditionnement de prompts ; injection d'intelligence dans l'app.", "rem": "Présentiel"}
    },
    {
        "week": "Week 13", "date": "2026/12/03",
        "us": {"prog": "ESG & Sentiment Analysis for Business", "hw": "In-class lab: ESG keyword extractor", "sum": "Corporate ESG report analysis; keyword entity extraction; sentiment scoring and corporate governance.", "rem": "In-person"},
        "tw": {"prog": "ESG 企業永續與文字情感分析", "hw": "課堂實作：永續報告書關鍵字提取", "sum": "企業 ESG 永續報告書解析；自然語言關鍵詞萃取；情緒分析與商業聲譽評分。", "rem": "實體上課"},
        "vn": {"prog": "ESG & Phân tích sắc thái văn bản kinh doanh", "hw": "Thực hành: Trích xuất từ khóa ESG", "sum": "Phân tích báo cáo phát triển bền vững ESG; trích xuất thực thể từ khóa; chấm điểm cảm xúc thương hiệu.", "rem": "Học trực tiếp"},
        "id": {"prog": "ESG & Analisis Sentimen Teks Bisnis", "hw": "Praktik kelas: Ekstraksi kata kunci ESG", "sum": "Analisis laporan keberlanjutan ESG; ekstraksi entitas teks kata kunci; skor sentimen dan reputasi korporat.", "rem": "Tatap muka"},
        "my": {"prog": "ESG & Analisis Sentimen Teks Perniagaan", "hw": "Latihan kelas: Pengekstrak kata kunci ESG", "sum": "Analisis laporan kemampanan korporat ESG; pengekstrakan entiti; pemarkahan sentimen reputasi jenama.", "rem": "Bersemuka"},
        "th": {"prog": "ESG และการวิเคราะห์ความรู้สึกในข้อความธุรกิจ", "hw": "แบบฝึกหัด: ระบบดึงคำสำคัญรายงาน ESG", "sum": "การสกัดรายงานความยั่งยืนขององค์กร; สกัดคำสำคัญเชิงหมวดหมู่; การให้คะแนนความรู้สึกต่อแบรนด์", "rem": "เรียนในชั้น"},
        "fr": {"prog": "ESG & Analyse de sentiment d'entreprise", "hw": "Exercice : Extracteur de termes ESG", "sum": "Analyse de rapports RSE/ESG ; extraction d'entités textuelles ; scoring de sentiment et gouvernance.", "rem": "Présentiel"}
    },
    {
        "week": "Week 14", "date": "2026/12/10",
        "us": {"prog": "UI/UX & Professional Dashboard Design", "hw": "Final project UI refinement", "sum": "Multi-column grid layouts; color palettes; mobile-first responsive design best practices.", "rem": "In-person"},
        "tw": {"prog": "使用者體驗優化與專業儀表板設計", "hw": "期末專案 UI/UX 優化", "sum": "多欄位卡片排版；主題配色（Light/Dark）；跨螢幕手機響應式設計調校。", "rem": "實體上課"},
        "vn": {"prog": "Thiết kế UI/UX & Bảng điều khiển chuyên nghiệp", "hw": "Hoàn thiện giao diện đồ án", "sum": "Bố cục lưới đa cột; bảng màu trực quan; tối ưu hóa thiết kế thích ứng ưu tiên di động (Mobile-first).", "rem": "Học trực tiếp"},
        "id": {"prog": "Desain UI/UX & Dashboard Profesional", "hw": "Penyempurnaan UI proyek akhir", "sum": "Tata letak grid multi-kolom; skema warna terpadu; praktik terbaik desain responsif ramah seluler.", "rem": "Tatap muka"},
        "my": {"prog": "Reka Bentuk UI/UX & Papan Pemuka Profesional", "hw": "Penambahbaikan antara muka projek", "sum": "Susun atur grid pelbagai lajur; skim warna estetik; amalan terbaik reka bentuk responsif mudah alih.", "rem": "Bersemuka"},
        "th": {"prog": "การออกแบบ UI/UX & แดชบอร์ดระดับมืออาชีพ", "hw": "ขัดเกลาหน้าตา UI ของโครงงานปลายภาค", "sum": "การจัดวางเค้าโครงแบบหลายคอลัมน์; โทนสีที่เป็นระเบียบ; การปรับหน้าจอให้ตอบสนองบนสมาร์ทโฟน", "rem": "เรียนในชั้น"},
        "fr": {"prog": "Design UI/UX & Tableaux de bord professionnels", "hw": "Peaufinage de l'UI du projet", "sum": "Mises en page multi-colonnes ; harmonies graphiques ; bonnes pratiques de design mobile-first.", "rem": "Présentiel"}
    },
    {
        "week": "Week 15", "date": "2026/12/17",
        "us": {"prog": "AI Ethics, Data Privacy & Security", "hw": "Lab 7: Compliance checklist", "sum": "Confidentiality; secrets management for API keys; defending against prompt injections in production.", "rem": "In-person"},
        "tw": {"prog": "AI 倫理、資料隱私與資安防護", "hw": "Lab 7: 資安合規自我檢核表", "sum": "商業機密界線；API Key 環境變數隱藏安全實踐；提示詞注入（Prompt Injection）防禦。", "rem": "實體上課"},
        "vn": {"prog": "Đạo đức AI, Quyền riêng tư & Bảo mật dữ liệu", "hw": "Lab 7: Bảng kiểm tra tuân thủ", "sum": "Bảo mật kinh doanh; quản lý an toàn khóa API; phòng thủ chống tấn công chèn lệnh (Prompt Injection).", "rem": "Học trực tiếp"},
        "id": {"prog": "Etika AI, Privasi Data & Keamanan Sistem", "hw": "Lab 7: Checklist kepatuhan keamanan", "sum": "Kerahasiaan data bisnis; manajemen kunci API yang aman; mitigasi serangan prompt injection.", "rem": "Tatap muka"},
        "my": {"prog": "Etika AI, Privasi Data & Keselamatan", "hw": "Lab 7: Senarai semak pematuhan privasi", "sum": "Kerahsiaan maklumat; pengurusan selamat kunci API; perlindungan daripada serangan suntikan prompt.", "rem": "Bersemuka"},
        "th": {"prog": "จริยธรรม AI, ความเป็นส่วนตัว & ความปลอดภัยข้อมูล", "hw": "Lab 7: ตรวจเช็กลิสต์ความสอดคล้องความปลอดภัย", "sum": "ขอบเขตความลับทางธุรกิจ; การจัดการคีย์ API ในไฟล์ลับ; การป้องกันการโจมตี Prompt Injection", "rem": "เรียนในชั้น"},
        "fr": {"prog": "Éthique de l'IA, Données & Cybersécurité", "hw": "TP 7 : Checklist de conformité", "sum": "Confidentialité d'affaires ; gestion sécurisée des clés d'API ; protection contre le prompt injection.", "rem": "Présentiel"}
    },
    {
        "week": "Week 16", "date": "2026/12/24",
        "us": {"prog": "Final Project Rehearsal & Stress Testing", "hw": "End-to-end user testing", "sum": "Peer review clinics; edge-case stress testing; performance debugging and UX hardening.", "rem": "In-person"},
        "tw": {"prog": "期中專案演練與壓力測試", "hw": "應用程式端對端完整測試", "sum": "同儕測試（Peer Review）；極端輸入測試；網頁載入效能調優與除錯。", "rem": "實體上課"},
        "vn": {"prog": "Tổng duyệt đồ án cuối kỳ & Thử nghiệm chịu tải", "hw": "Kiểm thử người dùng toàn diện", "sum": "Đánh giá chéo ngang hàng; thử nghiệm các trường hợp biên; tinh chỉnh hiệu năng và hoàn thiện sản phẩm.", "rem": "Học trực tiếp"},
        "id": {"prog": "Geladi Bersih Proyek Akhir & Uji Beban", "hw": "Pengujian pengguna menyeluruh", "sum": "Sesi peer-review antar kelompok; pengujian kondisi batas ekstrem; optimasi performa dan debugging.", "rem": "Tatap muka"},
        "my": {"prog": "Latihan Akhir Projek & Ujian Tekanan", "hw": "Pengujian aplikasi dari hujung ke hujung", "sum": "Ulasan rakan sebaya; ujian situasi melampau; penalaan prestasi masa tindak balas dan pepijat.", "rem": "Bersemuka"},
        "th": {"prog": "ซ้อมใหญ่โครงงานปลายภาค & การทดสอบโหลด", "hw": "การทดสอบการใช้งานจริงแบบครบวงจร", "sum": "การประเมินผลโดยกลุ่มเพื่อนร่วมรุ่น; การทดสอบกรณีขอบเขตสุดขั้ว; ตรวจสอบและปรับปรุงประสิทธิภาพเว็บ", "rem": "เรียนในชั้น"},
        "fr": {"prog": "Répétition générale du projet & Stress test", "hw": "Tests utilisateurs de bout en bout", "sum": "Ateliers de revue par les pairs ; tests de charge et cas limites ; optimisation des temps de chargement.", "rem": "Présentiel"}
    },
    {
        "week": "Week 17", "date": "2026/12/31",
        "us": {"prog": "[Final Showcase] Interactive App Demo (Day 1)", "hw": "Final app & documentation release", "sum": "Live presentation of deployed FinTech web applications; expert feedback and peer exchange.", "rem": "In-person"},
        "tw": {"prog": "【期末發表】專題成果展示會 (Day 1)", "hw": "期末專題報告與網頁交付", "sum": "學生分組上台發表互動式金融科技 Web 應用；業界專家/師長講評交流。", "rem": "實體上課"},
        "vn": {"prog": "【Báo cáo cuối kỳ】Thuyết trình ứng dụng (Ngày 1)", "hw": "Bàn giao ứng dụng & tài liệu", "sum": "Thuyết trình trực tiếp ứng dụng FinTech trên sân khấu lớp học; nhận góp ý và trao đổi thực tế.", "rem": "Học trực tiếp"},
        "id": {"prog": "[Showcase Akhir] Demo Aplikasi Interaktif (Hari 1)", "hw": "Rilis aplikasi akhir & dokumentasi", "sum": "Presentasi langsung aplikasi web FinTech yang telah live; umpan balik penguji dan tanya jawab.", "rem": "Tatap muka"},
        "my": {"prog": "[Pameran Akhir] Demonstrasi Aplikasi (Hari 1)", "hw": "Penyerahan aplikasi akhir & dokumentasi", "sum": "Pembentangan langsung aplikasi web FinTech atas talian; maklum balas penilai dan perbincangan.", "rem": "Bersemuka"},
        "th": {"prog": "【นำเสนอผลงานปลายภาค】สาธิตเว็บแอป (วันที่ 1)", "hw": "ส่งมอบเว็บแอปและคู่มือฉบับสมบูรณ์", "sum": "นำเสนอแอปพลิเคชัน FinTech แบบสดในห้องเรียน; รับข้อเสนอแนะจากผู้ทรงคุณวุฒิและเพื่อนร่วมชั้น", "rem": "เรียนในชั้น"},
        "fr": {"prog": "[Showcase final] Démo d'application en direct (J1)", "hw": "Livraison de l'application et documentation", "sum": "Présentation des applications FinTech déployées ; retours d'évaluation et échanges avec la salle.", "rem": "Présentiel"}
    },
    {
        "week": "Week 18", "date": "2027/01/07",
        "us": {"prog": "[Final Showcase] Demo (Day 2) & Wrap-up", "hw": "Learning portfolio compilation", "sum": "Showcase round 2; course synthesis; mapping AI skills to future careers in financial analytics.", "rem": "In-person"},
        "tw": {"prog": "【期末發表】專題成果展示會 (Day 2) 與總結", "hw": "學習歷程檔案彙整", "sum": "第二階段專題成果發表；全學期知識回顧；生成式 AI 與商業分析職涯藍圖展拓。", "rem": "實體上課"},
        "vn": {"prog": "【Báo cáo cuối kỳ】Thuyết trình (Ngày 2) & Tổng kết", "hw": "Tổng hợp hồ sơ học tập cá nhân", "sum": "Thuyết trình đợt 2; đúc kết kiến thức toàn khóa; định hướng phát triển sự nghiệp cùng AI tài chính.", "rem": "Học trực tiếp"},
        "id": {"prog": "[Showcase Akhir] Demo (Hari 2) & Kesimpulan", "hw": "Penyusunan portofolio belajar", "sum": "Showcase sesi 2; rangkuman materi satu semester; pemetaan keterampilan AI ke karier analitik bisnis.", "rem": "Bersemuka"},
        "th": {"prog": "【นำเสนอผลงานปลายภาค】สาธิต (วันที่ 2) & สรุปบทเรียน", "hw": "รวบรวมแฟ้มสะสมผลงานการเรียนรู้", "sum": "นำเสนอรอบที่สอง; สรุปเนื้อหาสำคัญตลอดทั้งภาคการศึกษา; แผนที่เส้นทางอาชีพวิเคราะห์ธุรกิจด้วย AI", "rem": "เรียนในชั้น"},
        "fr": {"prog": "[Showcase final] Démo (J2) & Bilan du semestre", "hw": "Consolidation du portfolio d'apprentissage", "sum": "Deuxième session de présentations ; synthèse générale ; opportunités professionnelles dans l'IA financière.", "rem": "Présentiel"}
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

# 核心改動：將 18 週大表放入預設收合的 expander 中
with st.expander(schedule_expander_titles.get(current_code, schedule_expander_titles["us"]), expanded=False):
    if hasattr(st, "html"):
        st.html(table_full)
    else:
        st.markdown(table_full, unsafe_allow_html=True)
