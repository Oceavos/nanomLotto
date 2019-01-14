import random

rand_1 = random.randint(1, 45)
rand_2 = random.randint(1, 45)
rand_3 = random.randint(1, 45)
rand_4 = random.randint(1, 45)
rand_5 = random.randint(1, 45)
rand_6 = random.randint(1, 45)
bonus_num = random.randint(1, 45)

prize_num = [rand_1, rand_2, rand_3, rand_4, rand_5, rand_6]
prize_bonus = bonus_num

print("당첨번호 : %s \n보너스 번호 : %d" % (prize_num, bonus_num))
