from tkinter import *
from tkinter import ttk
from tkcalendar import *
from Task import *
import calendar
import math
#from datetime import datetime
import datetime
import tkinter as tk
#ttk stands for themed tk


from Google import Create_Service, add_event, delete_events, schedule_events

# GOOGLE API
CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']
    
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)



# List of task objects and user days user can work
#global task_List
task_List = []

#global workTimeList 
workTimeList = [[0,1] for _ in range(7)]

# Check if tasks have been scheduled to calendar
check_added = False

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

k2 = 0.21
k3 = 0.5
k4 = 6

i = 2 #gap between Select Avalilabity and add Task

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title("Team Bits")
        self.minsize(1000, 1600)
        self.create_heading()
        self.create_mainpagelabels()
        self.create_mainpageentry()
        self.save_mainpageentry()
        self.create_availabletimelabels()
        self.create_availabletimepageentry()
        self.save_availability()
        self.reset_time()
        
        

    def create_heading(self):
        self.heading = Label(self, text = "Welcome to Scheduler",background='#101010',
                            foreground="#D6D6D6")
        self.heading.config(font=("Courier", 20))
        self.heading.grid(column = 0, row = 0)
        
    def create_availabletimelabels(self):
        #Label asking user to enter availablity
        self.availibitylabel = tk.Label(self, text = "Select Availability",anchor=W)
        self.availibitylabel.config(font= font_stye2)
        self.availibitylabel.grid(column = 0, row = 1, sticky = W)

        #Label asking user to enter available time
        self.availibitylabel = tk.Label(self, text = "Monday:",anchor=W)
        self.availibitylabel.config(font= font_stye1)
        self.availibitylabel.grid(column = 0, row = 2, sticky = W)

        self.availibitylabel = tk.Label(self, text = "Tuesday",anchor=W)
        self.availibitylabel.config(font= font_stye1)
        self.availibitylabel.grid(column = 0, row = 3, sticky = W)

        self.availibitylabel = tk.Label(self, text = "Wednesday",anchor=W)
        self.availibitylabel.config(font= font_stye1)
        self.availibitylabel.grid(column = 0, row = 4, sticky = W)
        
        self.availibitylabel = tk.Label(self, text = "Thursday",anchor=W)
        self.availibitylabel.config(font= font_stye1)
        self.availibitylabel.grid(column = 0, row = 5, sticky = W)
        
        self.availibitylabel = tk.Label(self, text = "Friday",anchor=W)
        self.availibitylabel.config(font= font_stye1)
        self.availibitylabel.grid(column = 0, row = 6, sticky = W)
        
        self.availibitylabel = tk.Label(self, text = "Saturday",anchor=W)
        self.availibitylabel.config(font= font_stye1)
        self.availibitylabel.grid(column = 0, row = 7, sticky = W)
        
        self.availibitylabel = tk.Label(self, text = "Sunday",anchor=W)
        self.availibitylabel.config(font= font_stye1)
        self.availibitylabel.grid(column = 0, row = 8, sticky = W)


    def create_availabletimepageentry(self):
        
#=================#Create dropdown menu to select time MONDAY
        self.clicked_startfreehoursMONDAY = tk.StringVar()
        self.clicked_startfreehoursMONDAY.set('12')
        self.drop_startfreehoursMONDAY = ttk.OptionMenu(self, self.clicked_startfreehoursMONDAY,'01','01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12')
        self.drop_startfreehoursMONDAY.grid(column = 1, row = 2, sticky = W)
        
        self.colon_startfreetimeMONDAY = Label(self, text = ":",anchor=W)
        self.colon_startfreetimeMONDAY.config(font=font_stye1)
        self.colon_startfreetimeMONDAY.grid(column = 2, row = 2)
        
        self.clicked_freestartminMONDAY = tk.StringVar()
        self.clicked_freestartminMONDAY.set('00')
        self.drop_freestartminMONDAY = ttk.OptionMenu(self, self.clicked_freestartminMONDAY,'00','00', '05', '10', '15' ,'20', '25', '30', '35', '40', '45', '50', '55')
        self.drop_freestartminMONDAY.grid(column = 3, row = 2, sticky = W)
        
        self.clicked_ampm_startfreetimeMONDAY = tk.StringVar()
        self.clicked_ampm_startfreetimeMONDAY.set('AM')
        self.drop_ampm_startfreetimeMONDAY = ttk.OptionMenu(self, self.clicked_ampm_startfreetimeMONDAY,'AM','AM', 'PM')
        self.drop_ampm_startfreetimeMONDAY.grid(column = 4, row = 2, sticky = W)

        self.colon_startfreetimeMONDAY = Label(self, text = " to ",anchor=W)
        self.colon_startfreetimeMONDAY.config(font=font_stye1)
        self.colon_startfreetimeMONDAY.grid(column = 5, row = 2)
        
        #Create dropdown menu to select the stating free time
        self.clicked_endfreehoursMONDAY = tk.StringVar()
        self.clicked_endfreehoursMONDAY.set('12')
        self.drop_endfreehoursMONDAY = ttk.OptionMenu(self, self.clicked_endfreehoursMONDAY,'01','01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12')
        self.drop_endfreehoursMONDAY.grid(column = 6, row = 2, sticky = W)
        
        self.colon_endfreetimeMONDAY = Label(self, text = ":",anchor=W)
        self.colon_endfreetimeMONDAY.config(font=font_stye1)
        self.colon_endfreetimeMONDAY.grid(column = 7, row = 2)
        
        self.clicked_endstartminMONDAY = tk.StringVar()
        self.clicked_endstartminMONDAY.set('00')
        self.drop_endstartminMONDAY = ttk.OptionMenu(self, self.clicked_endstartminMONDAY,'00','00', '05', '10', '15' ,'20', '25', '30', '35', '40', '45', '50', '55')
        self.drop_endstartminMONDAY.grid(column = 8, row = 2, sticky = W)
        
        self.clicked_ampm_endfreetimeMONDAY = tk.StringVar()
        self.clicked_ampm_endfreetimeMONDAY.set('AM')
        self.drop_ampm_endfreetimeMONDAY = ttk.OptionMenu(self, self.clicked_ampm_endfreetimeMONDAY,'AM','AM', 'PM')
        self.drop_ampm_endfreetimeMONDAY.grid(column = 9, row = 2, sticky = W)
        
