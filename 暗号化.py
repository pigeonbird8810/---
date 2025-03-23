import streamlit as st

st.header("暗号化プログラム")

if "num" not in st.session_state:
    st.session_state.num = ""
st.session_state.num = st.text_input(label="ここに暗号化したい文字列を入れてね！（ひらがなでね！）")

# elif later == "":
#     return_num += "



def make_code(text):
    return_num = []
    for later in text:
        if later == "あ":
            return_num += "a"
        elif later == "い":
            return_num += "i"
        elif later == "う":
            return_num += "u"
        elif later == "え":
            return_num += "e"
        elif later == "お":
            return_num += "o"
        elif later == "か":
            return_num += "ka"
        elif later == "き":
            return_num += "ki"
        elif later == "く":
            return_num += "ku"
        elif later == "け":
            return_num += "ke"
        elif later == "こ":
            return_num += "ko"
        elif later == "さ":
            return_num += "sa"
        elif later == "し":
            return_num += "si"
        elif later == "す":
            return_num += "su"
        elif later == "せ":
            return_num += "se"
        elif later == "そ":
            return_num += "so"
        elif later == "た":
            return_num += "ta"
        elif later == "ち":
            return_num += "ti"
        elif later == "つ":
            return_num += "tu"
        elif later == "て":
            return_num += "te"
        elif later == "と":
            return_num += "to"
        elif later == "な":
            return_num += "na"
        elif later == "に":
            return_num += "ni"
        elif later == "ぬ":
            return_num += "nu"
        elif later == "ね":
            return_num += "ne"
        elif later == "の":
            return_num += "no"
        elif later == "は":
            return_num += "ha"
        elif later == "ひ":
            return_num += "hi"
        elif later == "ふ":
            return_num += "hu"
        elif later == "へ":
            return_num += "he"
        elif later == "ほ":
            return_num += "ho"
        elif later == "ま":
            return_num += "ma"
        elif later == "み":
            return_num += "mi"
        elif later == "む":
            return_num += "mu"
        elif later == "め":
            return_num += "me"
        elif later == "も":
            return_num += "mo"
        elif later == "や":
            return_num += "ya"
        elif later == "ゆ":
            return_num += "yu"
        elif later == "よ":
            return_num += "yo"
        elif later == "ら":
            return_num += "ra"
        elif later == "り":
            return_num += "ri"
        elif later == "る":
            return_num += "ru"
        elif later == "れ":
            return_num += "re"
        elif later == "ろ":
            return_num += "ro"
        elif later == "わ":
            return_num += "wa"
        elif later == "を":
            return_num += "wo"
        elif later == "ん":
            return_num += "nn"
        else:
            return_num += "?"
    return return_num



def make_code2(before_text):
    code = []
    for i in range (len(before_text)):
        if before_text[i] == "a":
            code += "+"
        elif before_text[i] == "i":
            code += "-"
        elif before_text[i] == "u":
            code += "*"
        elif before_text[i] == "e":
            code += "%"
        elif before_text[i] == "o":
            code += "="
        elif before_text[i] == "k":
            code += "1"
        elif before_text[i] == "s":
            code += "2"
        elif before_text[i] == "t":
            code += "3"
        elif before_text[i] == "n":
            code += "4"
        elif before_text[i] == "h":
            code += "5"
        elif before_text[i] == "m":
            code += "6"
        elif before_text[i] == "y":
            code += "7"
        elif before_text[i] == "r":
            code += "8"
        elif before_text[i] == "w":
            code += "9"
        else:
            code += "?"
    return code

def make_code3(before_code):
    if "code_text" not in st.session_state:
        st.session_state.code_text = ""
    if "before" not in st.session_state:
        st.session_state.before = []
    st.session_state.code_text = ""
    st.session_state.before = []
    st.session_state.before = before_code
    for r in range(len(st.session_state.before)):
        st.session_state.code_text += str(st.session_state.before[r])
    return st.session_state.code_text

if st.button(label="変換！"):
    code1 = make_code(st.session_state.num)
    code2 = make_code2(code1)
    code3 = make_code3(code2)
    st.write(f"暗号は {code3}")