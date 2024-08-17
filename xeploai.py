n = float (input("Điểm trung bình GPA: "))
if n < 3.5:
    print ("Học lực Kém")
elif n >= 3.5 and n < 5.0:
    print ("Học lực Yếu")
elif n >= 5.0 and n < 7.0:
    print  ("Học lực Trung bình")
elif n >= 7.0 and n < 8.0:
    print ("Học lực Khá")
elif n >= 8.0 and n < 9.0:
    print ("Học lực Giỏi")
else:
    print ("Học lực Xuất sắc")
    