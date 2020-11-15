import math
from datetime import datetime, date, timedelta

class Task:
    
    # Constructor
    """
    def __init__(self, name, description, total_time, due_date, start_time, end_time):
        self.name = name
        self.description = description
        self.total_time = total_time
        self.due_date = due_date
        self.start_time = start_time
        self.end_time = end_time
    """
    
    def __init__(self, name, description, total_time, due_date, due_time):
        self.name = name
        self.description = description
        self.total_time = total_time
        self.due_date = due_date
        self.due_time = due_time
        self.start_time = [0]*5
        self.end_time = [0]*5


    # Create Setters and Getters for Task variables
      
    #Setters
    def set_name(self,value):
        self.name = value
    
    def set_description(self, value):
        self.description = value
    
    #def set_difficulty(self, value):
        #self.difficulty = value
    
    def set_total_time(self, value):
        self.total_time = value
    
    def set_due_date(self, value):
        self.due_date = value
        
    def set_due_time(self, value):
        self.due_time = value
    
    def set_start_time(self, day_date_time):
        #format in year, month, day, hour, minute
        cur_date_time = day_date_time[:]
        self.start_time[0] = int(cur_date_time[6:10])
        self.start_time[1] = int(cur_date_time[3:5])
        self.start_time[2] = int(cur_date_time[0:2])
        self.start_time[3] = int(cur_date_time[11:13])
        self.start_time[4] = int(cur_date_time[14:16])
        
    
    def set_end_time(self, day_date_time):
        #format in year, month, day, hour, minute
        cur_date_time = day_date_time[:]
        self.end_time[0] = int(cur_date_time[6:10])
        self.end_time[1] = int(cur_date_time[3:5])
        self.end_time[2] = int(cur_date_time[0:2])
        self.end_time[3] = int(cur_date_time[11:13])
        self.end_time[4] = int(cur_date_time[14:16])
        
        
    #Getters
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    #def get_difficulty(self):
        #return self.difficulty
    
    def get_total_time(self):
        return self.total_time
    
    def get_due_date(self):
        return self.due_date
    
    def get_due_time(self):
        return self.due_time
    
    def get_start_time(self):
        return self.start_time
    
    def get_end_time(self):
        return self.end_time
    
    #Printing Task method variables
    def printTask(self):
        print(self.name) 
        print(self.description)
        print(self.total_time) 
        print(self.due_date) 
        print(self.start_time)
        print(self.end_time)
   
        
# Compares the time1 to time2 in the time format h:m:s   
# Returns 0 if time1 <= time2 or 1 if time1 > time2 
def compareTimes(time1, time2):
    if int(time1[0:2]) <= int(time2[0:2]):
        return 0
    elif int(time1[3:5]) <= int(time2[3:5]):
        return 0 
    else:
        return 1
    

# Find the difference of the work times in hours
def availableWorkTime(startTime, endTime):
    t1 = int(startTime[0:2]) + math.floor(int(startTime[3:5])/60)
    t2 = int(endTime[0:2]) + math.floor(int(endTime[3:5])/60)
    
    return t2-t1
    

# Calculate the appropriate end time based on the start time and end time
def calcEndTime(startTime, taskTime):
    end_hour = int(startTime[0:2]) + taskTime
    if end_hour < 10:
        end_Time = "0" + str(end_hour) + startTime[2:8]
    else: 
        end_Time = str(end_hour) + startTime[2:8]
    return end_Time
    
     
def setEndDateTime(date_time, end_Time):
    end_date_time = date_time[0:11] + end_Time
    return end_date_time

    
"""
Description: Sets start and end times of tasks based on the the total time it takes to complete the task
and how much free time the user sets up
Input: sorted list of tasks in terms of closest to furthest due dates
Output: each task is ready to be added as an event by google api
"""
def taskAllocater(taskList, workTimeList):
        # Get the current day and time
        now = datetime.now()
        day_date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        day_of_week = date.today().weekday()
        
        # Trying this
        now = now + timedelta(days=1)
        now = now.replace(hour=int(workTimeList[day_of_week][0][0:2]),
                          minute=int(workTimeList[day_of_week][0][3:5]), second=0)
        day_date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        day_of_week = (day_of_week+1) % 7 
        
        i = 0
        while i < len(taskList):
            
            # Check if work time hasn't ended yet 
            #if compareTimes(workTimeList[day_of_week][1], day_date_time[11:19]) == 0:
            workTime = availableWorkTime(day_date_time[11:19], workTimeList[day_of_week][1])
            
            # Check if there's enough work time in the day to schedule the entire task
            if workTime >= taskList[i].get_total_time():
                # Set start time for task
                taskList[i].set_start_time(day_date_time)
                # Update the day_date_time
                endTime = calcEndTime(day_date_time[11:19], taskList[i].get_total_time())
                end_date_time = setEndDateTime(day_date_time, endTime)
                # Set end time for task
                taskList[i].set_end_time(end_date_time)
             
                # Update the day_date_time  
                day_date_time = end_date_time
                
                # Update to the next day if there isn't anymore time  
                i += 1
        
                
            # If there isn't enough work time in the day then split up schedule
            else:
                # Set start time for task
                taskList[i].set_start_time(day_date_time)
                # Update the day_date_time
                end_date_time = setEndDateTime(day_date_time, workTimeList[day_of_week][1])
                taskList[i].set_end_time(end_date_time)
                taskList[i].printTask()
                
                # Split up the remaining task into a new task 
                # Calculate amount of time already scheduled to task
                scheduledTime = availableWorkTime(day_date_time[11:19],end_date_time[11:19])
                print("available time to work: " + str(scheduledTime))
                
                # Add split task into taskList 
                taskSplitter(taskList[i], taskList, scheduledTime, i)
                
                # Update the day_date_Time to the next day
                now = now + timedelta(days=1)
                now = now.replace(hour=int(workTimeList[day_of_week][0][0:2]),
                                                      minute=int(workTimeList[day_of_week][0][3:5]), second=0)
                day_date_time = now.strftime("%d/%m/%Y %H:%M:%S")
                # Update the day of week
                day_of_week = (day_of_week+1) % 7 
                i += 1 
        
      
        
"""
Description: If insufficient work time to fit in task in one day -> Splits up tasks to be carried out in multiple days
Input: task that needs to be split 
Output: new task object with the allocated time subtracted from total estimated time
"""
def taskSplitter(task, taskList, setTime, i):
        # Create new task object
        new_total_time = task.get_total_time() - setTime
        print("new total time: " + str(new_total_time))
        newTask = Task(task.get_name(), task.get_description(), new_total_time, task.get_due_date(), task.get_due_time())
        taskList.insert(i+1, newTask)
        # Copy previous task object characteristics and sub the number of setTime from total time
        
 
  
        