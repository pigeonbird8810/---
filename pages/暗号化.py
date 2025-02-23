num = input("暗号化したい文字（ひらがな）:")
return_num = []

# elif later == "":
#     return_num += ""

for later in num:
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

print(return_num)
code = []

for i in range (len(return_num)):
    if return_num[i] == "a":
        code += "+"
    elif return_num[i] == "i":
        code += "-"
    elif return_num[i] == "u":
        code += "*"
    elif return_num[i] == "e":
        code += "%"
    elif return_num[i] == "o":
        code += "="
    elif return_num[i] == "k":
        code += "1"
    elif return_num[i] == "s":
        code += "2"
    elif return_num[i] == "t":
        code += "3"
    elif return_num[i] == "n":
        code += "4"
    elif return_num[i] == "h":
        code += "5"
    elif return_num[i] == "m":
        code += "6"
    elif return_num[i] == "y":
        code += "7"
    elif return_num[i] == "r":
        code += "8"
    elif return_num[i] == "w":
        code += "9"
    else:
        code += "?"
print(code)
code_text = ""
for r in range(len(code)):
    code_text += str(code[r])
print(code_text)