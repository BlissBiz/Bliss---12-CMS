from tkinter import *
from PIL import Image, ImageTk
import random
names_list = []
asked = []
score=0

def randomiser():
  global qnum
  qnum =random.randint(1,10)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    randomiser() 


  
class Starter:
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
    self.entry_box.destroy()
    self.continue_button.destroy()
    Questions(root)

class Questions:
  def __init__(self, parent):
    self.quiz_questions = {
      1: ["Who are known as the trinity in DC?",
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
  
         5:["How did the Fantastic Four get their superpowers?",
          'Gentic mutation',
          'Chemical Spill',
          'Cosmic rays',
          'Failed Exeperiment',
          'Cosmic rays'
         ,3],
  
        6:["Who is Aquaman's side kick?",
           'Aqualad',
           'Aquaboy',
           'Aquafish',
           'Mermaid man',
           'Aqualad'
          ,1],
  
        7:["Who is Darth Vaders Master?",
          'Darth Maul',
          'Anakin Skywalker',
          'Obi-Wan Kenobi',
          'Darth Sidious',
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
  
    background_color = "lightgrey"
      #Frame setup
    # self.quiz_frame = Frame(parent, bg = background_color, padx=150, pady=300)
    # self.quiz_frame.grid()
      #randomiser 
    randomiser()
    img = Image.open("or1.jpg")
    img= img.resize((800, 700),Image.ANTIALIAS)
    picture = ImageTk.PhotoImage(img) 
    image_label.configure(image = picture) #this has to be same name you started at bottom
    image_label.image = picture # keep a reference!   

    
      #label widget for our Question
    self.question_label = Label (parent, text = self.quiz_questions[qnum][0], font=("Times", "16", "bold"), bg="orange")
    self.question_label.place(x=90, y=200)
      #Holds the value of radio buttons
    self.var1=IntVar()
  
      #Radio button 1
    self.rb1= Radiobutton(parent, text=self.quiz_questions[qnum][1], font=("Courier","11", "bold"), bg=background_color,value=1,padx=10,pady=10,
                  variable=self.var1, background = background_color)
    self.rb1.place(x=90, y=300)
        
         #Radio button 2
    self.rb2= Radiobutton(parent, text=self.quiz_questions[qnum][2], font=("Courier","11", "bold"), bg=background_color,value=2,padx=10,pady=10,
                  variable=self.var1, background = background_color)
    self.rb2.place(x=90, y=350)
  
         #Radio button 3
    self.rb3= Radiobutton(parent, text=self.quiz_questions[qnum][3], font=("Courier","11", "bold"), bg=background_color,value=3,padx=10,pady=10,
                  variable=self.var1, background = background_color)
    self.rb3.place(x=90, y=400)
        
         #Radio button 4
    self.rb4= Radiobutton(parent, text=self.quiz_questions[qnum][4], font=("Courier","11", "bold"), bg=background_color,value=4,padx=10,pady=10,
                  variable=self.var1, background = background_color)
    self.rb4.place(x=90, y=450)
  
    #Confrim answer button
    self.confirm_button = Button(parent, text="Confirm", font=("Courier","11", "bold"), bg="whitesmoke", command=self.testing)
    self.confirm_button.place(x=90, y=600)
        
        #Score Label
    self.score_label=Label(parent, text="Score", font=("Courier","11"), bg=background_color)
    self.score_label.place(x=450, y=600)


    self.quit=Button(parent, text="Quit", font=("Courier","11", 'bold'), bg="red", command=self.ending_screen)
    self.quit.place(x=300, y=600)
    
      #confifuring (editing) the question label to new questions and possible answers as new raido button choices
    #check whats wrong in this method below
  def question_setup(self):
       randomiser()
       self.var1.set(0)
       self.question_label.config(text=self.quiz_questions[qnum][0])
       self.rb1.config(text=self.quiz_questions[qnum][1])
       self.rb2.config(text=self.quiz_questions[qnum][2])
       self.rb3.config(text=self.quiz_questions[qnum][3])
       self.rb4.config(text=self.quiz_questions[qnum][4])
  
  def testing(self):
      global score
      points_label=self.score_label
      choice=self.var1.get()
      if len(asked)>9:
          if choice == self.quiz_questions[qnum][6]:
            score +=1
            points_label.configure(text=score)
            self.confirm_button.config(text="Confirm")
            self.endingScreen()
          else:
            score+=0
            points_label.configure(text="The correct answer was: " + self.quiz_questions[qnum][5])
            self.confirm_button.config(text="Confirm")
      else:
          if choice == 0:
             self.confirm_button.config(text="You didn't select an option")
             choice=self.var1.get()
             
          else:
              if choice == self.quiz_questions[qnum][6]:
                score+=1
                points_label.configure(text=score)
                self.confirm_button.config(text="Confirm")
                self.question_setup()
              else:
                score+=0
                points_label.configure(text="The right answer was : " + self.quiz_questions[qnum][5])
                self.confim_button.config(text="Confirm")
                self.question_setup()

class Ending:
  def __init__(self):
    background="darkorange"
    global opened
    opened = Tk()
    opened.title('Action Movie Quiz')
    opened.geometry('400x600')

    self.ending_frame = Frame(self.end_box, width = 1000, height = 1000, bg = background)
    self.ending_frame_frame.grid(row=1)

    self.end_heading = Label (self.end_frame, text='Well Done', font = ("Courier","22", 'bold'), bg=background, pady=15)
    self.end_heading.grid(row=0)

    self.quit= Button (self.end_frame, text='Exit', width=10, bg='Red', font=('Courier', ' 14', 'bold'), command=self.close_end)
    exit_button.grid(row=4, pady =20)

  def close_end(self):
    window.destroy()
    root.withdraw()


  
  def endingScreen(self):
    root.withdraw()
    name=names[0]
    file.open("leaderBoard.txt", "a")
    if name == "admin_rest":
      file=open("leaderBoard.txt", "w")
    else:
      file.write(str(score))
      file.write(" - ")
      file.write(name+"\n")
      file.close()

    inputFile = open("leaderBoard.txt",'r')
    lineList = inputFile.readline()
    lineList.sort()
    top=[]
    top5=(lineList[-5:])
    for line in top5:
      point=line.split(" - ")
      top.append((int(point[0]), point[1]))
    file.close()
    top.sort()
    return_string = ""
    for i in range(len(top)):
      return_string +="{} - {}\n".format(top[i][0], top[i][1])
    print(return_string)

    open_endscrn=Ending()
    open_endscrn.listLabek.config(text=return_string)
    
#************** Starting Point of Program *************#
if __name__ == '__main__':
    root = Tk()
    root.title('Action Movie Quiz')
    root.geometry('800x700')
    bg_image = Image.open('1image.png')
    bg_image = bg_image.resize((800, 700),Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    image_label= Label(root, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1) 
    quiz_starter_window = Starter(root)
    root.mainloop()