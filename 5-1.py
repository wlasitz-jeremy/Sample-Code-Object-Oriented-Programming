kpm=1.61
print(f'{"MPH"}',f'{"KPH":>10}')
print('==========',"==========")
for mph in range(10,80,10):
    kph=mph*kpm
    print(f'{mph:10d}{kph:>10.0f}')



for i in range (1,3):
    for j in range (1,3):
        print(f'{i}*{j}=',i*j)







