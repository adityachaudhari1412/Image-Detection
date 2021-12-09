'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
#This code works as a log viewer for application log data from reading from given set of of files taking 
# input range from user in unix time and returning all log entries in that range 
# Aditya Chaudhari

                  
 

import datetime  # library to support datetime
import  os


def main():
   
    path = os.getcwd()  # gets the current working directory
    file_names=[]   # array to store filenames
    for fil in os.listdir(path):     # loop to read filenames ending with .lo  
        if fil.endswith('.log'):
            file_names.append(fil)
                     
    log_data = []      # array storing log data  
    start = input("Enter starting timestamp in unix format: ")    
    dt_start = int(start)      # converts the start datetime to int
    end = input("Enter ending timestamp in unix format: ")     
    dt_end = int(end)   # converts the end datetime from string
    
    sev = input("Enter [0-3] to apply severity  filter or leave blank for all: ")
    
    if(sev !=''):       # checks if the input is severity
        sev = int(sev)        

    else:
        sev=999
    tsev = int(sev)      
    

    
    for fn in file_names:    # loop thru all the log files
        # open the file 
        with open(fn, 'r') as f:              
            for line in f:
                # splits the line using comma separator      
                log_data.append(line.split(','))
                
                dt = (int(log_data[-1][1]))   # converts the current line unix time into int
                dsev = (int(log_data[-1][2])) #reads the current line severity
                
                if(sev==999):   # check if the date is within range and apply severity filter
                    sev=dsev                
                if ((dt_start <= dt <= dt_end) and (dsev==sev)):   
                    print("\n",log_data[-1][0]," ",log_data[-1][1]," ",log_data[-1][2]," ",log_data[-1][3])
                sev=tsev    
                    
if __name__ == "__main__":
    main() 
