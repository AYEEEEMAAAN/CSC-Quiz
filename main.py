from tkinter import *
import random
asked=[]
names_list=[]
score = 0

global questions_answers


# Dictionary has key of number (for each question and number) and : the value for each is a list that has 7 items, so index 0 to 6
questions_answers = {
    1: ["What role constantly roams the map and helps the team", 
        'Top laner', 
        'Mid',
        'ADC', 
        'Support',
        'Jungler', 
        'Jungler' 
        ,5], 
    2: ["What is the max level you can reach withing a game",
        '16',
        '20',
        '8',
        '5',
        '18',
        '18'
        ,5],
    3: ["What summoner spells does a top laner use",
        'smite',
        'ghost',
        'ignite',
        'exhaust',
        'teleport',
        'teleport'
        ,5],
    4: ["What does an inhibitor do",
        'extra damage',
        'extra life',
        'gives money',
        'gives vision',
        'spawns minions',
        'spawns minions'
        ,5],
    5: ["How long till the jungle mosnters spawn at the start of the game",
       '1 minute',
       '10 seconds',
       '5 minutes',
       '30 seconds',
       '22 seconds',
       '22 seconds'
       ,5],
    6: ["How many champions are there in the game",
       '50',
       '80',
       '140',
       '20',
       '90',
       '140'
       ,3], 
    7: ["How mnay lanes are there in the map",
       '2',
       '3',
       '5',
       '1',
       '4',
       '3'
       ,2],
    8: ["What is the name of the server that Australia and New Zealand plays on",
       'oceania',
       'asia',
       'america',
       'germany',
       'europe',
       'oceania'
       ,2],
    9: ["How many items can you have all together",
       '3',
       '6',
       '8',
       '5',
       '2',
       '6'
       ,2],    
    10: ["When was league of legends released",
       'october 2009',
       'september 2009',
       'january 2009',
       'march 2009',
       'july 2009',
       'october 2009'
       ,2],     
    
}
def randomiser():
  global qnum
  qnum = random.randint(1,10)
  if qnum not in asked:
      asked.append(qnum)
  elif qnum in asked:
      randomiser()




class QuizStarter:
  def __init__(self, parent):
      background_color="white"
      #frame set up
      self.quiz_frame = Frame(parent, bg = background_color, padx = 100, pady = 100)
      self.quiz_frame.grid()

      #Label widget for our heading
      self.heading_label = Label (self.quiz_frame, text = "League Of Legends Quiz", font=("Tw Cen Mt", "18", "bold"), bg=background_color)
      self.heading_label.grid(row=0)

      #Label for user name prompt
      self.user_label = Label ( self.quiz_frame, text= "Please enter your name below", font=("Tw Cen MT", "16"), bg=background_color)
      self.user_label.grid(row=1, pady=20)

      #users input is taken by Entry Widget
      self.entry_box=Entry(self.quiz_frame)
      self.entry_box.grid(row=2, pady=20)

      #continue Button
      self.continue_button = Button (self.quiz_frame, text ="Continue", bg="grey", command=self.name_collection)
      self.continue_button.grid(row=3, pady=20)

  def name_collection(self):
    name=self.entry_box.get()
    if name.strip () != "" and len (name) <= 15:
       names_list.append(name)
       self.quiz_frame.destroy()
       Quiz(root)
    elif len(name) >15:
      self.user_label.config(text="Please enter name of 1-15 charcters", fg="red")
    elif len(name) ==0 :
      self.user_label.config(text="Must enter at least 1 character", fg="red")
      

