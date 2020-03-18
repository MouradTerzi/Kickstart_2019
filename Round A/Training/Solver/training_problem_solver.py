class trainingProblemSolver:

  # p: Number of students per team 
  # std_skills: List of students skills 
  # part_mn_hrs : Partial min hours 

  def getMinHourNumbers(self,std_skills,p):

    std_skills.sort()
    hrs_from_ind_min, part_ind_min = self.computeMinHours(std_skills[0:p],0) #Get the min hours from the first p students 
    hrs_from_ind_max, part_ind_max = self.computeMinHours(std_skills[len(std_skills) - p:len(std_skills)],1) #Get the min hours from the last p students
    i_min, i_max, mn_hrs = p, len(std_skills) -2, hrs_from_ind_min
    
    while i_min <= i_max:
        
      hrs_from_ind_min += - part_ind_min + (p - 1)*(std_skills[i_min] - std_skills[i_min -1])
      part_ind_min += (std_skills[i_min] - std_skills[i_min -1]) - (std_skills[i_min - p + 1] - std_skills[i_min - p])
      
      hrs_from_ind_max += part_ind_max + (std_skills[i_max - p + 1] - std_skills[i_max - p]) - (p - 1)*(std_skills[i_max + 1] - std_skills[i_max])
      part_ind_max += std_skills[i_max - p + 1] - std_skills[i_max - p] - (std_skills[i_max] - std_skills[i_max - 1])
      mn_hrs = min(mn_hrs,hrs_from_ind_min,hrs_from_ind_max)
      i_min += 1
      i_max -= 1
    
    return mn_hrs
    
  def computeMinHours(self,sub_students_list,position): #Get the minimum hours numbers and the corresponding partial minimum hours
    mn_hrs, part_mn_hrs = 0,0
    for i in range(len(sub_students_list)-1):
      mn_hrs += (i+1)*(sub_students_list[i+1] - sub_students_list[i])
      part_mn_hrs += sub_students_list[i+1] - sub_students_list[i]
    
    if position == 1:
      part_mn_hrs -= (sub_students_list[i+1] - sub_students_list[i])

    print(sub_students_list,mn_hrs,part_mn_hrs)
    return mn_hrs, part_mn_hrs



