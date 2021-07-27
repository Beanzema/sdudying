import random

my = input("안 내면 진거 가위 바위 보: ")
print("나: ", my)
if my == "가위":
    my = 0
elif my == "바위":
    my = 1
elif my == "보":
    my = 2
else:
    my = 3
computer = random.randint(0,2)
print("컴퓨터:",end='')
if computer == 0:
     print("가위")
elif computer == 1:
    print("바위")
elif computer == 2:
    print("보")

if (computer-my) == 0:
    print("비겼습니다!")
elif ((computer-my) == 1) or ((computer-my) == -2):
    print("컴퓨터 승리!")
elif ((my-computer) == 1) or ((my-computer) == -2):
    print("당신의 승리!")