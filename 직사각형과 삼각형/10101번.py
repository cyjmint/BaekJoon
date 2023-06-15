angle = []
for i in range(3):
    angle.append(int(input()))
    
if all(value == 60 for value in angle):
    print('Equilateral')
elif sum(angle) == 180 and (angle[0] == angle[1] or angle[0] == angle[2] or angle[1] == angle[2]):
    print('Isosceles')
elif sum(angle) == 180 and (angle[0] != angle[1] and angle[0] != angle[2] and angle[1] != angle[2]):
    print('Scalene')
else:
    print('Error')