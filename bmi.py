import tkinter

root = tkinter.Tk()
root.title("BMI Calculator")

# Create function(s)
def calculate_bmi():
    # Convert weight to kg if selected in pounds
    if weight_unit.get() == "Pounds":
        kg = float(entry_weight.get()) * 0.453592  # 1 pound = 0.453592 kg
    else:
        kg = float(entry_weight.get())

    # Convert height to meters
    if height_unit.get() == "Centimeters":
        height = float(entry_height.get()) / 100  # Convert cm to meters
    else:
        feet = float(entry_feet.get())
        inches = float(entry_inches.get())
        height = (feet * 12 + inches) * 0.0254  # Convert feet and inches to meters

    bmi = round(kg / (height ** 2), 2)
    label_result['text'] = f"BMI: {bmi}"

# Create GUI
label_weight = tkinter.Label(root, text="Weight: ")
label_weight.grid(column=0, row=0)

entry_weight = tkinter.Entry(root)
entry_weight.grid(column=1, row=0)

weight_unit = tkinter.StringVar(root)
weight_unit.set("Kilograms")  # Default unit is Kilograms
weight_menu = tkinter.OptionMenu(root, weight_unit, "Kilograms", "Pounds")
weight_menu.grid(column=2, row=0)

label_height = tkinter.Label(root, text="Height: ")
label_height.grid(column=0, row=1)

height_unit = tkinter.StringVar(root)
height_unit.set("Centimeters")  # Default unit is Centimeters
height_menu = tkinter.OptionMenu(root, height_unit, "Centimeters", "Feet and Inches")
height_menu.grid(column=2, row=1)

entry_height = tkinter.Entry(root)
entry_height.grid(column=1, row=1)

entry_feet = tkinter.Entry(root, width=5)
entry_feet.grid(column=1, row=2)
label_feet = tkinter.Label(root, text="Feet")
label_feet.grid(column=2, row=2)

entry_inches = tkinter.Entry(root, width=5)
entry_inches.grid(column=3, row=2)
label_inches = tkinter.Label(root, text="Inches")
label_inches.grid(column=4, row=2)

button_calculate = tkinter.Button(root, text="Calculate", command=calculate_bmi, bg="green", fg="white")
button_calculate.grid(column=0, row=3)

label_result = tkinter.Label(root, text="BMI: ")
label_result.grid(column=1, row=3)

root.mainloop()
