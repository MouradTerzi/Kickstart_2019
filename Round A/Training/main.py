import os 
import sys 

sys.path.insert(0,'Inputs')
sys.path.insert(0,'Solver')
sys.path.insert(0,'Output')

import read_input 
import training_problem_solver

def solve_training_problems(instances_path_list):
    
    rd = read_input.reader()  #Instantiate a reader
    solver = training_problem_solver.trainingProblemSolver() #Instantiate a solver 

    for i, path in enumerate(instances_path_list):
      training_instance = rd.readInput(path)
      if training_instance != -1 :# Resolve the input instance
        f = open('Outputs/instance_'+str(i+1)+"_solution","w")
        for j,skills in enumerate(training_instance.skills_list):
        
          best_min_hours = solver.getMinHourNumbers(skills,training_instance.numb_students_per_team[j])
          f.write("Case #"+str(j+1)+": "+str(best_min_hours)+"\n")
        
        f.close()
    
      else:
        print("The input instance path not corresponds to an existing file !!")
    
    return 0


if __name__ == '__main__':

  instances_path_list = ['Inputs/test_instance']
  solve_training_problems(instances_path_list)