#=================#Create dropdown menu to select time TUESDAY
        self.clicked_startfreehoursTUESDAY = tk.StringVar()
        self.clicked_startfreehoursTUESDAY.set('12')
        self.drop_startfreehoursTUESDAY = ttk.OptionMenu(self, self.clicked_startfreehoursTUESDAY,'01','01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12')
        self.drop_startfreehoursTUESDAY.grid(column = 1, row = 3, sticky = W)
        
        self.colon_startfreetimeTUESDAY = Label(self, text = ":",anchor=W)
        self.colon_startfreetimeTUESDAY.config(font=font_stye1)
        self.colon_startfreetimeTUESDAY.grid(column = 2, row = 3)
        
        self.clicked_freestartminTUESDAY = tk.StringVar()
        self.clicked_freestartminTUESDAY.set('00')
        self.drop_freestartminTUESDAY = ttk.OptionMenu(self, self.clicked_freestartminTUESDAY,'00','00', '05', '10', '15' ,'20', '25', '30', '35', '40', '45', '50', '55')
        self.drop_freestartminTUESDAY.grid(column = 3, row = 3, sticky = W)
        
        self.clicked_ampm_startfreetimeTUESDAY = tk.StringVar()
        self.clicked_ampm_startfreetimeTUESDAY.set('AM')
        self.drop_ampm_startfreetimeTUESDAY = ttk.OptionMenu(self, self.clicked_ampm_startfreetimeTUESDAY,'AM','AM', 'PM')
        self.drop_ampm_startfreetimeTUESDAY.grid(column = 4, row = 3, sticky = W)

        self.colon_startfreetimeTUESDAY = Label(self, text = " to ",anchor=W)
        self.colon_startfreetimeTUESDAY.config(font=font_stye1)
        self.colon_startfreetimeTUESDAY.grid(column = 5, row = 3)
        
        #Create dropdown menu to select the stating free time
        self.clicked_endfreehoursTUESDAY = tk.StringVar()
        self.clicked_endfreehoursTUESDAY.set('12')
        self.drop_endfreehoursTUESDAY = ttk.OptionMenu(self, self.clicked_endfreehoursTUESDAY,'01','01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12')
        self.drop_endfreehoursTUESDAY.grid(column = 6, row = 3, sticky = W)
        
        self.colon_endfreetimeTUESDAY = Label(self, text = ":",anchor=W)
        self.colon_endfreetimeTUESDAY.config(font=font_stye1)
        self.colon_endfreetimeTUESDAY.grid(column = 7, row = 3)
        
        self.clicked_endstartminTUESDAY = tk.StringVar()
        self.clicked_endstartminTUESDAY.set('00')
        self.drop_endstartminTUESDAY = ttk.OptionMenu(self, self.clicked_endstartminTUESDAY,'00','00', '05', '10', '15' ,'20', '25', '30', '35', '40', '45', '50', '55')
        self.drop_endstartminTUESDAY.grid(column = 8, row = 3, sticky = W)
        
        self.clicked_ampm_endfreetimeTUESDAY = tk.StringVar()
        self.clicked_ampm_endfreetimeTUESDAY.set('AM')
        self.drop_ampm_endfreetimeTUESDAY = ttk.OptionMenu(self, self.clicked_ampm_endfreetimeTUESDAY,'AM','AM', 'PM')
        self.drop_ampm_endfreetimeTUESDAY.grid(column = 9, row = 3, sticky = W)
        
