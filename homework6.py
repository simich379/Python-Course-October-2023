# ################################################################
# Problem 0:
# Create a class "Person" with a special method "__str__" to provide a string representation.
# Instantiate an object of this class and print it.
class Person:
    def __init__(self, name, age, ssn):
        self.name = name
        self.age = age
        self.__ssn = ssn

    def __str__(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old! "


person1 = Person("Simona", 24, 9910065554)

print(person1.__str__())


# ################################################################
# Problem 1:
# Define a class "Email" with special methods "__eq__" and "__ne__" to compare two email
# addresses. Test the equality and inequality operators with different email instances.

class Email:
    def __init__(self, email_name):
        self.email_name = email_name

    def __eq__(self, other):
        if isinstance(other, Email):
            return self.email_name == other.email_name
        return False

    def __ne__(self, other):
        if isinstance(other, Email):
            return self.email_name != other.email_name
        return False

    def __str__(self):
        return f"The email is : {self.email_name} "


email1 = Email("simona.yako@gmial.com")
email2 = Email("simonam.ilieva@gmial.com")
email3 = Email("simona.yako@gmial.com")
print(email1)
print(email2)
print(email3)
print(email1.__eq__(email2))
print(email2.__ne__(email3))
print(email3.__eq__(email1))


# ################################################################
# Problem 2:
# Create a class "Student" with private attributes for name and age. Implement getter and setter
# methods for these attributes. Demonstrate their usage.

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f"My name is {self.__name} and I am {self.__age} years old! "

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age


student1 = Student("Simona", 24)
student2 = Student("Ivan", 19)
student3 = student2

student1.set_age(23)
student2.get_name()
print(student1.get_name())
print(student2)
print(student3)
student3.set_name("Pesho")
student3.set_age(15)
print(student3)


# ################################################################
# Problem 3:
# Design a class "BankAccount" with methods for deposit, withdrawal, and balance inquiry. Use
# encapsulation to protect the account balance. Demonstrate proper usage of the class.

class BankAccount:

    def __init__(self, num_bank_account, owner, balance):
        self.__num_bank_account = num_bank_account
        self._owner = owner
        self.__balance = balance

    def set_name(self, new_owner):
        self._owner = new_owner

    def set_num_bank_account(self, new_num_bank_account):
        self.__num_bank_account = new_num_bank_account

    def set_balance(self, new_balance):
        if new_balance < 0:
            print("You have to have positive balance. Please enter a value again!")
        self.__balance = new_balance

    def get_bank_account(self):
        return self.__num_bank_account

    def get_owner_name(self):
        return self._owner

    def get_balance(self):
        return self.__balance

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.__balance += amount
        print("\n Amount Deposited: ", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.__balance >= amount:
            self.__balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Over a limit ! Insufficient balance. Please try again with less value!  ")

    def display(self):
        print("\n Net Available Balance=", self.__balance)

    def __str__(self):
        return f"The bank account {self.__num_bank_account} of {self._owner} has {self.__balance}"


banacc1 = BankAccount("34567890", "SImona", 466)
banacc1.deposit()
banacc1.display()
banacc1.withdraw()
banacc1.display()
banacc1.__str__()
# ################################################################
