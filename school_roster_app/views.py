from django.shortcuts import render
from .models import School # import our School class

my_school = School("Django School") # create a school instance
staff_list = []
student_list = []

def index(request):
    my_data = { 
        "school_name": my_school.name
    }
    return render(request, "pages/index.html", my_data)


def list_staff(request):
    my_data = {'staff_list': my_school.staff}
    for staff in my_school.staff:
        staff_list.append(staff)

    return render(request, 'pages/staff.html', my_data)

# add employee_id para back here
def staff_detail(request, employee_id):
    my_data = {}
    for staff in staff_list:
        if staff.employee_id == int(employee_id):
            my_data['employee'] = staff
        

    return render(request, 'pages/staffdetail.html', my_data)
    


def list_students(request):
    my_data = {'student_names': my_school.students}
    for students in my_school.students:
        student_list.append(students)
    

    return render(request, 'pages/students.html', my_data)


def student_detail(request, student_id):
    my_data = {}
    for student in student_list:
        if student.school_id == int(student_id):
            my_data['student'] = student
        

    return render(request, 'pages/studentdetail.html', my_data)

