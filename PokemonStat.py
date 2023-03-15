import math

flag2 = False
flag3 = False

while(not flag2):
    try:
        a = int(input("종족값:"))
        if (a > 0 and a <= 300):
            flag2 = True
        else:
            print("1과 300 사이의 값을 입력하세요.")

    except:
        print("유효하지 않은 값입니다.")

while(not flag3):
    try:
        effort = int(input("노력치:"))
        if effort >= 0 and effort <=252:
            flag3 = True
        else:
            print("0과 252 사이의 값을 입력하세요.")
    except:
        print("유효하지 않은 값입니다.")
        
stat = (a * 2 + 31 + effort/4) * 0.5 + 5
flag = False
while(not flag):
    character = input("성격 보정 여부(y or n):")
    if(character == 'n' or character == 'N'):
        flag = True
        print("성격 보정 안함")
    elif (character == 'y' or character == 'Y'):
        flag = True
        print("성격 보정 함")
        stat = stat * 1.1
    else:
        print("y 또는 n으로 입력하세요.")

realstat = math.floor(stat)

print("실능력치는",realstat, "입니다.")


