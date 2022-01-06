#

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    ot_hrs = float(hrs)-40
    gross = float(hrs)*float(rate)
    gross40 = 40*float(rate)
    gross_ot = float(ot_hrs)*(float(rate)*1.5)
except:
    print("Error, please input numeric value.")

if float(hrs) <= 40:
    print(gross)
else:
    print(gross40 + gross_ot)



###############

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

if hrs or rate != float():
    print("Error, please input numeric value!:")
