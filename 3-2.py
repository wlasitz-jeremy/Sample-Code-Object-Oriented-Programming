grd = int(input('Enter grade point'))
if grd>90 and grd<=100:
    print('A+')
elif grd>85 and grd<=89:
    print('A')
elif grd>80 and grd<=84:
    print('A-')
elif grd>77 and grd<=79:
    print('B+')
elif grd>73 and grd<=76:
    print('B')
elif 70<grd<72:
    print('B-')
elif grd>67 and grd<=69:
    print('C+')
elif grd>63 and grd<=66:
    print('C')
elif grd>60 and grd<=62:
    print('C-')
elif grd>55 and grd<=59:
    print('D+')
elif grd>50 and grd<=54:
    print('D')
else:
    print('F')
