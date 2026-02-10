rent = int(input("enter your hostel rent : "))
food_charge = int(input("enter the amound of food ordered : "))
electricity_spend = int(input("enter the total of electricity spend : "))
charge_per_unit = int(input("enter the charge per unit : "))
persons = int(input("enter the number of persons living in the room :  "))
total_bill = electricity_spend* charge_per_unit


total_rent = (rent + food_charge + total_bill) // persons
print("Each person will pay : ", total_rent)