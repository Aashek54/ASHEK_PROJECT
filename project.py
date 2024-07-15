class Driver:
    def __init__(self, worker_id, name, start_city):
        self.worker_id = worker_id
        self.name = name
        self.start_city = start_city

class City:
    def __init__(self, name):
        self.name = name
        self.connections = []

def main_menu():
    print("\nHello! Please enter:")
    print("1. To go to the drivers' menu")
    print("2. To go to the cities' menu")
    print("3. To exit the system")


def drivers_menu():
    print("\nDrivers' Menu:")
    print("1. Add a driver")
    print("2. View all drivers")
    print("3. Search for a driver by ID")
    print("4. Add delivery city for a driver")
    print("5. Go back to the main menu")


def cities_menu():
    print("\nCities' Menu:")
    print("1. Add a city")
    print("2. Add a connection between cities")
    print("3. View all cities and their connections")
    print("4. Print neighboring cities")
    print("5. Print drivers delivering to a city")
    print("6. Go back to the main menu")


    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            driver_id_counter = handle_drivers_menu(drivers, driver_id_counter, cities)
        elif choice == "2":
            handle_cities_menu(drivers, cities)
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


def handle_drivers_menu(drivers, driver_id_counter, cities):
    while True:
        drivers_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            driver_id_counter = add_driver(drivers, driver_id_counter, cities)
        elif choice == "2":
            view_drivers(drivers)
        elif choice == "3":
            search_driver(drivers)
        elif choice == "4":
            add_delivery_city_for_driver(drivers, cities)
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")
    return driver_id_counter
