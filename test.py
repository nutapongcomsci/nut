def grad_assign(s):
    if s>=80:
        return "A"
    elif s>=75:
        return "B+"
    elif s>=70:
         return "B"
    elif s>=65:
         return "C+"
    elif s>=60:
         return "C"
    elif s>=55:
         return "D+"
    elif s>=50:
         return "D"
    else :
         return "F"
def grade_req(eng, math):
    if eng > 70 and math < 80:
        return True
    else:
  
