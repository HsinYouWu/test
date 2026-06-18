print("Reverse Column Zigzag Multiplication Table:")
# 給兩個 lists，a 給被乘數，b 給乘數
a = list(range(1, 10))
b = list(range(1, 10))

i = 0
# 每換一行乘數加 1，zigzag 用裡面的判斷式
while i <= 8:
    j = 1 # 逆著數 list 要從 -1 開始取
    # 先給一個空字串 text
    text = ""
    # 同一行被乘數從大到小，這裡使用逆著數 list
    while j <= 9:
        # 被乘數是奇數時乘數小到大(順著數list)，乘數是偶數時乘數大到小(逆著數list)
        if j % 2 == 1:
            ans = a[-j]*b[i]
            text += f"{a[-j]}*{b[i]}={ans}\t"
        else:
            ans = a[-j]*b[-i-1]
            text += f"{a[-j]}*{b[-i-1]}={ans}\t"
        j += 1
    # 每行算完再 print
    print(text)
    i += 1