# 入力値
max_row = int(input("行数を入力してください: "))
max_column = int(input("列数を入力してください: "))

# ９９の計算
for kakerukazu in range(1, max_row + 1):
    for kakerarerukazu in range(1, max_column + 1):
        calc = kakerarerukazu * kakerukazu
        formated_calc = str(calc).rjust(2, " ")
        text = f"{kakerarerukazu} x {kakerukazu} = {formated_calc} | "
        print(text, end="")
    print("")