#=================#Create dropdown menu to select time WEDNESDAY
        self.clicked_startfreehoursWEDNESDAY = tk.StringVar()
        self.clicked_startfreehoursWEDNESDAY.set('12')
        self.drop_startfreehoursWEDNESDAY = ttk.OptionMenu(self, self.clicked_startfreehoursWEDNESDAY,'01','01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12')
        self.drop_startfreehoursWEDNESDAY.grid(column = 1, row = 4, sticky = W)
        
        self.colon_startfreetimeWEDNESDAY = Label(self, text = ":",anchor=W)
        self.colon_startfreetimeWEDNESDAY.config(font=font_stye1)
        self.colon_startfreetimeWEDNESDAY.grid(column = 2, row = 4)
        
        self.clicked_freestartminWEDNESDAY = tk.StringVar()
        self.clicked_freestartminWEDNESDAY.set('00')
        self.drop_freestartminWEDNESDAY = ttk.OptionMenu(self, self.clicked_freestartminWEDNESDAY,'00','00', '05', '10', '15' ,'20', '25', '30', '35', '40', '45', '50', '55')
        self.drop_freestartminWEDNESDAY.grid(column = 3, row = 4, sticky = W)
        
        self.clicked_ampm_startfreetimeWEDNESDAY = tk.StringVar()
        self.clicked_ampm_startfreetimeWEDNESDAY.set('AM')
        self.drop_ampm_startfreetimeWEDNESDAY = ttk.OptionMenu(self, self.clicked_ampm_startfreetimeWEDNESDAY,'AM','AM', 'PM')
        self.drop_ampm_startfreetimeWEDNESDAY.grid(column = 4, row = 4, sticky = W)

        self.colon_startfreetimeWEDNESDAY = Label(self, text = " to ",anchor=W)
        self.colon_startfreetimeWEDNESDAY.config(font=font_stye1)
        self.colon_startfreetimeWEDNESDAY.grid(column = 5, row = 4)
        
        #Create dropdown menu to select the stating free time
        self.clicked_endfreehoursWEDNESDAY = tk.StringVar()
        self.clicked_endfreehoursWEDNESDAY.set('12')
        self.drop_endfreehoursWEDNESDAY = ttk.OptionMenu(self, self.clicked_endfreehoursWEDNESDAY,'01','01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12')
        self.drop_endfreehoursWEDNESDAY.grid(column = 6, row = 4, sticky = W)
        
        self.colon_endfreetimeWEDNESDAY= Label(self, text = ":",anchor=W)
        self.colon_endfreetimeWEDNESDAY.config(font=font_stye1)
        self.colon_endfreetimeWEDNESDAY.grid(column = 7, row = 4)
        
        self.clicked_endstartminWEDNESDAY = tk.StringVar()
        self.clicked_endstartminWEDNESDAY.set('00')
        self.drop_endstartminWEDNESDAY = ttk.OptionMenu(self, self.clicked_endstartminWEDNESDAY,'00','00', '05', '10', '15' ,'20', '25', '30', '35', '40', '45', '50', '55')
        self.drop_endstartminWEDNESDAY.grid(column = 8, row = 4, sticky = W)
        
        self.clicked_ampm_endfreetimeWEDNESDAY = tk.StringVar()
        self.clicked_ampm_endfreetimeWEDNESDAY.set('AM')
        self.drop_ampm_endfreetimeWEDNESDAY = ttk.OptionMenu(self, self.clicked_ampm_endfreetimeWEDNESDAY,'AM','AM', 'PM')
        self.drop_ampm_endfreetimeWEDNESDAY.grid(column = 9, row = 4, sticky = W)
        
#=================#Create dropdown menu to select time THURSDAY
        self.clicked_startfreehoursTHURSDAY = tk.StringVar()
        self.clicked_startfreehoursTHURSDAY.set('12')
        self.drop_startfreehoursTHURSDAY = ttk.OptionMenu(self, self.clicked_startfreehoursTHURSDAY,'01','01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12')
        self.drop_startfreehoursTHURSDAY.grid(column = 1, row = 5, sticky = W)
        
        self.colon_startfreetimeTHURSDAY = Label(self, text = ":",anchor=W)
        self.colon_startfreetimeTHURSDAY.config(font=font_stye1)
        self.colon_startfreetimeTHURSDAY.grid(column = 2, row = 5)
        
        self.clicked_freestartminTHURSDAY = tk.StringVar()
        self.clicked_freestartminTHURSDAY.set('00')
        self.drop_freestartminTHURSDAY = ttk.OptionMenu(self, self.clicked_freestartminTHURSDAY,'00','00', '05', '10', '15' ,'20', '25', '30', '35', '40', '45', '50', '55')
        self.drop_freestartminTHURSDAY.grid(column = 3, row = 5, sticky = W)
        
        self.clicked_ampm_startfreetimeTHURSDAY = tk.StringVar()
        self.clicked_ampm_startfreetimeTHURSDAY.set('AM')
        self.drop_ampm_startfreetimeTHURSDAY = ttk.OptionMenu(self, self.clicked_ampm_startfreetimeTHURSDAY,'AM','AM', 'PM')
        self.drop_ampm_startfreetimeTHURSDAY.grid(column = 4, row = 5, sticky = W)

        self.colon_startfreetimeTHURSDAY = Label(self, text = " to ",anchor=W)
        self.colon_startfreetimeTHURSDAY.config(font=font_stye1)
        self.colon_startfreetimeTHURSDAY.grid(column = 5, row = 5)
        
        #Create dropdown menu to select the stating free time
        self.clicked_endfreehoursTHURSDAY = tk.StringVar()
        self.clicked_endfreehoursTHURSDAY.set('12')
        self.drop_endfreehoursTHURSDAY = ttk.OptionMenu(self, self.clicked_endfreehoursTHURSDAY,'01','01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12')
        self.drop_endfreehoursTHURSDAY.grid(column = 6, row = 5, sticky = W)
        
        self.colon_endfreetimeTHURSDAY = Label(self, text = ":",anchor=W)
        self.colon_endfreetimeTHURSDAY.config(font=font_stye1)
        self.colon_endfreetimeTHURSDAY.grid(column = 7, row = 5)
        
        self.clicked_endstartminTHURSDAY = tk.StringVar()
        self.clicked_endstartminTHURSDAY.set('00')
        self.drop_endstartminTHURSDAY = ttk.OptionMenu(self, self.clicked_endstartminTHURSDAY,'00','00', '05', '10', '15' ,'20', '25', '30', '35', '40', '45', '50', '55')
        self.drop_endstartminTHURSDAY.grid(column = 8, row = 5, sticky = W)
        
        self.clicked_ampm_endfreetimeTHURSDAY = tk.StringVar()
        self.clicked_ampm_endfreetimeTHURSDAY.set('AM')
        self.drop_ampm_endfreetimeTHURSDAY = ttk.OptionMenu(self, self.clicked_ampm_endfreetimeTHURSDAY,'AM','AM', 'PM')
        self.drop_ampm_endfreetimeTHURSDAY.grid(column = 9, row = 5, sticky = W)
        
