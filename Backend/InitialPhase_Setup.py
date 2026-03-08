import numpy as np

class GridEnvironment:    
        
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
                    break
            except ValueError:
                print("Invalid Input, Please enter a whole number: ") 
                
        while True:
            try:
                self.start_x=int(input("Enter start position x axis: "))
                self.start_y=int(input("Enter start position y axis: "))
                if((self.start_x<0) or (self.start_x>self.rows-1)):
                    print("Invalid Input! Try again: ")
                elif((self.start_y<0) or (self.start_y>self.cols-1)):
                    print("Invalid Input! Try again: ")
                else: 
                    break
                
            except ValueError:
                print("Invalid Input, Please enter a whole number: ") 
        
        while True:
            try:
                self.end_x=int(input("Enter end position x axis: "))
                self.end_y=int(input("Enter end position y axis: "))
                if((self.end_x<0) or (self.end_x>self.rows-1)):
                    print("Invalid Input! Try again: ")
                elif((self.end_y<0) or (self.end_y>self.cols-1)):
                    print("Invalid Input! Try again: ")
                else: 
                    break
                
            except ValueError:
                print("Invalid Input, Please enter a whole number: ")             
                
        while True:
            try:
                self.occupied=int(input("Enter percentage of obstacles: "))
                if(self.occupied<0 or self.occupied>80):
                    print("Percentage occupancy should not exceed 80 percent or less than 0 percent ! Try again: ");
                else:
                    break
            except ValueError:
                print("Invalid Input! Please enter a whole number:")
                                                    
        return self.rows, self.cols, self.start_x, self.start_y, self.end_x, self.end_y, self.occupied

    def gridGenerationAndSetup(self,rows,cols,start_x,start_y,end_x,end_y,occupancy):
        
        grid=np.zeros((rows,cols),dtype=int)
        
        occupancy=occupancy/100
        
        randomGrid=np.random.random((rows,cols))
        
        mask=randomGrid<occupancy
        grid[mask]=1
        
        grid[start_x,start_y]=2
        grid[end_x,end_y]=3
        
        return grid
 
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
    
        
    
        
        
    