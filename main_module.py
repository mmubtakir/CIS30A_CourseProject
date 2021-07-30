# Name: Musamim Mubtakir
# CIS 30A
# Professor Kasey Nguyen
# CIS 30A Course Project Option A
# main_module

import receipt_module 

#List of services for the user to add to their detailing package
service_pkgs = {1:('Exterior Wash', 25.00),
                2:('Interior Vacuum', 10.00),
                3:('Interior Seat Extraction', 20.00),
                4:('Exterior Detail', 35.00),
                5:('Interior Detail', 15.00),
                6:('Paint Correction', 50.00)}

# Welcome message
print("*******     Welcome to Mubtakir's Mobile Auto Detailing!     *******\n")

# Get user info, appointment data& time and vehicle info
print('In order to better serve you, please answer a few questions for us...')

class user_info:
    def __init__(user, name, pNumber, date, time):
        user.name = name
        user.pNumber = pNumber
        user.date = date
        user.time = time
        
user_info = user_info(
    input("What is your name? "),
    input("What is your phone number? "),
    input("Please enter the date for your appointment (MM/DD/YYYY): "),
    input("Please enter the time for your appointment (HH:MM AM/PM): "))

class vehicle_info:
    def __init__(car, make, model, color, year):
        car.make = make
        car.model = model
        car.color = color
        car.year = year
        
user_vehicle = vehicle_info(
    input("What is the make of your vehicle? "),
    input("What is the model of your vehicle? "),
    input("What is the color of your vehicle? "),
    input("What is the year of your vehicle? \n"))


# Write user user info, appointment data& time and vehicle info into receipt.txt file
f_out = open('receipt.txt', 'w')
f_out.write('...Order Confirmation for ' + user_info.name + '...\n')
f_out.write('Phone Number: ' + user_info.pNumber + '\n')
f_out.write('Appointment Date: ' + user_info.date + '\n')
f_out.write('Appointment Time ' + user_info.time + '\n\n')

f_out.write('Vehicle information: \n')
f_out.write(user_vehicle.make + ' ')
f_out.write(user_vehicle.model + ' ')
f_out.write(user_vehicle.year + ', ')
f_out.write(user_vehicle.color + '\n\n')
f_out.close()


# Options for the user to choose from
print("Please select from the services we provide and make your own detailing package: ")

for k, v in service_pkgs.items():
    print('{}) {}: $ {}' .format(k,v[0],v[1]))

customer_list = []

# Prompts the user to input choices and whether to continue or not
add_service = 'Y'
while add_service == 'Y':
    choice = int(input('\nWhich services would you like to add to your detail package?: '))

    if choice in service_pkgs.keys():
        customer_list.append((service_pkgs[choice][0], service_pkgs[choice][1]))
    else:
        print('Invalid Choice')

    add_service = input('''Would you like to add more services to your detail package?
(Please input "Y" for Yes, and "N" for No): ''').upper()

print('\n')

receipt_module.total(customer_list)



