class student:
    '''It's example of class, object and reference variable'''

    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name

    def talk(self):
        print('Hello my Rollno is:', self.rollno)
        print('my name is:', self.name)

s = student(101,'neha')     # (student(101,'neha')==> object, (self)==> Reference variable
print(s.rollno)
print(s.name)
s.talk()

s1 = student(102, 'risha')
s1.talk()