class Quiz :

  def __init__(self, parent):
      background_color="white"
      #frame set up
      self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
      self.quiz_frame.grid()


      randomiser()
      #Label widget for our heading
      self.question_label = Label (self.quiz_frame, text = questions_answers[qnum][0], font = ("Tw Cen Mt", "18", "bold"), bg = background_color)
      self.question_label.grid(row=0)


      self.var1=IntVar()
      

      self.rb1 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_color,value=1,padx=50,pady=5, variable=self.var1, indicator = 0, background = "lightblue")
      self.rb1.grid(row=2, sticky=W)   

      self.rb2 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg=background_color,value=2,padx=40,pady=5,variable=self.var1, indicator = 0, background = "lightblue")
      self.rb2.grid(row=3, sticky=W)   

      self.rb3 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_color,value=3,padx=40,pady=5,variable=self.var1, indicator = 0, background = "lightblue")
      self.rb3.grid(row=4, sticky=W)   

      self.rb4 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg=background_color,value=4,padx=40,pady=5,variable=self.var1, indicator = 0, background = "lightblue")
      self.rb4.grid(row=5, sticky=W)

      self.rb5 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][5], font=("Helvetica", "12"), bg=background_color,value=5,padx=40,pady=5,variable=self.var1, indicator = 0, background = "lightblue")
      self.rb5.grid(row=6, sticky=W)   

      self.confirm_button= Button(self.quiz_frame, text="Confirm", font=("Helvetica","13", "bold" ), bg="grey", command=self.test_progress)
      self.confirm_button.grid(row=7, padx=5, pady=5)

      self.score_label=Label(self.quiz_frame, text="SCORE", font=("Tw Cen MT", "16"),bg=background_color,)
      self.score_label.grid(row=8, padx=10, pady=3)

  def questions_setup(self):
        randomiser()
        self.var1.set(0)
        self.question_label.config(text=questions_answers[qnum][0])
        self.rb1.config(text=questions_answers[qnum][1])
        self.rb2.config(text=questions_answers[qnum][2])
        self.rb3.config(text=questions_answers[qnum][3])
        self.rb4.config(text=questions_answers[qnum][4])
        self.rb5.config(text=questions_answers[qnum][5])


  def test_progress(self):
       global score
       scr_label = self.score_label
       choice = self.var1.get()
       if len(asked)>9:#if the question is last
          if choice == questions_answers[qnum][6]:#if last question is right answer
              score +=1
              scr_label.configure(text = score)
              self.confirm_button.config(text = "confirm")
              self.end_frame()

          else:#if the last question is wrong answer
              score +=0
              scr_label.configure(text = "The correct answer was " + questions_answers[qnum][5])
              self.confirm_button.config(text= "Confirm")
              self.end_frame()

       else: 
          if choice == 0: #check if the user has made a choice
              self.confirm_button.configure(text = "Try again please, you didnt select anything")
              choice = self.var1.get()
          else:# if they made a choice and its not last question
             if choice == questions_answers[qnum][6]:#if their choice is right
                 score +=1
                 scr_label.configure(text = score)
                 self.confirm_button.configure(text = "Confirm")
                 self.questions_setup()#run this method to move to next question 
             else: #if the choice is wrong
              score +=0
              scr_label.configure(text = "The correct answer was: " + questions_answers[qnum][5])
              self.confirm_button.configure(text = "Confirm")
              self.questions_setup()

  def end_frame(self):
      root.withdraw()
      name=names_list[0]
      file=open("LeaderBoard.txt","a")
      file.write(str(score))
      file.write(" - ")
      file.write(name+"\n")
      file.close()

      inputFile = open("LeaderBoard.txt", "r")
      lineList = inputFile.readlines()
      lineList.sort()
      top=[]
      print(top)
      top5=(lineList[-5:])
      for line in top5:
          point=line.split(" - ")
          top.append((int(point[0]), point[1]))
      file.close()
      top.sort()
      top.reverse()
      return_string=""
      for i in range(len(top)):
            return_string +="{} - {}\n".format(top[i][0], top[i][1])
      print(return_string)

      open_endscrn=End()
      open_endscrn.listLabel.config(text=return_string)
    





class End:
    def __init__(self):
        background="white"
        self.end_box= Toplevel(root)
        self.end_box.title("End Box")

        self.end_frame = Frame (self.end_box, width=1000, height=1000, bg=background)
        self.end_frame.grid()

        end_heading = Label (self.end_frame, text='Well Done', font=('Tw Cen MT', 22, 'bold'),fg='White', bg=background, pady=15)
        end_heading.grid(row=0)

        exit_button = Button (self.end_frame, text='Exit', width=10, bg='grey', font=('Tw Cen MT', 12, 'bold'),fg='black', command=self.close_end)
        exit_button.grid(row=4, pady=20)
        self.listLabel = Label(self.end_frame, text="1st Place Avaliable", font=("Tw Cen MT", 18), width=40, bg=background,fg="black", padx=10, pady=10)
        self.listLabel.grid(column=0, row=2)

        self.quit= Button(self.end_frame, text="Quit", font=("Helvetica", "13", "bold",))

    
    def close_end(self):
        self.end_box.destroy()
        root.withdraw()





#***************Starting point of program******************#
randomiser()
if __name__ == "__main__":
  root = Tk()
  root.title("League Of Legends")
  quizStarter_object = QuizStarter(root)
  root.mainloop()#so the window doesnt disappear 
  