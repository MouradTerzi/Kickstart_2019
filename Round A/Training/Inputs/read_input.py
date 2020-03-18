import os 
import sys 
from training_problem import * 

class reader:
  
  def readInput(self,path):
    
    try:
    
      #Read the input file 
      input_file = open(path,"r")
      #Instantiate an object of trainingproblem class 
      training_problem = trainingProblem()
      #Read the tests number
      training_problem.tests_number = int(input_file.readline()[:-1])
      
      current_line = input_file.readline()
      while len(current_line) != 0:
        #Add the number of students for each team
        training_problem.numb_students_per_team.append(int(current_line[2]))
        current_line = input_file.readline().split(' ')
        skills_list = list()
        [skills_list.append(int(current_line[i])) for i in range(len(current_line))]
        training_problem.skills_list.append(skills_list)
        current_line = input_file.readline()
      
      return training_problem
    
    except FileNotFoundError:
        print("The input instance path not corresponds to an existing file !!")
        return -1 
