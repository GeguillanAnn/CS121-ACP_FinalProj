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
