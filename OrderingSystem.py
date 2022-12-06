import os 
import datetime
import csv
import sys
import time
from tabulate import tabulate

# Main Menu Class
class MainMenu():
    def __init__(self, listFood, listDrink, listService, listPriceFood, listPriceDrink, listPriceService, listOrder):
        # Constructors
        self.food = listFood
        self.drink = listDrink
        self.service = listService
        self.priceFood = listPriceFood
        self.priceDrink= listPriceDrink
        self.priceService = listPriceService
        self.order = listOrder
    
    # Method to display main page of the program
    def displayMainMenu(self):
        while True:
            os.system('cls')
            # Display operation
            print("*" * 30 + "MAIN MENU" + "*" * 30 + "\n"
                        "\t(O) ORDER\n"
                        "\t(R) RECEIPT\n"
                        "\t(P) PAYMENT\n"
                        "\t(E) EXIT\n" + 
                        "_" * 70)
            input_1 = str(input("Select Your Choice: ")).upper() # prompt next operation
            if input_1 in ['O', 'R', 'P', 'E']:
                time.sleep(1) # sleep 1 second
                os.system("cls")
                if input_1 == 'O':
                    OrderMenu.displayOrderMenu(self) # navigate to order page
                    break
                elif input_1 == 'R':
                    Report.DisplayReport(self) # display report of sales
                    break
                elif input_1 == 'P':
                    Payment.displayPayment(self) # payment form
                    break
                elif input_1 == 'E':
                    Exit.ExitProgram() # end program
            else:
                print(f"\nERROR: INVALID INPUT({str(input_1)}). Try again!") # error checking
                time.sleep(1)
                
                # File Reader class          
class File(MainMenu):
    # Headers fields: for table header
    headerFood      = ["Food", "Price"]
    headerDrink     = ["Drink", "Price"]
    headerService   = ["Service", "Price"]
    
    # Read and display foods available from file
    def Food(self):
        rowID = []; counter = 0
        with open(r"C:\Users\Lenovo iya\Desktop\OS\files\listFoods.csv", mode='r') as fileFoods:
            csv_reader = csv.reader(fileFoods, delimiter=',')
            next(csv_reader, None) # ignore first row of files
            for row in csv_reader:
                counter += 1; rowID.append(counter)
                self.food.append(row)
                self.priceFood.append(row[1])
            # display table of foods available using tabulate
            print(tabulate(self.food, headers=File.headerFood, tablefmt="pretty", showindex=rowID))
    
    # Read and display drinks available from file
    def Drink(self):
        rowID = []; counter = 0
        with open(r"C:\Users\Lenovo iya\Desktop\OS\files\listDrinks.csv", mode='r') as fileDrinks:
            csv_reader = csv.reader(fileDrinks, delimiter=',')
            next(csv_reader, None) # ignore first row of files
            for row in csv_reader:
                counter += 1; rowID.append(counter)
                self.drink.append(row)
                self.priceDrink.append(row[1])
            # display table of drinks available using tabulate
            print(tabulate(self.drink, headers=File.headerDrink, tablefmt="pretty", showindex=rowID))
    
    # Read and display services available from file
    def Service(self):
        rowID = []; counter = 0
        with open(r"C:\Users\Lenovo iya\Desktop\OS\files\listServices.csv", mode='r') as fileServices:
            csv_reader = csv.reader(fileServices, delimiter=',')
            next(csv_reader, None) # ignore first row of files
            for row in csv_reader:
                counter += 1; rowID.append(counter)
                self.service.append(row)
                self.priceService.append(row[1])
            # display table of services available using tabulate
            print(tabulate(self.service, headers=File.headerService, tablefmt="pretty", showindex=rowID))

# Order Menu Class
class OrderMenu(MainMenu):
    totalPrice = []; date = []
    # Method to display order menu
    def displayOrderMenu(self): 
        while True:
            time.sleep(1)
            os.system("cls")
            print("*" * 30 + "ORDER PAGE" + "*" * 30 + "\n"
                    "\t(F) FOOD\n"
                    "\t(D) DRINKS\n"
                    "\t(S) SERVICES\n"
                    "\t(B) BACK TO MAIN MENU\n"
                    "\t(E) EXIT\n" + 
                    "_" * 70)
            input_1 = str(input("Select Your Choice: ")).upper()
            if input_1 in ['F', 'D' ,'S', 'B', 'E']:
                os.system("cls")
                if   input_1 == 'F':
                    File.Food(self) # order food
                    OrderMenu.ProcessOrder(self, input_1)
                elif input_1 == 'D':
                    File.Drink(self) # order drink
                    OrderMenu.ProcessOrder(self, input_1)                
                elif input_1 == 'S':
                    File.Service(self) # order other services
                    OrderMenu.ProcessOrder(self, input_1)                
                elif input_1 == 'B': # back to main menu
                    MainMenu.displayMainMenu(self) 
                    break
                elif input_1 == 'E': # exit program
                    Exit.ExitProgram()
            else:
                print(f"\nERROR: INVALID INPUT({str(input_1)}). Try again!")
                
    def ProcessOrder(self, _input_):
        while True:
            OrderMenu.date.extend([str(datetime.datetime.now())[:10]])
            input_1 = int(input("Please Select Your Order: ")) # Prompt and get order
            if _input_ == 'F':
                quantity = str(input("Quantity: "))
                if input_1 >= 1 and input_1 <= len(self.food):
                    self.food[input_1-1].extend(quantity)
                    self.order.append(self.food[input_1-1])
                    Payment.totalPrice += float(self.priceFood[input_1-1])
                    OrderMenu.totalPrice.extend([float(self.priceFood[input_1-1]) * float(quantity)])
                else:
                    print(f"\nERROR: INVALID ORDER({str(input_1)}). Try again!")
            elif _input_ == 'D':
                quantity = str(input("Quantity: "))
                if input_1 >= 1 and input_1 <= len(self.drink):
                    self.drink[input_1-1].extend(quantity)
                    self.order.append(self.drink[input_1-1])
                    Payment.totalPrice += float(self.priceDrink[input_1-1])
                    OrderMenu.totalPrice.extend([float(self.priceDrink[input_1-1]) * float(quantity)])
                else:
                    print(f"\nERROR: INVALID ORDER({str(input_1)}). Try again!")
            elif _input_ == 'S':
                quantity = '0'
                if input_1 >= 1 and input_1 <= len(self.service):
                    self.service[input_1-1].extend(quantity)
                    self.order.append(self.service[input_1-1])
                    Payment.totalPrice += float(self.priceService[input_1-1])
                    OrderMenu.totalPrice.extend([float(self.priceService[input_1-1]) * float(quantity)])
                else:
                    print(f"\nERROR: INVALID ORDER({str(input_1)}). Try again!")
            else:
                print(f"\nERROR: INVALID INPUT({str(input_1)}). Try again!")
            
            endLoop = str(input("Do you want to add anything else (y/n)? ")).upper()
            if endLoop == 'Y':
                print()
                continue
            elif endLoop == 'N':
                print("********Successfully Ordered!********")
                break
