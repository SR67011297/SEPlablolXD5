from incomplete import Walk
from taxi import Taxi
from train import Train


trip = [ Walk("KMITL","KMITL SCB Bank",0.6),
         Taxi("KMITL SCB Bank","Ladkrabang Station",5),
         Train("Ladkrabang Station","Payathai Station",40,6),
         Taxi("Payathai Station","The British Council",3) ]

travel_cost = 0.0
for travel in trip:
   travel_cost += travel.find_cost()
print(travel_cost)
