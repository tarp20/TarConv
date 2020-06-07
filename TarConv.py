from tkinter import *
from tkinter import ttk
import urllib.request
import json
from tkinter import messagebox


root = Tk()

root.title("TarConv 0.0.1")
root.geometry('400x400+900+100')
root.resizable(False, False)


START_AMOUNT = 100


def exchange():
    pass
try:
    html = urllib.request.urlopen('https://api.nbp.pl/api/exchangerates/tables/C')
    data = html.read()
    json_data = json.loads(data)
    print(json_data['ExchangeRatesTable'])
except:
	messagebox.showerror("ERROR", 'Error receiving courses')


# Header
header_frame = Frame(root)
header_frame.pack(fill=X)
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

h_cur = Label(header_frame, text="Currency", bg='#ccc', font='Arial 12 bold')
h_cur.grid(row=0, column=0, sticky=EW)
h_buy = Label(header_frame, text='Buy', bg='#ccc', font='Arial 12 bold')
h_buy.grid(row=0, column=1, sticky=EW)
h_sale = Label(header_frame, text='Sale', bg='#ccc', font='Arial 12 bold')
h_sale.grid(row=0, column=2, sticky=EW)


# USD
usd_cur = Label(header_frame, text='USD', font='Arial 10')
usd_cur.grid(row=1, column=0, sticky=EW)
usd_buy = Label(header_frame, text='unn', font='Arial 10')
usd_buy.grid(row=1, column=1, sticky=EW)
usd_sale = Label(header_frame, text='unn', font='Arial 10')
usd_sale.grid(row=1, column=2, sticky=EW)


eur_cur = Label(header_frame, text='EUR', font='Arial 10')
eur_cur.grid(row=2, column=0, sticky=EW)
eur_buy = Label(header_frame, text='unn', font='Arial 10')
eur_buy.grid(row=2, column=1, sticky=EW)
eur_sale = Label(header_frame, text='unn', font='Arial 10')
eur_sale.grid(row=2, column=2, sticky=EW)


# UAH
uah_cur = Label(header_frame, text='UAH', font='Arial 10')
uah_cur.grid(row=3, column=0, sticky=EW)
uah_buy = Label(header_frame, text='unn', font='Arial 10')
uah_buy.grid(row=3, column=1, sticky=EW)
uah_sale = Label(header_frame, text='unn', font='Arial 10')
uah_sale.grid(row=3, column=2, sticky=EW)


# Calc Frame

calc_frame = Label(root, bg="#fff")
calc_frame.pack(expand=1, fill=BOTH)
calc_frame.grid_columnconfigure(1,weight = 1)


#PLN

l_pln =Label(calc_frame, text = 'PLN',bg = '#fff',font = 'Arial 10 bold')
l_pln.grid(row = 0,column = 0 ,padx = 10)
e_pln = ttk.Entry(calc_frame,justify= CENTER,font="Arial 10 bold")
e_pln.grid(row = 0,column = 1,columnspan = 2,pady = 10,padx = 10,sticky =EW)
e_pln.insert(0, START_AMOUNT)


btn_calc = ttk.Button(calc_frame,text = "Calculate",command  = exchange)
btn_calc.grid(row=1,column=1,columnspan=2,sticky = EW,padx=10)


res_frame = Frame(root)
res_frame.pack(expand=1, fill=BOTH, pady=5)
res_frame.grid_columnconfigure(1, weight=1)


l_usd = Label(res_frame, text="USD:", font="Arial 10 bold")
l_usd.grid(row=2, column=0)
e_usd = ttk.Entry(res_frame, justify=CENTER, font="Arial 10")
e_usd.grid(row=2, column=1, columnspan=2, padx=10, sticky=EW)
e_usd.insert(0, "unn")


# EUR
l_eur = Label(res_frame, text="EUR:", font="Arial 10 bold")
l_eur.grid(row=3, column=0)
e_eur = ttk.Entry(res_frame, justify=CENTER, font="Arial 10")
e_eur.grid(row=3, column=1, columnspan=2, padx=10, sticky=EW)
e_eur.insert(0, "unn")

# UAH
l_rur = Label(res_frame, text="UAH:", font="Arial 10 bold")
l_rur.grid(row=4, column=0)
e_rur = ttk.Entry(res_frame, justify=CENTER, font="Arial 10")
e_rur.grid(row=4, column=1, columnspan=2, padx=10, sticky=EW)
e_rur.insert(0, "unn")





root.mainloop()
