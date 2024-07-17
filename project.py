class Driver:
    def __init__(self, worker_id, name, start_city):
        self.worker_id = worker_id
        self.name = name
        self.start_city = start_city
        self.delivery_cities = [start_city]

    def add_delivery_city(self, city_name): #
        if city_name not in self.delivery_cities:
            self.delivery_cities.append(city_name)


class City:
    def __init__(self, name):
        self.name = name
        self.connections = []

    def add_connection(self, city): #
        if city not in self.connections:
            self.connections.append(city)
            print("Connection added between " + self.name + " and " + city.name + ".")
        else:
            print("Connection between " + self.name + " and " + city.name + " already exists.")


def main_menu():
    print("\nHello! Please enter:")
    print("1. To go to the drivers menu")
    print("2. To go to the cities menu")
    print("3. To exit the system")


def drivers_menu():
    print("\nDrivers Menu:")
    print("1. Add a driver")
    print("2. View all drivers")
    print("3. Search for a driver by ID")
    print("4. Add delivery city for a driver")
    print("5. Go back to the main menu")


def cities_menu():
    print("\nCities Menu:")
    print("1. Add a city")
    print("2. Add a connection between cities")
    print("3. View all cities and their connections")
    print("4. Print neighboring cities")
    print("5. Print drivers delivering to a city")
    print("6. Go back to the main menu")


def main():
    drivers = {
        1: Driver(1, "Ali Achkar", "Mansourieh"),
        2: Driver(2, "Ahmad Azzam", "Beirut"),
        3: Driver(3, "Joe Assaf", "Zalka"),
        4: Driver(4, "Joe Bassam abdlrahman", "Akkar"),
        5: Driver(5, "Mhamad Delbani", "Beirut"),
        6: Driver(6, "Yassine Atwi", "Saida"),
        7:Driver(7,"Hsein saker","Dahieh"),
        8:Driver(8,"Hassan Kanso","Khaldeh")
    }

    cities = {
        "BEIRUT": City("BEIRUT"),
        "ZALKA": City("ZALKA"),
        "MANSOURIEH": City("MANSOURIEH"),
        "TRIPOLI": City("TRIPOLI"),
        "SAIDA":City("SAIDA"),
        "AKKAR":City("AKKAR"),
        "Dahieh":City("Dahieh"),
        "Khaldeh":City("Khaldeh")
    }

    driver_id_counter = len(drivers) + 1  

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


def handle_cities_menu(drivers, cities):
    while True:
        cities_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_city(cities)
        elif choice == "2":
            add_city_connection(cities)
        elif choice == "3":
            view_cities(cities)
        elif choice == "4":
            print_neighboring_cities(cities)
        elif choice == "5":
            print_drivers_delivering_to_city(drivers, cities)
        elif choice == "6":
            break
        else:
            print("Invalid choice, please try again.")


def add_driver(drivers, driver_id_counter, cities):
    name = input("Enter name: ")
    start_city = input("Enter start city: ").upper()

    if start_city not in cities:
        print("City does not exist.")
        return driver_id_counter

    drivers[driver_id_counter] = Driver(driver_id_counter, name, start_city)
    print("Driver added successfully!")
    return driver_id_counter + 1


def view_drivers(drivers):
    if not drivers:
        print("No drivers available.")
    else:
        print("List of drivers:")
        for driver_id, driver in drivers.items():
            print("Driver ID: " + str(driver_id) + ", Name: " + driver.name + ", Start City: " + driver.start_city)
            print("Delivery Cities: " + ", ".join(driver.delivery_cities))


def search_driver(drivers):
    worker_id = int(input("Enter worker ID to search: "))
    driver = drivers.get(worker_id)
    if driver:
        print("Driver ID: " + str(driver.worker_id) + ", Name: " + driver.name + ", Start City: " + driver.start_city)
        print("Delivery Cities: " + ", ".join(driver.delivery_cities))
    else:
        print("Driver not found.")


def add_city(cities):
    name = input("Enter city name: ").upper()
    if name in cities:
        print("City already exists.")
    else:
        cities[name] = City(name)
        print("City added successfully!")


def add_city_connection(cities):
    city1 = input("Enter the first city name: ").upper()
    city2 = input("Enter the second city name: ").upper()

    if city1 not in cities or city2 not in cities:
        print("One or both cities do not exist.")
        return

    cities[city1].add_connection(cities[city2])
    cities[city2].add_connection(cities[city1])
    print("Connection added successfully!")


def view_cities(cities):
    if not cities:
        print("No cities available.")
    else:
        print("List of cities and their connections:")
        for city_name, city in cities.items():
            connections = []
            for c in city.connections:
                connections.append(c.name)
            print("City: " + city_name + ", Connections: " + ", ".join(connections))


def print_neighboring_cities(cities):
    city_name = input("Enter the city name: ").upper()
    if city_name not in cities:
        print("City not found.")
    else:
        city = cities[city_name]
        connections = []
        for c in city.connections:
            connections.append(c.name)
        print("Neighboring cities for " + city_name + ": " + ", ".join(connections))


def print_drivers_delivering_to_city(drivers, cities):
    city_name = input("Enter the city name: ").upper()
    if city_name not in cities:
        print("City not found.")
    else:
        delivering_drivers = []
        for driver in drivers.values():
            if city_name in driver.delivery_cities:
                delivering_drivers.append(driver)
        if delivering_drivers:
            print("Drivers delivering to " + city_name + ":")
            for driver in delivering_drivers:
                print("Driver ID: " + str(driver.worker_id) + ", Name: " + driver.name)
        else:
            print("No drivers are delivering to " + city_name + ".")


def add_delivery_city_for_driver(drivers, cities):
    worker_id = int(input("Enter the driver ID: "))
    if worker_id not in drivers:
        print("Driver not found.")
        return

    city_name = input("Enter the delivery city: ").upper()
    if city_name not in cities:
        print("City not found.")
        return

    drivers[worker_id].add_delivery_city(city_name)
    print("Delivery city added successfully!")


if __name__ == "__main__":
    main()
