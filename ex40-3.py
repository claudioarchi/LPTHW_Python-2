#  To see wich version of Python it's used
import sys
print(sys.executable)
print(sys.version)

# Employees names class


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (first + '.' + last + '@mail.com').lower()

    def fullname(self):
        return "%s %s" % (self.first, self.last)

    def newemail(self):
        return (self.first + '.' + self.last + '@mail.com').lower()

    def newpay(self):
        return self.pay


# emp1 is set to an instance of Employee and pass some parameters
emp1 = Employee('Claudio', 'Nunez', 35000)

print "\tGet the function from > instance < emp1 Method"
print "\t", "-" * 25, "\n"
# This will get the function named .something from the instance emp1
# and call it with self parameter
print "The employee's fullname is: %s" % emp1.fullname()
print "The employee's email is: %s" % emp1.email
print "The employee's salary is: %s$ per year" % emp1.pay, "\n"

print "\tFrom class > Employee < get the function and call it with emp1 method"
print "\t", "-" * 25, "\n"
# From class Employee get the function named .something
# and call it with parameter  beloning to instance emp1
print "The employee's fullname is: %s" % Employee.fullname(emp1)
print "The employee's email is: %s" % Employee.newemail(emp1)
print "The employee's pay is: %s$ per year" % Employee.newpay(emp1), "\n"