#=================#Create dropdown menu to select time FRIDAY
        self.clicked_startfreehoursFRIDAY = tk.StringVar()
        self.clicked_startfreehoursFRIDAY.set('12')
        self.drop_startfreehoursFRIDAY = ttk.OptionMenu(self, self.clicked_startfreehoursFRIDAY,'01','01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12')
        self.drop_startfreehoursFRIDAY.grid(column = 1, row = 6, sticky = W)
        
        self.colon_startfreetimeFRIDAY = Label(self, text = ":",anchor=W)
        self.colon_startfreetimeFRIDAY.config(font=font_stye1)
        self.colon_startfreetimeFRIDAY.grid(column = 2, row = 6)
        
        self.clicked_freestartminFRIDAY = tk.StringVar()
        self.clicked_freestartminFRIDAY.set('00')
        self.drop_freestartminFRIDAY = ttk.OptionMenu(self, self.clicked_freestartminFRIDAY,'00','00', '05', '10', '15' ,'20', '25', '30', '35', '40', '45', '50', '55')
        self.drop_freestartminFRIDAY.grid(column = 3, row = 6, sticky = W)
        
        self.clicked_ampm_startfreetimeFRIDAY = tk.StringVar()
        self.clicked_ampm_startfreetimeFRIDAY.set('AM')
        self.drop_ampm_startfreetimeFRIDAY = ttk.OptionMenu(self, self.clicked_ampm_startfreetimeFRIDAY,'AM','AM', 'PM')
        self.drop_ampm_startfreetimeFRIDAY.grid(column = 4, row = 6, sticky = W)

        self.colon_startfreetimeFRIDAY = Label(self, text = " to ",anchor=W)
        self.colon_startfreetimeFRIDAY.config(font=font_stye1)
        self.colon_startfreetimeFRIDAY.grid(column = 5, row = 6)
        
        #Create dropdown menu to select the stating free time
        self.clicked_endfreehoursFRIDAY = tk.StringVar()
        self.clicked_endfreehoursFRIDAY.set('12')
        self.drop_endfreehoursFRIDAY = ttk.OptionMenu(self, self.clicked_endfreehoursFRIDAY,'01','01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12')
        self.drop_endfreehoursFRIDAY.grid(column = 6, row = 6, sticky = W)
        
        self.colon_endfreetimeFRIDAY = Label(self, text = ":",anchor=W)
        self.colon_endfreetimeFRIDAY.config(font=font_stye1)
        self.colon_endfreetimeFRIDAY.grid(column = 7, row = 6)
        
        self.clicked_endstartminFRIDAY = tk.StringVar()
        self.clicked_endstartminFRIDAY.set('00')
        self.drop_endstartminFRIDAY = ttk.OptionMenu(self, self.clicked_endstartminFRIDAY,'00','00', '05', '10', '15' ,'20', '25', '30', '35', '40', '45', '50', '55')
        self.drop_endstartminFRIDAY.grid(column = 8, row = 6, sticky = W)
        
        self.clicked_ampm_endfreetimeFRIDAY = tk.StringVar()
        self.clicked_ampm_endfreetimeFRIDAY.set('AM')
        self.drop_ampm_endfreetimeFRIDAY = ttk.OptionMenu(self, self.clicked_ampm_endfreetimeFRIDAY,'AM','AM', 'PM')
        self.drop_ampm_endfreetimeFRIDAY.grid(column = 9, row = 6, sticky = W)
        
