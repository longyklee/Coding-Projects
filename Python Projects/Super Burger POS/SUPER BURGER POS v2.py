import tkinter as tk
from collections import Counter as count
import datetime
from datetime import date
import sys

cashier_num = int(input("Cashier Number: "))
print()
if cashier_num == 999:
    cashier = "[999] Testing"
    print(cashier+" has successfully logged in")
if cashier_num == 101:
    cashier = "[101] Aaron Lee"
    print(cashier+" has successfully logged in")
if cashier_num == 200:
    cashier = "[200] Eric Chen"
    print(cashier+" has successfully logged in")
if cashier_num == 300:
    cashier = "[300] Maria Lopez"
    print(cashier+" has successfully logged in")
if cashier_num == 888:
    print("PASSWORD CHALLENGE: [888] Store Manager")
    manager_pswd = "ilovetw99"
    manager_pswd_entered = input("Password: ")
    print()
    if manager_pswd == manager_pswd_entered:
        cashier = "[888] Store Manager"
        print(cashier+" has successfully logged in")
    if manager_pswd != manager_pswd_entered:
        input("Wrong Password! Press Enter to Exit")
        sys.exit(0)
if cashier_num != 999:
    if cashier_num != 101:
        if cashier_num != 200:
            if cashier_num != 300:
                if cashier_num != 888:
                    input("NOT VALID!! Press Enter to EXIT")
                    sys.exit()
    
