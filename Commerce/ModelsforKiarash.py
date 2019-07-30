class Business:
    def __init__(self, title = None, description = None, address = None, employees = None):
        falseTitle = None
        falseDescription = None
        falseAdress = None
        noTitle = False
        noAddress = False
        noDescription = False
        notEmployee = None
        error = False
        errorMessage = ""
        notEmployee = None
        self.employees = []
        if title == None:
            noTitle = True
        elif isinstance(title,str):
            self.title = title
        else:
            falseTitle = str(type(title))
        if description == None:
            noDescription = True
        elif isinstance(description,str):
            self.description = description
        else:
            falseDescription = str(type(description))
        if address == None:
            noAddress = True
        elif isinstance(address,str):
            self.address = address
        else:
            falseAdress = str(type(address))
        if isinstance(employees, list):
            for employee in employees:
                if isinstance(employee,str):
                    self.employees.append(employee)
                else:
                    notEmployee = str(type(employee))
        elif isinstance(employees,str):
            self.employees.append(employees)
        elif not employees == None:
            notEmployee = str(type(employees))
        if noTitle is True:
            error = True
            errorMessage = errorMessage + "no param passed for title\n"
        if isinstance(falseTitle,str):
            error = True
            errorMessage = errorMessage + "param title requires a str, you passed : " + falseTitle + "\n"
        if noDescription is True:
            error = True
            errorMessage = errorMessage + "no param passed for description\n"
        if isinstance(falseDescription, str):
            error = True
            errorMessage = errorMessage + "param for description requires a str, you passed : " + falseDescription + "\n"
        if noAddress is True:
            error = True
            errorMessage = errorMessage + "no param passed for address\n"
        if isinstance(falseAdress,str):
            error = True
            errorMessage = errorMessage + "param for adress requires a str, you passed : " + falseAdress + "\n"
        if isinstance(notEmployee,str):
            error = True
            errorMessage = errorMessage + "param for employees contains a bad type. str expected, you passed : " \
                           + notEmployee +"\n"
        if error is True:
            raise Exception("Here are your problems \n" + errorMessage)

    def resetTitle(self,newTitle = None):
        if isinstance(newTitle,str):
            print(self.title + " has been overwritten to " + newTitle)
            self.title = newTitle
        else:
            raise Exception(" Method param requires a str, you passed :",str(type(newTitle)))

    def resetDescription(self,newDescription = None):
        if isinstance(newDescription,str):
            print(self.description + " has been overwritten to " + newDescription)
            self.description = newDescription
        else:
            raise Exception("Method param requires a str, you passed : " + str(type(newDescription)))

    def resetAdress(self, newAddress = None):
        if isinstance(newAddress,str):
            print(self.address + " has been overwritten to " + newAddress)
            self.address = newAddress
        else:
            raise Exception('Method param requires a str, you passed : ' + str(type(newAddress)))

    def addEmployees(self,employees = None):
        if isinstance(employees,str):
            self.employees.append(employees)
        elif isinstance(employees,list):
            for employee in employees:
                if isinstance(employee,str):
                    print(employee + " appended to employee list")
                    self.employees.append(employee)
                else:
                    raise Exception("param list requires str types, you passed: ",str(type(employee)))
        else:
            raise Exception("param required str or list, you passed: ",str(type(employees)))

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def getAdress(self):
        return self.address

    def findEmployee(self,employee = None):
        if isinstance(employee,str):
            if self.employees.__contains__(employee):
                return True
            else:
                return False
        else:
            raise Exception("Param requires str, you passed: ",str(type(employee)))

    def getEmployees(self):
        self.employees.sort()
        return self.employees

    def getNumEmployees(self):
        return len(self.employees)

    def toString(self):
        string = self.title + "\n" + self.description + "\n" + self.address
        stringlist = ""
        for each in self.employees:
            stringlist = stringlist + ("\n" + each)
        string = string + stringlist
        return string



if __name__ == "__main__":
    breaker = 11
    newClass = Business("Dick","Sporting Goods","Baton Rouge,LA",["Dick Dickerson","Andy Anderson"])
    print(newClass.toString())
    newTitle = "Dick's Sporting Goods"
    newClass.resetTitle(newTitle)
    newDescription = "Sporting Goods and Hunting Supplies Store"
    newClass.resetDescription(newDescription)
    newAddress = "9330 Mall of Louisiana Blvd Suite 200, Baton Rouge, LA 70809"
    newClass.resetAdress(newAddress)
    Richard = "Richard Richardson"
    newClass.addEmployees(Richard)
    emplist = ["Dave Davidson" 'Davers Daverson','Chris Christopherson']


