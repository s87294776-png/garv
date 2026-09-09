import tkinter as tk

root = tk.Tk()
root.title("himesh")




ws=root.winfo_screenmmwidth()
hs=root.winfo_height()

w=400
h=500

x=int(ws/2-w/2)
y=int(hs/2-h/2)

data=str(w)+"x"+str(h)+str(x)+"+"+str(y)

root.geometry(data)
Label=tk.Button(root,text="welcome to my app",font=("Arial",18,"bold"))
Label.grid(row=0,column=0,columnspan=3,pady=20)



Label_btn1=tk.Label(root,text="Button 1",width=15,height=2)
Label_btn1.grid(row=0,column=0,padx=10,pady=10)
btn2=tk.Button(root,text="button 2",width=15,height=2)
btn2.grid(row=0,column=1,padx=10,pady=10)
btn3=tk.Button(root,text="button 3",width=15,height=2)
btn3.grid(row=0,column=2,padx=10,pady=10)




root.configure(background="#44B961")



root.mainloop()