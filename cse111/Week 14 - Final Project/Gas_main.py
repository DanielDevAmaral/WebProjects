import tkinter as tk

cars_list = ["Corola/2023", "HR10/2023", "Iveco/2023", "Compass/2023"]
gas_price = 5.19 #($ BLR)
diesel_price = 6.45 #($ BLR)


def main():
    my_w = tk.Tk()
    my_w.title("Travel cost calculation")
    #define the width and heith of the main frame
    my_w.geometry('500x300')
    #define the background color
    my_w.configure(bg='AliceBlue')
    #Create a "entry" that allows the user write the input for the calculation function
    distance = tk.Entry(my_w, font=('calibre', 10, 'normal'))
    distance.grid(row=2, column=4)
    #Calls the select vehicle functions, creating a dropdown list.
    select_vehicle(my_w, distance)
    #Create a label above the entry command
    entry_label = tk.Label(my_w, text="Entrer the distance of the trip in Km", bg='AliceBlue')
    entry_label.grid(row=1, column=4)

    my_w.mainloop()

def select_vehicle(my_w, distance_entry):
    #StringVar() holds a string data where we can set text value and can retrieve it.
    selected_car = tk.StringVar()
    #Setting the text value
    selected_car.set("Your car")
    label_select = tk.Label(my_w, text="Select the Vehicle", bg='AliceBlue')
    label_select.grid(row=1, column=2)
    #Create the dropdown menu
    options_menu = tk.OptionMenu(my_w, selected_car, *cars_list)
    options_menu.grid(row=2, column=2)
    #Create a button and define a command that calls the calculate fucntion 
    button_calculate = tk.Button(my_w, text="Calculate", command=lambda: calculate(selected_car.get(), my_w, distance_entry))
    button_calculate.grid(row=5, column=3)

def calculate(selected_car, my_w, distance_entry):
    #Retrive the input of distance
    distance = distance_entry
    #calls the calculation fuction
    result = calculation(selected_car, distance.get())

    result_label = tk.Label(my_w, text=f"For: {distance.get()}km - Travel will cost: {result:.2f}$", bg='IndianRed')
    result_label.grid(row=2, column=4)

def calculation(car_list, distance):
    if car_list == "Corola/2023":
        car_spend = 16.3 #per liter
        travel_cost = (gas_price / car_spend) * float(distance) 
        return travel_cost
    
    if car_list == "HR10/2023":
        car_spend = 9.0 #per liter
        travel_cost = (diesel_price / car_spend) * float(distance)
        return travel_cost
    
    if car_list == "Iveco/2023":
        car_spend = 7.9 #per liter
        travel_cost = (diesel_price / car_spend) * float(distance)
        return travel_cost
    
    if car_list == "Compass/2023":
        car_spend = 10.3 #per liter
        travel_cost = (diesel_price / car_spend) * float(distance)
        return travel_cost

if __name__ == "__main__":
    main()