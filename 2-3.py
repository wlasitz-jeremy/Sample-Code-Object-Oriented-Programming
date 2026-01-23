sd=float(input('Enter starting distance '))
ed=float(input('Enter stopping distance '))
st=float(input('Enter starting time '))
et=float(input('Enter stopping time '))
d=ed-sd
t=et-st
v1=sd/st
v2=ed/et
cv=float(v2)-float(v1)
a=float(cv)/float(t)
print(f'"Velocity="{v2}m/s\nAccelleration="{a}m/s**2')