# 台積電（TSMC）股價變動換算小工具

# ===== 1. 題目給定的固定參數 =====
base_price = 1000.0          # 基準股價（元/股）
lots = 10                    # 買入張數
shares_per_lot = 1000        # 每張股數
total_shares = lots * shares_per_lot   # 總股數
fee_rate = 0.001425          # 手續費率（0.1425%）
tax_rate = 0.003             # 證券交易稅率（0.3%，只在賣出時收）

# ===== 2. 讓使用者輸入今日漲跌幅(%) =====
change_pct = float(input("請輸入台積電今日漲跌幅(%)（例如 1.25 或 -0.80）："))

# ===== 3. 計算今日股價 =====
today_price = base_price * (1 + change_pct / 100)

# ===== 4. 計算持股市值變化 =====
base_value = base_price * total_shares
today_value = today_price * total_shares
value_change = today_value - base_value

# ===== 5. 計算等效每股變動金額 =====
delta_price = today_price - base_price

# ===== 6. 計算損益兩平賣出價與所需漲幅 =====
buy_cost = base_price * total_shares * (1 + fee_rate)
break_even_sell_price = base_price * (1 + fee_rate) / (1 - fee_rate - tax_rate)
break_even_pct = (break_even_sell_price / base_price - 1) * 100

# ===== 7. 輸出結果 =====
print("\n=== 台積電股價變動換算結果 ===")
print(f"基準股價： {base_price} 元/股")
print(f"持股數量： {lots} 張（ {total_shares} 股）")
print(f"今日漲跌幅： {change_pct} %\n")

print("1) 今日股價")
print(f"{today_price} 元/股\n")

print("2) 持股市值變化")
print(f"基準市值： {base_value} 元")
print(f"今日市值： {today_value} 元")
print(f"市值變化： {value_change} 元\n")

print("3) 等效每股變動金額")
print(f"每股變動： {delta_price:+.2f} 元/股\n")

print("4) 損益兩平漲幅（含手續費與賣出交易稅）")
print(f"手續費率（買/賣）： {fee_rate * 100} %")
print(f"交易稅率（賣出）： {tax_rate * 100} %")
print(f"兩平所需賣出價： {break_even_sell_price} 元/股")
print(f"兩平所需漲幅： {break_even_pct} %")