input("Press Enter to enter the SUPER BURGER POS")
specialitemyn = input("Special Item? (Y/N): ")
if specialitemyn == 'y':
    specialname = input("Special Input: ")
    specialcost = eval(input(specialname+" Costs: "))
    print()
    print("[LOG] ENTERED LOG MODE")
    timetoday = str(datetime.datetime.now())
    print("[LOGIN] "+cashier+" has entered at "+timetoday)

    class Item:
        def __init__(self, name, price, button):
            self.name = name
            self.price = price
            self.button = button

    class Register:
        def __init__(self, parent):
            self.parent = parent
            parent.title('SUPER BURGER POS (Tax is 9.5%)')
            self.font = ('Courier New', 12)
            self.till = 0
            self.TAX = 0.095
            self.items = {'fountain':Item('Fountain Soda', 150,
                                          tk.Button(root,
                                          text='Fountain Soda',
                                          command=lambda: self.scan('fountain'),
                                          font=self.font)),
                          'new':Item('--------------------------------', 0,
                                          tk.Button(root,
                                          text='New Item',
                                          command=lambda: self.scan('new'),
                                          font=self.font)),
                           'special':Item(specialname, specialcost,
                                          tk.Button(root,
                                          text=specialname,
                                          command=lambda: self.scan('special'),
                                          font=self.font)),
                           'hamburger':Item('Hamburger', 250,
                                         tk.Button(root,
                                         text='Hamburger',
                                         command=lambda: self.scan('hamburger'),
                                         font=self.font)),
                            'cheese_burger':Item('Cheese Burger', 300,
                                         tk.Button(root,
                                         text='Cheese Burger',
                                         command=lambda: self.scan('cheese_burger'),
                                         font=self.font)),
                            'fries':Item('Fries', 100,
                                         tk.Button(root,
                                         text='Fries',
                                         command=lambda: self.scan('fries'),
                                         font=self.font)),
                          'package':Item('   Package (Fries)', 150,
                                         tk.Button(root,
                                         text='Package (Fries)',
                                         command=lambda: self.scan('package'),
                                         font=self.font)),
                          'coke':Item('   Coke', 0,
                                         tk.Button(root,
                                         text='Coke',
                                         command=lambda: self.scan('coke'),
                                         font=self.font)),
                          'sprite':Item('   Sprite', 0,
                                         tk.Button(root,
                                         text='Sprite',
                                         command=lambda: self.scan('sprite'),
                                         font=self.font)),
                          'lettuce':Item('   No Lettuce', 0,
                                         tk.Button(root,
                                         text='No Lettuce',
                                         command=lambda: self.scan('lettuce'),
                                         font=self.font)),
                          'tomato':Item('   No Tomato', 0,
                                         tk.Button(root,
                                         text='No Tomato',
                                         command=lambda: self.scan('tomato'),
                                         font=self.font)),
                          'grilled_onion':Item('   Grilled Onion', 0,
                                         tk.Button(root,
                                         text='Grilled Onion',
                                         command=lambda: self.scan('grilled_onion'),
                                         font=self.font))}
            self.MAX_NAME_WIDTH = max(map(len, (item.name for item in self.items.values()))) + 3
            self.MAX_PRICE_WIDTH = 10
            self.server_label = tk.Label(root, text='Cashier: ' + cashier, font=self.font)
            self.server_label.grid(row=0, column=0, sticky='W')
            self.time_label = tk.Label(root, text='', font=self.font)
            self.time_label.grid(row=0, column=1, columnspan=4, sticky='E')
            for idx,item in enumerate(self.items.values(), start=1):
                item.button.grid(row=idx, column=0, sticky='W')
            self.frame = tk.Frame(root)
            self.frame.grid(row=1, column=1, sticky='W', rowspan=idx+1, columnspan=4)
            self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
            self.box = tk.Listbox(self.frame,
                                  yscrollcommand=self.scrollbar.set,
                                  width=self.MAX_NAME_WIDTH + self.MAX_PRICE_WIDTH + 10,
                                  font=self.font)
            self.scrollbar.config(command=self.box.yview)
            self.box.grid(row=0, column=1, sticky='NS')
            self.scrollbar.grid(row=0, column=2, sticky='NS')
            self.box.bind("<Double-Button-1>", self.modify_item)
            self.checkout_button = tk.Button(root, text='Checkout', command=self.checkout)
            self.checkout_button.grid(row=idx+2, column=1, sticky='W')
            self.till_button = tk.Button(root, text='Till', command=self.check_till)
            self.till_button.grid(row=idx+2, column=2, sticky='W')
            self.new_order_button = tk.Button(root, text='Clear', command=self.new_order)
            self.new_order_button.grid(row=idx+2, column=3, sticky='W')
            self.total_label = tk.Label(root, text='', font=self.font)
            self.total_label.grid(row=idx+2, column=4, sticky='E')
            self.new_order()
            self.tick()
        def modify_item(self, event=None):
            top = tk.Toplevel()
            entry = tk.Entry(top, font=self.font)
            entry.pack()
            entry.focus_set()
            def set_new_quantity():
                new_value = int(entry.get())
                idx = self.box.index(tk.ACTIVE)
                self.box.delete(idx)
                code = self.current_codes.pop(idx)
                self.current_order[code] -= 1
                for i in range(new_value):
                    self.scan(code)
                top.destroy()
                self.update_totals()
            confirm = tk.Button(top, text='OK', command=set_new_quantity, font=self.font)
            confirm.pack()
        def update_totals(self):
            self.subtotal = sum(self.items[key].price * value for key,value in self.current_order.items())
            self.tax = round(self.subtotal * self.TAX)
            self.total = self.subtotal + self.tax
            self.total_label.config(text=f'{self.format_money(self.subtotal):>25}\n{self.format_money(self.total):>25}')
        def scan(self, code):
            self.current_order[code] += 1
            self.current_codes.append(code)
            name = self.items[code].name
            price = self.format_money(self.items[code].price)
            self.box.insert(tk.END, f'{name:<{self.MAX_NAME_WIDTH}}' + f'{price:>{self.MAX_PRICE_WIDTH+10}}')
            self.box.see(self.box.size()-1)
            self.update_totals()
        def format_money(self, cents):
            d,c = divmod(cents, 100)
            return f'${d}.{c:0>2}'
        def checkout(self):
            self.total_label.config(text=f'TOTAL: {self.format_money(self.total)}\n')
            totalneedtobepaid = str(self.format_money(self.total))
            print("[TOTAL] Total for this transaction is "+totalneedtobepaid)
            for item in self.items.values():
                item.button.config(state=tk.DISABLED)
            top = tk.Toplevel()
            label = tk.Label(top, text='Input money: ')
            label.grid(row=0, column=0)
            text = tk.Entry(top)
            text.grid(row=0, column=1)
            text.focus_set()
            def pay(event=None):
                # tender is integer of pennies
                tender = int(text.get().replace('.', ''))
                tenderinstr = str(self.format_money(tender))
                change = tender - self.total
                print("[PAID] Paid "+tenderinstr+" to cashier")
                label.config(text=f'Change: {self.format_money(change)}. Have a nice day!')
                changeinstr = str(self.format_money(change))
                print("[CHANGE] The change for this transaction is "+changeinstr)
                print("[TRANSACTION] Cashier "+cashier+" has completed transaction with total of "+totalneedtobepaid+" and custormer paid "+tenderinstr+" with the change being "+changeinstr)
                tillinstr = str(self.format_money(self.till))
                print("[SCREENSHOT] Cashier "+cashier+" can add **"+totalneedtobepaid+"** to virtual wallet")
                print()
                self.till += self.total
                self.new_order()
                text.config(state=tk.DISABLED)
                go.config(text='Close', command=top.destroy)
            go = tk.Button(top, text='Pay', command=pay)
            go.grid(row=0, column=2)
        def check_till(self, event=None):
            top = tk.Toplevel()
            b = tk.Button(top, text=self.format_money(self.till), command=top.destroy)
            b.pack()
            b.focus_set()
        def new_order(self, event=None):
            self.subtotal = self.tax = self.total = 0
            for item in self.items.values():
                item.button.config(state=tk.NORMAL)
            self.box.delete(0, tk.END)
            self.current_order = count()
            self.current_codes = []
            self.update_totals()
        def tick(self):
            self.time_label.config(text=str(datetime.datetime.now()).rpartition('.')[0])
            self.parent.after(1000, self.tick)
    root = tk.Tk()
    app = Register(root)
    root.mainloop()
