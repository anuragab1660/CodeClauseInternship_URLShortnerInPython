from tkinter import *
import pyshorteners

root = Tk()
root.title("Simple URL Shortener App")
width = 400
height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2) 
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="white")

def urlShortend():
    s=pyshorteners.Shortener().tinyurl.short(URL.get())
    RESULT.set(s)
    URL.set("")

URL = StringVar()
RESULT = StringVar()


Top = Frame(root, width=400, bd=1, relief=SOLID)
Top.pack(side=TOP)
BottomTitle = Frame(root, width=400, bd=1, relief=SOLID)
BottomTitle.pack(side=TOP, pady=10)
BottomForm = Frame(root, width=400, bg="white")
BottomForm.pack(side=TOP)




lbl_title = Label(Top, text="SIMPLE URL SHORTENER APP", width=400 ,font=('arial', 18))
lbl_title.pack(fill=X)
lbl1 = Label(BottomForm, text="Enter your URL",font=('arial', 12))
lbl1.grid(row=0, columnspan=5, column=0)




myurl = Entry(BottomForm, textvariable=URL, width=50)
myurl.grid(row=1, column=1)
result_txt = Entry(BottomForm, textvariable=RESULT,font=('arial', 10), width=50, bd=0)
result_txt.grid(row=4, columnspan=5, column=0)


btn = Button(BottomForm, text="Shortend", width=20,fg="black", bg="white", command=urlShortend)
btn.grid(row=2, columnspan=5, column=0, pady=10)


if __name__ == '__main__':
    root.mainloop()
