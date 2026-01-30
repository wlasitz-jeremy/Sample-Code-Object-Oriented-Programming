course = 'Python'
print(f'{course:>20}')
print(f'{course:<20}')
print(f'{course:20}')
print(f'{"Centered":^20}\n')

cadtd= 1.2798
usdtd= 0.940
cadytd= 2.7843
usdytd= 2.050
changeusd= (usdtd-usdytd)
changecad= (cadtd-cadytd)
print(f'{"Date":^10}{"Rate":^20}')
print(f'Cad Yesterday{cadytd:^17.4f}')
print(f'Cad Today{cadtd:^24.4f}')
print(f'Cad Change{changecad:^22.4f}')
print(f'Usd Yesterday{usdytd:^16.4f}')
print(f'Usd Today{cadtd:^24.4f}')
print(f'Usd Change{changeusd:^22.4f}')





num=2
while num<=512:
    print(num)
    num+=2






