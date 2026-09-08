# 7. 側邊欄：動態多語系 AI 助教（隨頂部按鈕自動切換語言）
with st.sidebar:
    # 介面多語系文本字典
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

    # 去識別化名單
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
            
            # 1. 期末專題相關
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

            # 2. 評分標準相關
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

            # 3. 環境與工具相關
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

            # 4. 其他一般問題
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

            # 顯示結果：以目前選擇的語言為主，搭配教師繁中與全班廣播英文
            st.success("✅ Recorded! / 已記錄")
            current_flag = LANG_CONFIG[current_code]["name"]
            st.markdown(f"**{current_flag}:**\n\n{local_answers.get(current_code, local_answers['us'])}")
            
            # 若當前不是繁中，額外顯示教師對照
            if current_code != "tw":
                st.markdown(f"**🇹🇼 教師對照 (繁體中文):**\n- 提問者: `{final_student_id}`\n- 核心摘要: {zh_summary}")
                
            # 若當前不是英文，額外顯示全班廣播英文
            if current_code != "us":
                st.markdown(f"**🇺🇸 For Class Broadcast (English):**\n*{en_broadcast}*")

            if "Anonymous" not in final_student_id:
                st.caption(f"🎉 Participation logged for `{final_student_id}`.")
        else:
            st.warning("Please type a question. (請輸入問題)")
