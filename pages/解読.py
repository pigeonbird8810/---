code = input("暗号を入力:")
print(code)
code_text = []
for later in code:
    if later == "+":
        code_text  += "a"
    elif later == "-":
        code_text += "i"
    elif later == "*":
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
print(code_text)
i = 0
text = ""
while i <= len(code_text)-1:
    print(f"{i}回目の復元")
    if code_text[i] == "a"or"i"or"u"or"e"or"o":
        if code_text[i] == "a":
            text += "あ"
        elif code_text[i] == "i":
            text += "い"
        elif code_text[i] == "u":
            text += "う"
        elif code_text[i] == "e":
            text += "え"
        elif code_text[i] == "o":
            text += "お"
        i += 1 
    elif code_text[i] == "k":
        print("k")
        if code_text[i+1] == "a":
            print("a")
            text += "か"
        elif code_text[i+1] == "i":
            text += "き"
        elif code_text[i+1] == "u":
            text += "く"
        elif code_text[i+1] == "e":
            text += "け"
        elif code_text[i+1] == "o":
            text += "こ"
        i += 2
    elif code_text[i] == "s":
        if code_text[i+1] == "a":
            text += "さ"
        elif code_text[i+1] == "i":
            text += "し"
        elif code_text[i+1] == "u":
            text += "す"
        elif code_text[i+1] == "e":
            text += "せ"
        elif code_text[i+1] == "o":
            text += "そ"
        i += 2
    elif code_text[i] == "t":
        if code_text[i+1] == "a":
            text += "た"
        elif code_text[i+1] == "i":
            text += "ち"
        elif code_text[i+1] == "u":
            text += "つ"
        elif code_text[i+1] == "e":
            text += "て"
        elif code_text[i+1] == "o":
            text += "と"
        i += 2
    elif code_text[i] == "n":
        if code_text[i+1] == "a":
            text += "な"
        elif code_text[i+1] == "i":
            text += "に"
        elif code_text[i+1] == "u":
            text += "ぬ"
        elif code_text[i+1] == "e":
            text += "ね"
        elif code_text[i+1] == "o":
            text += "の"
        elif code_text[i+1] == "n":
            text += "ん"
        i += 2
    elif code_text[i] == "h":
        if code_text[i+1] == "a":
            text += "は"
        elif code_text[i+1] == "i":
            text += "ひ"
        elif code_text[i+1] == "u":
            text += "ふ"
        elif code_text[i+1] == "e":
            text += "へ"
        elif code_text[i+1] == "o":
            text += "ほ"
        i += 2
    elif code_text[i] == "m":
        if code_text[i+1] == "a":
            text += "ま"
        elif code_text[i+1] == "i":
            text += "み"
        elif code_text[i+1] == "u":
            text += "む"
        elif code_text[i+1] == "e":
            text += "め"
        elif code_text[i+1] == "o":
            text += "も"
        i += 2
    elif code_text[i] == "y":
        if code_text[i+1] == "a":
            text += "や"
        elif code_text[i+1] == "u":
            text += "ゆ"
        elif code_text[i+1] == "o":
            text += "よ"
        i += 2
    elif code_text[i] == "r":
        if code_text[i+1] == "a":
            text += "ら"
        elif code_text[i+1] == "i":
            text += "り"
        elif code_text[i+1] == "u":
            text += "る"
        elif code_text[i+1] == "e":
            text += "れ"
        elif code_text[i+1] == "o":
            text += "ろ"
        i += 2
    elif code_text[i] == "w":
        if code_text[i+1] == "a":
            text += "わ"
        elif code_text[i+1] == "o":
            text += "を"
        i += 2
    else:
        text += "?"
        i += 1
    

print(text)