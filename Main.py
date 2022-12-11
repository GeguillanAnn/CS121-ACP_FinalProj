import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image, ImageTk
import random
from datetime import date
from datetime import datetime

prices = {
    "Bulalo" : 260,
    "Sisig" : 150,
    "Sinigang" : 150,
    "Kare-Kare" : 200,
    "Kaldereta" : 25,
    "Bicol Express" : 10,
}

root  = Tk()

root.title("TTC - Binary Restaurant")

# ------------------------------------FUNCTIONS--------------------------------------------- #

#region Generating a random Order ID when starting a new order
def ORDER_ID():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    order_id = "BIN_"
    random_letters = ""
    random_digits = ""
    for i in range(0,3):
        random_letters += random.choice(letters)
        random_digits += str(random.choice(numbers))

    order_id += random_letters + random_digits
    return order_id
#endregion

#region Add to Order Button
def add():
    # updating the transaction label
    current_order = orderTransaction.cget("text")
    added_dish = displayLabel.cget("text") + "...." + "Php " + str(prices[displayLabel.cget("text")]) + "\n"
    updated_order = current_order + added_dish
    orderTransaction.configure(text=updated_order)

    # updating the order total label
    order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
    order_total = order_total.replace("$", "")
    updated_total = int(order_total) + prices[displayLabel.cget("text")]
    orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")
#endregion

#region Remove Button Function
def remove():
    dish_to_remove = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")])
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    if dish_to_remove in transaction_list:
        # update transaction label
        transaction_list.remove(dish_to_remove)
        updated_order = ""
        for item in transaction_list:
            updated_order += item + "$ "

        orderTransaction.configure(text = updated_order)

        # update transaction total
        order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
        order_total = order_total.replace("$", "")
        updated_total = int(order_total) - prices[displayLabel.cget("text")]
        orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")

#endregion

#region Display Button Functions
def displayBulalo():
    bulaloDishFrame.configure(
        relief = "sunken",
        style = "SelectedDish.TFrame"
    )
    sinigangDishFrame.configure(style = "DishFrame.TFrame")
    bicolDishFrame.configure(style= "DishFrame.TFrame")
    kaldeDishFrame.configure(style = "DishFrame.TFrame")
    kareDishFrame.configure(style = "DishFrame.TFrame")
    sisigDishFrame.configure(style = "DishFrame.TFrame")

    displayLabel.configure(
        image = bulaloImage,
        text = "Bulalo",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        compound = "bottom",
        padding = (5, 5, 5, 5),
    )

def displaySisig():
    sisigDishFrame.configure(
        relief = "sunken",
        style = "SelectedDish.TFrame"
    )
    sinigangDishFrame.configure(style="DishFrame.TFrame")
    bicolDishFrame.configure(style="DishFrame.TFrame")
    kaldeDishFrame.configure(style="DishFrame.TFrame")
    kareDishFrame.configure(style="DishFrame.TFrame")
    bulaloDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        text = "Sisig",
        font = ('Helvetica', 14,"bold"),
        foreground = "white",
        image = sisigImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displaySinigang():
    sinigangDishFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame"
    )
    bulaloDishFrame.configure(style="DishFrame.TFrame")
    bicolDishFrame.configure(style="DishFrame.TFrame")
    kaldeDishFrame.configure(style="DishFrame.TFrame")
    kareDishFrame.configure(style="DishFrame.TFrame")
    sisigDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        text = "Sinigang",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        image = sinigangImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displayKareKare():
    kareDishFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame"
    )
    sinigangDishFrame.configure(style="DishFrame.TFrame")
    kareDishFrame.configure(style="DishFrame.TFrame")
    kaldeDishFrame.configure(style="DishFrame.TFrame")
    bulaloDishFrame.configure(style="DishFrame.TFrame")
    sisigDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        text = "Kare-Kare",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        image = kareImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displayBicolExpress():
    bicolDishFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame"
    )
    sinigangDishFrame.configure(style="DishFrame.TFrame")
    bulaloDishFrame.configure(style="DishFrame.TFrame")
    kaldeDishFrame.configure(style="DishFrame.TFrame")
    kareDishFrame.configure(style="DishFrame.TFrame")
    sisigDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        text = "Bicol Express",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        image = bicolImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displayKaldereta():
    kaldeDishFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame"
    )
    sinigangDishFrame.configure(style="DishFrame.TFrame")
    bicolDishFrame.configure(style="DishFrame.TFrame")
    bulaloDishFrame.configure(style="DishFrame.TFrame")
    kareDishFrame.configure(style="DishFrame.TFrame")
    sisigDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        image = kaldeImage,
        text = "Kaldereta",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )
#endregion

