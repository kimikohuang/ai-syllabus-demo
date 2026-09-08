# ==============================================================================
# [Script] 18-Week Interactive Multilingual Syllabus Table (Pure HTML / No Indent)
# 【腳本】18 週完整多語系課綱表格（st.html 原生解析，徹底根除縮排代碼塊問題）
# ==============================================================================

import streamlit as st

# 1. 頁面基本配置
st.set_page_config(
    page_title="Python AI Applications - 18-Week Syllabus",
    layout="wide",
    page_icon="🎓"
)

# 2. 標題與簡介
st.title("🎓 Python AI Applications (Python AI 應用)")
st.caption("115 學期 四技經管系2丙 (3.0 學分 / 3.0 時數) | 互動式多語系完整課程進度表")

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

# 自訂 CSS：按鈕與表格樣式（固定欄寬比例、無橫向 scrollbar、文字自動換行）
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

/* 核心表格樣式：自適應寬度、徹底消除底端 scrollbar、文字自然斷行 */
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

st.markdown("**🌐 Select Parallel Language (點擊按鈕切換表格對照語言):**")

# 7 國語言按鈕列
btn_items = "".join([
    f'<a class="flag-btn {"active" if code == current_code else ""}" href="?lang={code}" target="_self"><img class="flag-img" src="{data["flag"]}" alt="{data["label"]}"><span>{data["label"]}</span></a>'
    for code, data in LANG_CONFIG.items()
])
st.markdown(f'<div class="flag-btn-grid">{btn_items}</div>', unsafe_allow_html=True)

st.info(f"💡 **Current Parallel View / 目前對照語言**: **{current_info['name']}**")

