#Collect the data
hour=int(input("Enter the hour:"))
if (hour<1) or (hour>12):
    print("Enter a valid hour value!")
    quit()

min=int(input("Enter the minute:"))
if (min<0) or (min>59):
    print("Enter a valid minute value!")
    quit()

am_or_pm=input("is it am or pm?").lower()
if am_or_pm not in ["am", "pm"]:
    print("Enter an am or pm value!")
    exit()
#24 hrs conversion function
def time_convert(hour,min,am_or_pm):
    #am conversion
    if am_or_pm=="am":
        if hour >= 10:
            if hour==12:
                 hour='00'
            else:
                hour
        else:
            hour=f"0{hour}"
            
    #pm conversion
    else:
        hour=hour+12 if hour<12 else hour

    print(f"{hour}{min} hrs")



time_convert(hour,min,am_or_pm)
