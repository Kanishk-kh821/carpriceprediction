from tkinter import *
import pickle

with open('RandomForestRegressor_model.pkl', 'rb') as f:
        model = pickle.load(f)
seller_selected_value=""
fuel_selected_value=""
transmission_selected_value=""

def pred_price():

    input_values=[]
    
    input_values.append(int(vehicle_age_entry.get()))
    input_values.append(int(km_driven_entry.get()))
    input_values.append(float(mileage_entry.get()))
    input_values.append(int(engine_entry.get()))
    input_values.append(float(max_power_entry.get()))
    input_values.append(int(seats_entry.get()))
    
    if seller_selected_value == "Dealer":
        input_values.append(1.0)
        input_values.append(0.0)
        input_values.append(0.0)
    elif seller_selected_value == "Individual":
        input_values.append(0.0)
        input_values.append(1.0)
        input_values.append(0.0)
    else:
        input_values.append(0.0)
        input_values.append(0.0)
        input_values.append(1.0)
    
    if fuel_selected_value == "CNG":
        input_values.append(1.0)
        input_values.append(0.0)
        input_values.append(0.0)
        input_values.append(0.0)
        input_values.append(0.0)
    elif fuel_selected_value== "Diesel":
        input_values.append(0.0)
        input_values.append(1.0)
        input_values.append(0.0)
        input_values.append(0.0)
        input_values.append(0.0)
    elif fuel_selected_value== "Electric":
        input_values.append(0.0)
        input_values.append(0.0)
        input_values.append(1.0)
        input_values.append(0.0)
        input_values.append(0.0)
    elif fuel_selected_value == "LPG":
        input_values.append(0.0)
        input_values.append(0.0)
        input_values.append(0.0)
        input_values.append(1.0)
        input_values.append(0.0)
    else:
        input_values.append(0.0)
        input_values.append(0.0)
        input_values.append(0.0)
        input_values.append(0.0)
        input_values.append(1.0)
    
    if transmission_selected_value == "Automatic":
        input_values.append(1.0)
        input_values.append(0.0)
    else:
        input_values.append(0.0)
        input_values.append(1.0)
        
    prediction = model.predict([input_values])[0]
    price_label.config(text = f"Predicted price:{prediction}")
    print(f"Predicted price: {prediction}")



root = Tk()
root.geometry("1080x720")
root.title("Car Price Predictor")

root.config(bg="black")

title_label = Label(root, text="Car Price Predictor", bg="black", fg="green", font=("Arial", 30, "bold"), justify="center")
title_label.pack(pady=30)

car_name_frame = Frame(root, bg="black")
car_name_frame.pack()
car_name_label = Label(car_name_frame, text="Car Name", bg="black", fg="white", font=("Arial", 20, "bold"),  justify="left")
car_name_label.pack(side=LEFT, padx=30)
car_name_entry = Entry(car_name_frame, font=('Arial', 15, "bold"))
car_name_entry.pack(side=LEFT)


vehicle_age_frame = Frame(root, bg="black")
vehicle_age_frame.pack()
vehicle_age_label = Label(vehicle_age_frame, text="Vehicle Age", bg="black", fg="white", font=("Arial", 20, "bold"), justify="left")
vehicle_age_label.pack(side=LEFT, padx=19)
vehicle_age_entry = Entry(vehicle_age_frame,  font=('Arial', 15, "bold"))
vehicle_age_entry.pack(side=LEFT)


km_driven_frame = Frame(root,bg="black")
km_driven_frame.pack()
km_driven_label = Label(km_driven_frame, text="KM Driven", bg="black", fg="white", font=("Arial", 20, "bold"), justify="left")
km_driven_label.pack(side=LEFT, padx=30)
km_driven_entry = Entry(km_driven_frame,  font=('Arial', 15, "bold"))
km_driven_entry.pack(side=LEFT)


mileage_frame = Frame(root,bg="black")
mileage_frame.pack()
mileage_label = Label(mileage_frame, text="Mileage", bg="black", fg="white", font=("Arial", 20, "bold"), justify="left")
mileage_label.pack(side=LEFT, padx=50)
mileage_entry = Entry(mileage_frame,  font=('Arial', 15, "bold"))
mileage_entry.pack(side=LEFT)