# 4. 完整的 18 週課綱資料庫
weeks_all = [
    {
        "week": "Week 1", "date": "2026/09/10",
        "tw": {"progress": "課程導覽與自然語言編程", "hw": "Lab 0: 課堂趣味實作探索", "sum": "課程總覽；自然語言提示詞編程；Colab 環境配置；指揮家思維建立。", "rem": "實體上課"},
        "us": {"progress": "Course Onboarding & Vibe Coding", "hw": "Lab 0: In-class fun exploration", "sum": "Course overview; prompt-driven programming with natural language; Google Colab setup; conductor mindset.", "rem": "In-person"}
    },
    {
        "week": "Week 2", "date": "2026/09/17",
        "tw": {"progress": "市場數據工程：台積電與蘋果", "hw": "課堂即時實作與練習", "sum": "加退選期間；Python 擷取每日股價；資料表 DataFrame 處理與繪製走勢圖。", "rem": "實體上課"},
        "us": {"progress": "Market Data Engineering: Apple & TSMC", "hw": "In-class live practice", "sum": "Add/drop period; fetching daily stock prices with Python; DataFrame processing; visual trend charts.", "rem": "In-person"}
    },
    {
        "week": "Week 3", "date": "2026/09/24",
        "tw": {"progress": "全球電動車趨勢：Tesla 與全球車廠", "hw": "Lab 1: 電動車趨勢筆記本", "sum": "選課名單確定；全球電動車供應鏈與龍頭對比；計算日報酬率與波動度指標。", "rem": "實體上課"},
        "us": {"progress": "Global EV Trends: Tesla vs. Leaders", "hw": "Lab 1: EV trends notebook", "sum": "Roster finalized; comparing global EV leaders and supply chain; calculating daily returns and volatility.", "rem": "In-person"}
    },
    {
        "week": "Week 4", "date": "2026/10/01",
        "tw": {"progress": "量化交易策略實戰", "hw": "Lab 2: 移動平均線策略報告", "sum": "均線交叉法則（20MA vs 60MA）；規則化策略與買進持有對比；報酬率與回撤評估。", "rem": "實體上課"},
        "us": {"progress": "Quantitative Trading Strategies", "hw": "Lab 2: Moving average strategy report", "sum": "Moving average concepts (20MA vs 60MA); rule-based trading vs Buy & Hold; returns and drawdown.", "rem": "In-person"}
    },
    {
        "week": "Week 5", "date": "2026/10/08",
        "tw": {"progress": "投資組合建構與分散風險", "hw": "課堂演練：雙資產權重配置", "sum": "資產相關係數矩陣；Markowitz 投資組合概念；權重配置模擬與報酬風險平衡。", "rem": "實體上課"},
        "us": {"progress": "Portfolio Construction & Diversification", "hw": "In-class drill: Two-asset allocation", "sum": "Correlation matrix; Markowitz portfolio concepts; asset weighting simulation and trade-offs.", "rem": "In-person"}
    },
    {
        "week": "Week 6", "date": "2026/10/15",
        "tw": {"progress": "總體經濟儀表板：FRED API 整合", "hw": "Lab 3: 總經指標觀測站", "sum": "串接聖路易斯聯準會 FRED API；通膨率（CPI）與聯邦基準利率數據工程與視覺化。", "rem": "實體上課"},
        "us": {"progress": "Macro Dashboard: FRED API Integration", "hw": "Lab 3: Macro tracker notebook", "sum": "Fetching data via FRED API; inflation (CPI) and interest rates; macroeconomic data engineering.", "rem": "In-person"}
    },
    {
        "week": "Week 7", "date": "2026/10/22",
        "tw": {"progress": "財務報表特徵工程與評分卡", "hw": "課堂練習：財務健康儀表板", "sum": "公開財務報表數據剖析；毛利率、營業利益率與流動比率指標計算與雷達圖呈現。", "rem": "實體上課"},
        "us": {"progress": "Financial Statement Feature Engineering", "hw": "In-class drill: Financial health scorecard", "sum": "Parsing corporate financial statements; calculating gross margins, operating ratios, and radar charts.", "rem": "In-person"}
    },
    {
        "week": "Week 8", "date": "2026/10/29",
        "tw": {"progress": "期中專案指導與架構審查", "hw": "期中專案架構初稿提交", "sum": "個人/小組專案商業邏輯梳理；數據源確認；代碼重構與問題診斷工作坊。", "rem": "實體上課"},
        "us": {"progress": "Midterm Project Guidance & Architecture Review", "hw": "Midterm architecture draft", "sum": "Clarifying business problem; verifying data pipelines; code refactoring and troubleshooting clinic.", "rem": "In-person"}
    },
    {
        "week": "Week 9", "date": "2026/11/05",
        "tw": {"progress": "【期中評量】期中報告與進度審查", "hw": "期中專案階段成果展示", "sum": "各組口頭分享數據管線進度與初步分析成果；課堂互評與反饋機制。", "rem": "實體上課"},
        "us": {"progress": "[Midterm Exam] Project Stage Review", "hw": "Midterm progress submission", "sum": "Group progress presentations on data pipelines and preliminary models; peer feedback sessions.", "rem": "In-person"}
    },
    {
        "week": "Week 10", "date": "2026/11/12",
        "tw": {"progress": "Streamlit 互動 Web 應用開發入門", "hw": "Lab 4: 打造第一個互動網頁", "sum": "從 Notebook 走向 Web App；滑桿、按鈕與下拉選單元件；即時計算與介面排版。", "rem": "實體上課"},
        "us": {"progress": "Streamlit Interactive Web Development", "hw": "Lab 4: Build your first interactive app", "sum": "Transitioning from notebooks to web apps; widgets, sliders, input forms; live UI computation.", "rem": "In-person"}
    },
    {
        "week": "Week 11", "date": "2026/11/19",
        "tw": {"progress": "雲端部署實戰：GitHub ＋ Streamlit Cloud", "hw": "Lab 5: 應用程式永久上線", "sum": "Git 與 GitHub 版本控制；雲端持續整合（CI/CD）；生成專屬公開網址與 QR Code 分享。", "rem": "實體上課"},
        "us": {"progress": "Cloud Deployment: GitHub + Streamlit Cloud", "hw": "Lab 5: Deploying live web app", "sum": "Git and GitHub version control; CI/CD cloud deployment; permanent custom URL and QR Code sharing.", "rem": "In-person"}
    },
    {
        "week": "Week 12", "date": "2026/11/26",
        "tw": {"progress": "AI 智慧助理串接：LLM API 整合", "hw": "Lab 6: 商業智能問答助手", "sum": "Google AI Studio 與 Gemini API 調度；將 AI 文本分析功能嵌入 Web 應用程式。", "rem": "實體上課"},
        "us": {"progress": "AI Agent Integration: LLM API Setup", "hw": "Lab 6: Business intelligence chat agent", "sum": "Google AI Studio and Gemini API; prompt conditioning; embedding intelligent reasoning in web apps.", "rem": "In-person"}
    },
    {
        "week": "Week 13", "date": "2026/12/03",
        "tw": {"progress": "ESG 企業永續與文字情感分析", "hw": "課堂實作：永續報告書關鍵字提取", "sum": "企業 ESG 永續報告書解析；自然語言關鍵詞萃取；情緒分析與商業聲譽評分。", "rem": "實體上課"},
        "us": {"progress": "ESG & Sentiment Analysis for Business", "hw": "In-class lab: ESG keyword extractor", "sum": "Corporate ESG report analysis; keyword entity extraction; sentiment scoring and corporate governance.", "rem": "In-person"}
    },
    {
        "week": "Week 14", "date": "2026/12/10",
        "tw": {"progress": "使用者體驗優化與專業儀表板設計", "hw": "期末專案 UI/UX 優化", "sum": "多欄位卡片排版；主題配色（Light/Dark）；跨螢幕手機響應式設計調校。", "rem": "實體上課"},
        "us": {"progress": "UI/UX & Professional Dashboard Design", "hw": "Final project UI refinement", "sum": "Multi-column grid layouts; color palettes; mobile-first responsive design best practices.", "rem": "In-person"}
    },
    {
        "week": "Week 15", "date": "2026/12/17",
        "tw": {"progress": "AI 倫理、資料隱私與資安防護", "hw": "Lab 7: 資安合規自我檢核表", "sum": "商業機密界線；API Key 環境變數隱藏安全實踐；提示詞注入（Prompt Injection）防禦。", "rem": "實體上課"},
        "us": {"progress": "AI Ethics, Data Privacy & Security", "hw": "Lab 7: Compliance checklist", "sum": "Confidentiality; secrets management for API keys; defending against prompt injections in production.", "rem": "In-person"}
    },
    {
        "week": "Week 16", "date": "2026/12/24",
        "tw": {"progress": "期末專案演練與壓力測試", "hw": "應用程式端對端完整測試", "sum": "同儕測試（Peer Review）；極端輸入測試；網頁載入效能調優與除錯。", "rem": "實體上課"},
        "us": {"progress": "Final Project Rehearsal & Stress Testing", "hw": "End-to-end user testing", "sum": "Peer review clinics; edge-case stress testing; performance debugging and UX hardening.", "rem": "In-person"}
    },
    {
        "week": "Week 17", "date": "2026/12/31",
        "tw": {"progress": "【期末發表】專題成果展示會 (Day 1)", "hw": "期末專題報告與網頁交付", "sum": "學生分組上台發表互動式金融科技 Web 應用；業界專家/師長講評交流。", "rem": "實體上課"},
        "us": {"progress": "[Final Showcase] Interactive App Demo (Day 1)", "hw": "Final app & documentation release", "sum": "Live presentation of deployed FinTech web applications; expert feedback and peer exchange.", "rem": "In-person"}
    },
    {
        "week": "Week 18", "date": "2027/01/07",
        "tw": {"progress": "【期末發表】專題成果展示會 (Day 2) 與總結", "hw": "學習歷程檔案彙整", "sum": "第二階段專題成果發表；全學期知識回顧；生成式 AI 與商業分析職涯藍圖展拓。", "rem": "實體上課"},
        "us": {"progress": "[Final Showcase] Demo (Day 2) & Wrap-up", "hw": "Learning portfolio compilation", "sum": "Showcase round 2; course synthesis; mapping AI skills to future careers in financial analytics.", "rem": "In-person"}
    }
]

