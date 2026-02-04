kpm=1.61
print(f'{"MPH"}',f'{"KPH":>8}')

for mph in range(10,80,10):
    kph=mph*kpm
    print(f'{mph}{kph:>9.0f}')




