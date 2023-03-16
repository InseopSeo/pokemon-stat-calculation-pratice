import math

flag_a = False
flag_effort = False

while(not flag_a):
    try:
        a = int(input("종족값:"))
        if (a > 0 and a <= 300):
            flag_a = True
        else:
            print("1과 300 사이의 값을 입력하세요.")

    except:
        print("유효하지 않은 값입니다.")

while(not flag_effort):
    try:
        effort = int(input("노력치:"))
        if effort >= 0 and effort <=252:
            flag_effort = True
        else:
            print("0과 252 사이의 값을 입력하세요.")
    except:
        print("유효하지 않은 값입니다.")
        
stat = (a * 2 + 31 + effort/4) * 0.5 + 5
flag_ch = False
while(not flag_ch):
    character = input("성격 보정 여부(y or n):")
    if(character == 'n' or character == 'N'):
        flag_ch = True
        print("성격 보정 안함")
    elif (character == 'y' or character == 'Y'):
        flag_ch = True
        print("성격 보정 함")
        stat = stat * 1.1
    else:
        print("y 또는 n으로 입력하세요.")

realstat = math.floor(stat)

print("실능력치는",realstat, "입니다.")


