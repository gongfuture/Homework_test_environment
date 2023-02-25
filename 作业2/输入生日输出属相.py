birth = eval(input("请输入出生年份（四位年，例：1900）："))
# 天干：年份减3，除以10，没有余数就是天干的最后一个，余数是1对应 甲 ，是2对应 乙 ，依次往后推
# 地支：年份减3，除以12，没有余数就是地支的最后一个，余数是1对应 子 ，是2对应丑，依次往后推。
# 年份÷12求余数 0猴 1鸡 2狗 3猪 4鼠 5牛 6虎 7兔 8龙 9蛇 10马 11羊
tiangan_remain = (birth - 4) % 10
dizhi_remain = (birth - 4) % 12
shengxiao_remain = (birth - 4) % 12
tiangan_list = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
dizhi_list = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
shengxiao_list = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
tiangan = tiangan_list[tiangan_remain]
dizhi = dizhi_list[dizhi_remain]
shengxiao = shengxiao_list[shengxiao_remain]
# print(tiangan_remain,dizhi_remain,shengxiao_remain)
print("您的属相是：{}".format(tiangan + dizhi + shengxiao))
