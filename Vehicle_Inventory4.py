#Portfolio Project Option 1, Vehicle Inventory Program
#By Tessa Lulloff



#Create class Automobile
class Automobile:
	id = 0 #Added ID to allow for easier identification for updating and removal.
	def __init__(self, make, model, color, year, mileage):
		self._make = make
		self._model = model
		self._color = color
		self._year = year
		self._mileage = mileage
		self._id = Automobile.id
		Automobile.id += 1
	def __repr__(self):
		return f"ID:{self._id} MAKE:{self._make} MODEL:{self._model} COLOR:{self._color} YEAR:{self._year} MILEAGE:{self._mileage}\n\n"
		#This is to return the values of the object instead of the memory location.


#Start with empty list 
inventory = []

#Function to add vehicle to list outside of class
def add_vehicle():
	try:
		make = input("Enter new vehicle make:\n")
		model = input("Enter new vehicle model:\n")
		color = input("Enter new vehicle color:\n")
		year = int(input("Enter new vehicle year:\n"))
		mileage = int(input("Enter new vehicle mileage\n"))
		inventory.append(Automobile(make, model, color, year, mileage))
		print("\nNew vehicle added.\n")
	except ValueError:
		print("Please enter numeric values for year and mileage.\n")

#Function to remove vehicle from Inventory
def remove_vehicle():
	print(inventory)
	vehicle_to_remove = int(input("Select vehicle ID to remove: "))
	del inventory[vehicle_to_remove]
	print(f"\nYou've removed vehicle {vehicle_to_remove} from inventory.\n")

#Function to update existing vehicle entry
def update_vehicle():
	pass

#Function to export inventory
def export_inventory():
	output_file = open('inventory.txt', 'w')
	for item in inventory:
		output_file.write(str(item))
	output_file.close()

program_running = True #This will allow us to end program when program_running becomes False

while program_running:
	try:
		print("____MENU____") 
		print("(1) Add vehicle to inventory.")
		print("(2) Remove vehicle from inventory.")
		print("(3) Update vehicle in inventory.")
		print("(4) View inventory.")
		print("(5) Export vehicle inventory.")
		print("(6) Exit program.")

		option = int(input("\nWhat would you like to do?  Please enter a number: \n"))
	

		if option == 1:
			add_vehicle()
		elif option == 2:
			remove_vehicle()
		elif option == 3:
			pass
			#run function to update vehicle in inventory
			print(f"You've updated {car_0} from the inventory.\n")
		elif option == 4:
			print(inventory)
		elif option == 5:
			export_inventory()
		elif option == 6:
			program_running = False
	except (ValueError, NameError):
		print("Please enter a number between 1 and 6.  Thank you!")