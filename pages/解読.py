import streamlit as st

st.header("暗号解読プログラム")

if "code" not in st.session_state:
    st.session_state.code = ""

st.session_state.code = st.text_input("暗号を入力")

def make_text1(code):
    code_text = []
    for later in code:
        if later == "+":
            code_text  += "a"
        elif later == "-":
            code_text += "i"
        elif later == "#":
            code_text += "u"
        elif later == "%":
            code_text += "e"
        elif later == "=":
            code_text += "o"
        elif later == "1":
            code_text += "k"
        elif later == "2":
            code_text += "s"
        elif later == "3":
            code_text += "t"
        elif later == "4":
            code_text += "n"
        elif later == "5":
            code_text += "h"
        elif later == "6":
            code_text += "m"
        elif later == "7":
            code_text += "y"
        elif later == "8":
            code_text += "r"
        elif later == "9":
            code_text += "w"
        else:
            code_text += "?"
    return code_text

def make_text2(num_text):
    i = 0
    if "text" not in st.session_state:
        st.session_state.text = ""
    st.session_state.text = ""
    while i <= len(num_text)-1:
        if (num_text[i] == "a")or(num_text[i] == "i")or(num_text[i] == "u")or(num_text[i] == "e")or(num_text[i] == "o"):
            if num_text[i] == "a":
                st.session_state.text += "あ"
            elif num_text[i] == "i":
                st.session_state.text += "い"
            elif num_text[i] == "u":
                st.session_state.text += "う"
            elif num_text[i] == "e":
                st.session_state.text += "え"
            elif num_text[i] == "o":
                st.session_state.text += "お"
            i += 1 
        elif num_text[i] == "k":
            if num_text[i+1] == "a":
                st.session_state.text += "か"
            elif num_text[i+1] == "i":
                st.session_state.text += "き"
            elif num_text[i+1] == "u":
                st.session_state.text += "く"
            elif num_text[i+1] == "e":
                st.session_state.text += "け"
            elif num_text[i+1] == "o":
                st.session_state.text += "こ"
            i += 2
        elif num_text[i] == "s":
            if num_text[i+1] == "a":
                st.session_state.text += "さ"
            elif num_text[i+1] == "i":
                st.session_state.text += "し"
            elif num_text[i+1] == "u":
                st.session_state.text += "す"
            elif num_text[i+1] == "e":
                st.session_state.text += "せ"
            elif num_text[i+1] == "o":
                st.session_state.text += "そ"
            i += 2
        elif num_text[i] == "t":
            if num_text[i+1] == "a":
               st.session_state.text += "た"
            elif num_text[i+1] == "i":
               st.session_state.text += "ち"
            elif num_text[i+1] == "u":
               st.session_state.text += "つ"
            elif num_text[i+1] == "e":
                st.session_state.text += "て"
            elif num_text[i+1] == "o":
                st.session_state.text += "と"
            i += 2
        elif num_text[i] == "n":
            if num_text[i+1] == "a":
                st.session_state.text += "な"
            elif num_text[i+1] == "i":
                st.session_state.text += "に"
            elif num_text[i+1] == "u":
                st.session_state.text += "ぬ"
            elif num_text[i+1] == "e":
                st.session_state.text += "ね"
            elif num_text[i+1] == "o":
                st.session_state.text += "の"
            elif num_text[i+1] == "n":
                st.session_state.text += "ん"
            i += 2
        elif num_text[i] == "h":
            if num_text[i+1] == "a":
                st.session_state.text += "は"
            elif num_text[i+1] == "i":
                st.session_state.text += "ひ"
            elif num_text[i+1] == "u":
                st.session_state.text += "ふ"
            elif num_text[i+1] == "e":
                st.session_state.text += "へ"
            elif num_text[i+1] == "o":
                st.session_state.text += "ほ"
            i += 2
        elif num_text[i] == "m":
            if num_text[i+1] == "a":
                st.session_state.text += "ま"
            elif num_text[i+1] == "i":
                st.session_state.text += "み"
            elif num_text[i+1] == "u":
                st.session_state.text += "む"
            elif num_text[i+1] == "e":
                st.session_state.text += "め"
            elif num_text[i+1] == "o":
                st.session_state.text += "も"
            i += 2
        elif num_text[i] == "y":
            if num_text[i+1] == "a":
                st.session_state.text += "や"
            elif num_text[i+1] == "u":
                st.session_state.text += "ゆ"
            elif num_text[i+1] == "o":
                st.session_state.text += "よ"
            i += 2
        elif num_text[i] == "r":
            if num_text[i+1] == "a":
                st.session_state.text += "ら"
            elif num_text[i+1] == "i":
                st.session_state.text += "り"
            elif num_text[i+1] == "u":
                st.session_state.text += "る"
            elif num_text[i+1] == "e":
                st.session_state.text += "れ"
            elif num_text[i+1] == "o":
                st.session_state.text += "ろ"
            i += 2
        elif num_text[i] == "w":
            if num_text[i+1] == "a":
                st.session_state.text += "わ"
            elif num_text[i+1] == "o":
                st.session_state.text += "を"
            i += 2
        else:
            st.session_state.text += "?"
            i += 1
    return st.session_state.text
if st.button(label="解読！"):
    text1 = make_text1(st.session_state.code)
    text2 = make_text2(text1)
    st.write(f"元の文字列は　「{text2}」")