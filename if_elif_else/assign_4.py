temperature = float(input("enter the temperature °C:"))
is_raining = input("is it  raining (yes/no)")
if temperature > 30:
     if is_raining == "yes":
         print("stay indoors and watch a movie:")
     else:
        print("go swimming")
elif 20<temperature <=30:
     if is_raining == "yes" :
        print("visi museum")    
     else:
         print("perfect for a picnic")
elif 10<temperature <=20:
     if is_raining =="yes" :
         print("indoor sports recommended")
     else:
         print("go for a walk")
else: 
     if temperature <=10:
        if is_raining == "yes":
            print("stay home with hot chocolate")
        else:
            print("ice skating would be fun")
