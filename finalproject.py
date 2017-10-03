listdata=[]
i = 0
team1= ("Rohodothea Karagiannis", "Mira Shah", "Jasmine Rodrigo")
team2= ("Adam Pitkin", "Joseph Baviello", "David Rabinovich")
team3= ("Orlev Gabbay", "Salvatore Costa", "Suzanne Silecchia")
team4= ("Kieran Reilly", "Bari Buchberg", "Jennifer Paez")
team5= ("Anita Wong", "Ben Su", "Jinyoung Moon")
team6= ("Zachary Tinn", "Fabian Perez", "Desiree Coombs")
team7= ("Kyle Alexander", "Thomas Gentzlinger", "William Weisbach") 
team8= ("Mandy Au", "William Kuettel", "Peiyu Zhang") 
team9= ("Shamsudeen Williams", "Justin Chang", "Kaichen Peng") 
team10= ("Cassidy Hartmann", "Raul Morales", "Chloe Tso") 
team11= ("Jacqueline Kaufman", "Araon Lai", "Huihui Wu") 
#create a dicitonary of teams and team members
Teams= {"Team 1": team1, "Team 2": team2, "Team 3": team3, "Team 4": team4, "Team 5": team5,"Team 6": team6, "Team 7": team7,"Team 8": team8, "Team 9": team9, "Team 10": team10, "Team 11": team11}
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

#creates a names object that is similar to the criteria class but alters listnames       
class TeamsGUI:
    def __init__(self):
        self.w = Tk()
        self.w.title('Welcome to the Team evaluation form')
        #create and position the frame 
        self.f = ttk.Frame(self.w, padding=(5, 5, 12, 0))
        self.f.grid(column=0, row=0, sticky=(N,W,E,S))
        self.w.grid_columnconfigure(0, weight=1)
        self.w.grid_rowconfigure(0,weight=1)
        self.lab_welcome = Label(self.f, text="Welcome to the team evaluation form for \n MIS 325: Essentials of Programming!") 
        self.lab_name = Label(self.f, text="Please enter your name: ")
        self.name = StringVar()
        self.ent = Entry(self.f, textvariable = self.name, width=15)
        self.lab_team = Label(self.f, text="Please select your team:")
        self.selected = StringVar()
        self.selected.set ("Team 1") 
        self.dropdown = OptionMenu(self.f, self.selected,*Teams)
        self.Confirm_button = Button(self.f, text="Confirm", command=self.confirm)
        self.Quit_button = Button(self.f, text="Quit", command=self.quit)


        self.lab_welcome.grid(column = 0, columnspan = 10, row = 1, sticky = N) 
        self.lab_name.grid(column = 1, row = 3, sticky = E)
        self.ent.grid(column = 2, columnspan = 3, row = 3, sticky = W)
        self.lab_team.grid(column = 1, row = 5, sticky = W)
        self.dropdown.grid(column = 2, row = 5, padx = 15, pady = 5, sticky =(N,W,E,S))
        self.Confirm_button.grid(column=2, row=15, sticky=W)
        self.Quit_button.grid(column=3, row=15, sticky=W)
            
        mainloop()

    def confirm(self):
        self.w.destroy()
        choice = self.selected.get()
        if choice == 'Team 1':
                Team1GUI()
        elif choice == 'Team 2':
                Team2GUI()
        elif choice == 'Team 3':
                Team3GUI()
        elif choice == 'Team 4':
                Team4GUI()
        elif choice == 'Team 5':
                Team5GUI()
        elif choice == 'Team 6':
                Team6GUI()
        elif choice == 'Team 7':
                Team7GUI()
        elif choice == 'Team 8':
                Team8GUI()
        elif choice == 'Team 9':
                Team9GUI()
        elif choice == 'Team 10':
                Team10GUI()
        elif choice == 'Team 11':
                Team11GUI()
    
            

    def quit(self):
        self.w.destroy()
        print("Forgot your team? Go check and come back again!")