# 動態產生翻譯
def get_translated_row(item, code):
    if code == "us":
        return item["us"]
    elif code == "tw":
        return item["tw"]
    base_tw = item["tw"]
    base_us = item["us"]
    return {
        "progress": f"{base_us['progress']}<br><span style='color:#6b7280; font-size:12px;'>({base_tw['progress']})</span>",
        "hw": base_us["hw"],
        "sum": f"{base_us['sum']}<br><span style='color:#6b7280; font-size:12px;'>({base_tw['sum']})</span>",
        "rem": f"{base_us['rem']} / {base_tw['rem']}"
    }

# 5. 採用單行無縮排方式拼接 HTML 表格，徹底避開 Markdown 解析陷阱
rows_html = "".join([
    f'<tr><td class="col-week">{r["week"]}</td><td class="col-date">{r["date"]}</td><td class="col-progress">{get_translated_row(r, current_code)["progress"]}</td><td class="col-hw">{get_translated_row(r, current_code)["hw"]}</td><td class="col-summary">{get_translated_row(r, current_code)["sum"]}</td><td class="col-remarks">{get_translated_row(r, current_code)["rem"]}</td></tr>'
    for r in weeks_all
])

table_full = f'<div class="syllabus-table-wrapper"><table class="syllabus-table"><thead><tr><th class="col-week">週次 (Week)</th><th class="col-date">上課日期 (Date)</th><th class="col-progress">教學進度 (Progress)</th><th class="col-hw">作業進度 (Homework)</th><th class="col-summary">內容摘要 (Summary)</th><th class="col-remarks">備註</th></tr></thead><tbody>{rows_html}</tbody></table></div>'

# 使用 st.html 或純 HTML 渲染
if hasattr(st, "html"):
    st.html(table_full)
else:
    st.markdown(table_full, unsafe_allow_html=True)
