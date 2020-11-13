from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
import datetime
#from datetime import datetime
import calendar

#ttk stands for themed tk

def convert24(str1):  #code from geeksforgeeks
    # Checking if last two elements of time 
    # is AM and first two elements are 12 
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return "00" + str1[2:-2] 
          
    # remove the AM     
    elif str1[-2:] == "AM": 
        return str1[:-2] 
      
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2] 
          
    else: 
        # add 12 to hours and remove PM 
        return str(int(str1[:2]) + 12) + str1[2:8] 
    
font_stye1 = ("Courier", 10)
font_stye2 = ("Courier", 13)

k1 = 0.2
k2 = 0.2
k3 = 0.2
k4 = 1

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title("Team Bits")
        self.minsize(1200, 800)
        self.create_heading()
        self.create_mainpagelabels()
        self.create_mainpageentry()
        self.save_mainpageentry()
        
        

    def create_heading(self):
        self.heading = Label(self, text = "Welcome to Scheduler",background='#101010',
                            foreground="#D6D6D6")
        self.heading.config(font=("Courier", 20))
        self.heading.grid(column = 0, row = 0)
        
    def create_mainpagelabels(self):
        self.tasknamelabel = tk.Label(self, text = "Enter the Course Name:",anchor=W)
        self.tasknamelabel.config(font= font_stye1)
        self.tasknamelabel.grid(column = 0, row = 1, sticky = W)
        
        self.tasksummarylabel = tk.Label(self, text = "Task Enter Task Summary:",anchor=W)
        self.tasksummarylabel.config(font= font_stye1)
        self.tasksummarylabel.grid(column = 0, row = 2, sticky = W)
        
        self.endtimelabel = tk.Label(self, text = "Select Due Time:",anchor=W)
        self.endtimelabel.config(font= font_stye1)
        self.endtimelabel.grid(column = 0, row = 4, sticky = W)
        
        self.daylabel = tk.Label(self, text = "Select the Duedate:",anchor=W)
        self.daylabel.config(font= font_stye1)
        self.daylabel.grid(column = 0, row = 5, sticky = W)

        self.difficulty  = tk.Label(self, text = "Select the Difficulty:",anchor=W)
        self.difficulty.config(font=font_stye1)
        self.difficulty.grid(column = 0, row = 6, sticky = W)
        
        self.weightagelabel  = tk.Label(self, text = "Enter the Weightage % Towards the Final Grade:",anchor=W)
        self.weightagelabel.config(font=font_stye1)
        self.weightagelabel.grid(column = 0, row = 7, sticky = W)
        
        self.percentagelabel = tk.Label(self, text = "%",anchor=W)
        self.percentagelabel.config(font=font_stye1)
        self.percentagelabel.grid(column = 5, row = 7, sticky = W)
        
        self.preparationlabel  = tk.Label(self, text = "How Much Prepared Are You For This Task?:",anchor=W)
        self.preparationlabel.config(font=font_stye1)
        self.preparationlabel.grid(column = 0, row = 8, sticky = W)
    
    def create_mainpageentry(self):
        #Create entry box to write the course name
        self.taskentry= tk.StringVar()
        self.textbox = ttk.Entry(self, width  = 20, textvariable = self.taskentry)
        self.textbox.focus()
        self.textbox.grid(column=1, row=1,columnspan = 4)
        
        self.tasksummary= tk.StringVar()
        self.summarytextbox = ttk.Entry(self, width  = 20, textvariable = self.tasksummary)
        self.summarytextbox.focus()
        self.summarytextbox.grid(column=1, row=2,columnspan = 4)

        #Create dropdown menu to select the end time
        self.clicked_endhours = tk.StringVar()
        self.clicked_endhours.set('12')
        self.drop_endhours = ttk.OptionMenu(self, self.clicked_endhours,'01','01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12')
        self.drop_endhours.grid(column = 1, row = 4, sticky = W)
        
        self.colon_endtime = Label(self, text = ":",anchor=W)
        self.colon_endtime.config(font=font_stye1)
        self.colon_endtime.grid(column = 2, row = 4)
        
        self.clicked_endmin = tk.StringVar()
        self.clicked_endmin.set('00')
        self.drop_endmin = ttk.OptionMenu(self, self.clicked_endmin,'00','00', '05', '10', '15' ,'20', '25', '30', '35', '40', '45', '50', '55')
        self.drop_endmin.grid(column = 3, row = 4, sticky = W)
        
        self.clicked_ampm_endtime = tk.StringVar()
        self.clicked_ampm_endtime.set('AM')
        self.drop_ampm_endtime = ttk.OptionMenu(self, self.clicked_ampm_endtime,'AM','AM', 'PM')
        self.drop_ampm_endtime.grid(column = 4, row = 4, sticky = W)
        
        #Create dropdown to select the date and day
        self.cal = Calendar(self, selectmode = 'day', year = 2020, month = 11, day = 1,date_pattern='mm/dd/y')
        self.cal.grid(column = 1, row = 5, sticky = W, columnspan = 5)
        
        #Create dropdown for difficulty level (3 most difficult, 2 moderate, 1 easy)
        self.clicked_difficulty = tk.StringVar()
        self.clicked_difficulty.set('easy')
        self.clicked_difficulty = ttk.OptionMenu(self, self.clicked_difficulty,'easy','easy', 'moderate', 'difficult')
        self.clicked_difficulty.grid(column = 1, row = 6, sticky = E, columnspan = 5)
        
        #entry box for weightage
        self.weightage= tk.StringVar()
        self.weightagebox = ttk.Entry(self, width  = 20, textvariable = self.weightage)
        self.weightagebox.focus()
        self.weightagebox.grid(column=1, row=7,columnspan = 4)
        
        #Create dropdown for difficulty level (3 fully prepared, 2 some what prepared, 1 not prepared)
        self.clicked_difficulty = tk.StringVar()
        self.clicked_difficulty.set('fully prepared')
        self.clicked_difficulty = ttk.OptionMenu(self, self.clicked_difficulty,'fully prepared','fully prepared', 'some what prepared', 'not prepared')
        self.clicked_difficulty.grid(column = 1, row = 8, sticky = E, columnspan = 5)
        

    def save_mainpageentry(self):
        def add_summary():
            #To do: clear last printed result
            
            
            #get task name
            self.taskname = self.taskentry.get()
            
            #get task description
            self.taskdescription = self.tasksummary.get()
            
            #get due time 
                #self.startingtime = str(self.clicked_starthours.get() + ":" + self.clicked_startmin.get() + ":00 " + self.clicked_ampm_starttime.get())
            self.endtime = str(self.clicked_endhours.get() + ":" + self.clicked_endmin.get() + ":00 " + self.clicked_ampm_endtime.get())
            
            #convert to 24 hour time for ease of calculation
            self.converted_endtime = convert24(self.endtime)
            self.converted_endhour, self.converted_endmin, self.converted_endsec = self.converted_endtime.split(":")
            
            #get due date
            self.taskdate = str(self.cal.get_date())
            self.month, self.day, self.year= self.taskdate.split("/")
            self.date_formatted = str (self.day + " " + self.month+ " " + self.year)
            
            #get weightage
            self.taskweightage = self.weightage.get()
            try:
                int(self.taskweightage)
            except ValueError:
                try:
                    float(self.taskweightage)
                except ValueError:
                    tk.messagebox.showinfo("Warning","Please enter the task weightage")
                    self.weightagebox.delete(0,'end')
                    
            
            
            #get today's date
            self.b = datetime.datetime.now()
            #self.nowhour,self.nowmin, self.now
            
            #time difference in minutes datetime(year, month, day, hour, minute, second)
            self.a = datetime.datetime(int(self.year), int(self.month), int(self.day), int(self.converted_endhour), int(self.converted_endmin), int(self.converted_endsec))
            #self.b = datetime.datetime(int(self.year), int(self.month), int(self.day), int(self.converted_starthour), int(self.converted_startmin), int(self.converted_startsec))

            self.tdelta = (self.a - self.b).total_seconds()/3600
            
            #get day name
            self.day_name = calendar.day_name[datetime.datetime.strptime(self.date_formatted,'%d %m %Y').weekday()]

            #calculate the time required to study
            self.diff_D = (self.clicked_endhours.get())
            if self.diff_D == 'easy':
                self.diff_D = 1;
            if self.diff_D == 'moderate':
                self.diff_D = 2;
            if self.diff_D == 'difficult':
                self.diff_D = 3;
            
            self.prep_P = (self.clicked_endhours.get())
            if self.prep_P == 'not prepared':
                self.prep_P = 1;
            if self.prep_P == 'some what prepared':
                self.prep_P = 2;
            if self.prep_P == 'fully prepared':
                self.prep_P = 3;
            
            
            
            if (self.taskname == "") or (self.taskdescription == ""):
                tk.messagebox.showinfo("Warning","Please enter the task information")
            elif(self.tdelta)<0:
                tk.messagebox.showwarning("Warning","Please select correct end date")
            elif (self.weightage == ""):
                tk.messagebox.showinfo("Warning","Please enter the task weightage")
            else:
                #calculate the required time 
                self.requiredTime = (k1/int(self.tdelta)) + (k2*int(self.diff_D)) + (k3*int(self.taskweightage)) + (k4/int(self.prep_P))
                
                #print summary
                self.summary  = Label(self, text = "Summary:",anchor=W)
                self.summary.config(font=font_stye2)
                self.summary.grid(column = 0, row = 10, sticky = W)
                
                self.tasksummaryshow  = Label(self, text = "Task : " + str (self.taskname) + ", " + str (self.taskdescription),anchor=W)
                self.tasksummaryshow.config(font=font_stye1)
                self.tasksummaryshow.grid(column = 0, row = 11, sticky = W)
                
                self.duesummary  = Label(self, text = "Task Due Date: " + str(self.day_name)+ " "+ str(self.taskdate),anchor=W)
                self.duesummary.config(font=font_stye1)
                self.duesummary.grid(column = 0, row = 12, sticky = W)
                
                self.requrired_studytime  = Label(self, text = "Required Study Time : "+ str(round(int(self.requiredTime))) + " hours" ,anchor=W)
                self.requrired_studytime.config(font=font_stye1)
                self.requrired_studytime.grid(column = 0, row = 13, sticky = W)
                        
                #reset entries
                self.textbox.delete(0, 'end')
                self.summarytextbox.delete(0, 'end')
                self.weightagebox.delete(0,'end')

        
        self.save_task = ttk.Button(self, text = 'Generate Summary', command = add_summary)
        self.save_task.grid (column = 0, row = 9, sticky = W)

root = Root()
root.mainloop()