import datetime

from tkinter import *
from entities import Classroom
from entities import Cls
from entities import Groupes
from entities import Users
from entities import Biometrics
from entities import PartOfDay

first_monday = datetime.date(2020,8,31)

def add_class():
    cls = Cls.Cls()
    cls.classRegistration()

def add_classroom():
    classroom = Classroom.Classroom()
    classroom.classroomRegistration()

def add_group():
    group = Groupes.Groupes()
    group.groupRegistration()

def add_user():
    user = Users.Users()
    user.userRegistration()
    user.insertUserIntoDatabase()
    user.getUserID()
    bio = Biometrics.Biometrics()
    bio.biometricsRegistration(user.userID)

def add_part_of_day():
    part_of_day = PartOfDay.PartOfDay()
    part_of_day.partOfDayRegistration()
    part_of_day.insertPartOfDayIntoDatabase(first_monday)

def Registration():
    root2 = Tk()
    root2.title("Face recognition in Python Registration")
    root2.geometry("400x200")

    Button(root2, text="Add class", command=add_class).pack()
    Button(root2, text="Add classroom", command=add_classroom).pack()
    Button(root2, text="Add group", command=add_group).pack()
    Button(root2, text="Add user", comman=add_user).pack()
    Button(root2, text="Add part of day", command=add_part_of_day).pack()

    root2.mainloop()

