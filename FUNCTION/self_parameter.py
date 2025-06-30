#Using self parameter:

class Employee:
    language='english'
    salary=10000

    def getInfo(self):
        print(f"the language is{self.language}.the salary is{self.salary}")

abc=Employee()
abc.getInfo()
