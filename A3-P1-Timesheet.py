#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #:     w0461513
#Student Name:  Chukwuemeka Mathew Akunyili
def getHoursWorked():  #defined this function to be able to call it, to store my list
    hours = []
    hoursWorked = ""

    for i in range (5):  #this makes the user enter the hours worked for 5 days using the help of the for loop
        hoursWorked = float(input(f"Enter hours worked on day #{i+1}: "))
        hours.append(hoursWorked) #appends what the user enters into the hours list
    return hours

def maxHours(hours):
    max_hours = max(hours)
    max_days = [i + 1 for i, h in enumerate(hours) if h == max_hours]
    
    if len(max_days) == 1:
        print(f"The most hours worked was on:\nDay #{max_days[0]} when you worked {max_hours} hours.")
    else:
        # I didnt know how to print the 2 highest numbers in the list, so this code is from chat gpt, and was modified by me
        print(f"The most hours worked was on:\nDay(s) #{', and #'.join(map(str, max_days))} when you worked {max_hours} hours.")

def totalHours(hours):
     print("The total number of hours worked was:",sum(hours))

def average(hours):
    average = (sum(hours)) / len(hours) #this fomula gets the average of the days worked
    print("The average number of hours worked each day was:", average)
def slackedDays(hours):
    print("Days you slacked off (i.e. worked less than 7 hours):")
    for i in range(len(hours)):
        if hours[i] < 7:
            print(f"Day #{i + 1}: {hours[i]} hours")
def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #call back all the functions to run the code
    hours = getHoursWorked()
    maxHours(hours)
    totalHours(hours)
    average(hours)
    slackedDays(hours)




    # YOUR CODE ENDS HERE

main()
