temp=float(input("Enter your body temperature in celcius: "))
if(temp>=37 and temp<=37.4):
    print("Normal Body Temperature")
elif(temp<37):
    print("Hypothermia!! Emergency")
elif(temp>=37.5 and temp<=38.5):
    print("Mild Fever!")
elif(temp>38.5 and temp<=44):
    print("High Fever")
else:
    print("Enter vlaid Body Temperature!!")