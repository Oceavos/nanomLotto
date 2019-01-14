import random

rand_1 = random.randint(1, 45)
rand_2 = random.randint(1, 45)
rand_3 = random.randint(1, 45)
rand_4 = random.randint(1, 45)
rand_5 = random.randint(1, 45)
rand_6 = random.randint(1, 45)
bonus_num = random.randint(1, 45)

your_num = [rand_1, rand_2, rand_3, rand_4, rand_5, rand_6]
your_bonus = bonus_num

result_rand_1 = random.randint(1, 45)
result_rand_2 = random.randint(1, 45)
result_rand_3 = random.randint(1, 45)
result_rand_4 = random.randint(1, 45)
result_rand_5 = random.randint(1, 45)
result_rand_6 = random.randint(1, 45)
result_bonus_num = random.randint(1, 45)

answer_result = [result_rand_1, result_rand_2, result_rand_3, result_rand_4, result_rand_5, result_rand_6]
answer_bonus = result_bonus_num

if answer_result == answer_bonus:
    print("당신은 행운인! 1등 당첨!")
else:
    print("아쉽게(?) 1등은 실패!")
