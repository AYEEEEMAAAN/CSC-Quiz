from tkinter import *

names_list = []

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
        "18",
        '8',
        '5',
        '20',
        '18'
        ,2],
    3: ["what summoner spells does a top laner use",
        'smite',
        'teleport',
        'ignite',
        'exhaust',
        'ghost',
        'teleport'
        ,2],
    4: ["what does an inhibitor do",
        'spawns minions',
        'gives health',
        'gives money',
        'spawns minions'
        ,1],
    5: ["How long till the jungle mosnters spawn at the start of the game",
       '1 minute',
       '22 seconds',
       '5 minutes',
       '30 seconds',
       '22 seconds'
       ,2]        
    
}
def randomiser():
    global qnum
    qnum = random.randit(1,10)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()




class QuizStarter:
  def __init__(self, parent):
      background_color="blue"
      #frame set up
      self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
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
      self.continue_button = Button (self.quiz_frame, text ="Continue", bg="yellow", command=self.name_collection)
      self.continue_button.grid(row=3, pady=20)

  def name_collection(self):
      name = self.entry_box.get()
      names_list.append(name)
      print(names_list)
      self.quiz_frame.destroy()
      

class Quiz :

  def __init__(self, parent):
      background_color="blue"
      #frame set up
      self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
      self.quiz_frame.grid()


      randomiser()

      #Label widget for our heading
      self.question_label = Label (self.quiz_frame, text = questions_answers[qnum][0], font=("Tw Cen Mt", "18", "bold"), bg=background_color)
      self.question_label.grid(row=0)


      self.var1=IntVar()
      

      self.rb1 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg=background      
    







#***************Starting point of program******************#
randomiser()
if __name__ == "__main__":
  root = Tk()
  root.title("League Of Legends")
  quizStarter_object = QuizStarter(root)
  root.mainloop()#so the window doesnt disappear 
  