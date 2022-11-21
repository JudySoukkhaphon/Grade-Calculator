# Uses 'Grid' functions from the tKinter library
# The "ugliness" of the program, i.e., the colors of the boxes are for visibility not aesthetic!

# (Changes)
    #(12/15/20)
    # Removed unused variables, redundant code and unnecessary comments.
    # Summarized/clarified function comments.


# (!) To do (!):
    # Figure out how to make a scroll bar because if there are too many entry fields they will not appear beyond the size of the window.
        # --a temporary option:
        # rewrite the height of the window to change dynamically based on user input
        # (must include a ceiling to maintain functionality; the program is now limited by the ceiling instead of the set window size)

    # The shell also still pops up on execution.


__version__ = "0.9"

from tkinter import *
import tkinter
import itertools


class Application(Frame):


# Creates the static gui components
    def __init__(self, master=None):

        #Creates the overall window
        sizex = 500 
        sizey = 300
        posx  = 250 
        posy  = 100
       
        Frame.__init__(self, master) 
        self.master.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy)) 
        self.master.title("Grid Manager") 

        for r in range(12):
            self.master.rowconfigure(r, weight=1)    
        for c in range(5):
            self.master.columnconfigure(c, weight=1)

        # This block defines the size and color of the frames that exist within the window.
        self.Frame1 = Frame(master, bg="grey") 
        self.Frame1.grid(row = 0, column = 0, rowspan = 1, columnspan = 4, sticky = W+E+N+S) 
        self.Frame2 = Frame(master, bg="white")
        self.Frame2.grid(row = 1, column = 0, rowspan = 10, columnspan = 4, sticky = W+E+N+S)
        self.Frame3 = Frame(master, bg="blue")
        self.Frame3.grid(row = 10, column = 0, rowspan = 1, columnspan = 6, sticky = W+E+N+S)
        self.Frame4 = Frame(master, bg="green")
        self.Frame4.grid(row = 0, column = 4, rowspan = 11, columnspan = 1, sticky = W+E+N+S)

        
        
        # entry field for user to enter the number of grades (stored in 'myvalue')
        self.myvalue=Entry(self.Frame4,width=12) 
        self.myvalue.place(x=14,y=50)

        # 'Ok' button
        self.mybutton=Button(self.Frame4,text="OK",command=self.myClick)
        self.mybutton.place(x=45,y=80)
        
        # 'Reset' button (just exits the current instance and restarts a new one)
        self.mybutton=Button(self.Frame4,text="RESET",command=Application) 
        self.mybutton.place(x=50,y=240)

        # 'Average' button
        self.abutton=tkinter.Button(self.Frame3,text="Average",command=self.getGrades)
        self.abutton.place(x=150, y=1)

        
        # text labels 
        self.test1_label2 = Label(self.Frame3, text='Final Grade: ').place(x=280, y=1)
        
        
        self.test2_label = Label(self.Frame1, text='Grade Average').place(x=150, y=1)
    

        self.label1 = Label(self.Frame4, text='Enter Number \n'\
                   'of Grades', width=12)
        self.label1.place(x=5, y=5)
        
        


# The "Ok" button is tied to this function which creates the entry fields for weighted grades (grade and their associated percent value)
    def myClick(self):       
        self.grades = []        # <-- holds str array of grades
        self.percents = []     # <-- holds str array of percentages

        # creates entry fields used to populate the two arrays     
        for n in range(int(self.myvalue.get())): 
            Label(self.Frame2,text="Grade "+str(n+1)).place(x=10,y=30+(30*n))        
            grade = Entry(self.Frame2, width=10) 
            grade.place(x=70,y=30+(30*n))
            self.grades.append(grade)               
            
            Label(self.Frame2,text="Percent "+str(n+1)).place(x=170,y=30+(30*n))
            percent = Entry(self.Frame2, width=10)
            percent.place(x=240,y=30+(30*n))
            self.percents.append(percent)          





            
 # (?) For some reason I couldn't reference the arrays with the 'self' parameter to use in the calculate() function
 # So getGrades() and getPercents() basically copy those values into a regular array without the 'self' parameter.

    #The "Average" button is tied to this function.
    def getGrades(self):
        index = 0
        gradeList = []          
        for grade in self.grades: 
            try:
                gradeList.append(grade.get())   
            except ValueError:
                print('Invalid value for grade: {}'.format(grade.get()))
                
        self.getPercents(gradeList)

     
    
    def getPercents(self, gradeList):
        percentList = []           
        for percent in self.percents:
            try:
                percentValue = (float(percent.get()))/100
                percentList.append(percentValue)
            except ValueError:
                print('Invalid value for grade: {}'.format(percent.get()))
                
        self.calculate(gradeList, percentList)         





# calculates the weighted values of each grade, stores them in an array, sums them and displays the result in Frame3
    # (I chose to store the results in an array for the purpose of having a way to reference each value in the event I want to expand on this program later)
    # but as it currently exists, the array is excessive as it requires an extra step to then sum up those values.
    # the other option was to instead accumulate the values into a single float variable to get the result
    def calculate(self, gradeList, percentList): 
        index = 0
        pointsList = []         
        while index < len(gradeList):
            result = ((float(gradeList[index]))*(float(percentList[index])))
            pointsList.append(result)
            index += 1
            

        total = sum(pointsList)     # <-- sums up all the values
        Label(self.Frame3, text=format(total, ',.2f')).place(x=350, y=1)
       
    



root = Tk()
app = Application(master=root)
app.mainloop()





