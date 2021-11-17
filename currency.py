import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk,Image
 
root = tk.Tk() 
root.title("GUI : Currency Conversion")
root.maxsize(600 , 400)

icon = PhotoImage(file = 'currencyico.png')
root.tk.call('wm' , 'iconphoto' , root._w , icon)

bg = PhotoImage(file = "BG.png")
lable_pic = Label(root , image = bg ).place(x=0 , y=0 , relwidth = 1 , relheight=1)



Tops = Frame(root,bg = '#663300',pady = 2, width =1850, height = 100, relief = "groove")
Tops.grid(row=0,column=0)

headlabel =Label(Tops,font=('Arial Rounded MT Bold', 19,'bold'), text = '                     Currency Converter                           ', bg= 'black',fg='white').grid(row=1, column=0,sticky=W)
 
var_1 = StringVar(root) 
var_2 = StringVar(root) 
 
var_1.set("Currency") 
var_2.set("Currency") 



def real_time_currency_conversion(): 
    from forex_python.converter import CurrencyRates
    c=CurrencyRates()
    
    from_currency = var_1.get() 
    to_currency = var_2.get()
    
    if (Amount1_field.get()==""):
        tkinter.messagebox.showinfo("Error !!","Amount Not Entered.\n Please a valid amount.")
        
    elif (from_currency=="currency" or to_currency=="currency"):
        tkinter.messagebox.showinfo("Error !!","Currency Not Selected.\n Please select FROM and TO Currency form menu.")
        
    else:
        new_amt = c.convert(from_currency,to_currency,float(Amount1_field.get()))
        new_amount = float("{:.4f}".format(new_amt))
        Amount2_field.insert(0, str(new_amount)) 

def clear_all() : 
	Amount1_field.delete(0, tk.END) 
	Amount2_field.delete(0, tk.END)
    
    
CurrenyCode_list = ["INR", "USD", "CAD", "CNY",  "EUR" ,'JPY','MYR','HKD','KRW','CNY', "PHP","ZAR"]


root.configure(background = '#e6e5e5') 
root.geometry("600x400") 

button_1=Label(root, font=('Arial Rounded MT Boldk', 27,'bold'), text="", padx=0,pady=0, bg="#e6e5e5",fg ="black").grid(row=1, column=0,sticky=W)
button1 = Label(root,font=('Arial Rounded MT Boldk', 15,'bold'), text = "    Amount              :", bg="#e6e5e5",fg = "black").grid(row=2, column=0,sticky=W)
button1 = Label(root,font=('Arial Rounded MT Boldk', 15,'bold'), text = "    From Currency  :", bg="#e6e5e5",fg = "black").grid(row=3, column=0,sticky=W)
button1 = Label(root,font=('Arial Rounded MT Boldk', 15,'bold'), text = "    To Currency      :", bg="#e6e5e5",fg = "black").grid(row=4, column=0,sticky=W)
button1 = Label(root,font=('Arial Rounded MT Boldk', 15,'bold'), text = "    Converted Amount  :  ", bg="#e6e5e5",fg = "black").grid(row=8, column=0,sticky=W)
button_1=Label(root, font=('Arial Rounded MT Boldk', 7,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black").grid(row=5, column=0,sticky=W)
button_1=Label(root, font=('Arial Rounded MT Boldk', 7,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black").grid(row=7, column=0,sticky=W)


FromCurrency_option = OptionMenu(root, var_1, *CurrenyCode_list ) 
ToCurrency_option = OptionMenu(root, var_2, *CurrenyCode_list) 
FromCurrency_option.grid(row = 3, column = 0, ipadx = 44.5,sticky=E) 
ToCurrency_option.grid(row = 4, column = 0, ipadx = 44.5,sticky=E) 


Amount1_field = Entry(root) 
Amount1_field.grid(row=2,column=0,ipadx =28,sticky=E)
Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8,column=0,ipadx =31,sticky=E) 


button_2 =Button(root, font=('arial', 15,'bold'), text="   Convert  ",padx=2,pady=2, bg="black",fg = "white",command=real_time_currency_conversion).grid(row=6, column=0)
button_1=Label(root, font=('Arial Rounded MT Boldk', 7,'bold'), text="",padx=2,pady=2, bg="#e6e5e5",fg ="black").grid(row=9, column=0,sticky=W)
button_2 =Button(root, font=('arial', 15,'bold'), text="   Clear All  ",padx=2,pady=2, bg="black",fg = "white",command=clear_all).grid(row=10, column=0)


root.mainloop()