if specialitemyn == 'n':
    print()
    print("[LOG] ENTERED LOG MODE")
    timetoday = str(datetime.datetime.now())
    print("[LOGIN] "+cashier+" has entered at "+timetoday)

    class Item:
        def __init__(self, name, price, button):
            self.name = name
            self.price = price
            self.button = button

    class Register:
        def __init__(self, parent):
            self.parent = parent
            parent.title('SUPER BURGER POS (Tax is 9.5%)')
            self.font = ('Courier New', 12)
            self.till = 0
            self.TAX = 0.095
            self.items = {'fountain':Item('Fountain Soda', 150,
                                          tk.Button(root,
                                          text='Fountain Soda',
                                          command=lambda: self.scan('fountain'),
                                          font=self.font)),
                          'new':Item('--------------------------------', 0,
                                          tk.Button(root,
                                          text='New Item',
                                          command=lambda: self.scan('new'),
                                          font=self.font)),
                           'hamburger':Item('Hamburger', 250,
                                         tk.Button(root,
                                         text='Hamburger',
                                         command=lambda: self.scan('hamburger'),
                                         font=self.font)),
                            'cheese_burger':Item('Cheese Burger', 300,
                                         tk.Button(root,
                                         text='Cheese Burger',
                                         command=lambda: self.scan('cheese_burger'),
                                         font=self.font)),
                            'fries':Item('Fries', 100,
                                         tk.Button(root,
                                         text='Fries',
                                         command=lambda: self.scan('fries'),
                                         font=self.font)),
                          'package':Item('   Package (Fries)', 150,
                                         tk.Button(root,
                                         text='Package (Fries)',
                                         command=lambda: self.scan('package'),
                                         font=self.font)),
                          'coke':Item('   Coke', 0,
                                         tk.Button(root,
                                         text='Coke',
                                         command=lambda: self.scan('coke'),
                                         font=self.font)),
                          'sprite':Item('   Sprite', 0,
                                         tk.Button(root,
                                         text='Sprite',
                                         command=lambda: self.scan('sprite'),
                                         font=self.font)),
                          'lettuce':Item('   No Lettuce', 0,
                                         tk.Button(root,
                                         text='No Lettuce',
                                         command=lambda: self.scan('lettuce'),
                                         font=self.font)),
                          'tomato':Item('   No Tomato', 0,
                                         tk.Button(root,
                                         text='No Tomato',
                                         command=lambda: self.scan('tomato'),
                                         font=self.font)),
                          'grilled_onion':Item('   Grilled Onion', 0,
                                         tk.Button(root,
                                         text='Grilled Onion',
                                         command=lambda: self.scan('grilled_onion'),
                                         font=self.font))}
            self.MAX_NAME_WIDTH = max(map(len, (item.name for item in self.items.values()))) + 3
            self.MAX_PRICE_WIDTH = 10
            self.server_label = tk.Label(root, text='Cashier: ' + cashier, font=self.font)
            self.server_label.grid(row=0, column=0, sticky='W')
            self.time_label = tk.Label(root, text='', font=self.font)
            self.time_label.grid(row=0, column=1, columnspan=4, sticky='E')
            for idx,item in enumerate(self.items.values(), start=1):
                item.button.grid(row=idx, column=0, sticky='W')
            self.frame = tk.Frame(root)
            self.frame.grid(row=1, column=1, sticky='W', rowspan=idx+1, columnspan=4)
            self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
            self.box = tk.Listbox(self.frame,
                                  yscrollcommand=self.scrollbar.set,
                                  width=self.MAX_NAME_WIDTH + self.MAX_PRICE_WIDTH + 10,
                                  font=self.font)
            self.scrollbar.config(command=self.box.yview)
            self.box.grid(row=0, column=1, sticky='NS')
            self.scrollbar.grid(row=0, column=2, sticky='NS')
            self.box.bind("<Double-Button-1>", self.modify_item)
            self.checkout_button = tk.Button(root, text='Checkout', command=self.checkout)
            self.checkout_button.grid(row=idx+2, column=1, sticky='W')
            self.till_button = tk.Button(root, text='Till', command=self.check_till)
            self.till_button.grid(row=idx+2, column=2, sticky='W')
            self.new_order_button = tk.Button(root, text='Clear', command=self.new_order)
            self.new_order_button.grid(row=idx+2, column=3, sticky='W')
            self.total_label = tk.Label(root, text='', font=self.font)
            self.total_label.grid(row=idx+2, column=4, sticky='E')
            self.new_order()
            self.tick()
        def modify_item(self, event=None):
            top = tk.Toplevel()
            entry = tk.Entry(top, font=self.font)
            entry.pack()
            entry.focus_set()
            def set_new_quantity():
                new_value = int(entry.get())
                idx = self.box.index(tk.ACTIVE)
                self.box.delete(idx)
                code = self.current_codes.pop(idx)
                self.current_order[code] -= 1
                for i in range(new_value):
                    self.scan(code)
                top.destroy()
                self.update_totals()
            confirm = tk.Button(top, text='OK', command=set_new_quantity, font=self.font)
            confirm.pack()
        def update_totals(self):
            self.subtotal = sum(self.items[key].price * value for key,value in self.current_order.items())
            self.tax = round(self.subtotal * self.TAX)
            self.total = self.subtotal + self.tax
            self.total_label.config(text=f'{self.format_money(self.subtotal):>25}\n{self.format_money(self.total):>25}')
        def scan(self, code):
            self.current_order[code] += 1
            self.current_codes.append(code)
            name = self.items[code].name
            price = self.format_money(self.items[code].price)
            self.box.insert(tk.END, f'{name:<{self.MAX_NAME_WIDTH}}' + f'{price:>{self.MAX_PRICE_WIDTH+10}}')
            self.box.see(self.box.size()-1)
            self.update_totals()
        def format_money(self, cents):
            d,c = divmod(cents, 100)
            return f'${d}.{c:0>2}'
        def checkout(self):
            self.total_label.config(text=f'TOTAL: {self.format_money(self.total)}\n')
            totalneedtobepaid = str(self.format_money(self.total))
            print("[TOTAL] Total for this transaction is "+totalneedtobepaid)
            for item in self.items.values():
                item.button.config(state=tk.DISABLED)
            top = tk.Toplevel()
            label = tk.Label(top, text='Input money: ')
            label.grid(row=0, column=0)
            text = tk.Entry(top)
            text.grid(row=0, column=1)
            text.focus_set()
            def pay(event=None):
                # tender is integer of pennies
                tender = int(text.get().replace('.', ''))
                tenderinstr = str(self.format_money(tender))
                change = tender - self.total
                print("[PAID] Paid "+tenderinstr+" to cashier")
                label.config(text=f'Change: {self.format_money(change)}. Have a nice day!')
                changeinstr = str(self.format_money(change))
                print("[CHANGE] The change for this transaction is "+changeinstr)
                print("[TRANSACTION] Cashier "+cashier+" has completed transaction with total of "+totalneedtobepaid+" and custormer paid "+tenderinstr+" with the change being "+changeinstr)
                tillinstr = str(self.format_money(self.till))
                print("[SCREENSHOT] Cashier "+cashier+" can add **"+totalneedtobepaid+"** to virtual wallet")
                print()
                self.till += self.total
                self.new_order()
                text.config(state=tk.DISABLED)
                go.config(text='Close', command=top.destroy)
            go = tk.Button(top, text='Pay', command=pay)
            go.grid(row=0, column=2)
        def check_till(self, event=None):
            top = tk.Toplevel()
            b = tk.Button(top, text=self.format_money(self.till), command=top.destroy)
            b.pack()
            b.focus_set()
        def new_order(self, event=None):
            self.subtotal = self.tax = self.total = 0
            for item in self.items.values():
                item.button.config(state=tk.NORMAL)
            self.box.delete(0, tk.END)
            self.current_order = count()
            self.current_codes = []
            self.update_totals()
        def tick(self):
            self.time_label.config(text=str(datetime.datetime.now()).rpartition('.')[0])
            self.parent.after(1000, self.tick)
    root = tk.Tk()
    app = Register(root)
    root.mainloop()
