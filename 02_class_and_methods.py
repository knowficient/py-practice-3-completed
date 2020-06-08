# Write a Python Class named ChargeCar
# constructed by electric car name and its battery capacity
# And 2 methods:
#   1. Charging time (h) = battery capacity / charging power
#   2. Charging cost ($) = battery capacity * charging rate

class ChargeCar:
    rate_pkwh = 0.414          # set the rate (unit in $)
    charging_kwh = 43          # Set the charging capacity of station
    def __init__(self, name, batt_capacity):
        self.name = name                    # initialise the name of object
        self.batt_capacity = batt_capacity  # initialise the battery capacity of object
        print("Electric Car =",self.name)
        print("Battery Capacity =",self.batt_capacity,"kWh")

    def get_charge_time(self):              #define method 1: charge_time
        time = round((self.batt_capacity/self.charging_kwh),2)  # compute full charging time and round 2 dec places
        print("Full Charging Time = ",time, "hrs")

    def get_charge_cost(self):              #define methd 2: charge_cost
        cost = round((self.batt_capacity*self.rate_pkwh),2)     # compute charging cost and round 2 dec places
        print("Charging Cost = $",cost)

# Tesla 3, battery capacity 75 kWh
Tesla3 = ChargeCar("Tesla 3", 75)
Tesla3.get_charge_time()
Tesla3.get_charge_cost()

# Nissan Leaf, battery capacity 30 kWh
NissanLeaf = ChargeCar("Nissan Leaf", 30)
NissanLeaf.get_charge_time()
NissanLeaf.get_charge_cost()
