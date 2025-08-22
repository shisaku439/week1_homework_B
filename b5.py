# 入力値
input_text = input("データを入力してください(スペース区切り) > ")

# int型のリストに変換
input_list = input_text.split(" ")
int_list = [int(v) for v in input_list]


# 合計値の算出関数
def get_sum(list):
    total = 0
    for value in list:
        total += value
    return total


# 最大値算出関数
def get_max(list):
    max_value = list[0]
    for value in list:
        if max_value < value:
            max_value = value
    return max_value


# 最小値算出関数
def get_min(list):
    min_value = list[0]
    for value in list:
        if min_value > value:
            min_value = value
    return min_value


# 平均値算出関数
def get_ave(list):
    return get_sum(list) // len(list)


# 出力
print(f"合計値: {get_sum(int_list)}")
print(f"最大値: {get_max(int_list)}")
print(f"最小値: {get_min(int_list)}")
print(f"平均値: {get_ave(int_list)}")
