from tkinter import *
from PIL import ImageTk,Image 
from Bot import processes


root=Tk()
root.title("Phoebe")
root.iconbitmap(r'C:\Users\itians\Desktop\Phoebe\an.ico')



bg_img= ImageTk.PhotoImage(Image.open(r'C:\Users\itians\Phoebe\an.jpg'))
img_label=Label(image=bg_img)
img_label.grid(row=0,column=0,columnspan=3)



startButton = Button(root,text="Wake Phoebe",command=processes)
startButton.grid(row=1,column=0)
#text_label=Label(root,text=processes())
#text_label.grid(row=1,column=1)
exitButton = Button(root,text="Sleep/Stop", command=root.quit)
exitButton.grid(row=1,column=2)


root.mainloop()
