 ## Creating and Modifying Lists project
 ## Python Gradebook

# a list that contains tuples as elements
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

# this semesters subjects
subjects = ["physics", "calculus", "poetry", "history"]
# adding a subject that we received it's grade later
subjects.append("computer science")

# this semesters grades
grades = [98, 97, 85, 88]
# adding a grade that we received later
grades.append(100)

# this semesters gradebook containing subjects and grades in pairs
gradebook = list(zip(subjects, grades))

# adding another subject with grade to this semesters gradebook
gradebook.append(("visual arts", 93)) # gradebook.append(["visual arts", 93]) worked too

print(gradebook)

# full years gradebook
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)
