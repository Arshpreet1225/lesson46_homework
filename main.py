import tkinter as tk
from tkinter import messagebox, ttk
class stationary():
    def __init__(self,window):
        self.window=window
        self.window.title('stationary order managment app')
        self.sta_items={"pencilbox":10,"pen":5,"pencil":5,"sharpener":4,"scale":6}
        self.exchangerate=90
        frame=ttk.Frame(window)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        ttk.Label(frame,text="stationary order managment",font=("Arial",20,"bold")).grid(row=0,columnspan=3,padx=10,pady=10)
        self.sta_label={}
        self.sta_quantity={}
        for i,(item ,price) in enumerate(self.sta_items.items(),start=1):
            label=ttk.Label(frame,text=f"{item} (${price}):",font=("Arial",12))
            label.grid(row=i,column=0,padx=10,pady=5)
            self.sta_label[item]=label
            quantity_entry=ttk.Entry(frame,width=5)
            quantity_entry.grid(row=i,column=1,padx=10,pady=5)
            self.sta_quantity[item]=quantity_entry
            self.currency_var=tk.StringVar()
            ttk.Label(frame,text='currency',font=("Arial",12)).grid(row=len(self.sta_items)+1,column=0,padx=10,pady=5)
            currency_dropdwon=ttk.Combobox(frame,textvariable=self.currency_var,state='readonly',width=18,values=('USD','INR'))
            currency_dropdwon.grid(row=len(self.sta_items)+1,column=1,padx=10,pady=5)
            currency_dropdwon.current(0)
            self.currency_var.trace("w",self.update_sta_prices)
            order_btn=ttk.Button(frame,text='place order',command=self.place_order)
            order_btn.grid(row=len(self.sta_items)+2,columnspan=3,padx=10,pady=10)
    def update_sta_prices(self,*args):
         currency=self.currency_var.get()
         rate=self.exchangerate if currency=='INR' else 1
         for item,label in self.sta_label.items():
             price=self.sta_items[item]*rate
             label.config(text=f'{item} {price}:')
    def place_order(self):
        total_cost=0
        order_summary="order summary:\n"
        currency=self.currency_var.get()
        rate=self.exchangerate if currency=='INR' else 1
        for items,entry in self.sta_quantity.items():
            quantity=entry.get()
            if quantity.isdigit():
                quantity=int(quantity)
                price=self.sta_items[items]*rate
                cost=quantity*price
                total_cost+=cost
                if quantity>0:
                    order_summary+=(f"{items}:{quantity}*{price}={cost}\n")
        if total_cost>0:
            order_summary+=f"\n total cost:{total_cost}"
            messagebox.showinfo("order placed",order_summary)
        else:
            messagebox.showerror("error","atleast order 1 item")
if __name__=="__main__":
    window=tk.Tk()
    app=stationary(window)
    window.geometry('800x600')
    window.mainloop()