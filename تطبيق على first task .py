total_money= float(input ("How much money do you have ? \n")) 
total_things =int(input( " How many things will you buy ? \n")) 
cost = 0
for  i in range (total_things) :
    item_price = float(input(f"How much is the {i+1} item? \n"))
    cost+=item_price
Rest= total_money - cost
print(f"The cost Of things are :  {cost:.2}" )  
print(f"The Rest Of Money is :  {Rest:.2}" )  