#region Generating Receipt from Order Button
def order():
    new_receipt = orderIDLabel.cget("text")
    new_receipt = new_receipt.replace("ORDER ID : ","")
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    order_day = date.today()
    order_time = datetime.now()

    for item in transaction_list:
        item += "$ "

    with open(new_receipt, 'w') as file:
        file.write("The Binary")
        file.write("\n")
        file.write("________________________________________________________")
        file.write("\n")
        file.write(order_day.strftime("%x"))
        file.write("\n")
        file.write(order_time.strftime("%X"))
        file.write("\n\n")
        for item in transaction_list:
            file.write(item + "\n")
        file.write("\n\n")
        file.write(orderTotalLabel.cget("text"))

    orderTotalLabel.configure(text = "TOTAL : 0$")
    orderIDLabel.configure(text = "ODER ID: " + ORDER_ID())
    orderTransaction.configure(text = "")

#endregion

# ---------------------------------- STYLING AND IMAGES ------------------------------------ #

#region Style configurations
s = ttk.Style()
s.configure('MainFrame.TFrame', background = "#2B2B28")
s.configure('MenuFrame.TFrame', background = "#4A4A48")
s.configure('DisplayFrame.TFrame', background = "#0F1110")
s.configure('OrderFrame.TFrame', background = "#B7C4CF")
s.configure('DishFrame.TFrame', background = "#4A4A48", relief = "raised")
s.configure('SelectedDish.TFrame', background = "#C4DFAA")
s.configure('MenuLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 13, "italic"),
            foreground = "white",
            padding = (5, 5, 5, 5),
            width = 21
            )
s.configure('orderTotalLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 10, "bold"),
            foreground = "white",
            padding = (2, 2, 2, 2),
            anchor = "w"
            )
s.configure('orderTransaction.TLabel',
            background = "#4A4A48",
            font = ('Helvetica', 12),
            foreground = "white",
            wraplength = 170,
            anchor = "nw",
            padding = (3, 3, 3, 3)
            )

# endregion

# region Images
# Top Banner images
LogoImageObject = Image.open("Images/Binary Logo.png").resize((130, 130))
LogoImage = ImageTk.PhotoImage(LogoImageObject)

TopBannerImageObject = Image.open("Images/restaurant top banner.jpg").resize((800, 130))
TopBannerImage = ImageTk.PhotoImage(TopBannerImageObject)

# Menu images
displayDefaultImageObject = Image.open("Images/display - Default.png").resize((350,360))
displayDefaultImage = ImageTk.PhotoImage(displayDefaultImageObject)

bulaloImageObject = Image.open("Images/menu/bulalo.png").resize((350,334))
bulaloImage = ImageTk.PhotoImage(bulaloImageObject)

sisigImageObject = Image.open("Images/menu/sisig.png").resize((350,334))
sisigImage = ImageTk.PhotoImage(sisigImageObject)

sinigangImageObject = Image.open("Images/menu/sinigang.png").resize((350,334))
sinigangImage = ImageTk.PhotoImage(sinigangImageObject)

kareImageObject = Image.open("Images/menu/karekare.png").resize((350,334))
kareImage = ImageTk.PhotoImage(kareImageObject)

kaldeImageObject = Image.open("Images/menu/kaldereta.png").resize((350,334))
kaldeImage = ImageTk.PhotoImage(kaldeImageObject)

bicolImageObject = Image.open("Images/menu/bicolexpress.png").resize((350,334))
bicolImage = ImageTk.PhotoImage(bicolImageObject)


#endregion

#----------------------------------- WIDGETS ----------------------------------------------- #

# region Frames

# Section Frames
mainFrame = ttk.Frame(root, width = 800, height = 580, style = 'MainFrame.TFrame')
mainFrame.grid(row = 0, column = 0, sticky = "NSEW")

topBannerFrame = ttk.Frame(mainFrame)
topBannerFrame.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 3)

menuFrame = ttk.Frame(mainFrame, style = 'MenuFrame.TFrame')
menuFrame.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = "NSEW")

displayFrame = ttk.Frame(mainFrame, style = "DisplayFrame.TFrame")
displayFrame.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = "NSEW")

orderFrame = ttk.Frame(mainFrame, style = "OrderFrame.TFrame")
orderFrame.grid(row = 1, column = 2, padx = 3, pady = 3, sticky = "NSEW")

# Dish Frames
bulaloDishFrame = ttk.Frame(menuFrame, style = "DishFrame.TFrame")
bulaloDishFrame.grid(row = 1, column = 0, sticky = "NSEW")

sisigDishFrame = ttk.Frame(menuFrame,style ="DishFrame.TFrame")
sisigDishFrame.grid(row = 2, column = 0, sticky ="NSEW")

sinigangDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
sinigangDishFrame.grid(row = 3, column = 0, sticky ="NSEW")

kareDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
kareDishFrame.grid(row = 4, column = 0, sticky ="NSEW")

kaldeDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
kaldeDishFrame.grid(row = 5, column = 0, sticky ="NSEW")

bicolDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
bicolDishFrame.grid(row = 6, column = 0, sticky ="NSEW")

#endregion

# region Top Banner Section

LogoLabel = ttk.Label(topBannerFrame, image = LogoImage, background = "#0F1110")
LogoLabel.grid(row = 0, column = 0, sticky = "W")

RestaurantBannerLabel = ttk.Label(topBannerFrame, image = TopBannerImage, background = "#0F1110")
RestaurantBannerLabel.grid(row = 0, column = 1, sticky = "NSEW")

