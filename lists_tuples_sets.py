courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses[0])
print(courses[3])

#can use negative indexes as well
print(courses[-1])
#prints "CompSci"

#slicing
#will print every item up to and not including 2
print(courses[:2])

#will print everything after and including index 2 till the end
print(courses[2:])

#list methods available to us
#add an item to our list append method
courses.append('Art')
print(courses)

#add to a specific location in the list 
courses.insert(0, 'Art')

#using the extend method
#want to use extend when adding multiple values to replace a current list
courses_2 = ['Art', 'Education']
#courses.insert(0, courses_2)

#add multiple values to an existing list
courses.extend(courses_2)

print(courses`  1)

