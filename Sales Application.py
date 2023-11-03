from tkinter import*
root = Tk()
root.title("Sales Application")
root.geometry("700x500")
root.configure(bg = "orange")

months = ("January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits = (100, 200, 12500, 125000, 125000000, 1345, 1000000, 125456, 123456789, 1234, 151515)

month_label = Label(root, bg = "orange2", text = str(months))
profit_label = Label(root, bg = "orange2", text = str(profits))

max_label = Label(root, bg = "orange2")
min_label = Label(root, bg = "orange2")

def findMax():
    max_profit = max(profits)
    max_index = profits.index(max_profit)
    max_month = months[max_index]
    max_label["text"] = "Maximum Profit Of " + str(max_profit) + " In The Month Of " + max_month

def findMin():
    min_profit = min(profits)
    min_index = profits.index(min_profit)
    min_month = months[min_index]
    min_label["text"] = "Minimum Profit Of " + str(min_profit) + " In The Month Of " + min_month


max_btn = Button(root, command = findMax, text = "Show Maximum Profitable Month", bg = "red1")
min_btn = Button(root, command = findMin, text = "Show Minimum Profitable Month", bg = "red1")

month_label.place(relx = "0.5", rely = "0.2", anchor = CENTER)
profit_label.place(relx = "0.5", rely = "0.3", anchor = CENTER)
max_label.place(relx = "0.5", rely = "0.5", anchor = CENTER)
min_label.place(relx = "0.5", rely = "0.7", anchor = CENTER)
max_btn.place(relx = "0.5", rely = "0.4", anchor = CENTER)
min_btn.place(relx = "0.5", rely = "0.6", anchor = CENTER)



root.mainloop()