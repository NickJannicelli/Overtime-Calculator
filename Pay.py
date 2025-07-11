def computepay(hours, rate):
    # print('in computepay', hours, rate)
    
    if hours > 40:
        reg = 40 * rate
        otp = (hours - 40) * (rate * 1.5)
        pay = reg + otp
    else:
        pay = hours * rate
    # print('returning', pay)
    return pay




sh = input('Enter Hours: ')
sr = input('Enter Rate: ')
fh = float(sh)
fr = float(sr)
xp = computepay(fh, fr)

print('Pay', xp)
