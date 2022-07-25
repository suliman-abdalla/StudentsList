import ast
students = {}
class Db:

    def add(stud):
        students = stud
        try:
            f = open('Data', 'r')
            sh = f.readline()
            sh1 = ast.literal_eval(sh)
            students=sh1
        except Exception:
            pass
        student=[]
        x=input('\nStudent ID: ')
        y=input('Student Name: ')
        z=int(input('Student Mark: '))
        student.append(y)
        student.append(z)
        if z >=50:
            student.append("Pass")
        elif z <=49:
            student.append("Fail")
        students[x]=student
        strr = str(students)
        f = open('Data', 'w')
        f.write(strr)
        return students

    def modi(stud):
        try:
            f = open('Data', 'r')
            sh = f.readline()
            sh1 = ast.literal_eval(sh)
            students = sh1
            student=[]
            a=input("Enter Student ID to Edit: ")
            y=str(input('New Student Name: '))
            z=int(input('New Student Mark: '))
            student.append(y)
            student.append(z)
            if z >=50:
                student.append("Pass")
            elif z <=49:
                student.append("Fail")
            students[a]=student
            strr = str(students)
            f = open('Data', 'w')
            f.write(strr)
            return students
        except Exception:
            print('No student Data Present...')

    def del1(data):
        try:
            f = open('Data', 'r')
            sh = f.readline()
            sh1 = ast.literal_eval(sh)
            students = sh1

            id=input("Enter Student ID to delete: ")
            sh1.pop(id,"ID Doesn't Exist")
            strr = str(students)
            f = open('Data', 'w')
            f.write(strr)
            return sh1
        except Exception:
            print('No student Data Present...')

    def dele(dd):
        print('This action will delete all students Data!!!')
        d=str(input('Proceed? Y/N: '))
        if d == 'Y':
            dd = {}
            globals()['students'] = {}
            f = open('Data', 'w')
            f.write("")
            print('All students data is deleted...')
            return dd
        elif d == 'y':
            dd = {}
            globals()['students'] = {}
            f = open('Data', 'w')
            f.write("")
            print('All students data is deleted...')
            return dd
        else:
            print('List is Not deleted')

    def show(students):
        f = open('Data', 'r')
        sh = f.readline()
        try:
            sh1 = ast.literal_eval(sh)
            print()
            print("{:<8} {:<15} {:<10} {:<10}".format('ID', 'NAME', 'MARK', 'PASS?'))
            for key, value in sh1.items():
                name1, mark1, pa = value
                print("{:<8} {:<15} {:<10} {:<10}".format(key, name1, mark1, pa))
        except Exception:
            print("No student Data Present...")

class Main:
    com1=Db()
    list={}
    choice=1
    try:
        file=open('Data','x')
    except Exception:
        pass
    print('** Welcome to Students Database **\n')
    while choice != '6':
        print('\n---------------------------- \nPlease Select Your Action: '
              '\n 1: Add New Student\n 2: Show Current Students\n 3: Edit a Student\n 4: Delete a Student\n 5: Delete All Students\n 6: Exit\n')
        choice=str(input(' Selection = '))
        if choice=='1':
            list=Db.add(list)
        elif choice=='2':
            Db.show(list)
        elif choice=='3':
            list=Db.modi(list)
        elif choice=='4':
            list=Db.del1(list)
        elif choice == '5':
            delist = list
            list=Db.dele(delist)
        elif choice == '6':
            print("Good Bye")
        else:
            print('\ninvalid Selection')