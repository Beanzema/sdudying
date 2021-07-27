age = int(input("나이 입력: "))
pay_way = input("지불 방식 입력(현금 또는 카드): ")

print("나이: %i 세" %age)
print("지불 유형: %s" %pay_way)

print("버스요금: ",end =" ")
if (age < 8) or (age >= 75):
    print("0원(면제)")
elif age < 14:
    print("450원")
elif age < 20:
    if pay_way == "카드":
        print("720원")
    else:
        print("1000원")
else:
    if pay_way == "카드":
        print("1200원")
    else:
        print("1300원")