#=================#Create dropdown menu to select time SATURDAY
        self.clicked_startfreehoursSATURDAY = tk.StringVar()
        self.clicked_startfreehoursSATURDAY.set('12')
        self.drop_startfreehoursSATURDAY = ttk.OptionMenu(self, self.clicked_startfreehoursSATURDAY,'01','01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12')
        self.drop_startfreehoursSATURDAY.grid(column = 1, row = 7, sticky = W)
        
        self.colon_startfreetimeSATURDAY = Label(self, text = ":",anchor=W)
        self.colon_startfreetimeSATURDAY.config(font=font_stye1)
        self.colon_startfreetimeSATURDAY.grid(column = 2, row = 7)
        
        self.clicked_freestartminSATURDAY = tk.StringVar()
        self.clicked_freestartminSATURDAY.set('00')
        self.drop_freestartminSATURDAY = ttk.OptionMenu(self, self.clicked_freestartminSATURDAY,'00','00', '05', '10', '15' ,'20', '25', '30', '35', '40', '45', '50', '55')
        self.drop_freestartminSATURDAY.grid(column = 3, row = 7, sticky = W)
        
        self.clicked_ampm_startfreetimeSATURDAY = tk.StringVar()
        self.clicked_ampm_startfreetimeSATURDAY.set('AM')
        self.drop_ampm_startfreetimeSATURDAY = ttk.OptionMenu(self, self.clicked_ampm_startfreetimeSATURDAY,'AM','AM', 'PM')
        self.drop_ampm_startfreetimeSATURDAY.grid(column = 4, row = 7, sticky = W)

        self.colon_startfreetimeSATURDAY = Label(self, text = " to ",anchor=W)
        self.colon_startfreetimeSATURDAY.config(font=font_stye1)
        self.colon_startfreetimeSATURDAY.grid(column = 5, row = 7)
        
        #Create dropdown menu to select the stating free time
        self.clicked_endfreehoursSATURDAY = tk.StringVar()
        self.clicked_endfreehoursSATURDAY.set('12')
        self.drop_endfreehoursSATURDAY = ttk.OptionMenu(self, self.clicked_endfreehoursSATURDAY,'01','01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12')
        self.drop_endfreehoursSATURDAY.grid(column = 6, row = 7, sticky = W)
        
        self.colon_endfreetimeSATURDAY = Label(self, text = ":",anchor=W)
        self.colon_endfreetimeSATURDAY.config(font=font_stye1)
        self.colon_endfreetimeSATURDAY.grid(column = 7, row = 7)
        
        self.clicked_endstartminSATURDAY = tk.StringVar()
        self.clicked_endstartminSATURDAY.set('00')
        self.drop_endstartminSATURDAY = ttk.OptionMenu(self, self.clicked_endstartminSATURDAY,'00','00', '05', '10', '15' ,'20', '25', '30', '35', '40', '45', '50', '55')
        self.drop_endstartminSATURDAY.grid(column = 8, row = 7, sticky = W)
        
        self.clicked_ampm_endfreetimeSATURDAY = tk.StringVar()
        self.clicked_ampm_endfreetimeSATURDAY.set('AM')
        self.drop_ampm_endfreetimeSATURDAY = ttk.OptionMenu(self, self.clicked_ampm_endfreetimeSATURDAY,'AM','AM', 'PM')
        self.drop_ampm_endfreetimeSATURDAY.grid(column = 9, row = 7, sticky = W)
        
