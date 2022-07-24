students = {}
class Db:

    def add(stud):
        students=stud
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
        return students

    def modi(stud):
        students=stud
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
        return students

    def del1(data):

        id=input("Enter Student ID to delete: ")
        data.pop(id,"ID Doesn't Exist")
        return data

    def dele(dd):

        print('This action will delete all students Data!!!')
        d=str(input('Proceed? Y/N: '))
        if d == 'Y':
            dd = {}
            globals()['students'] = {}
            return dd
        else:
            print('List is Not deleted')

    def show(students):

        print()
        print("{:<8} {:<15} {:<10} {:<10}".format('ID', 'NAME', 'MARK', 'PASS?'))

        for key, value in students.items():
            name1, mark1, pa = value
            print("{:<8} {:<15} {:<10} {:<10}".format(key, name1, mark1, pa))

class Main:
    com1=Db()
    list={}
    choice=1
    print('** Welcome to Students Database **\n')
    while choice != 6:
        print('\n---------------------------- \nPlease Select Your Action: '
              '\n 1: Add New Student\n 2: Show Current Students\n 3: Edit a Student\n 4: Delete a Student\n 5: Delete All Students\n 6: Exit\n')
        choice=int(input(' Selection = '))
        if choice==1:
            list=Db.add(list)
        elif choice==2:
            Db.show(list)
        elif choice==3:
            list=Db.modi(list)
        elif choice==4:
            list=Db.del1(list)
        elif choice == 5:
            print(list)
            delist = list
            list=Db.dele(delist)
        elif choice == 6:
            print("Good Bye")
        else:
            print('\ninvalid Selection')