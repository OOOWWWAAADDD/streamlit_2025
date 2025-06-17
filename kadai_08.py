import streamlit as st
from PIL import Image

if "mail" not in st.session_state:
    st.session_state.mail = ""
if "forgot_password" not in st.session_state:
    st.session_state.forgot_password = False
if "count" not in st.session_state:
    st.session_state.count = 0
if "check" not in st.session_state:
    st.session_state.check = False

st.write("パスコード突破ゲーム")
st.header('ここから先はパスコードが必要です')
passcode = st.text_input("パスワードを入力してください", type="password")

if passcode:
    st.session_state.count += 1 

if passcode:
    if passcode == "WebProgramming":
        st.success('ログイン成功！')
        st.write(f"あなたは{st.session_state.count}回で突破に成功しました")
        st.markdown("パスワードを知る方法は二つあります")
        st.balloons()
    else:
        st.error('パスワードが間違っています')

if st.button("パスワードを忘れた場合", key="forgot_password_button"):
    st.session_state.forgot_password = True
    st.session_state.check = True

if st.session_state.forgot_password:
    with st.expander("パスワードお問い合わせ"):
        st.session_state.mail = st.text_input("メールアドレスを入力してください", key="mail_input")
        check = st.checkbox('私はロボットではありません', key='robot_check')
        
        if check:
            col1, col2 = st.columns(2)
            img = Image.open('8.jpg')
            with col1:
                st.image(img, caption='image file', width=100)
            with col2:
                img_pass = st.text_input('画像の数字を入力してください', key='img_pass')
        else:
            img_pass = None
        
        if check and img_pass:
            try:
                if int(img_pass) == 8:
                    if st.button("送信する", key="send_button"):
                        if st.session_state.mail:
                            st.info("パスワードはWebProgrammingです")
                        else:
                            st.error("メールアドレスにエラーがあります。")
                else:
                    st.error("認証をクリアしてください")
            except ValueError:
                st.error("画像の数字を入力してください")

st.sidebar.write("大妻花子さん、ようこそ")
with st.sidebar.expander("オプションを開く"):
    st.markdown('学生証情報表示')
    name = st.text_input("名前を入力してください")

if name:
    if name == "大妻花子":
        st.sidebar.success('大妻花子生年月日:1916年11月20日  \n学部:社会情報学部社会情報学科情報デザイン専攻  \n学籍番号:1313   \nメールアドレス:  \ns1313@cst.otsuma.ac.jp')
    else:
        st.sidebar.error('データが見つかりません')

with st.sidebar.expander("お問い合わせフォーム"):
    with st.sidebar.expander("お問い合わせ"):

        if "mail_sidebar" not in st.session_state:
            st.session_state.mail_sidebar = ""
        if "show_inquiry_form" not in st.session_state:
            st.session_state.show_inquiry_form = False
        if "selected_item" not in st.session_state:
            st.session_state.selected_item = "成績開示"

        mail = st.text_input("メールアドレスを入力してください", key="mail_sidebar_input")
        passbutton = st.button("送信する", key="submit_email_button")

        if passbutton:
            if mail == "s1313@cst.otsuma.ac.jp":
                st.session_state.mail_sidebar = mail
                st.session_state.show_inquiry_form = True
            else:
                st.sidebar.error('メールアドレスにエラーがあります')

        if st.session_state.show_inquiry_form:
            st.session_state.selected_item = st.radio(
                'お問い合わせ内容を選択してください。',
                ['成績開示', 'パスワード請求', 'その他'],
                key="sidebar_radio"
            )
            a_button = st.button("送信", key="inquiry_send_button")

            if a_button:
                if st.session_state.selected_item == '成績開示':
                    st.sidebar.info("提示可能な成績がありません")
                elif st.session_state.selected_item == 'パスワード請求':
                    st.sidebar.info("パスワードはWebProgrammingです")
                elif st.session_state.selected_item == 'その他':
                    st.sidebar.error("その他お問い合わせは現在ご利用できません")
