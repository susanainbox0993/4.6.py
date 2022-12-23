def computepay(h, r):
    if h>40:
        p=((h-40)*r*1.5)+(40*r)
    else:
        p=h*r
    return p

hrs = input("Enter Hours:")
hr = float(hrs)
rhrs = input("Enter Rater Per Hours")
rhr = float(rhrs)
p = computepay(hr, rhr)
print("Pay", p)