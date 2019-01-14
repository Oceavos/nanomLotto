
import random

rand_1 = random.randint(1, 45)
rand_2 = random.randint(1, 45)
rand_3 = random.randint(1, 45)
rand_4 = random.randint(1, 45)
rand_5 = random.randint(1, 45)
rand_6 = random.randint(1, 45)
bonus_num = random.randint(1, 45)

prize_num = [rand_1, rand_2, rand_3, rand_4, rand_5, rand_6]  # 랜덤
prize_bonus = bonus_num   # 랜덤

first = Second = Third = Fourth = Fifth = fail = 0
chk = 0
chk_2 = False


def Lotto_rand(rand_num):
    for i in range(0, 6):
        if i == 0:
            rand_bonus = random.randint(1, 45)

        rand_num.append(random.randint(1, 45))
        rand_bonus = random.randint(1, 45)
    print("Number :", rand_num, "// bonus : {}".format(rand_bonus))
    return rand_num, rand_bonus

def Lotto_chk(rand_num, rand_bonus):
    global chk, chk_2,first, Second, Third, Fourth, Fifth, fail

    for i in range(0, 6):
        for j in range(0, 6):
            if rand_num[i] == prize_num[j]:
                chk += 1
            if rand_bonus == prize_bonus:
                chk_2 = True

    if chk == 6:
        first += 1
    elif chk == 5 and chk_2 == True:
        Second += 1
    elif chk == 5:
        Third += 1
    elif chk == 4:
        Fourth += 1
    elif chk == 3:
        Fifth += 1
    else:
        if chk_2 == True:
            fail += 1
        else:
            fail += 1
print("로또 프로그램")
while True:
    first = Second = Third = Fourth = Fifth = fail = 0
    count = int(input("몇번 플레이? : "))
    print()
    if count == 0:
        break

    for i in range(0, count):
        chk = 0
        chk_2 = False
        rand_num = []

        rand_num, rand_bonus = Lotto_rand(rand_num)
        Lotto_chk(rand_num, rand_bonus)

    print()
    print("당첨번호")
    print("번호 :", prize_num, "// 보너스 : {}".format(prize_bonus))
    print()
    print("결과")
    print("1등 : %5d번, 2등 : %5d번, 3등 : %5d번\n"
          "4등 : %5d번, 5등 : %5d번, 꽝  : %5d번" % (first, Second, Third, Fourth, Fifth, fail))
