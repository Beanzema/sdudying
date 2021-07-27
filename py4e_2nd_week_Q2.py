monthly_payment = int(input("세전 월급이 얼마신가요?: (만원 단위 정수 입력)"))
yearly_payment = 12*monthly_payment

print("세전 연봉: ", yearly_payment,"만원", sep="")
print("세후 연봉: ", end="")
if yearly_payment <= 1200:
    yearly_payment *= (1-0.06)
elif yearly_payment <= 4600:
    yearly_payment *= (1-0.15)
elif yearly_payment <= 8800:
    yearly_payment *= (1-0.24)
elif yearly_payment <= 15000:
    yearly_payment *= (1-0.35)
elif yearly_payment <= 30000:
    yearly_payment *= (1-0.38)
elif yearly_payment <= 50000:
    yearly_payment *= (1-0.40)
else:
    yearly_payment *= (1-0.42)
print(int(yearly_payment),"만원",sep="")