class Team1GUI: 
    def __init__(self):
        global i
        while i < 3: 
            self.w = Tk()
            self.w.title('Welcome to the Team Evaluation form for Team 1')
            #create and position the frame 
            self.f = ttk.Frame(self.w, padding=(5, 5, 12, 0))
            self.f.grid(column=0, row=0, sticky=(N,W,E,S))
            self.w.grid_columnconfigure(0, weight=1)
            self.w.grid_rowconfigure(0,weight=1)

            #define all the widgets
            #creates an entry box for user to type their name 
            #creates associated label and a status label
            #creates an Enter button
            #creates a dropdown menu to select the team
            #creates a done button to exit the window

            self.lab3 = Label(self.f, text='Teammate:'+team1[i])
            self.lab_rating = Label(self.f, text="Please evaluate your team members according to the following criteria:\n 1 = Terrible, 2 = Bad, 3 = Average, 4 = Good, 5 = Outstanding \n Choose N/A if the person displayed is you.")
            
            #Attendance Radio Buttons
            self.a_radio_var =IntVar()
            self.a_radio_var.set(1)
            self.a_label = Label(self.f, text='Attendance') 
            self.a_rb1 = Radiobutton(self.f, text='1', variable=self.a_radio_var, value=1)
            self.a_rb2 = Radiobutton(self.f, text='2', variable=self.a_radio_var, value=2)
            self.a_rb3 = Radiobutton(self.f, text='3', variable=self.a_radio_var, value=3)
            self.a_rb4 = Radiobutton(self.f, text='4', variable=self.a_radio_var, value=4)
            self.a_rb5 = Radiobutton(self.f, text='5', variable=self.a_radio_var, value=5)
            self.a_rb6 = Radiobutton(self.f, text='N/A', variable=self.a_radio_var, value=0)

            #Communication Radio Buttons
            self.cm_radio_var =IntVar()
            self.cm_radio_var.set(1)
            self.cm_label = Label(self.f, text='Communication') 
            self.cm_rb1 = Radiobutton(self.f, text='1', variable=self.cm_radio_var, value=1)
            self.cm_rb2 = Radiobutton(self.f, text='2', variable=self.cm_radio_var, value=2)
            self.cm_rb3 = Radiobutton(self.f, text='3', variable=self.cm_radio_var, value=3)
            self.cm_rb4 = Radiobutton(self.f, text='4', variable=self.cm_radio_var, value=4)
            self.cm_rb5 = Radiobutton(self.f, text='5', variable=self.cm_radio_var, value=5)
            self.cm_rb6 = Radiobutton(self.f, text='N/A', variable=self.cm_radio_var, value=0)

            #Contribution Radio Buttons
            self.c_radio_var =IntVar()
            self.c_radio_var.set(1)
            self.c_label = Label(self.f, text='Contribution') 
            self.c_rb1 = Radiobutton(self.f, text='1', variable=self.c_radio_var, value=1)
            self.c_rb2 = Radiobutton(self.f, text='2', variable=self.c_radio_var, value=2)
            self.c_rb3 = Radiobutton(self.f, text='3', variable=self.c_radio_var, value=3)
            self.c_rb4 = Radiobutton(self.f, text='4', variable=self.c_radio_var, value=4)
            self.c_rb5 = Radiobutton(self.f, text='5', variable=self.c_radio_var, value=5)
            self.c_rb6 = Radiobutton(self.f, text='N/A', variable=self.c_radio_var, value=0)

            #Next and Quit buttons 
            self.Next_button = Button(self.f, text="Next", command=self.next)
            self.Quit_button = Button(self.f, text="Quit", command=self.quit)

            #pack the widgets
            self.lab3.grid(column = 0, row = 6, rowspan = 2, sticky = W)
            self.lab_rating.grid(column = 1, row = 8, columnspan = 5, rowspan= 3, sticky = W)
            
            #pack radiobutton widgets 
            self.a_label.grid(column = 0, row = 11, columnspan = 3 , sticky = W)
            self.a_rb1.grid(column = 1, row = 11, sticky = W)
            self.a_rb2.grid(column = 2, row = 11, sticky = W) 
            self.a_rb3.grid(column = 3, row = 11, sticky = W)
            self.a_rb4.grid(column = 4, row = 11, sticky = W)
            self.a_rb5.grid(column = 5, row = 11, sticky = W)
            self.a_rb6.grid(column = 6, row = 11, sticky = W) 

            self.cm_label.grid(column = 0, row = 12, columnspan = 4, sticky = W)
            self.cm_rb1.grid(column = 1, row = 12, sticky = W)
            self.cm_rb2.grid(column = 2, row = 12, sticky = W) 
            self.cm_rb3.grid(column = 3, row = 12, sticky = W)
            self.cm_rb4.grid(column = 4, row = 12, sticky = W)
            self.cm_rb5.grid(column = 5, row = 12, sticky = W)
            self.cm_rb6.grid(column = 6, row = 12, sticky = W)

            self.c_label.grid(column = 0, row = 13, columnspan = 4, sticky = W)
            self.c_rb1.grid(column = 1, row = 13, sticky = W)
            self.c_rb2.grid(column = 2, row = 13, sticky = W) 
            self.c_rb3.grid(column = 3, row = 13, sticky = W)
            self.c_rb4.grid(column = 4, row = 13, sticky = W)
            self.c_rb5.grid(column = 5, row = 13, sticky = W)
            self.c_rb6.grid(column = 6, row = 13, sticky = W)
            
            #pack submit and quit buttons 
            self.Next_button.grid(column=2, row=15, sticky=W)
            self.Quit_button.grid(column=3, row=15, sticky=W)

            
            i+=1
            #Enter tinkter mainloop
            mainloop()
    def next(self):
        if i == 1:
            self.w.destroy()
            listTemp = [str(team1[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 2:
            self.w.destroy()
            listTemp = [str(team1[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 3:
            self.w.destroy()
            listTemp = [str(team1[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
            print ('Here is the evaluation for Team 1! \n', end='\n' "".join(map(str, listdata)))

    def quit(self):
        global i
        i+=3
        self.w.destroy()
        print("Just rated someone wrong? It's okay let's restart!")

class Team2GUI: 
    def __init__(self):
        global i
        while i < 3: 
            self.w = Tk()
            self.w.title('Welcome to the Team Evaluation form for Team 2')
            #create and position the frame 
            self.f = ttk.Frame(self.w, padding=(5, 5, 12, 0))
            self.f.grid(column=0, row=0, sticky=(N,W,E,S))
            self.w.grid_columnconfigure(0, weight=1)
            self.w.grid_rowconfigure(0,weight=1)

            #define all the widgets
            #creates an entry box for user to type their name 
            #creates associated label and a status label
            #creates an Enter button
            #creates a dropdown menu to select the team
            #creates a done button to exit the window

            self.lab3 = Label(self.f, text='Teammate:'+team2[i])
            self.lab_rating = Label(self.f, text="Please evaluate your team members according to the following criteria:\n 1 = Terrible, 2 = Bad, 3 = Average, 4 = Good, 5 = Outstanding \n Choose N/A if the person displayed is you.")
            
            #Attendance Radio Buttons
            self.a_radio_var =IntVar()
            self.a_radio_var.set(1)
            self.a_label = Label(self.f, text='Attendance') 
            self.a_rb1 = Radiobutton(self.f, text='1', variable=self.a_radio_var, value=1)
            self.a_rb2 = Radiobutton(self.f, text='2', variable=self.a_radio_var, value=2)
            self.a_rb3 = Radiobutton(self.f, text='3', variable=self.a_radio_var, value=3)
            self.a_rb4 = Radiobutton(self.f, text='4', variable=self.a_radio_var, value=4)
            self.a_rb5 = Radiobutton(self.f, text='5', variable=self.a_radio_var, value=5)
            self.a_rb6 = Radiobutton(self.f, text='N/A', variable=self.a_radio_var, value=0)

            #Communication Radio Buttons
            self.cm_radio_var =IntVar()
            self.cm_radio_var.set(1)
            self.cm_label = Label(self.f, text='Communication') 
            self.cm_rb1 = Radiobutton(self.f, text='1', variable=self.cm_radio_var, value=1)
            self.cm_rb2 = Radiobutton(self.f, text='2', variable=self.cm_radio_var, value=2)
            self.cm_rb3 = Radiobutton(self.f, text='3', variable=self.cm_radio_var, value=3)
            self.cm_rb4 = Radiobutton(self.f, text='4', variable=self.cm_radio_var, value=4)
            self.cm_rb5 = Radiobutton(self.f, text='5', variable=self.cm_radio_var, value=5)
            self.cm_rb6 = Radiobutton(self.f, text='N/A', variable=self.cm_radio_var, value=0)

            #Contribution Radio Buttons
            self.c_radio_var =IntVar()
            self.c_radio_var.set(1)
            self.c_label = Label(self.f, text='Contribution') 
            self.c_rb1 = Radiobutton(self.f, text='1', variable=self.c_radio_var, value=1)
            self.c_rb2 = Radiobutton(self.f, text='2', variable=self.c_radio_var, value=2)
            self.c_rb3 = Radiobutton(self.f, text='3', variable=self.c_radio_var, value=3)
            self.c_rb4 = Radiobutton(self.f, text='4', variable=self.c_radio_var, value=4)
            self.c_rb5 = Radiobutton(self.f, text='5', variable=self.c_radio_var, value=5)
            self.c_rb6 = Radiobutton(self.f, text='N/A', variable=self.c_radio_var, value=0)

            #Next and Quit buttons 
            self.Next_button = Button(self.f, text="Next", command=self.next)
            self.Quit_button = Button(self.f, text="Quit", command=self.quit)

            #pack the widgets
            self.lab3.grid(column = 0, row = 6, rowspan = 2, sticky = W)
            self.lab_rating.grid(column = 1, row = 8, columnspan = 5, rowspan= 3, sticky = W)
            
            #pack radiobutton widgets 
            self.a_label.grid(column = 0, row = 11, columnspan = 3 , sticky = W)
            self.a_rb1.grid(column = 1, row = 11, sticky = W)
            self.a_rb2.grid(column = 2, row = 11, sticky = W) 
            self.a_rb3.grid(column = 3, row = 11, sticky = W)
            self.a_rb4.grid(column = 4, row = 11, sticky = W)
            self.a_rb5.grid(column = 5, row = 11, sticky = W)
            self.a_rb6.grid(column = 6, row = 11, sticky = W) 

            self.cm_label.grid(column = 0, row = 12, columnspan = 4, sticky = W)
            self.cm_rb1.grid(column = 1, row = 12, sticky = W)
            self.cm_rb2.grid(column = 2, row = 12, sticky = W) 
            self.cm_rb3.grid(column = 3, row = 12, sticky = W)
            self.cm_rb4.grid(column = 4, row = 12, sticky = W)
            self.cm_rb5.grid(column = 5, row = 12, sticky = W)
            self.cm_rb6.grid(column = 6, row = 12, sticky = W)

            self.c_label.grid(column = 0, row = 13, columnspan = 4, sticky = W)
            self.c_rb1.grid(column = 1, row = 13, sticky = W)
            self.c_rb2.grid(column = 2, row = 13, sticky = W) 
            self.c_rb3.grid(column = 3, row = 13, sticky = W)
            self.c_rb4.grid(column = 4, row = 13, sticky = W)
            self.c_rb5.grid(column = 5, row = 13, sticky = W)
            self.c_rb6.grid(column = 6, row = 13, sticky = W)
            
            #pack submit and quit buttons 
            self.Next_button.grid(column=2, row=15, sticky=W)
            self.Quit_button.grid(column=3, row=15, sticky=W)

            
            i+=1
            #Enter tinkter mainloop
            mainloop()
    def next(self):
        if i == 1:
            self.w.destroy()
            listTemp = [str(team2[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 2:
            self.w.destroy()
            listTemp = [str(team2[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 3:
            self.w.destroy()
            listTemp = [str(team2[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
            print ('Here is the evaluation for Team 2! \n', end='\n' "".join(map(str, listdata)))

    def quit(self):
        global i
        i+=3
        self.w.destroy()
        print("Just rated someone wrong? It's okay let's restart!")

class Team3GUI: 
    def __init__(self):
        global i
        while i < 3: 
            self.w = Tk()
            self.w.title('Welcome to the Team Evaluation form for Team 3')
            #create and position the frame 
            self.f = ttk.Frame(self.w, padding=(5, 5, 12, 0))
            self.f.grid(column=0, row=0, sticky=(N,W,E,S))
            self.w.grid_columnconfigure(0, weight=1)
            self.w.grid_rowconfigure(0,weight=1)

            #define all the widgets
            #creates an entry box for user to type their name 
            #creates associated label and a status label
            #creates an Enter button
            #creates a dropdown menu to select the team
            #creates a done button to exit the window

            self.lab3 = Label(self.f, text='Teammate:'+team3[i])
            self.lab_rating = Label(self.f, text="Please evaluate your team members according to the following criteria:\n 1 = Terrible, 2 = Bad, 3 = Average, 4 = Good, 5 = Outstanding \n Choose N/A if the person displayed is you.")
            
            #Attendance Radio Buttons
            self.a_radio_var =IntVar()
            self.a_radio_var.set(1)
            self.a_label = Label(self.f, text='Attendance') 
            self.a_rb1 = Radiobutton(self.f, text='1', variable=self.a_radio_var, value=1)
            self.a_rb2 = Radiobutton(self.f, text='2', variable=self.a_radio_var, value=2)
            self.a_rb3 = Radiobutton(self.f, text='3', variable=self.a_radio_var, value=3)
            self.a_rb4 = Radiobutton(self.f, text='4', variable=self.a_radio_var, value=4)
            self.a_rb5 = Radiobutton(self.f, text='5', variable=self.a_radio_var, value=5)
            self.a_rb6 = Radiobutton(self.f, text='N/A', variable=self.a_radio_var, value=0)

            #Communication Radio Buttons
            self.cm_radio_var =IntVar()
            self.cm_radio_var.set(1)
            self.cm_label = Label(self.f, text='Communication') 
            self.cm_rb1 = Radiobutton(self.f, text='1', variable=self.cm_radio_var, value=1)
            self.cm_rb2 = Radiobutton(self.f, text='2', variable=self.cm_radio_var, value=2)
            self.cm_rb3 = Radiobutton(self.f, text='3', variable=self.cm_radio_var, value=3)
            self.cm_rb4 = Radiobutton(self.f, text='4', variable=self.cm_radio_var, value=4)
            self.cm_rb5 = Radiobutton(self.f, text='5', variable=self.cm_radio_var, value=5)
            self.cm_rb6 = Radiobutton(self.f, text='N/A', variable=self.cm_radio_var, value=0)

            #Contribution Radio Buttons
            self.c_radio_var =IntVar()
            self.c_radio_var.set(1)
            self.c_label = Label(self.f, text='Contribution') 
            self.c_rb1 = Radiobutton(self.f, text='1', variable=self.c_radio_var, value=1)
            self.c_rb2 = Radiobutton(self.f, text='2', variable=self.c_radio_var, value=2)
            self.c_rb3 = Radiobutton(self.f, text='3', variable=self.c_radio_var, value=3)
            self.c_rb4 = Radiobutton(self.f, text='4', variable=self.c_radio_var, value=4)
            self.c_rb5 = Radiobutton(self.f, text='5', variable=self.c_radio_var, value=5)
            self.c_rb6 = Radiobutton(self.f, text='N/A', variable=self.c_radio_var, value=0)

            #Next and Quit buttons 
            self.Next_button = Button(self.f, text="Next", command=self.next)
            self.Quit_button = Button(self.f, text="Quit", command=self.quit)

            #pack the widgets
            self.lab3.grid(column = 0, row = 6, rowspan = 2, sticky = W)
            self.lab_rating.grid(column = 1, row = 8, columnspan = 5, rowspan= 3, sticky = W)
            
            #pack radiobutton widgets 
            self.a_label.grid(column = 0, row = 11, columnspan = 3 , sticky = W)
            self.a_rb1.grid(column = 1, row = 11, sticky = W)
            self.a_rb2.grid(column = 2, row = 11, sticky = W) 
            self.a_rb3.grid(column = 3, row = 11, sticky = W)
            self.a_rb4.grid(column = 4, row = 11, sticky = W)
            self.a_rb5.grid(column = 5, row = 11, sticky = W)
            self.a_rb6.grid(column = 6, row = 11, sticky = W) 

            self.cm_label.grid(column = 0, row = 12, columnspan = 4, sticky = W)
            self.cm_rb1.grid(column = 1, row = 12, sticky = W)
            self.cm_rb2.grid(column = 2, row = 12, sticky = W) 
            self.cm_rb3.grid(column = 3, row = 12, sticky = W)
            self.cm_rb4.grid(column = 4, row = 12, sticky = W)
            self.cm_rb5.grid(column = 5, row = 12, sticky = W)
            self.cm_rb6.grid(column = 6, row = 12, sticky = W)

            self.c_label.grid(column = 0, row = 13, columnspan = 4, sticky = W)
            self.c_rb1.grid(column = 1, row = 13, sticky = W)
            self.c_rb2.grid(column = 2, row = 13, sticky = W) 
            self.c_rb3.grid(column = 3, row = 13, sticky = W)
            self.c_rb4.grid(column = 4, row = 13, sticky = W)
            self.c_rb5.grid(column = 5, row = 13, sticky = W)
            self.c_rb6.grid(column = 6, row = 13, sticky = W)
            
            #pack submit and quit buttons 
            self.Next_button.grid(column=2, row=15, sticky=W)
            self.Quit_button.grid(column=3, row=15, sticky=W)

            
            i+=1
            #Enter tinkter mainloop
            mainloop()
    def next(self):
        if i == 1:
            self.w.destroy()
            listTemp = [str(team1[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 2:
            self.w.destroy()
            listTemp = [str(team1[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 3:
            self.w.destroy()
            listTemp = [str(team1[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
            print ('Here is the evaluation for Team 3! \n', end='\n' "".join(map(str, listdata)))

    def quit(self):
        global i
        i+=3
        self.w.destroy()
        print("Just rated someone wrong? It's okay let's restart!")

class Team4GUI: 
    def __init__(self):
        global i
        while i < 3: 
            self.w = Tk()
            self.w.title('Welcome to the Team Evaluation form for Team 4')
            #create and position the frame 
            self.f = ttk.Frame(self.w, padding=(5, 5, 12, 0))
            self.f.grid(column=0, row=0, sticky=(N,W,E,S))
            self.w.grid_columnconfigure(0, weight=1)
            self.w.grid_rowconfigure(0,weight=1)

            #define all the widgets
            #creates an entry box for user to type their name 
            #creates associated label and a status label
            #creates an Enter button
            #creates a dropdown menu to select the team
            #creates a done button to exit the window

            self.lab3 = Label(self.f, text='Teammate:'+team4[i])
            self.lab_rating = Label(self.f, text="Please evaluate your team members according to the following criteria:\n 1 = Terrible, 2 = Bad, 3 = Average, 4 = Good, 5 = Outstanding \n Choose N/A if the person displayed is you.")
            
            #Attendance Radio Buttons
            self.a_radio_var =IntVar()
            self.a_radio_var.set(1)
            self.a_label = Label(self.f, text='Attendance') 
            self.a_rb1 = Radiobutton(self.f, text='1', variable=self.a_radio_var, value=1)
            self.a_rb2 = Radiobutton(self.f, text='2', variable=self.a_radio_var, value=2)
            self.a_rb3 = Radiobutton(self.f, text='3', variable=self.a_radio_var, value=3)
            self.a_rb4 = Radiobutton(self.f, text='4', variable=self.a_radio_var, value=4)
            self.a_rb5 = Radiobutton(self.f, text='5', variable=self.a_radio_var, value=5)
            self.a_rb6 = Radiobutton(self.f, text='N/A', variable=self.a_radio_var, value=0)

            #Communication Radio Buttons
            self.cm_radio_var =IntVar()
            self.cm_radio_var.set(1)
            self.cm_label = Label(self.f, text='Communication') 
            self.cm_rb1 = Radiobutton(self.f, text='1', variable=self.cm_radio_var, value=1)
            self.cm_rb2 = Radiobutton(self.f, text='2', variable=self.cm_radio_var, value=2)
            self.cm_rb3 = Radiobutton(self.f, text='3', variable=self.cm_radio_var, value=3)
            self.cm_rb4 = Radiobutton(self.f, text='4', variable=self.cm_radio_var, value=4)
            self.cm_rb5 = Radiobutton(self.f, text='5', variable=self.cm_radio_var, value=5)
            self.cm_rb6 = Radiobutton(self.f, text='N/A', variable=self.cm_radio_var, value=0)

            #Contribution Radio Buttons
            self.c_radio_var =IntVar()
            self.c_radio_var.set(1)
            self.c_label = Label(self.f, text='Contribution') 
            self.c_rb1 = Radiobutton(self.f, text='1', variable=self.c_radio_var, value=1)
            self.c_rb2 = Radiobutton(self.f, text='2', variable=self.c_radio_var, value=2)
            self.c_rb3 = Radiobutton(self.f, text='3', variable=self.c_radio_var, value=3)
            self.c_rb4 = Radiobutton(self.f, text='4', variable=self.c_radio_var, value=4)
            self.c_rb5 = Radiobutton(self.f, text='5', variable=self.c_radio_var, value=5)
            self.c_rb6 = Radiobutton(self.f, text='N/A', variable=self.c_radio_var, value=0)

            #Next and Quit buttons 
            self.Next_button = Button(self.f, text="Next", command=self.next)
            self.Quit_button = Button(self.f, text="Quit", command=self.quit)

            #pack the widgets
            self.lab3.grid(column = 0, row = 6, rowspan = 2, sticky = W)
            self.lab_rating.grid(column = 1, row = 8, columnspan = 5, rowspan= 3, sticky = W)
            
            #pack radiobutton widgets 
            self.a_label.grid(column = 0, row = 11, columnspan = 3 , sticky = W)
            self.a_rb1.grid(column = 1, row = 11, sticky = W)
            self.a_rb2.grid(column = 2, row = 11, sticky = W) 
            self.a_rb3.grid(column = 3, row = 11, sticky = W)
            self.a_rb4.grid(column = 4, row = 11, sticky = W)
            self.a_rb5.grid(column = 5, row = 11, sticky = W)
            self.a_rb6.grid(column = 6, row = 11, sticky = W) 

            self.cm_label.grid(column = 0, row = 12, columnspan = 4, sticky = W)
            self.cm_rb1.grid(column = 1, row = 12, sticky = W)
            self.cm_rb2.grid(column = 2, row = 12, sticky = W) 
            self.cm_rb3.grid(column = 3, row = 12, sticky = W)
            self.cm_rb4.grid(column = 4, row = 12, sticky = W)
            self.cm_rb5.grid(column = 5, row = 12, sticky = W)
            self.cm_rb6.grid(column = 6, row = 12, sticky = W)

            self.c_label.grid(column = 0, row = 13, columnspan = 4, sticky = W)
            self.c_rb1.grid(column = 1, row = 13, sticky = W)
            self.c_rb2.grid(column = 2, row = 13, sticky = W) 
            self.c_rb3.grid(column = 3, row = 13, sticky = W)
            self.c_rb4.grid(column = 4, row = 13, sticky = W)
            self.c_rb5.grid(column = 5, row = 13, sticky = W)
            self.c_rb6.grid(column = 6, row = 13, sticky = W)
            
            #pack submit and quit buttons 
            self.Next_button.grid(column=2, row=15, sticky=W)
            self.Quit_button.grid(column=3, row=15, sticky=W)

            
            i+=1
            #Enter tinkter mainloop
            mainloop()
    def next(self):
        if i == 1:
            self.w.destroy()
            listTemp = [str(team4[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 2:
            self.w.destroy()
            listTemp = [str(team4[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 3:
            self.w.destroy()
            listTemp = [str(team4[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
            print ('Here is the evaluation for Team 4! \n', end='\n' "".join(map(str, listdata)))

    def quit(self):
        global i
        i+=3
        self.w.destroy()
        print("Just rated someone wrong? It's okay let's restart!")

class Team5GUI: 
    def __init__(self):
        global i
        while i < 3: 
            self.w = Tk()
            self.w.title('Welcome to the Team Evaluation form for Team 5')
            #create and position the frame 
            self.f = ttk.Frame(self.w, padding=(5, 5, 12, 0))
            self.f.grid(column=0, row=0, sticky=(N,W,E,S))
            self.w.grid_columnconfigure(0, weight=1)
            self.w.grid_rowconfigure(0,weight=1)

            #define all the widgets
            #creates an entry box for user to type their name 
            #creates associated label and a status label
            #creates an Enter button
            #creates a dropdown menu to select the team
            #creates a done button to exit the window

            self.lab3 = Label(self.f, text='Teammate:'+team5[i])
            self.lab_rating = Label(self.f, text="Please evaluate your team members according to the following criteria:\n 1 = Terrible, 2 = Bad, 3 = Average, 4 = Good, 5 = Outstanding \n Choose N/A if the person displayed is you.")
            
            #Attendance Radio Buttons
            self.a_radio_var =IntVar()
            self.a_radio_var.set(1)
            self.a_label = Label(self.f, text='Attendance') 
            self.a_rb1 = Radiobutton(self.f, text='1', variable=self.a_radio_var, value=1)
            self.a_rb2 = Radiobutton(self.f, text='2', variable=self.a_radio_var, value=2)
            self.a_rb3 = Radiobutton(self.f, text='3', variable=self.a_radio_var, value=3)
            self.a_rb4 = Radiobutton(self.f, text='4', variable=self.a_radio_var, value=4)
            self.a_rb5 = Radiobutton(self.f, text='5', variable=self.a_radio_var, value=5)
            self.a_rb6 = Radiobutton(self.f, text='N/A', variable=self.a_radio_var, value=0)

            #Communication Radio Buttons
            self.cm_radio_var =IntVar()
            self.cm_radio_var.set(1)
            self.cm_label = Label(self.f, text='Communication') 
            self.cm_rb1 = Radiobutton(self.f, text='1', variable=self.cm_radio_var, value=1)
            self.cm_rb2 = Radiobutton(self.f, text='2', variable=self.cm_radio_var, value=2)
            self.cm_rb3 = Radiobutton(self.f, text='3', variable=self.cm_radio_var, value=3)
            self.cm_rb4 = Radiobutton(self.f, text='4', variable=self.cm_radio_var, value=4)
            self.cm_rb5 = Radiobutton(self.f, text='5', variable=self.cm_radio_var, value=5)
            self.cm_rb6 = Radiobutton(self.f, text='N/A', variable=self.cm_radio_var, value=0)

            #Contribution Radio Buttons
            self.c_radio_var =IntVar()
            self.c_radio_var.set(1)
            self.c_label = Label(self.f, text='Contribution') 
            self.c_rb1 = Radiobutton(self.f, text='1', variable=self.c_radio_var, value=1)
            self.c_rb2 = Radiobutton(self.f, text='2', variable=self.c_radio_var, value=2)
            self.c_rb3 = Radiobutton(self.f, text='3', variable=self.c_radio_var, value=3)
            self.c_rb4 = Radiobutton(self.f, text='4', variable=self.c_radio_var, value=4)
            self.c_rb5 = Radiobutton(self.f, text='5', variable=self.c_radio_var, value=5)
            self.c_rb6 = Radiobutton(self.f, text='N/A', variable=self.c_radio_var, value=0)

            #Next and Quit buttons 
            self.Next_button = Button(self.f, text="Next", command=self.next)
            self.Quit_button = Button(self.f, text="Quit", command=self.quit)

            #pack the widgets
            self.lab3.grid(column = 0, row = 6, rowspan = 2, sticky = W)
            self.lab_rating.grid(column = 1, row = 8, columnspan = 5, rowspan= 3, sticky = W)
            
            #pack radiobutton widgets 
            self.a_label.grid(column = 0, row = 11, columnspan = 3 , sticky = W)
            self.a_rb1.grid(column = 1, row = 11, sticky = W)
            self.a_rb2.grid(column = 2, row = 11, sticky = W) 
            self.a_rb3.grid(column = 3, row = 11, sticky = W)
            self.a_rb4.grid(column = 4, row = 11, sticky = W)
            self.a_rb5.grid(column = 5, row = 11, sticky = W)
            self.a_rb6.grid(column = 6, row = 11, sticky = W) 

            self.cm_label.grid(column = 0, row = 12, columnspan = 4, sticky = W)
            self.cm_rb1.grid(column = 1, row = 12, sticky = W)
            self.cm_rb2.grid(column = 2, row = 12, sticky = W) 
            self.cm_rb3.grid(column = 3, row = 12, sticky = W)
            self.cm_rb4.grid(column = 4, row = 12, sticky = W)
            self.cm_rb5.grid(column = 5, row = 12, sticky = W)
            self.cm_rb6.grid(column = 6, row = 12, sticky = W)

            self.c_label.grid(column = 0, row = 13, columnspan = 4, sticky = W)
            self.c_rb1.grid(column = 1, row = 13, sticky = W)
            self.c_rb2.grid(column = 2, row = 13, sticky = W) 
            self.c_rb3.grid(column = 3, row = 13, sticky = W)
            self.c_rb4.grid(column = 4, row = 13, sticky = W)
            self.c_rb5.grid(column = 5, row = 13, sticky = W)
            self.c_rb6.grid(column = 6, row = 13, sticky = W)
            
            #pack submit and quit buttons 
            self.Next_button.grid(column=2, row=15, sticky=W)
            self.Quit_button.grid(column=3, row=15, sticky=W)

            
            i+=1
            #Enter tinkter mainloop
            mainloop()
    def next(self):
        if i == 1:
            self.w.destroy()
            listTemp = [str(team5[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 2:
            self.w.destroy()
            listTemp = [str(team5[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 3:
            self.w.destroy()
            listTemp = [str(team5[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
            print ('Here is the evaluation for Team 5! \n', end='\n' "".join(map(str, listdata)))

    def quit(self):
        global i
        i+=3
        self.w.destroy()
        print("Just rated someone wrong? It's okay let's restart!")

class Team6GUI: 
    def __init__(self):
        global i
        while i < 3: 
            self.w = Tk()
            self.w.title('Welcome to the Team Evaluation form for Team 6')
            #create and position the frame 
            self.f = ttk.Frame(self.w, padding=(5, 5, 12, 0))
            self.f.grid(column=0, row=0, sticky=(N,W,E,S))
            self.w.grid_columnconfigure(0, weight=1)
            self.w.grid_rowconfigure(0,weight=1)

            #define all the widgets
            #creates an entry box for user to type their name 
            #creates associated label and a status label
            #creates an Enter button
            #creates a dropdown menu to select the team
            #creates a done button to exit the window

            self.lab3 = Label(self.f, text='Teammate:'+team6[i])
            self.lab_rating = Label(self.f, text="Please evaluate your team members according to the following criteria:\n 1 = Terrible, 2 = Bad, 3 = Average, 4 = Good, 5 = Outstanding \n Choose N/A if the person displayed is you.")
            
            #Attendance Radio Buttons
            self.a_radio_var =IntVar()
            self.a_radio_var.set(1)
            self.a_label = Label(self.f, text='Attendance') 
            self.a_rb1 = Radiobutton(self.f, text='1', variable=self.a_radio_var, value=1)
            self.a_rb2 = Radiobutton(self.f, text='2', variable=self.a_radio_var, value=2)
            self.a_rb3 = Radiobutton(self.f, text='3', variable=self.a_radio_var, value=3)
            self.a_rb4 = Radiobutton(self.f, text='4', variable=self.a_radio_var, value=4)
            self.a_rb5 = Radiobutton(self.f, text='5', variable=self.a_radio_var, value=5)
            self.a_rb6 = Radiobutton(self.f, text='N/A', variable=self.a_radio_var, value=0)

            #Communication Radio Buttons
            self.cm_radio_var =IntVar()
            self.cm_radio_var.set(1)
            self.cm_label = Label(self.f, text='Communication') 
            self.cm_rb1 = Radiobutton(self.f, text='1', variable=self.cm_radio_var, value=1)
            self.cm_rb2 = Radiobutton(self.f, text='2', variable=self.cm_radio_var, value=2)
            self.cm_rb3 = Radiobutton(self.f, text='3', variable=self.cm_radio_var, value=3)
            self.cm_rb4 = Radiobutton(self.f, text='4', variable=self.cm_radio_var, value=4)
            self.cm_rb5 = Radiobutton(self.f, text='5', variable=self.cm_radio_var, value=5)
            self.cm_rb6 = Radiobutton(self.f, text='N/A', variable=self.cm_radio_var, value=0)

            #Contribution Radio Buttons
            self.c_radio_var =IntVar()
            self.c_radio_var.set(1)
            self.c_label = Label(self.f, text='Contribution') 
            self.c_rb1 = Radiobutton(self.f, text='1', variable=self.c_radio_var, value=1)
            self.c_rb2 = Radiobutton(self.f, text='2', variable=self.c_radio_var, value=2)
            self.c_rb3 = Radiobutton(self.f, text='3', variable=self.c_radio_var, value=3)
            self.c_rb4 = Radiobutton(self.f, text='4', variable=self.c_radio_var, value=4)
            self.c_rb5 = Radiobutton(self.f, text='5', variable=self.c_radio_var, value=5)
            self.c_rb6 = Radiobutton(self.f, text='N/A', variable=self.c_radio_var, value=0)

            #Next and Quit buttons 
            self.Next_button = Button(self.f, text="Next", command=self.next)
            self.Quit_button = Button(self.f, text="Quit", command=self.quit)

            #pack the widgets
            self.lab3.grid(column = 0, row = 6, rowspan = 2, sticky = W)
            self.lab_rating.grid(column = 1, row = 8, columnspan = 5, rowspan= 3, sticky = W)
            
            #pack radiobutton widgets 
            self.a_label.grid(column = 0, row = 11, columnspan = 3 , sticky = W)
            self.a_rb1.grid(column = 1, row = 11, sticky = W)
            self.a_rb2.grid(column = 2, row = 11, sticky = W) 
            self.a_rb3.grid(column = 3, row = 11, sticky = W)
            self.a_rb4.grid(column = 4, row = 11, sticky = W)
            self.a_rb5.grid(column = 5, row = 11, sticky = W)
            self.a_rb6.grid(column = 6, row = 11, sticky = W) 

            self.cm_label.grid(column = 0, row = 12, columnspan = 4, sticky = W)
            self.cm_rb1.grid(column = 1, row = 12, sticky = W)
            self.cm_rb2.grid(column = 2, row = 12, sticky = W) 
            self.cm_rb3.grid(column = 3, row = 12, sticky = W)
            self.cm_rb4.grid(column = 4, row = 12, sticky = W)
            self.cm_rb5.grid(column = 5, row = 12, sticky = W)
            self.cm_rb6.grid(column = 6, row = 12, sticky = W)

            self.c_label.grid(column = 0, row = 13, columnspan = 4, sticky = W)
            self.c_rb1.grid(column = 1, row = 13, sticky = W)
            self.c_rb2.grid(column = 2, row = 13, sticky = W) 
            self.c_rb3.grid(column = 3, row = 13, sticky = W)
            self.c_rb4.grid(column = 4, row = 13, sticky = W)
            self.c_rb5.grid(column = 5, row = 13, sticky = W)
            self.c_rb6.grid(column = 6, row = 13, sticky = W)
            
            #pack submit and quit buttons 
            self.Next_button.grid(column=2, row=15, sticky=W)
            self.Quit_button.grid(column=3, row=15, sticky=W)

            
            i+=1
            #Enter tinkter mainloop
            mainloop()
    def next(self):
        if i == 1:
            self.w.destroy()
            listTemp = [str(team6[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 2:
            self.w.destroy()
            listTemp = [str(team6[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 3:
            self.w.destroy()
            listTemp = [str(team6[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
            print ('Here is the evaluation for Team 6! \n', end='\n' "".join(map(str, listdata)))

    def quit(self):
        global i
        i+=3
        self.w.destroy()
        print("Just rated someone wrong? It's okay let's restart!")

class Team7GUI: 
    def __init__(self):
        global i
        while i < 3: 
            self.w = Tk()
            self.w.title('Welcome to the Team Evaluation form for Team 7')
            #create and position the frame 
            self.f = ttk.Frame(self.w, padding=(5, 5, 12, 0))
            self.f.grid(column=0, row=0, sticky=(N,W,E,S))
            self.w.grid_columnconfigure(0, weight=1)
            self.w.grid_rowconfigure(0,weight=1)

            #define all the widgets
            #creates an entry box for user to type their name 
            #creates associated label and a status label
            #creates an Enter button
            #creates a dropdown menu to select the team
            #creates a done button to exit the window

            self.lab3 = Label(self.f, text='Teammate:'+team7[i])
            self.lab_rating = Label(self.f, text="Please evaluate your team members according to the following criteria:\n 1 = Terrible, 2 = Bad, 3 = Average, 4 = Good, 5 = Outstanding \n Choose N/A if the person displayed is you.")
            
            #Attendance Radio Buttons
            self.a_radio_var =IntVar()
            self.a_radio_var.set(1)
            self.a_label = Label(self.f, text='Attendance') 
            self.a_rb1 = Radiobutton(self.f, text='1', variable=self.a_radio_var, value=1)
            self.a_rb2 = Radiobutton(self.f, text='2', variable=self.a_radio_var, value=2)
            self.a_rb3 = Radiobutton(self.f, text='3', variable=self.a_radio_var, value=3)
            self.a_rb4 = Radiobutton(self.f, text='4', variable=self.a_radio_var, value=4)
            self.a_rb5 = Radiobutton(self.f, text='5', variable=self.a_radio_var, value=5)
            self.a_rb6 = Radiobutton(self.f, text='N/A', variable=self.a_radio_var, value=0)

            #Communication Radio Buttons
            self.cm_radio_var =IntVar()
            self.cm_radio_var.set(1)
            self.cm_label = Label(self.f, text='Communication') 
            self.cm_rb1 = Radiobutton(self.f, text='1', variable=self.cm_radio_var, value=1)
            self.cm_rb2 = Radiobutton(self.f, text='2', variable=self.cm_radio_var, value=2)
            self.cm_rb3 = Radiobutton(self.f, text='3', variable=self.cm_radio_var, value=3)
            self.cm_rb4 = Radiobutton(self.f, text='4', variable=self.cm_radio_var, value=4)
            self.cm_rb5 = Radiobutton(self.f, text='5', variable=self.cm_radio_var, value=5)
            self.cm_rb6 = Radiobutton(self.f, text='N/A', variable=self.cm_radio_var, value=0)

            #Contribution Radio Buttons
            self.c_radio_var =IntVar()
            self.c_radio_var.set(1)
            self.c_label = Label(self.f, text='Contribution') 
            self.c_rb1 = Radiobutton(self.f, text='1', variable=self.c_radio_var, value=1)
            self.c_rb2 = Radiobutton(self.f, text='2', variable=self.c_radio_var, value=2)
            self.c_rb3 = Radiobutton(self.f, text='3', variable=self.c_radio_var, value=3)
            self.c_rb4 = Radiobutton(self.f, text='4', variable=self.c_radio_var, value=4)
            self.c_rb5 = Radiobutton(self.f, text='5', variable=self.c_radio_var, value=5)
            self.c_rb6 = Radiobutton(self.f, text='N/A', variable=self.c_radio_var, value=0)

            #Next and Quit buttons 
            self.Next_button = Button(self.f, text="Next", command=self.next)
            self.Quit_button = Button(self.f, text="Quit", command=self.quit)

            #pack the widgets
            self.lab3.grid(column = 0, row = 6, rowspan = 2, sticky = W)
            self.lab_rating.grid(column = 1, row = 8, columnspan = 5, rowspan= 3, sticky = W)
            
            #pack radiobutton widgets 
            self.a_label.grid(column = 0, row = 11, columnspan = 3 , sticky = W)
            self.a_rb1.grid(column = 1, row = 11, sticky = W)
            self.a_rb2.grid(column = 2, row = 11, sticky = W) 
            self.a_rb3.grid(column = 3, row = 11, sticky = W)
            self.a_rb4.grid(column = 4, row = 11, sticky = W)
            self.a_rb5.grid(column = 5, row = 11, sticky = W)
            self.a_rb6.grid(column = 6, row = 11, sticky = W) 

            self.cm_label.grid(column = 0, row = 12, columnspan = 4, sticky = W)
            self.cm_rb1.grid(column = 1, row = 12, sticky = W)
            self.cm_rb2.grid(column = 2, row = 12, sticky = W) 
            self.cm_rb3.grid(column = 3, row = 12, sticky = W)
            self.cm_rb4.grid(column = 4, row = 12, sticky = W)
            self.cm_rb5.grid(column = 5, row = 12, sticky = W)
            self.cm_rb6.grid(column = 6, row = 12, sticky = W)

            self.c_label.grid(column = 0, row = 13, columnspan = 4, sticky = W)
            self.c_rb1.grid(column = 1, row = 13, sticky = W)
            self.c_rb2.grid(column = 2, row = 13, sticky = W) 
            self.c_rb3.grid(column = 3, row = 13, sticky = W)
            self.c_rb4.grid(column = 4, row = 13, sticky = W)
            self.c_rb5.grid(column = 5, row = 13, sticky = W)
            self.c_rb6.grid(column = 6, row = 13, sticky = W)
            
            #pack submit and quit buttons 
            self.Next_button.grid(column=2, row=15, sticky=W)
            self.Quit_button.grid(column=3, row=15, sticky=W)

            
            i+=1
            #Enter tinkter mainloop
            mainloop()
    def next(self):
        if i == 1:
            self.w.destroy()
            listTemp = [str(team7[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 2:
            self.w.destroy()
            listTemp = [str(team7[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 3:
            self.w.destroy()
            listTemp = [str(team7[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
            print ('Here is the evaluation for Team 7! \n', end='\n' "".join(map(str, listdata)))

    def quit(self):
        global i
        i+=3
        self.w.destroy()
        print("Just rated someone wrong? It's okay let's restart!")

class Team8GUI: 
    def __init__(self):
        global i
        while i < 3: 
            self.w = Tk()
            self.w.title('Welcome to the Team Evaluation form for Team 8')
            #create and position the frame 
            self.f = ttk.Frame(self.w, padding=(5, 5, 12, 0))
            self.f.grid(column=0, row=0, sticky=(N,W,E,S))
            self.w.grid_columnconfigure(0, weight=1)
            self.w.grid_rowconfigure(0,weight=1)

            #define all the widgets
            #creates an entry box for user to type their name 
            #creates associated label and a status label
            #creates an Enter button
            #creates a dropdown menu to select the team
            #creates a done button to exit the window

            self.lab3 = Label(self.f, text='Teammate:'+team8[i])
            self.lab_rating = Label(self.f, text="Please evaluate your team members according to the following criteria:\n 1 = Terrible, 2 = Bad, 3 = Average, 4 = Good, 5 = Outstanding \n Choose N/A if the person displayed is you.")
            
            #Attendance Radio Buttons
            self.a_radio_var =IntVar()
            self.a_radio_var.set(1)
            self.a_label = Label(self.f, text='Attendance') 
            self.a_rb1 = Radiobutton(self.f, text='1', variable=self.a_radio_var, value=1)
            self.a_rb2 = Radiobutton(self.f, text='2', variable=self.a_radio_var, value=2)
            self.a_rb3 = Radiobutton(self.f, text='3', variable=self.a_radio_var, value=3)
            self.a_rb4 = Radiobutton(self.f, text='4', variable=self.a_radio_var, value=4)
            self.a_rb5 = Radiobutton(self.f, text='5', variable=self.a_radio_var, value=5)
            self.a_rb6 = Radiobutton(self.f, text='N/A', variable=self.a_radio_var, value=0)

            #Communication Radio Buttons
            self.cm_radio_var =IntVar()
            self.cm_radio_var.set(1)
            self.cm_label = Label(self.f, text='Communication') 
            self.cm_rb1 = Radiobutton(self.f, text='1', variable=self.cm_radio_var, value=1)
            self.cm_rb2 = Radiobutton(self.f, text='2', variable=self.cm_radio_var, value=2)
            self.cm_rb3 = Radiobutton(self.f, text='3', variable=self.cm_radio_var, value=3)
            self.cm_rb4 = Radiobutton(self.f, text='4', variable=self.cm_radio_var, value=4)
            self.cm_rb5 = Radiobutton(self.f, text='5', variable=self.cm_radio_var, value=5)
            self.cm_rb6 = Radiobutton(self.f, text='N/A', variable=self.cm_radio_var, value=0)

            #Contribution Radio Buttons
            self.c_radio_var =IntVar()
            self.c_radio_var.set(1)
            self.c_label = Label(self.f, text='Contribution') 
            self.c_rb1 = Radiobutton(self.f, text='1', variable=self.c_radio_var, value=1)
            self.c_rb2 = Radiobutton(self.f, text='2', variable=self.c_radio_var, value=2)
            self.c_rb3 = Radiobutton(self.f, text='3', variable=self.c_radio_var, value=3)
            self.c_rb4 = Radiobutton(self.f, text='4', variable=self.c_radio_var, value=4)
            self.c_rb5 = Radiobutton(self.f, text='5', variable=self.c_radio_var, value=5)
            self.c_rb6 = Radiobutton(self.f, text='N/A', variable=self.c_radio_var, value=0)

            #Next and Quit buttons 
            self.Next_button = Button(self.f, text="Next", command=self.next)
            self.Quit_button = Button(self.f, text="Quit", command=self.quit)

            #pack the widgets
            self.lab3.grid(column = 0, row = 6, rowspan = 2, sticky = W)
            self.lab_rating.grid(column = 1, row = 8, columnspan = 5, rowspan= 3, sticky = W)
            
            #pack radiobutton widgets 
            self.a_label.grid(column = 0, row = 11, columnspan = 3 , sticky = W)
            self.a_rb1.grid(column = 1, row = 11, sticky = W)
            self.a_rb2.grid(column = 2, row = 11, sticky = W) 
            self.a_rb3.grid(column = 3, row = 11, sticky = W)
            self.a_rb4.grid(column = 4, row = 11, sticky = W)
            self.a_rb5.grid(column = 5, row = 11, sticky = W)
            self.a_rb6.grid(column = 6, row = 11, sticky = W) 

            self.cm_label.grid(column = 0, row = 12, columnspan = 4, sticky = W)
            self.cm_rb1.grid(column = 1, row = 12, sticky = W)
            self.cm_rb2.grid(column = 2, row = 12, sticky = W) 
            self.cm_rb3.grid(column = 3, row = 12, sticky = W)
            self.cm_rb4.grid(column = 4, row = 12, sticky = W)
            self.cm_rb5.grid(column = 5, row = 12, sticky = W)
            self.cm_rb6.grid(column = 6, row = 12, sticky = W)

            self.c_label.grid(column = 0, row = 13, columnspan = 4, sticky = W)
            self.c_rb1.grid(column = 1, row = 13, sticky = W)
            self.c_rb2.grid(column = 2, row = 13, sticky = W) 
            self.c_rb3.grid(column = 3, row = 13, sticky = W)
            self.c_rb4.grid(column = 4, row = 13, sticky = W)
            self.c_rb5.grid(column = 5, row = 13, sticky = W)
            self.c_rb6.grid(column = 6, row = 13, sticky = W)
            
            #pack submit and quit buttons 
            self.Next_button.grid(column=2, row=15, sticky=W)
            self.Quit_button.grid(column=3, row=15, sticky=W)

            
            i+=1
            #Enter tinkter mainloop
            mainloop()
    def next(self):
        if i == 1:
            self.w.destroy()
            listTemp = [str(team8[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 2:
            self.w.destroy()
            listTemp = [str(team8[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 3:
            self.w.destroy()
            listTemp = [str(team8[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
            print ('Here is the evaluation for Team 8! \n', end='\n' "".join(map(str, listdata)))

    def quit(self):
        global i
        i+=3
        self.w.destroy()
        print("Just rated someone wrong? It's okay let's restart!")

class Team9GUI: 
    def __init__(self):
        global i
        while i < 3: 
            self.w = Tk()
            self.w.title('Welcome to the Team Evaluation form for Team 9')
            #create and position the frame 
            self.f = ttk.Frame(self.w, padding=(5, 5, 12, 0))
            self.f.grid(column=0, row=0, sticky=(N,W,E,S))
            self.w.grid_columnconfigure(0, weight=1)
            self.w.grid_rowconfigure(0,weight=1)

            #define all the widgets
            #creates an entry box for user to type their name 
            #creates associated label and a status label
            #creates an Enter button
            #creates a dropdown menu to select the team
            #creates a done button to exit the window

            self.lab3 = Label(self.f, text='Teammate:'+team9[i])
            self.lab_rating = Label(self.f, text="Please evaluate your team members according to the following criteria:\n 1 = Terrible, 2 = Bad, 3 = Average, 4 = Good, 5 = Outstanding \n Choose N/A if the person displayed is you.")
            
            #Attendance Radio Buttons
            self.a_radio_var =IntVar()
            self.a_radio_var.set(1)
            self.a_label = Label(self.f, text='Attendance') 
            self.a_rb1 = Radiobutton(self.f, text='1', variable=self.a_radio_var, value=1)
            self.a_rb2 = Radiobutton(self.f, text='2', variable=self.a_radio_var, value=2)
            self.a_rb3 = Radiobutton(self.f, text='3', variable=self.a_radio_var, value=3)
            self.a_rb4 = Radiobutton(self.f, text='4', variable=self.a_radio_var, value=4)
            self.a_rb5 = Radiobutton(self.f, text='5', variable=self.a_radio_var, value=5)
            self.a_rb6 = Radiobutton(self.f, text='N/A', variable=self.a_radio_var, value=0)

            #Communication Radio Buttons
            self.cm_radio_var =IntVar()
            self.cm_radio_var.set(1)
            self.cm_label = Label(self.f, text='Communication') 
            self.cm_rb1 = Radiobutton(self.f, text='1', variable=self.cm_radio_var, value=1)
            self.cm_rb2 = Radiobutton(self.f, text='2', variable=self.cm_radio_var, value=2)
            self.cm_rb3 = Radiobutton(self.f, text='3', variable=self.cm_radio_var, value=3)
            self.cm_rb4 = Radiobutton(self.f, text='4', variable=self.cm_radio_var, value=4)
            self.cm_rb5 = Radiobutton(self.f, text='5', variable=self.cm_radio_var, value=5)
            self.cm_rb6 = Radiobutton(self.f, text='N/A', variable=self.cm_radio_var, value=0)

            #Contribution Radio Buttons
            self.c_radio_var =IntVar()
            self.c_radio_var.set(1)
            self.c_label = Label(self.f, text='Contribution') 
            self.c_rb1 = Radiobutton(self.f, text='1', variable=self.c_radio_var, value=1)
            self.c_rb2 = Radiobutton(self.f, text='2', variable=self.c_radio_var, value=2)
            self.c_rb3 = Radiobutton(self.f, text='3', variable=self.c_radio_var, value=3)
            self.c_rb4 = Radiobutton(self.f, text='4', variable=self.c_radio_var, value=4)
            self.c_rb5 = Radiobutton(self.f, text='5', variable=self.c_radio_var, value=5)
            self.c_rb6 = Radiobutton(self.f, text='N/A', variable=self.c_radio_var, value=0)

            #Next and Quit buttons 
            self.Next_button = Button(self.f, text="Next", command=self.next)
            self.Quit_button = Button(self.f, text="Quit", command=self.quit)

            #pack the widgets
            self.lab3.grid(column = 0, row = 6, rowspan = 2, sticky = W)
            self.lab_rating.grid(column = 1, row = 8, columnspan = 5, rowspan= 3, sticky = W)
            
            #pack radiobutton widgets 
            self.a_label.grid(column = 0, row = 11, columnspan = 3 , sticky = W)
            self.a_rb1.grid(column = 1, row = 11, sticky = W)
            self.a_rb2.grid(column = 2, row = 11, sticky = W) 
            self.a_rb3.grid(column = 3, row = 11, sticky = W)
            self.a_rb4.grid(column = 4, row = 11, sticky = W)
            self.a_rb5.grid(column = 5, row = 11, sticky = W)
            self.a_rb6.grid(column = 6, row = 11, sticky = W) 

            self.cm_label.grid(column = 0, row = 12, columnspan = 4, sticky = W)
            self.cm_rb1.grid(column = 1, row = 12, sticky = W)
            self.cm_rb2.grid(column = 2, row = 12, sticky = W) 
            self.cm_rb3.grid(column = 3, row = 12, sticky = W)
            self.cm_rb4.grid(column = 4, row = 12, sticky = W)
            self.cm_rb5.grid(column = 5, row = 12, sticky = W)
            self.cm_rb6.grid(column = 6, row = 12, sticky = W)

            self.c_label.grid(column = 0, row = 13, columnspan = 4, sticky = W)
            self.c_rb1.grid(column = 1, row = 13, sticky = W)
            self.c_rb2.grid(column = 2, row = 13, sticky = W) 
            self.c_rb3.grid(column = 3, row = 13, sticky = W)
            self.c_rb4.grid(column = 4, row = 13, sticky = W)
            self.c_rb5.grid(column = 5, row = 13, sticky = W)
            self.c_rb6.grid(column = 6, row = 13, sticky = W)
            
            #pack submit and quit buttons 
            self.Next_button.grid(column=2, row=15, sticky=W)
            self.Quit_button.grid(column=3, row=15, sticky=W)

            
            i+=1
            #Enter tinkter mainloop
            mainloop()
    def next(self):
        if i == 1:
            self.w.destroy()
            listTemp = [str(team9[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 2:
            self.w.destroy()
            listTemp = [str(team9[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 3:
            self.w.destroy()
            listTemp = [str(team9[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
            print ('Here is the evaluation for Team 9! \n', end='\n' "".join(map(str, listdata)))

    def quit(self):
        global i
        i+=3
        self.w.destroy()
        print("Just rated someone wrong? It's okay let's restart!")

class Team10GUI: 
    def __init__(self):
        global i
        while i < 3: 
            self.w = Tk()
            self.w.title('Welcome to the Team Evaluation form for Team 10')
            #create and position the frame 
            self.f = ttk.Frame(self.w, padding=(5, 5, 12, 0))
            self.f.grid(column=0, row=0, sticky=(N,W,E,S))
            self.w.grid_columnconfigure(0, weight=1)
            self.w.grid_rowconfigure(0,weight=1)

            #define all the widgets
            #creates an entry box for user to type their name 
            #creates associated label and a status label
            #creates an Enter button
            #creates a dropdown menu to select the team
            #creates a done button to exit the window

            self.lab3 = Label(self.f, text='Teammate:'+team10[i])
            self.lab_rating = Label(self.f, text="Please evaluate your team members according to the following criteria:\n 1 = Terrible, 2 = Bad, 3 = Average, 4 = Good, 5 = Outstanding \n Choose N/A if the person displayed is you.")
            
            #Attendance Radio Buttons
            self.a_radio_var =IntVar()
            self.a_radio_var.set(1)
            self.a_label = Label(self.f, text='Attendance') 
            self.a_rb1 = Radiobutton(self.f, text='1', variable=self.a_radio_var, value=1)
            self.a_rb2 = Radiobutton(self.f, text='2', variable=self.a_radio_var, value=2)
            self.a_rb3 = Radiobutton(self.f, text='3', variable=self.a_radio_var, value=3)
            self.a_rb4 = Radiobutton(self.f, text='4', variable=self.a_radio_var, value=4)
            self.a_rb5 = Radiobutton(self.f, text='5', variable=self.a_radio_var, value=5)
            self.a_rb6 = Radiobutton(self.f, text='N/A', variable=self.a_radio_var, value=0)

            #Communication Radio Buttons
            self.cm_radio_var =IntVar()
            self.cm_radio_var.set(1)
            self.cm_label = Label(self.f, text='Communication') 
            self.cm_rb1 = Radiobutton(self.f, text='1', variable=self.cm_radio_var, value=1)
            self.cm_rb2 = Radiobutton(self.f, text='2', variable=self.cm_radio_var, value=2)
            self.cm_rb3 = Radiobutton(self.f, text='3', variable=self.cm_radio_var, value=3)
            self.cm_rb4 = Radiobutton(self.f, text='4', variable=self.cm_radio_var, value=4)
            self.cm_rb5 = Radiobutton(self.f, text='5', variable=self.cm_radio_var, value=5)
            self.cm_rb6 = Radiobutton(self.f, text='N/A', variable=self.cm_radio_var, value=0)

            #Contribution Radio Buttons
            self.c_radio_var =IntVar()
            self.c_radio_var.set(1)
            self.c_label = Label(self.f, text='Contribution') 
            self.c_rb1 = Radiobutton(self.f, text='1', variable=self.c_radio_var, value=1)
            self.c_rb2 = Radiobutton(self.f, text='2', variable=self.c_radio_var, value=2)
            self.c_rb3 = Radiobutton(self.f, text='3', variable=self.c_radio_var, value=3)
            self.c_rb4 = Radiobutton(self.f, text='4', variable=self.c_radio_var, value=4)
            self.c_rb5 = Radiobutton(self.f, text='5', variable=self.c_radio_var, value=5)
            self.c_rb6 = Radiobutton(self.f, text='N/A', variable=self.c_radio_var, value=0)

            #Next and Quit buttons 
            self.Next_button = Button(self.f, text="Next", command=self.next)
            self.Quit_button = Button(self.f, text="Quit", command=self.quit)

            #pack the widgets
            self.lab3.grid(column = 0, row = 6, rowspan = 2, sticky = W)
            self.lab_rating.grid(column = 1, row = 8, columnspan = 5, rowspan= 3, sticky = W)
            
            #pack radiobutton widgets 
            self.a_label.grid(column = 0, row = 11, columnspan = 3 , sticky = W)
            self.a_rb1.grid(column = 1, row = 11, sticky = W)
            self.a_rb2.grid(column = 2, row = 11, sticky = W) 
            self.a_rb3.grid(column = 3, row = 11, sticky = W)
            self.a_rb4.grid(column = 4, row = 11, sticky = W)
            self.a_rb5.grid(column = 5, row = 11, sticky = W)
            self.a_rb6.grid(column = 6, row = 11, sticky = W) 

            self.cm_label.grid(column = 0, row = 12, columnspan = 4, sticky = W)
            self.cm_rb1.grid(column = 1, row = 12, sticky = W)
            self.cm_rb2.grid(column = 2, row = 12, sticky = W) 
            self.cm_rb3.grid(column = 3, row = 12, sticky = W)
            self.cm_rb4.grid(column = 4, row = 12, sticky = W)
            self.cm_rb5.grid(column = 5, row = 12, sticky = W)
            self.cm_rb6.grid(column = 6, row = 12, sticky = W)

            self.c_label.grid(column = 0, row = 13, columnspan = 4, sticky = W)
            self.c_rb1.grid(column = 1, row = 13, sticky = W)
            self.c_rb2.grid(column = 2, row = 13, sticky = W) 
            self.c_rb3.grid(column = 3, row = 13, sticky = W)
            self.c_rb4.grid(column = 4, row = 13, sticky = W)
            self.c_rb5.grid(column = 5, row = 13, sticky = W)
            self.c_rb6.grid(column = 6, row = 13, sticky = W)
            
            #pack submit and quit buttons 
            self.Next_button.grid(column=2, row=15, sticky=W)
            self.Quit_button.grid(column=3, row=15, sticky=W)

            
            i+=1
            #Enter tinkter mainloop
            mainloop()
    def next(self):
        if i == 1:
            self.w.destroy()
            listTemp = [str(team10[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 2:
            self.w.destroy()
            listTemp = [str(team10[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 3:
            self.w.destroy()
            listTemp = [str(team10[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
            print ('Here is the evaluation for Team 10! \n', end='\n' "".join(map(str, listdata)))

    def quit(self):
        global i
        i+=3
        self.w.destroy()
        print("Just rated someone wrong? It's okay let's restart!")

class Team11GUI: 
    def __init__(self):
        global i
        while i < 3: 
            self.w = Tk()
            self.w.title('Welcome to the Team Evaluation form for Team 11')
            #create and position the frame 
            self.f = ttk.Frame(self.w, padding=(5, 5, 12, 0))
            self.f.grid(column=0, row=0, sticky=(N,W,E,S))
            self.w.grid_columnconfigure(0, weight=1)
            self.w.grid_rowconfigure(0,weight=1)

            #define all the widgets
            #creates an entry box for user to type their name 
            #creates associated label and a status label
            #creates an Enter button
            #creates a dropdown menu to select the team
            #creates a done button to exit the window

            self.lab3 = Label(self.f, text='Teammate:'+team11[i])
            self.lab_rating = Label(self.f, text="Please evaluate your team members according to the following criteria:\n 1 = Terrible, 2 = Bad, 3 = Average, 4 = Good, 5 = Outstanding \n Choose N/A if the person displayed is you.")
            
            #Attendance Radio Buttons
            self.a_radio_var =IntVar()
            self.a_radio_var.set(1)
            self.a_label = Label(self.f, text='Attendance') 
            self.a_rb1 = Radiobutton(self.f, text='1', variable=self.a_radio_var, value=1)
            self.a_rb2 = Radiobutton(self.f, text='2', variable=self.a_radio_var, value=2)
            self.a_rb3 = Radiobutton(self.f, text='3', variable=self.a_radio_var, value=3)
            self.a_rb4 = Radiobutton(self.f, text='4', variable=self.a_radio_var, value=4)
            self.a_rb5 = Radiobutton(self.f, text='5', variable=self.a_radio_var, value=5)
            self.a_rb6 = Radiobutton(self.f, text='N/A', variable=self.a_radio_var, value=0)

            #Communication Radio Buttons
            self.cm_radio_var =IntVar()
            self.cm_radio_var.set(1)
            self.cm_label = Label(self.f, text='Communication') 
            self.cm_rb1 = Radiobutton(self.f, text='1', variable=self.cm_radio_var, value=1)
            self.cm_rb2 = Radiobutton(self.f, text='2', variable=self.cm_radio_var, value=2)
            self.cm_rb3 = Radiobutton(self.f, text='3', variable=self.cm_radio_var, value=3)
            self.cm_rb4 = Radiobutton(self.f, text='4', variable=self.cm_radio_var, value=4)
            self.cm_rb5 = Radiobutton(self.f, text='5', variable=self.cm_radio_var, value=5)
            self.cm_rb6 = Radiobutton(self.f, text='N/A', variable=self.cm_radio_var, value=0)

            #Contribution Radio Buttons
            self.c_radio_var =IntVar()
            self.c_radio_var.set(1)
            self.c_label = Label(self.f, text='Contribution') 
            self.c_rb1 = Radiobutton(self.f, text='1', variable=self.c_radio_var, value=1)
            self.c_rb2 = Radiobutton(self.f, text='2', variable=self.c_radio_var, value=2)
            self.c_rb3 = Radiobutton(self.f, text='3', variable=self.c_radio_var, value=3)
            self.c_rb4 = Radiobutton(self.f, text='4', variable=self.c_radio_var, value=4)
            self.c_rb5 = Radiobutton(self.f, text='5', variable=self.c_radio_var, value=5)
            self.c_rb6 = Radiobutton(self.f, text='N/A', variable=self.c_radio_var, value=0)

            #Next and Quit buttons 
            self.Next_button = Button(self.f, text="Next", command=self.next)
            self.Quit_button = Button(self.f, text="Quit", command=self.quit)

            #pack the widgets
            self.lab3.grid(column = 0, row = 6, rowspan = 2, sticky = W)
            self.lab_rating.grid(column = 1, row = 8, columnspan = 5, rowspan= 3, sticky = W)
            
            #pack radiobutton widgets 
            self.a_label.grid(column = 0, row = 11, columnspan = 3 , sticky = W)
            self.a_rb1.grid(column = 1, row = 11, sticky = W)
            self.a_rb2.grid(column = 2, row = 11, sticky = W) 
            self.a_rb3.grid(column = 3, row = 11, sticky = W)
            self.a_rb4.grid(column = 4, row = 11, sticky = W)
            self.a_rb5.grid(column = 5, row = 11, sticky = W)
            self.a_rb6.grid(column = 6, row = 11, sticky = W) 

            self.cm_label.grid(column = 0, row = 12, columnspan = 4, sticky = W)
            self.cm_rb1.grid(column = 1, row = 12, sticky = W)
            self.cm_rb2.grid(column = 2, row = 12, sticky = W) 
            self.cm_rb3.grid(column = 3, row = 12, sticky = W)
            self.cm_rb4.grid(column = 4, row = 12, sticky = W)
            self.cm_rb5.grid(column = 5, row = 12, sticky = W)
            self.cm_rb6.grid(column = 6, row = 12, sticky = W)

            self.c_label.grid(column = 0, row = 13, columnspan = 4, sticky = W)
            self.c_rb1.grid(column = 1, row = 13, sticky = W)
            self.c_rb2.grid(column = 2, row = 13, sticky = W) 
            self.c_rb3.grid(column = 3, row = 13, sticky = W)
            self.c_rb4.grid(column = 4, row = 13, sticky = W)
            self.c_rb5.grid(column = 5, row = 13, sticky = W)
            self.c_rb6.grid(column = 6, row = 13, sticky = W)
            
            #pack submit and quit buttons 
            self.Next_button.grid(column=2, row=15, sticky=W)
            self.Quit_button.grid(column=3, row=15, sticky=W)

            
            i+=1
            #Enter tinkter mainloop
            mainloop()
    def next(self):
        if i == 1:
            self.w.destroy()
            listTemp = [str(team11[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 2:
            self.w.destroy()
            listTemp = [str(team11[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
        elif i == 3:
            self.w.destroy()
            listTemp = [str(team11[i-1])+ ': Attendance: '+str(self.a_radio_var.get())+ '; Contribution: '+str(self.c_radio_var.get())+'; Communication: '+str(self.cm_radio_var.get())]
            listdata.append(listTemp)
            print ('Here is the evaluation for Team 11! \n', end='\n' "".join(map(str, listdata)))

    def quit(self):
        global i
        i+=3
        self.w.destroy()
        print("Just rated someone wrong? It's okay let's restart!")

x = TeamsGUI()

