import random

# 入力値
dice_side = int(input("サイコロの面の数は?: "))
play_cout = int(input("何回振りますか?: "))

# サイコロを指定の回数振る
result_list = []
for i in range(1, play_cout + 1):
    result_list.append(random.randint(1, dice_side))

# 出力
print(result_list)
