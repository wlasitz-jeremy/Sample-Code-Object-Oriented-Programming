course = 'Python'
print(f'{course:>20}')
print(f'{course:<20}')
print(f'{course:20}')
print(f'{"Centered":^20}\n')

cadtd= 1
usdtd= 0.74357
cadytd= 1
usdytd= 0.73658
changeusd= (usdtd-usdytd)
changecad= (cadtd-cadytd)
print(f'{"Date":^10}{"Rate":^20}')
print(f'Cad Yesterday{cadytd:^17.4f}')
print(f'Cad Today{cadtd:^24.4f}')
print(f'Cad Change{changecad:^22.4f}')
print(f'Usd Yesterday{usdytd:^16.4f}')
print(f'Usd Today{cadtd:^24.4f}')
print(f'Usd Change{changeusd:^22.4f}')




