engine_frame = Frame(root,bg="black")
engine_frame.pack()
engine_label = Label(engine_frame, text="Engine", bg="black", fg="white", font=("Arial", 20, "bold"), justify="left")
engine_label.pack(side=LEFT, padx=50)
engine_entry = Entry(engine_frame,  font=('Arial', 15, "bold"))
engine_entry.pack(side=LEFT)


max_power_frame = Frame(root,bg="black")
max_power_frame.pack()
max_power_label = Label(max_power_frame, text="Max Power", bg="black", fg="white", font=("Arial", 20, "bold"), justify="left")
max_power_label.pack(side=LEFT, padx=30)
max_power_entry = Entry(max_power_frame,  font=('Arial', 15, "bold"))
max_power_entry.pack(side=LEFT)

seats_frame = Frame(root,bg="black")
seats_frame.pack()
seats_label = Label(seats_frame, text="Seats", bg="black", fg="white", font=("Arial", 20, "bold"), justify="left")
seats_label.pack(side=LEFT, padx=60)
seats_entry = Entry(seats_frame,  font=('Arial', 15, "bold"))
seats_entry.pack(side=LEFT)

seller_type_frame = Frame(root,bg="black")
seller_type_frame.pack()
seller_type_label = Label(seller_type_frame, text="Seller Type", bg="black", fg="white", font=("Arial", 20, "bold"), justify="left")
seller_type_label.pack(side=LEFT, padx=60)
# Dictionary to create multiple buttons
seller_type_values = {"Dealer" : "Dealer",
          "Individual" : "Individual",
          "Trustmark Dealer" : "Trustmark Dealer"}
selected_seller = StringVar(root, "1")
def on_seller_selected():
    seller_selected_value = selected_seller.get()
    print(f"Selected value: {seller_selected_value}")
  
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in seller_type_values.items():
    Radiobutton(seller_type_frame, text = text, variable = selected_seller, 
                value = value, font=("Arial", 10, "bold"), command=on_seller_selected).pack(side=LEFT, ipady = 5)

fuel_type_frame = Frame(root,bg="black")
fuel_type_frame.pack()
fuel_type_label = Label(fuel_type_frame, text="Fuel Type", bg="black", fg="white", font=("Arial", 20, "bold"), justify="left")
fuel_type_label.pack(side=LEFT, padx=80)
# Dictionary to create multiple buttons
fuel_type_values = {"CNG" : "CNG",
          "Diesel" : "Diesel",
          "Electric": "Electric",
          "LPG": "LPG",
          "Petrol" : "Petrol"}
selected_fuel = StringVar(root, "1")
def on_fuel_selected():
    fuel_selected_value = selected_fuel.get()
    print(f"Selected value: {fuel_selected_value}")
  
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in fuel_type_values.items():
    Radiobutton(fuel_type_frame, text = text, variable = selected_fuel, 
                value = value, font=("Arial", 10, "bold"), command=on_fuel_selected).pack(side=LEFT, ipady = 5)    

transmission_type_frame = Frame(root,bg="black")
transmission_type_frame.pack()
transmission_type_label = Label(transmission_type_frame, text="Transmission Type", bg="black", fg="white", font=("Arial", 20, "bold"), justify="left")
transmission_type_label.pack(side=LEFT,padx=10)
# Dictionary to create multiple buttons
transmission_type_values = {"Automatic" : "Automatic",
          "Manual" : "Manual"}
selected_transmission = StringVar(root, "1")
def on_transmission_selected():
    transmission_selected_value = selected_transmission.get()
    print(f"Selected value: {transmission_selected_value}")
  
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in transmission_type_values.items():
    Radiobutton(transmission_type_frame, text = text, variable = selected_transmission, 
                value = value, font=("Arial", 10, "bold"), command=on_transmission_selected).pack(side=LEFT, ipady = 5)    
    
pred_btn =Button(root, text="Predict Price", command=pred_price,bg= "green", fg="white", font=("Arial", 20, "bold"))
pred_btn.pack(pady=30)

price_label=Label(root, text=f"Predicted Price: {0}", bg="black", fg="white", font=("Arial", 20, "bold"))
price_label.pack()


root.mainloop()