# endregion

#region Menu Section
MainMenuLabel = ttk.Label(menuFrame, text = "MENU", style = "MenuLabel.TLabel")
MainMenuLabel.grid(row = 0, column = 0, sticky = "WE")
MainMenuLabel.configure(
    anchor = "center",
    font = ("Helvetica", 14, "bold")
)

BulaloDishLabel = ttk.Label(bulaloDishFrame, text ="Bulalo ..... 260Php", style ="MenuLabel.TLabel")
BulaloDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

SisigDishLabel = ttk.Label(sisigDishFrame, text ="Sisig ..... 150Php", style ="MenuLabel.TLabel")
SisigDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

SinigangDishLabel = ttk.Label(sinigangDishFrame, text ="Sinigang ..... 150Php", style ="MenuLabel.TLabel")
SinigangDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

KareDishLabel = ttk.Label(kareDishFrame, text ="Kare-Kare ..... 200Php", style ="MenuLabel.TLabel")
KareDishLabel.grid(row = 0, column = 0, padx =10, pady = 10, sticky = "W")

KaldeDishLabel = ttk.Label(kaldeDishFrame, text ="Kaldereta ..... 200Php", style ="MenuLabel.TLabel")
KaldeDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

BicolDishLabel = ttk.Label(bicolDishFrame, text ="Bicol Express .... 150Php", style ="MenuLabel.TLabel")
BicolDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

#Buttons
BulaloDisplayButton = ttk.Button(bulaloDishFrame, text ="Display", command = displayBulalo)
BulaloDisplayButton.grid(row = 0, column = 1, padx = 10)

SisigDisplayButton = ttk.Button(sisigDishFrame, text ="Display", command = displaySisig)
SisigDisplayButton.grid(row = 0, column = 1, padx = 10)

SinigangDisplayButton = ttk.Button(sinigangDishFrame, text ="Display", command = displaySinigang)
SinigangDisplayButton.grid(row = 0, column = 1, padx = 10)

KareDisplayButton = ttk.Button(kareDishFrame, text ="Display", command = displayKareKare)
KareDisplayButton.grid(row = 0, column = 1, padx = 10)

KaldeDisplayButton = ttk.Button(kaldeDishFrame, text ="Display", command = displayKaldereta)
KaldeDisplayButton.grid(row = 0, column = 1, padx = 10)

BicolDisplayButton = ttk.Button(bicolDishFrame, text ="Display", command = displayBicolExpress)
BicolDisplayButton.grid(row = 0, column = 1, padx = 10)

# endregion

#region Order Section
orderTitleLabel = ttk.Label(orderFrame, text = "ORDER")
orderTitleLabel.configure(
    foreground="white", background="black",
    font=("Helvetica", 14, "bold"), anchor = "center",
    padding = (5, 5, 5, 5),
)
orderTitleLabel.grid(row = 0, column = 0, sticky = "EW")

orderIDLabel = ttk.Label(orderFrame, text = "ORDER ID : " + ORDER_ID())
orderIDLabel.configure(
    background = "black",
    foreground = "white",
    font = ("Helvetica", 11, "italic"),
    anchor = "center",
)
orderIDLabel.grid(row = 1, column = 0, sticky = "EW", pady = 1)

orderTransaction = ttk.Label(orderFrame, style = 'orderTransaction.TLabel')
orderTransaction.grid(row = 2, column = 0, sticky = "NSEW")

orderTotalLabel = ttk.Label(orderFrame, text = "TOTAL : 0$", style = "orderTotalLabel.TLabel")
orderTotalLabel.grid(row = 3, column = 0, sticky = "EW")

orderButton = ttk.Button(orderFrame, text = "ORDER", command = order)
orderButton.grid(row = 4, column = 0, sticky = "EW")


# endregion

# region Display Section
displayLabel = ttk.Label(displayFrame, image = displayDefaultImage)
displayLabel.grid(row = 0, column = 0 , sticky = "NSEW", columnspan = 2)
displayLabel.configure(background = "#0F1110")

addOrderButton = ttk.Button(displayFrame, text = "ADD TO ORDER", command = add)
addOrderButton.grid(row = 1, column = 0, padx = 2, sticky = "NSEW")

removeOrderButton = ttk.Button(displayFrame, text = "REMOVE", command = remove)
removeOrderButton.grid(row = 1, column = 1, padx = 2, sticky = "NSEW")

#endregion



#----------------------------- GRID CONFIGURATIONS -------------------------------------------#
mainFrame.columnconfigure(2, weight = 1)
mainFrame.rowconfigure(1, weight = 1)
menuFrame.columnconfigure(0, weight = 1)
menuFrame.rowconfigure(1, weight = 1)
menuFrame.rowconfigure(2, weight = 1)
menuFrame.rowconfigure(3, weight = 1)
menuFrame.rowconfigure(4, weight = 1)
menuFrame.rowconfigure(5, weight = 1)
menuFrame.rowconfigure(6, weight = 1)
orderFrame.columnconfigure(0, weight = 1)
orderFrame.rowconfigure(2, weight = 1)



root.mainloop()
