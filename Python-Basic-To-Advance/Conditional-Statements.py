# syntex --> if-elif-else
# indentation --> Proper spacing

age = 25

# if(age >= 18):
#     print("Gaurav! You can vote now.")

# if(True): # always true
#     print("Gaurav! You can learn anytime.")

traffic_light = "Green"
if(traffic_light == "red"): # if alwayse check
    print("STOP")
elif(traffic_light == "Green"): # elif comes only after if - elif only check when if statment is False. 
    print("GO")
elif(traffic_light == "Yellow"):
    print("See and Go")
else: # last and only once 
    print("Traffic light is broken")


# Nesting

if(age >=  18):
    if(age > 80):
        print("Can Not Drive because age is more than 80")
    else:
        print("You can Drive!!")
else:
    print("Can not deive because age is less than 18 years")