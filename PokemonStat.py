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
    character = input("성격 보정 여부(up or down or no):")
    if(character == "up" or character == "UP"):
        flag_ch = True
        print("성격 상승 보정")
        stat = stat * 1.1
    elif (character == "down" or character == "DOWN"):
        flag_ch = True
        print("성격 하락 보정")
        stat = stat * 0.9
    elif (character == "no" or character == "NO"):
        flag_ch = True
        print("성격 보정 없음")
    else:
        print("up 또는 down 또는 no로 입력하세요.")

realstat = math.floor(stat)

print("실능력치는",realstat, "입니다.")


