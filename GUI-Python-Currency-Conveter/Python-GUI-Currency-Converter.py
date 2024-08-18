## Python Currency Converter GUI Programing using OpenExchangeRates API and Tkinter by Team Achivers

## Import tkinter, requests and json

from tkinter import *
from tkinter import ttk
import requests
import json

## tkinter message box for displaying errors

from tkinter.messagebox import showerror

## API keys and URL for the API request

API_KEY = "..."
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

## Making the standard request to the API and return the request and store it in the variable

response = requests.get(f"{url}").json()

## Converting the currencies to dictionary format for easier readability and accessibility of data

currencies = dict(response["conversion_rates"])

## Defining conversion functions and logic when 

def convert_currency():
    
    try:

        source = from_currency_combo.get()

        destination = to_currency_combo.get()

        amount = amount_entry.get()

        result = requests.get(f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{source}/{destination}/{amount}").json()

        converted_result = result["conversion_result"]

        formatted_result = f"{amount} {source} = {converted_result} {destination}"

        result_label.config(text=formatted_result)

        time_label.config(Text="Last Updated On,"+ result["time_last_update_utc"])
    except:
        showerror(title="Error !", message="Failed to Fetch Results !!.\n Suggestion : Internet Connection is Required!!")


window = Tk()

window.geometry("500x500")

window.title("Currency Converter by Team Achievers")

window.resizable(height=FALSE, width=FALSE)



primary = "#010308"
secondary = "#00ff7c"
white = "#f5df78"

## Top frame customizations 
top_frame = Frame(window, bg=primary, width=500, height = 500)
top_frame.grid(row=0, column=0)

## Label for the text Currency Converter
name_label = Label(top_frame, text = "Currency Converter", bg=primary, fg=white, pady=30, padx=120, justify=CENTER, font = ("Poppins 20 bold") )
name_label.grid(row=0, column=0)

## Customization for the bottom frame
bottom_frame = Frame(window, width=500, height=250)
bottom_frame.grid(row=1, column=0)

## widgets inside the bottom frame
from_currency_label = Label(bottom_frame, text = "Initial Currency", font = ("Poppins 10 bold"))
from_currency_label.place(x=5, y=10)

to_currency_label = Label(bottom_frame, text="Converted Currency", font=("Poppins 10 bold"))
to_currency_label.place(x=330, y=10)

## Combobox for holding from_currencies
from_currency_combo = ttk.Combobox(bottom_frame, values=list(currencies.keys()), width=18, font=("Poppins 10 bold"))
from_currency_combo.place(x=5, y=30)

## Combobox for holding to_currencies
to_currency_combo = ttk.Combobox(bottom_frame, values=list(currencies.keys()),width=18, font=("Poppins 10 bold"))
to_currency_combo.place(x=330, y=30)

## Label for Amount
amount_label = Label(bottom_frame, text= "Amount", font=("Arial 10 bold"))
amount_label.place(x=210, y=55)

## Entry for Amount
amount_entry = Entry(bottom_frame, width=25, font=("Arial 13"))
amount_entry.place(x=120, y=80)

## Empty Label for Displaying the Result
result_label = Label(bottom_frame, text="", font=("Arial 13 bold"), fg="blue", justify=CENTER)
result_label.place(x=110, y=115)

## An Empty Label for displaying the time
time_label = Label(bottom_frame, text="", font=("Poppins 10 bold"), fg="green")
time_label.place(x=100, y=230)

## Clickable Button for converting the currency
convert_button = Button(bottom_frame, text="Convert", bg="#010308", fg="#f5df78", font=("Times_New_Roman 12 bold"), command=convert_currency, padx=10, pady=10, justify=CENTER)
convert_button.place(x=180, y=165)

## Runs the Window indefinitely until its closed
window.mainloop()
