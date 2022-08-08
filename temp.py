class Pizzabase:
    def __init__(self,base_pizza):
        self.base_pizza=base_pizza
        self.baseprice={"Regular":50,"Whole wheat":75}
    def basetype(self):
        return ( self.baseprice[self.base_pizza])
class toppings:
    def __init__(self,topping):
        self.topping=topping
        self.topprize={"Mozerilla cheese":30,"Cheddar cheese":35,"Spinach":20,"Corn":15,"Mushroom":15,"Chicken":50,"Pepporoni":45}
    def topprice(self):
        return (self.topprize[self.topping])
class Drinks:
    def __init__(self,drinks):
        self.drinks=drinks
        self.extra_prize={"Pepsi":17,"7-UP":19,"Coke":20,"Lava Cake":95,"Chocolate brownie":86}
    def drinksprice(self):
        return (self.extra_prize[self.drinks])
def ordering(base_pizza,Sauce,topping):
    pb=Pizzabase(base_pizza)
    baseprice=pb.basetype()
    tpprice=list()
    dkprice=list()
    for i in topping:
        toppp=toppings(i)
        tpprice.append(str(toppp.topprice()))
    tpprice="+".join(tpprice)
    extra=input("Do you like drinks or deserts Yes \\ No")
    if extra=="Yes":
        drink=input("Enter your drink")
        drink=drink.split()
        for j in drink:
            dr=Drinks(j)
            dkprice.append(str(dr.drinksprice()))
        dkprice="+".join(dkprice)
        total=baseprice+eval(tpprice)+(eval(dkprice))
        discount=round(total*0.05,2)
        finaltotal=total-discount
        return (f"{baseprice} (base)+{tpprice} (toppings)+{dkprice} (drinks+deserts) - 5% discount{discount}= {finaltotal}")

    else:
        return (f"{baseprice} (base)+ {tpprice} (toppings)")
base_pizza=input("Base of the base Regular / Whole wheat:   ")
Sauce=input("Which sauce do you like Marinara sauce \\ Pesto sauce")
topping=input("What toppings do you like ")
topping=topping.split()
print(ordering(base_pizza,Sauce,topping))
print("TmFnZW5kcmEgdG9wcGVy")