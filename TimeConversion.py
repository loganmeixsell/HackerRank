def timeConversion(s):
    time = ''
    if s[:2] == '12' and s[-2:] == 'AM':
        time = '0' + (str(int(s[:2]) - 12)) + s[2:-2]
    elif s[:2] == '12' and s[-2:] == 'PM':
        time = s[:-2]
    elif s[-2:] == 'PM':
        time = (str(int(s[:2]) + 12)) + s[2:-2]
    else:
        time = s[:-2]
    return time

time = '12:45:54PM'
test = timeConversion(time)
print (test)
timelist = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']
# for x in timelist:
#     time1 = '12:40:22PM'
#     time1 = x + time1[2:]
#     print (time1)
#     ok = timeConversion(time1)
#     print (ok)    