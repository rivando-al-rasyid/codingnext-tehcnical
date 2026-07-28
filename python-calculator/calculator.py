import tkinter as tk

def calculate_price(original_price, discount):
    return original_price * (1 - (discount / 100))

def show_result():
    try:
        original_price = float(entry1.get())
        discount_value = float(entry2.get())

        final_price = calculate_price(original_price, discount_value)

        result_label.config(text=f"Final Price: Rp. {final_price:.2f}")

    except ValueError:
        result_label.config(text="Please enter valid numbers.")


root = tk.Tk()
root.title("Discount Calculator")
root.geometry("600x400")

font = ("Arial", 16)

tk.Label(root, text="Original Price", font=font).pack(pady=5)
entry1 = tk.Entry(root, font=font)
entry1.pack()

tk.Label(root, text="Discount (%)", font=font).pack(pady=5)
entry2 = tk.Entry(root, font=font)
entry2.pack()

button = tk.Button(root, text="Calculate", width=10, command=show_result, font=font)
button.pack(pady=10)

result_label = tk.Label(root, text="", font=font)
result_label.pack(pady=20)

root.mainloop()