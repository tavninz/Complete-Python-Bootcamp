class Run:
    def runner(self):
        print("Animal can run!!!")

class Fly:
    def flyer(self):
        print("Animal can Fly!!!")

class Both(Run,Fly):
    def boths(self):
        print("Animal can fly and run!!!")


airplane = Both()
airplane.boths()
airplane.runner()
airplane.flyer()




class MonthExam:
    def AverageMonth(self,score=0,subject=0):
        return score / subject

class YearExam:
    def AverageYear(self,monthScore=0,subject=0):
        return monthScore / subject


class Student(MonthExam,YearExam):
    def showInfo(self,AverageMonth,AverageYear):
        print("Your Month Score = {} and Final Year Score = {}".format(AverageMonth,AverageYear))

student1 = Student()
month = student1.AverageMonth(100,5)
year = student1.AverageYear(50,2)

student1.showInfo(month,year)
