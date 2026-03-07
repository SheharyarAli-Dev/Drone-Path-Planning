import numpy as np

class GridEnviroment:
    def __init__(self,rows:int,cols:int):
        self.rows=rows
        self.cols=cols
        
        
    def getUserInput(self):
        print("Welcome to Autonomous Drone Path Planning\n")
        while True:
            try:
                self.rows=int(input("Enter number of rows for grid: "))
                if(self.rows<0):
                    print("Cannot be negative! Try again: ");
                elif(self.rows<=2):
                    print("Rows must be greater than 2, Try Again: ")
                else:
                    break
            except ValueError:
                print("Invalid Input, Please enter a whole number: ")
                
        while True:
            try:
                self.cols=int(input("Enter number of cols for grid: "))
                if(self.cols<0):
                    print("Cannot be negative! Enter greater: ");
                elif(self.cols<=2):
                    print("Cols should be greater than 2, Try again: ");
                else:
                    break;
            except ValueError:
                print("Invalid Input, Please enter a whole number: ")      
                
        return self.rows, self.cols
        
a=GridEnviroment(0,0);   
        
        
        
        
    
        
    
        
        
    