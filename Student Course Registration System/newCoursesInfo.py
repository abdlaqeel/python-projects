from random import *
course_no = 5
studentno = 6
students = ["Andy Pandy","Benny Menny", "Kim Simms","Rolly Polly","Cindy Mindy","Geeta Peeta"]
courses = ["CS101", "CS105", "CS110", "CS115", "CS120"]    
def main():
    #INitializes variables
    course_no = 5
    studentno = 6
    students = ["Andy Pandy","Benny Menny", "Kim Simms","Rolly Polly","Cindy Mindy","Geeta Peeta"]
    courses = ["CS101", "CS105", "CS110", "CS115", "CS120"]  
    printRangeForCourse(course_no, courses)
    print() #leaves a line between output
    computeAllAverages(students,studentno,course_no)
    
def initializeMarks(course_no, studentno): #2 dimensional list with outerloop to generate a 2d list of random marks
    marks = [[]for x in range(course_no)]
    for x in range(studentno):
        for i in range (course_no):
            marks[i].append(randint(1,100))
    return marks
                 
def findMinForRow(x): #selects a row and finds min
    min_row = min(initializeMarks(course_no, studentno)[x])
    return min_row

def findMaxForRow(x): #selects a row and finds min
    max_row = max(initializeMarks(course_no, studentno)[x])
    return max_row

def printRangeForCourse(course_no, courses): #prints the range
    print("Courses       Range of Marks")
    for i in range(0,course_no):
        print("%7s" %courses[i], "%13d" % (findMaxForRow(i) - findMinForRow(i)))
        
def computeAllRanges(marks, courses):
    printRangeForCourse(marks, courses)
    
def computeAllAverages(students,studentno,course_no):  #computes average and print with the name of student
    print("Student Name         Average Marks")
    for i in range(0, studentno):
        sum = 0
        for x in range(0,course_no):
            sum = sum + initializeMarks(course_no, studentno)[x][i]
        avg = sum/5
        print(" ", "%-12s" %students[i], "%16.1f" % avg)


main()
