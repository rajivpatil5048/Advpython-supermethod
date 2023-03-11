# supermethod:= It is used to call parent method.
#=============  The super() function is used to give access to methods and properties of a parent
#               or sibling class.

class Rajiv:
    def m1(self):
        print('This is from Rajiv')
class Patil(Rajiv):
    def m1(self):
        super().m1()
        print('This is also from Patil')

obj=Patil()
obj.m1()


class Personal_details:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print('Name::',self.name)
        print('Age::',self.age)

class Emp(Personal_details):
    def __init__(self,name,age,sal,id):
        super().__init__(name,age)
        self.sal = sal
        self.id = id

    def show(self):
        super().show()
        print('Sal::', self.sal)
        print('ID::', self.id)

class student(Personal_details):
    def __init__(self,name,age,batch,sport):
        super().__init__(name,age)
        self.batch=batch
        self.sport=sport

    def show(self):
        super().show()
        print('Batch::',self.batch)
        print('Sport::',self.sport)

obj=student('Rajiv',27,16,'Badminton')
obj.show()
obj=Emp('Rohini',25,80000,5048)
obj.show()
