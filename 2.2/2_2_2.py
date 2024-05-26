let_3 = [input() for _ in range(3)]
en_let = "AaBCcEeHKMOoPpTXxy"
ru_let = "АаВСсЕеНКМОоРрТХху"
flag = ""
for i in let_3:
    if i in en_let:
        flag += "e"
    elif i in ru_let:
        flag += 'r'
if "r" not in flag:
    print("en")
elif "e" not in flag:
    print("ru")
else:
    print("mix")