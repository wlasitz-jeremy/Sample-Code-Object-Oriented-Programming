kpm=1.61
print(f'{"MPH"}',f'{"KPH":>10}')
print(format('==========',"10s"), format("==========", "10s"))
for mph in range(10,80,10):
    kph=mph*kpm
    print(format(mph,"10d"),format(kph,"10.0f"))



