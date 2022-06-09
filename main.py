from tkinter import *
from PIL import Image, ImageTk

names_list = []

class QuizStarter:

  def __init__(self, parent):
 
    #Label for user name prompt
    #self.user_label = Label (parent, text="Please enter your name below", font=("Tw Cen MT", "18", "bold"))
    #self.user_label.place(x=200, y=50)

    #users input is taken by an Entry Widget
    self.entry_box=Entry(parent)
    self.entry_box.place(x=486, y=618)

  #continue Button
    self.continue_button = Button (parent, text="Next", bg="orange", command=self.name_collection)
    self.continue_button.place(x=717, y=618)

  def name_collection(self):
    name = self.entry_box.get()
    names_list.append(name)
    print(names_list)
    self.user_label.destroy()
    #Quiz(root)




#************** Starting Point of Program *************#
if __name__ == '__main__':
  root = Tk()
  root.title('Action movie quiz')
  root.geometry('750x650')
  bg_image = Image.open('placeholder.png')
  bg_image = bg_image.resize((750, 650),Image.ANTIALIAS)
  bg_image = ImageTk.PhotoImage(bg_image)
  image_label= Label(root, image=bg_image)
  image_label.place(x=0, y=0, relwidth=1, relheight=1) 
  quiz_starter_window = QuizStarter(root)
  root.mainloop()