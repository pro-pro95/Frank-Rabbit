#Hourly Rate

def computepay (h, r):
    return payrate

h = input("Enter Hours:")
r = input("Enter Rate:")
fh = float (h)
fr = float (r)

if fh > 40:
    reg = fh * fr
    otp = (fh - 40) * (fr * 0.5)

    payrate = reg + otp

else:
    payrate = fh * fr

payrate = computepay (h, r)
print("Pay", payrate)
