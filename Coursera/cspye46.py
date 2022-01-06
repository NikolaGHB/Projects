#v.1

def computepay(h, r):
    ot_hrs = float(h)-40
    gross = float(h)*float(r)
    gross40 = 40*float(r)
    gross_ot = float(ot_hrs)*(float(r)*1.5)

    if float(h) <= 40:
        return gross
    else:
        return(gross40 + gross_ot)

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please input numeric value.")
    quit()

p = computepay(h, r)
print("Pay", p)

#v2

def computepay(h, r):
    ot_hrs = float(h)-40
    gross = float(h)*float(r)
    gross40 = 40*float(r)
    gross_ot = float(ot_hrs)*(float(r)*1.5)

    if float(h) <= 40:
        return gross
    else:
        return(gross40 + gross_ot)

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please input numeric value.")
    quit()

p = computepay(h, r)
print("Pay", p)