#=================#Create dropdown menu to select time SUNDAY
        self.clicked_startfreehoursSUNDAY = tk.StringVar()
        self.clicked_startfreehoursSUNDAY.set('12')
        self.drop_startfreehoursSUNDAY = ttk.OptionMenu(self, self.clicked_startfreehoursSUNDAY,'01','01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12')
        self.drop_startfreehoursSUNDAY.grid(column = 1, row = 8, sticky = W)
        
        self.colon_startfreetimeSUNDAY = Label(self, text = ":",anchor=W)
        self.colon_startfreetimeSUNDAY.config(font=font_stye1)
        self.colon_startfreetimeSUNDAY.grid(column = 2, row = 8)
        
        self.clicked_freestartminSUNDAY = tk.StringVar()
        self.clicked_freestartminSUNDAY.set('00')
        self.drop_freestartminSUNDAY = ttk.OptionMenu(self, self.clicked_freestartminSUNDAY,'00','00', '05', '10', '15' ,'20', '25', '30', '35', '40', '45', '50', '55')
        self.drop_freestartminSUNDAY.grid(column = 3, row = 8, sticky = W)
        
        self.clicked_ampm_startfreetimeSUNDAY = tk.StringVar()
        self.clicked_ampm_startfreetimeSUNDAY.set('AM')
        self.drop_ampm_startfreetimeSUNDAY = ttk.OptionMenu(self, self.clicked_ampm_startfreetimeSUNDAY,'AM','AM', 'PM')
        self.drop_ampm_startfreetimeSUNDAY.grid(column = 4, row = 8, sticky = W)

        self.colon_startfreetimeSUNDAY = Label(self, text = " to ",anchor=W)
        self.colon_startfreetimeSUNDAY.config(font=font_stye1)
        self.colon_startfreetimeSUNDAY.grid(column = 5, row = 8)
        
        #Create dropdown menu to select the stating free time
        self.clicked_endfreehoursSUNDAY = tk.StringVar()
        self.clicked_endfreehoursSUNDAY.set('12')
        self.drop_endfreehoursSUNDAY = ttk.OptionMenu(self, self.clicked_endfreehoursSUNDAY,'01','01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12')
        self.drop_endfreehoursSUNDAY.grid(column = 6, row = 8, sticky = W)
        
        self.colon_endfreetimeSUNDAY = Label(self, text = ":",anchor=W)
        self.colon_endfreetimeSUNDAY.config(font=font_stye1)
        self.colon_endfreetimeSUNDAY.grid(column = 7, row = 8)
        
        self.clicked_endstartminSUNDAY = tk.StringVar()
        self.clicked_endstartminSUNDAY.set('00')
        self.drop_endstartminSUNDAY = ttk.OptionMenu(self, self.clicked_endstartminSUNDAY,'00','00', '05', '10', '15' ,'20', '25', '30', '35', '40', '45', '50', '55')
        self.drop_endstartminSUNDAY.grid(column = 8, row = 8, sticky = W)
        
        self.clicked_ampm_endfreetimeSUNDAY = tk.StringVar()
        self.clicked_ampm_endfreetimeSUNDAY.set('AM')
        self.drop_ampm_endfreetimeSUNDAY = ttk.OptionMenu(self, self.clicked_ampm_endfreetimeSUNDAY,'AM','AM', 'PM')
        self.drop_ampm_endfreetimeSUNDAY.grid(column = 9, row = 8, sticky = W)

    def save_availability(self):
        def get_availability():
            
            self.availabilityMONDAY = str(self.clicked_startfreehoursMONDAY.get() + ":" + self.clicked_freestartminMONDAY.get() + ":00 " + self.clicked_ampm_startfreetimeMONDAY.get() + " to " 
                                        + self.clicked_endfreehoursMONDAY.get() + ":" + self.clicked_endstartminMONDAY.get() + ":00 " + self.clicked_ampm_endfreetimeMONDAY.get())
           
            workTimeList[0][0] = convert24(self.availabilityMONDAY[0:11])
            workTimeList[0][1] = convert24(self.availabilityMONDAY[15:26])
            
            self.availabilityTUESDAY = str(self.clicked_startfreehoursTUESDAY.get() + ":" + self.clicked_freestartminTUESDAY.get() + ":00 " + self.clicked_ampm_startfreetimeTUESDAY.get() + " to " 
                                        + self.clicked_endfreehoursTUESDAY.get() + ":" + self.clicked_endstartminTUESDAY.get() + ":00 " + self.clicked_ampm_endfreetimeTUESDAY.get())
            
            workTimeList[1][0] = convert24(self.availabilityTUESDAY[0:11])
            workTimeList[1][1] = convert24(self.availabilityTUESDAY[15:26])
            
            self.availabilityWEDNESDAY = str(self.clicked_startfreehoursWEDNESDAY.get() + ":" + self.clicked_freestartminWEDNESDAY.get() + ":00 " + self.clicked_ampm_startfreetimeWEDNESDAY.get() + " to " 
                                        + self.clicked_endfreehoursWEDNESDAY.get() + ":" + self.clicked_endstartminWEDNESDAY.get() + ":00 " + self.clicked_ampm_endfreetimeWEDNESDAY.get())
            
            workTimeList[2][0] = convert24(self.availabilityWEDNESDAY[0:11])
            workTimeList[2][1] = convert24(self.availabilityWEDNESDAY[15:26])
            
            self.availabilityTHURSDAY = str(self.clicked_startfreehoursTHURSDAY.get() + ":" + self.clicked_freestartminTHURSDAY.get() + ":00 " + self.clicked_ampm_startfreetimeTHURSDAY.get() + " to " 
                                        + self.clicked_endfreehoursTHURSDAY.get() + ":" + self.clicked_endstartminTHURSDAY.get() + ":00 " + self.clicked_ampm_endfreetimeTHURSDAY.get())
            
            workTimeList[3][0] = convert24(self.availabilityTHURSDAY[0:11])
            workTimeList[3][1] = convert24(self.availabilityTHURSDAY[15:26])
            
            self.availabilityFRIDAY = str(self.clicked_startfreehoursFRIDAY.get() + ":" + self.clicked_freestartminFRIDAY.get() + ":00 " + self.clicked_ampm_startfreetimeFRIDAY.get() + " to " 
                                        + self.clicked_endfreehoursFRIDAY.get() + ":" + self.clicked_endstartminFRIDAY.get() + ":00 " + self.clicked_ampm_endfreetimeFRIDAY.get())
            
            workTimeList[4][0] = convert24(self.availabilityFRIDAY[0:11])
            workTimeList[4][1] = convert24(self.availabilityFRIDAY[15:26])
            
            self.availabilitySATURDAY = str(self.clicked_startfreehoursSATURDAY.get() + ":" + self.clicked_freestartminSATURDAY.get() + ":00 " + self.clicked_ampm_startfreetimeSATURDAY.get() + " to " 
                                        + self.clicked_endfreehoursSATURDAY.get() + ":" + self.clicked_endstartminSATURDAY.get() + ":00 " + self.clicked_ampm_endfreetimeSATURDAY.get())
            
            workTimeList[5][0] = convert24(self.availabilitySATURDAY[0:11])
            workTimeList[5][1] = convert24(self.availabilitySATURDAY[15:26])

            self.availabilitySUNDAY = str(self.clicked_startfreehoursSUNDAY.get() + ":" + self.clicked_freestartminSUNDAY.get() + ":00 " + self.clicked_ampm_startfreetimeSUNDAY.get() + " to " 
                                        + self.clicked_endfreehoursSUNDAY.get() + ":" + self.clicked_endstartminSUNDAY.get() + ":00 " + self.clicked_ampm_endfreetimeSUNDAY.get())
            
            workTimeList[6][0] = convert24(self.availabilitySUNDAY[0:11])
            workTimeList[6][1] = convert24(self.availabilitySUNDAY[15:26])
                    
            self.save_availibity['state']= DISABLED
            self.save_task['state']= NORMAL
            
        #create save button
        self.save_availibity = ttk.Button(self, text = 'Save Time', command = get_availability)
        self.save_availibity.grid (column = 0, row = 9, sticky = W)
        
        self.reset_availibity = ttk.Button(self, text = 'Reset Time', command = self.reset_time)
        self.reset_availibity.grid (column = 1, row = 9, sticky = W)
        
        self.save_task['state']= DISABLED
   
    def reset_time(self):
        self.save_availibity['state']= NORMAL
        
        
    def create_mainpagelabels(self):
        
        
        self.tasknamelabel = tk.Label(self, text = " ",anchor=W)
        self.tasknamelabel.config(font= font_stye1)
        self.tasknamelabel.grid(column = 0, row = 10, sticky = W)
        
        
        self.tasknamelabel = tk.Label(self, text = "Enter Task",anchor=W)
        self.tasknamelabel.config(font= font_stye2)
        self.tasknamelabel.grid(column = 0, row = 11, sticky = W)
        
        self.tasknamelabel = tk.Label(self, text = "Enter the Course Name:",anchor=W)
        self.tasknamelabel.config(font= font_stye1)
        self.tasknamelabel.grid(column = 0, row = 12, sticky = W)
        
        self.tasksummarylabel = tk.Label(self, text = "Task Enter Task Summary:",anchor=W)
        self.tasksummarylabel.config(font= font_stye1)
        self.tasksummarylabel.grid(column = 0, row = 13, sticky = W)
        
        self.endtimelabel = tk.Label(self, text = "Select Due Time:",anchor=W)
        self.endtimelabel.config(font= font_stye1)
        self.endtimelabel.grid(column = 0, row = 15, sticky = W)
        
        self.daylabel = tk.Label(self, text = "Select the Duedate:",anchor=W)
        self.daylabel.config(font= font_stye1)
        self.daylabel.grid(column = 0, row = 16, sticky = W)

        self.difficulty  = tk.Label(self, text = "Select the Difficulty:",anchor=W)
        self.difficulty.config(font=font_stye1)
        self.difficulty.grid(column = 0, row = 17, sticky = W)
        
        self.weightagelabel  = tk.Label(self, text = "Enter the Weightage % Towards the Final Grade:",anchor=W)
        self.weightagelabel.config(font=font_stye1)
        self.weightagelabel.grid(column = 0, row = 18, sticky = W)
        
        self.percentagelabel = tk.Label(self, text = "%",anchor=W)
        self.percentagelabel.config(font=font_stye1)
        self.percentagelabel.grid(column = 5, row = 18, sticky = W)
        
        self.preparationlabel  = tk.Label(self, text = "How Much Prepared Are You For This Task?:",anchor=W)
        self.preparationlabel.config(font=font_stye1)
        self.preparationlabel.grid(column = 0, row = 19, sticky = W)
    
    def create_mainpageentry(self):
        #Create entry box to write the course name
        self.taskentry= tk.StringVar()
        self.textbox = ttk.Entry(self, width  = 20, textvariable = self.taskentry)
        self.textbox.focus()
        self.textbox.grid(column=1, row=12,columnspan = 4)
        
        self.tasksummary= tk.StringVar()
        self.summarytextbox = ttk.Entry(self, width  = 20, textvariable = self.tasksummary)
        self.summarytextbox.focus()
        self.summarytextbox.grid(column=1, row=13,columnspan = 4)

        #Create dropdown menu to select the end time
        self.clicked_endhours = tk.StringVar()
        self.clicked_endhours.set('12')
        self.drop_endhours = ttk.OptionMenu(self, self.clicked_endhours,'01','01', '02', '03', '04', '05', '06','07', '08', '09', '10', '11', '12')
        self.drop_endhours.grid(column = 1, row = 15, sticky = W)
        
        self.colon_endtime = Label(self, text = ":",anchor=W)
        self.colon_endtime.config(font=font_stye1)
        self.colon_endtime.grid(column = 2, row = 15)
        
        self.clicked_endmin = tk.StringVar()
        self.clicked_endmin.set('00')
        self.drop_endmin = ttk.OptionMenu(self, self.clicked_endmin,'00','00', '05', '10', '15' ,'20', '25', '30', '35', '40', '45', '50', '55')
        self.drop_endmin.grid(column = 3, row = 15, sticky = W)
        
        self.clicked_ampm_endtime = tk.StringVar()
        self.clicked_ampm_endtime.set('AM')
        self.drop_ampm_endtime = ttk.OptionMenu(self, self.clicked_ampm_endtime,'AM','AM', 'PM')
        self.drop_ampm_endtime.grid(column = 4, row = 15, sticky = W)
        
        #Create dropdown to select the date and day
        self.cal = Calendar(self, selectmode = 'day', year = 2020, month = 11, day = 1,date_pattern='mm/dd/y')
        self.cal.grid(column = 1, row = 16, sticky = W, columnspan = 5)
        
        #Create dropdown for difficulty level (3 most difficult, 2 moderate, 1 easy)
        self.clicked_difficulty = tk.StringVar()
        self.clicked_difficulty.set('easy')
        self.drop_difficulty = ttk.OptionMenu(self, self.clicked_difficulty,'easy','easy', 'moderate', 'difficult')
        self.drop_difficulty.grid(column = 1, row = 17, sticky = E, columnspan = 5)
        
        #entry box for weightage
        self.weightage= tk.StringVar()
        self.weightagebox = ttk.Entry(self, width  = 20, textvariable = self.weightage)
        self.weightagebox.focus()
        self.weightagebox.grid(column=1, row=18,columnspan = 4)
        
        #Create dropdown for prep level (3 fully prepared, 2 some what prepared, 1 not prepared)
        self.clicked_prep = tk.StringVar()
        self.clicked_prep.set('fully prepared')
        self.drop_prep = ttk.OptionMenu(self, self.clicked_prep,'fully prepared','fully prepared', 'some what prepared', 'not prepared')
        self.drop_prep.grid(column = 1, row = 19, sticky = E, columnspan = 5)
        

    def save_mainpageentry(self):
        
        #Empty labels later filled by the program
        self.summary  = Label(self, text = " ",anchor=W)
        self.summary.config(font=font_stye2)
        self.summary.grid(column = 0, row = 21, sticky = W)
        
        self.tasksummaryshow  = Label(self, text = " " ,anchor=W)
        self.tasksummaryshow.config(font=font_stye1)
        self.tasksummaryshow.grid(column = 0, row = 22, sticky = W)
        
        self.duesummary  = Label(self, text = " " ,anchor=W)
        self.duesummary.config(font=font_stye1)
        self.duesummary.grid(column = 0, row = 23, sticky = W)
                
        self.requrired_studytime  = Label(self, text = " " ,anchor=W)
        self.requrired_studytime.config(font=font_stye1)
        self.requrired_studytime.grid(column = 0, row = 24, sticky = W)
        
        def add_summary():
            #To do: clear last printed result

            self.summary.destroy()
            self.tasksummaryshow.destroy()
            self.duesummary.destroy()
            self.requrired_studytime.destroy()
            
            
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
            self.diff_D = (self.clicked_difficulty.get())
            if self.diff_D == 'easy':
                self.diff_D = 1;
            if self.diff_D == 'moderate':
                self.diff_D = 2;
            if self.diff_D == 'difficult':
                self.diff_D = 3;
            
            self.prep_P = (self.clicked_prep.get())
            #print(self.prep_P)
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
                """
                print(k2*int(self.diff_D))
                print(k3*int(self.taskweightage))
                print(self.prep_P)
                """
                
                self.requiredTime = (k2*int(self.diff_D)) + (k3*int(self.taskweightage)) + (k4/int(self.prep_P))
                
                #print summary
                self.summary  = Label(self, text = "Summary:",anchor=W)
                self.summary.config(font=font_stye2)
                self.summary.grid(column = 0, row = 21, sticky = W)
                
                self.tasksummaryshow  = Label(self, text = "Task : " + str (self.taskname) + ", " + str (self.taskdescription),anchor=W)
                self.tasksummaryshow.config(font=font_stye1)
                self.tasksummaryshow.grid(column = 0, row = 22, sticky = W)
                
                self.duesummary  = Label(self, text = "Task Due Date: " + str(self.day_name)+ " "+ str(self.taskdate),anchor=W)
                self.duesummary.config(font=font_stye1)
                self.duesummary.grid(column = 0, row = 23, sticky = W)
                
                self.requrired_studytime  = Label(self, text = "Required Study Time : "+ str(round(int(self.requiredTime))) + " hours" ,anchor=W)
                self.requrired_studytime.config(font=font_stye1)
                self.requrired_studytime.grid(column = 0, row = 24, sticky = W)
                        
                #reset entries
                self.textbox.delete(0, 'end')
                self.summarytextbox.delete(0, 'end')
                self.weightagebox.delete(0,'end')
                
                
                
                """
                Task Schedular call
                """
                # Save user input in Task object and adding to tasks to a list
                userTask = Task(self.taskname, self.taskdescription, round(int(self.requiredTime)), self.taskdate, self.converted_endtime)
                task_List.append(userTask)
                
                
                task_List.sort(key= sortTaskDuetime)
                task_List.sort(key= sortTaskDuedate) 
                
                # Clear the calendar after items have been added
                global check_added
                if check_added:
                    delete_events(service)
                
                # Call allocate taskList
                taskAllocater(task_List, workTimeList)
                
                schedule_events(service, task_List)
                check_added = True

                

        #Blank Label to print summary
        self.availibitylabel = tk.Label(self, text = " ",anchor=W)
        self.availibitylabel.grid(column = 0, row = 21, sticky = W)
        self.availibitylabel = tk.Label(self, text = " ",anchor=W)
        self.availibitylabel.grid(column = 0, row = 22, sticky = W)
        self.availibitylabel = tk.Label(self, text = " ",anchor=W)
        self.availibitylabel.grid(column = 0, row = 23, sticky = W)
        self.availibitylabel = tk.Label(self, text = " ",anchor=W)
        self.availibitylabel.grid(column = 0, row = 24, sticky = W)
        self.availibitylabel = tk.Label(self, text = " ",anchor=W)
        self.availibitylabel.grid(column = 0, row = 25, sticky = W)
        
        
        self.save_task = ttk.Button(self, text = 'Generate Summary and Add to Calendar', command = add_summary)
        self.save_task.grid (column = 0, row = 20, sticky = W)



root = Root()
root.mainloop()