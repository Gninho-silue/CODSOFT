import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operations.get()

    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 == 0:
            result = "Error! Division by zero."
        else:
            result = num1 / num2
    else:
        result = "Invalid operation"

    label_result.config(text=f"Result: {result}")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields and labels
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=0)

operations = tk.StringVar(root)
operations.set("Add")
option_menu = tk.OptionMenu(root, operations, "Add", "Subtract", "Multiply", "Divide")
option_menu.grid(row=0, column=1)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=0, column=2)

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.grid(row=1, column=0, columnspan=3)

label_result = tk.Label(root, text="Result: ")
label_result.grid(row=2, column=0, columnspan=3)

root.mainloop()
