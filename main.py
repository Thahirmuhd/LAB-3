#LAB 3
#CODED BY : MUHD THAHIR BIN AINUDDIN
#HOTEL RESERVATION SERVICE



from datetime import datetime

def display_room_types_and_rates(room_types, nightly_rates):
    print("Welcome to Our Hotel Reservation System")
    print("Available Room Types:")
    print("=" * 30)
    for i in range(len(room_types)):
        print(f"{i + 1}. {room_types[i]} Room - RM{nightly_rates[i]} per night")
    print("=" * 30)

def calculate_total_cost(room_type_index, num_rooms, check_in, check_out, nightly_rate, additional_services):
    duration = (check_out - check_in).days + 1
    subtotal = nightly_rate * num_rooms * duration
    additional_cost = sum(additional_services.values())
    total_cost = subtotal + additional_cost
    return total_cost

def display_reservation_details(room_type, num_rooms, check_in, check_out, total_cost, additional_services):
    print("\nThank you for your reservation.")
    print("Reservation Details:")
    print("=" * 30)
    print(f"Room Type: {room_type} Room")
    print(f"Number of Rooms: {num_rooms}")
    print(f"Check-in Date: {check_in}")
    print(f"Check-out Date: {check_out}")
    print("Additional Services:")
    for service, cost in additional_services.items():
        print(f"- {service} ({num_rooms} persons) - RM{cost}")
    print(f"Total Cost: RM{total_cost}")
    print("=" * 30)

def select_additional_services_price_list():
    additional_services = {"Breakfast": 20, "WiFi": 10, "Parking": 15}
    print("\nAdditional Services Price List:")
    for service, cost in additional_services.items():
        print(f"{service}: RM{cost}")

def select_additional_services():
    additional_services = {"Breakfast": 20, "WiFi": 10, "Parking": 15}
    selected_additional_services = {}

    print("\nAdditional Services:")
    for service, cost in additional_services.items():
        choice = input(f"Do you want {service}? (yes/no): ")
        if choice.lower() == 'yes':
            num_persons = int(input(f"Enter number of persons for {service}: "))
            selected_additional_services[service] = cost * num_persons
    return selected_additional_services

def main():
    room_types = ["Single", "Double", "Suite"]
    nightly_rates = [100, 150, 250]

    display_room_types_and_rates(room_types, nightly_rates)

    try:
        room_type_index = int(input("\nPlease select a room type (1/2/3): ")) - 1
        if room_type_index < 0 or room_type_index >= len(room_types):
            print("Invalid room type selection.")
            return

        num_rooms = int(input("Enter the number of rooms: "))
        if num_rooms < 1:
            print("Number of rooms must be at least 1.")
            return

        check_in = input("Enter your check-in date (YYYY-MM-DD): ")
        check_out = input("Enter your check-out date (YYYY-MM-DD): ")

        check_in = datetime.strptime(check_in, '%Y-%m-%d')
        check_out = datetime.strptime(check_out, '%Y-%m-%d')
        if check_out <= check_in:
            print("Check-out date must be after check-in date.")
            return

        select_additional_services_price_list()
        additional_services = select_additional_services()

    except ValueError:
        print("Invalid input.")
        return

    selected_room_type = room_types[room_type_index]
    nightly_rate = nightly_rates[room_type_index]

    total_cost = calculate_total_cost(room_type_index, num_rooms, check_in, check_out, nightly_rate, additional_services)

    display_reservation_details(selected_room_type, num_rooms, check_in.strftime('%Y-%m-%d'), check_out.strftime('%Y-%m-%d'), total_cost, additional_services)

    confirm = input("\nWould you like to confirm your reservation? (yes/no): ")
    if confirm.lower() == 'yes':
        print("\nReservation confirmed. Thank you for choosing our hotel. Enjoy your stay!")
    else:
        print("\nReservation canceled.")

if __name__ == "__main__":
    main()
