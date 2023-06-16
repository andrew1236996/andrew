from tkinter import *

window = Tk()
window.title("bank app")
window.geometry("300x266")


def saving():
    root= Tk()
    root.title("saving account")
    root .geometry("360*266")
    balance_lbl = Button(master = root, text="balance",)
    balance_lbl.pack()
    withdrawl_btn =Button(master = root, text="balance" ,padx=10)



    withdrawl_btn.pack()
    deposite_btn = Button(master=root, text="deposit",padx=10)
    deposite_btn.pack()

def current():
    root = Tk()
    root.title("current account")
    root.geometry("380*266")
    balance_lbl= Button(master=root, text="balance")
    balance_lbl.pack()
    withdrawl_btn= Button(master=root , text="withdraw",  padx=10)
    withdrawl_btn.pack()
    deposit_btn = Button(master=root,text="deposite",padx=10)
    deposit_btn.pack()

def balance():
    acc_balance= "$4000"
    Label(master=window, text=acc_balance.pack() )

def withdraw():
    root2= Tk()
    root2.title("withdrawal")
    root2.geometry("366x266")
    amount_entry = Entry(master=root2)
    amount_entry.pack()
    amount_entry + float(balance)


    lbl= Label(master=window,text="what is your type of account")
    lbl.pack()
    saving_btn = Button(master=window, text="saving",command=saving())
    saving_btn.pack()

    current_btn = Button(master=window,text="current",command=current)
