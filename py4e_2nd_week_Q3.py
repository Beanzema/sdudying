s_name = input("학생의 이름 입력: ")
s_grade = int(input("위 학생 성적 입력: "))
s_alphbet = "F"

print("학생이름 : ",s_name,sep="")
print("점수 : ",s_grade,"점",sep="")

if s_grade >= 95:
    s_alphbet = "A+"
elif s_grade >= 90:
    s_alphbet = "A"
elif s_grade >= 85:
    s_alphbet = "B+"
elif s_grade >= 80:
    s_alphbet = "B"
elif s_grade >= 75:
    s_alphbet = "C+"
elif s_grade >= 70:
    s_alphbet = "C"
elif s_grade >= 65:
    s_alphbet = "D+"
elif s_grade >= 60:
    s_alphbet = "D"

print("학점 : ",s_alphbet,sep="")