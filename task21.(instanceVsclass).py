# If we have an object which has both instance
# as well as class attr, who will get preference?

# Class attribute

class School:
    name = "DSSD"
    place = "jalandhar"
    student_non = 150
    student_arts = 100
Nonmedical = School()
arts = School()

# Here CLASS attribute work
print(Nonmedical.student_non)
print(arts.student_arts)

# Here INSTANCE attribute work
Nonmedical.student_non = 150 + 50
arts.student_arts = 100 + 50
print(Nonmedical.student_non)
print(arts.student_arts)

# As we can see the INSTANCE attribute took preference over CLASS attribute.