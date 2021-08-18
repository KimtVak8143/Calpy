yy = int(input("Enter :"))
day = (yy-1) % 400
print(day)
d1 = (day//100)*5
print(d1)
d2 = ((day % 100) - (day % 100)//4)
print(d2)
d3 = ((day % 100)//4)*2
print(d3)
d4 = d1+d2+d3
print(d4)
day = day % 7
print(day)
