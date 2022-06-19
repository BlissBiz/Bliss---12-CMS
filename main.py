from tkinter import *
from PIL import Image, ImageTk

names_list = []
global question_answers
asked = []
questions_answers = {
    1: ["Who is the trinity in DC?",
       'Batman, Superman, Flash',
       'Batman, Superman, Wonder Woman',
       'Batman, Superman, Green Lantern',
       'Batman, Aquaman, Flash',
       'Batman, Superman, Wonder Woman'
       ,2],

    2: ["Why did Thor go to earth?",
        'Because he went for fun',
        'He heard the Avengers were being formed',
        'He was being disobedient to his father',
        'He was tricked by Loki',
        'He was being disobedient to his father'
         ,3],

      3: ["Who founded the Avengers?",
         'Captian America',
         'Bruce Banner',
         'Ironman',
         'Nick Fury',
         'Nick Fury'
         ,4],


      4:["How is the Green Lantern Ring powered?",
         'Willpower',
         'Hope',
         'Justice',
         'Virtue',
         'Willpower'
         ,1],

       5:["How did the Fantastic Four get their superpowers?"
        'Gentic mutation'
        'Chemical Spill'
        'Cosmic rays'
        'Failed Exeperiment'
        'Cosmic rays'
       ,3],

      6:["Who is Aquaman's side kick?",
         'Aqualad',
         'Aquaboy'
         'Aquafish',
         'Mermaid man',
         'Aqualad'
        ,1],

      7:["Who is Darth Vaders Master?",
        'Darth Maul'
        'Anakin Skywalker'
        'Obi-Wan Kenobi'
        'Darth Sidious'
        'Darth Sidious'
         ,4],

      8:["Who did Dwayne Johnson play in Fast and Furious?",
        'Deckard Shaw',
        'Luke Hobbs',
        'Victor Loke',
        'Jonah',
        'Deckard Shaw'
        ,1],


      9:["In The Batman, who was the main villan",
        'Carmine Falcone',
        'The Penguin',
        'The Riddler',
        'The Joker',
        'The Riddler'
        ,3],


      10:["Who is the Chosen One in Starwars",
        'Luke Skywalker',
        'Anakin Skywalker',
        'Rey Skywalker',
        'Chewbacca',
        'Anakin Skywalker'       
       ,2],
}




  
class QuizStarter:

  def __init__(self, parent):
 

    #users input is taken by an Entry Widget
    self.entry_box=Entry(parent)
    self.entry_box.place(x=480, y=640)

  #continue Button
    self.continue_button = Button (parent, text="Next", bg="orange", command=self.name_collection)
    self.continue_button.place(x=723, y=640)

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
  root.geometry('800x700')
  bg_image = Image.open('1image.png')
  bg_image = bg_image.resize((800, 700),Image.ANTIALIAS)
  bg_image = ImageTk.PhotoImage(bg_image)
  image_label= Label(root, image=bg_image)
  image_label.place(x=0, y=0, relwidth=1, relheight=1) 
  quiz_starter_window = QuizStarter(root)
  root.mainloop()