class trainingProblemSolver:

   
  def getMinHourNumbers(self,list_students_skills,number_student_per_team):

    list_students_skills.sort()
    
    best_min_hours = self.computeMinHours(list_students_skills[0:number_student_per_team])
    
    ind_min = number_student_per_team
    ind_max = len(list_students_skills) - 1

    while ind_min <= ind_max:
      min_hours_from_ind_min = self.computeMinHours(list_students_skills[ind_min:ind_min+number_student_per_team])
      min_hours_from_ind_max = self.computeMinHours(list_students_skills[ind_max - number_student_per_team:ind_max])
      best_min_hours = min(best_min_hours,min_hours_from_ind_min,min_hours_from_ind_max)
      ind_min += 1
      ind_max -=1

    return 0
  
  def computeMinHours(self,sub_students_list):
    min_hours = 0
    for i in range(len(sub_students_list)-1):
      min_hours += (i+1)*(sub_students_list[i+1] - sub_students_list[i])
    
    print(sub_students_list,min_hours)
    return min_hours

if __name__ == '__main__':
  
  solver = trainingProblemSolver()
  solver.getMinHourNumbers([3,1,9,100,102,101],3)

