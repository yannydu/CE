
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
    
    

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title("Geekscoders.com - Tkinter Label")
        self.minsize(1200, 1600)
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
        self.tasknamelabel = Label(self, text = "Enter the Task:",anchor=W)
        self.tasknamelabel.config(font=("Courier", 12))
        self.tasknamelabel.grid(column = 0, row = 1, sticky = W)
        
        self.starttimelabel = Label(self, text = "Select Start Time:",anchor=W)
        self.starttimelabel.config(font=("Courier", 12))
        self.starttimelabel.grid(column = 0, row = 2, sticky = W)
        
        self.endtimelabel = Label(self, text = "Select End Time:",anchor=W)
        self.endtimelabel.config(font=("Courier", 12))
        self.endtimelabel.grid(column = 0, row = 3, sticky = W)
        
        self.daylabel = Label(self, text = "Select the Day:",anchor=W)
        self.daylabel.config(font=("Courier", 12))
        self.daylabel.grid(column = 0, row = 4, sticky = W)
    
    def create_mainpageentry(self):
        #Create entry box to write the course name
        self.taskentry= tk.StringVar()
        self.textbox = ttk.Entry(self, width  = 20, textvariable = self.taskentry)
        self.textbox.focus()
        self.textbox.grid(column=1, row=1,columnspan = 4)
        
        #Create dropdown menu to select the starting time
        self.clicked_starthours = tk.StringVar()
        self.clicked_starthours.set('12')
        self.drop_starthours = ttk.OptionMenu(self, self.clicked_starthours,'01','01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12')
        self.drop_starthours.grid(column = 1, row = 2, sticky = W)
        
        self.colon_starttime = Label(self, text = ":",anchor=W)
        self.colon_starttime.config(font=("Courier", 12))
        self.colon_starttime.grid(column = 2, row = 2)
        
        self.clicked_startmin = tk.StringVar()
        self.clicked_startmin.set('00')
        self.drop_startmin = ttk.OptionMenu(self, self.clicked_startmin,'00','00', '05', '10', '15' ,'20', '25', '30', '35', '40', '45', '50', '55')
        self.drop_startmin.grid(column = 3, row = 2, sticky = W)
        
        self.clicked_ampm_starttime = tk.StringVar()
        self.clicked_ampm_starttime.set('AM')
        self.drop_ampm_starttime = ttk.OptionMenu(self, self.clicked_ampm_starttime,'AM','AM', 'PM')
        self.drop_ampm_starttime.grid(column = 4, row = 2, sticky = W)
        
        
        #Create dropdown menu to select the end time
        self.clicked_endhours = tk.StringVar()
        self.clicked_endhours.set('12')
        self.drop_endhours = ttk.OptionMenu(self, self.clicked_endhours,'01','01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12')
        self.drop_endhours.grid(column = 1, row = 3, sticky = W)
        
        self.colon_endtime = Label(self, text = ":",anchor=W)
        self.colon_endtime.config(font=("Courier", 12))
        self.colon_endtime.grid(column = 2, row = 3)
        
        self.clicked_endmin = tk.StringVar()
        self.clicked_endmin.set('00')
        self.drop_endmin = ttk.OptionMenu(self, self.clicked_endmin,'00','00', '05', '10', '15' ,'20', '25', '30', '35', '40', '45', '50', '55')
        self.drop_endmin.grid(column = 3, row = 3, sticky = W)
        
        self.clicked_ampm_endtime = tk.StringVar()
        self.clicked_ampm_endtime.set('AM')
        self.drop_ampm_endtime = ttk.OptionMenu(self, self.clicked_ampm_endtime,'AM','AM', 'PM')
        self.drop_ampm_endtime.grid(column = 4, row = 3, sticky = W)
        
        #Create dropdown to select the date and day
        self.cal = Calendar(self, selectmode = 'day', year = 2020, month = 10, date_pattern='mm/dd/y')
        self.cal.grid(column = 1, row = 4, sticky = W, columnspan = 5)
        
        
        #Create dropdown to select the day
        #self.clicked_day = tk.StringVar()
        #self.clicked_day.set('Monday')
        #self.drop_day = ttk.OptionMenu(self, self.clicked_day,'Monday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday')
        #self.drop_day.grid(column = 1, row = 4, sticky = W)

    def save_mainpageentry(self):
        def add_schedule():
            self.taskname = self.taskentry.get()
            self.startingtime = str(self.clicked_starthours.get() + ":" + self.clicked_startmin.get() + ":00 " + self.clicked_ampm_starttime.get())
            self.endtime = str(self.clicked_endhours.get() + ":" + self.clicked_endmin.get() + ":00 " + self.clicked_ampm_endtime.get())
            
            #convert to 24 hour time for ease of calculation
            self.converted_startingtime = convert24(self.startingtime)
            self.converted_endtime = convert24(self.endtime)
            self.converted_starthour, self.converted_startmin, self.converted_startsec = self.converted_startingtime.split(":")
            self.converted_endhour, self.converted_endmin, self.converted_endsec = self.converted_endtime.split(":")
            

            
            
            self.taskdate = str(self.cal.get_date())
            self.month, self.day, self.year= self.taskdate.split("/")
            self.date_formatted = str (self.day + " " + self.month+ " " + self.year)
            
            
            #time difference in minutes datetime(year, month, day, hour, minute, second)
            self.a = datetime.datetime(int(self.year), int(self.month), int(self.day), int(self.converted_endhour), int(self.converted_endmin), int(self.converted_startsec))
            self.b = datetime.datetime(int(self.year), int(self.month), int(self.day), int(self.converted_starthour), int(self.converted_startmin), int(self.converted_startsec))

            self.tdelta = (self.a - self.b).total_seconds()/60
            
            self.day_name = calendar.day_name[datetime.datetime.strptime(self.date_formatted,'%d %m %Y').weekday()]
            
            if (self.day_name) == 'Monday' :
                self.day_name = 1
            elif (self.day_name) == 'Tuesday' :
                self.day_name = 2 
            elif (self.day_name) == 'Wednesday' :
                self.day_name = 3 
            elif (self.day_name) == 'Thursday' :
                self.day_name = 4
            elif (self.day_name) == 'Friday' :
                self.day_name = 5 
            elif (self.day_name) == 'Saturday' :
                self.day_name = 6
            elif (self.day_name) == 'Sunday' :
                self.day_name = 7 
            #self.taskday = str(self.cal.getday())
            
            if (self.taskname) == "":
                tk.messagebox.showinfo("Warning","Please enter the task name")
            else:
                #data need to create the schedule 
                #day_name|Starting Hour(24 hour clock)|Starting Min (24 hour clock)| Duration (min)| Task name
                print (self.day_name)
                print (self.converted_starthour)
                print(self.converted_startmin)
                print (self.tdelta)
                print (self.taskname)

        
        self.save_task = ttk.Button(self, text = 'Add to Schedule', command = add_schedule)
        self.save_task.grid (column = 0, row = 5, sticky = W)


root = Root()
root.mainloop()