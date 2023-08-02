import customtkinter
from tkinter import *
from forex_python.converter import CurrencyRates

app = customtkinter.CTk()
app.config(bg="#d4af37")
app.geometry("450x500")
app.title("Currency Converter")
image = PhotoImage(file="currency.png")
img_label = customtkinter.CTkLabel(app, bg_color="#d4af37", image=image)
img_label.place(x=110, y=0)
app.iconphoto(False, image)


from_label = customtkinter.CTkLabel(app, text="From", font=("Arial", 15, "bold"), bg_color="#d4af37", text_color="#000000", width=1)
from_label.place(x=30, y=150)

to_label = customtkinter.CTkLabel(app, text="To", font=("Arial", 15, "bold"), bg_color="#d4af37", text_color="#000000", width=1)
to_label.place(x=268, y=150)

currency_list = ['INR', 'USD', 'CAD', 'CNY', 'DKK', 'EUR', 'GBP']

variable1 = StringVar()
variable2 = StringVar()
txt = StringVar()


def convert():
    from_currency = variable1.get()
    to_currency = variable2.get()

    c = CurrencyRates()
    amt = c.convert(from_currency, to_currency, float(amount_entry.get()))
    amount = float("{:.3f}".format(amt))
    txt.set(amount)
    result_label = customtkinter.CTkLabel(app, textvariable=txt, font=("Arial", 30, "bold"), fg_color="#d4af37", text_color="#000000", width=50)
    result_label.place(x=160, y=350)


def reset():
    amount_entry.delete(0, END)


from_list = customtkinter.CTkComboBox(app, variable=variable1, values=currency_list, font=("Arial", 12, "bold"), dropdown_font=("Arial", 12, "bold"), bg_color="#FFFFFF", text_color="#FFFFFF", button_color="#1A1110", button_hover_color="#884A39", border_color="#000000", dropdown_fg_color="#FFFFFF", dropdown_hover_color="#884A39", dropdown_text_color="#000000")
from_list.place(x=30, y=180)

to_list = customtkinter.CTkComboBox(app, variable=variable2, values=currency_list, font=("Arial", 12, "bold"), dropdown_font=("Arial", 12, "bold"), bg_color="#FFFFFF", text_color="#FFFFFF", button_color="#1A1110", button_hover_color="#884A39", border_color="#000000", dropdown_fg_color="#FFFFFF", dropdown_hover_color="#884A39", dropdown_text_color="#000000")
to_list.place(x=260, y=180)

amount_entry = customtkinter.CTkEntry(app, font=("Arial", 20, "bold"), text_color="#FFFFFF", justify= CENTER, width=370, bg_color="#FFFFFF", border_color="#000000")
amount_entry.place(x=30, y=240)

convert_btn = customtkinter.CTkButton(app, command=convert, text="Convert", font=("Arial", 20, "bold"), text_color="#000000", fg_color="#0B666A", hover_color="#0B666A", border_color="#000000", border_width=1)
convert_btn.place(x=65, y=300)

reset_btn = customtkinter.CTkButton(app, command=reset, text="Reset", font=("Arial", 20, "bold"), text_color="#000000", fg_color="#EF6262", hover_color="#EF6262", border_color="#000000", border_width=1)
reset_btn.place(x=230, y=300)


app.mainloop()
