class Teams:
    def __init__(self, members):
        self.__myTeam = members

    def __len__(self):
        return len(self.__myTeam)

    def __contains__(self, member):
        return member in self.__myTeam

    def __iter__(self):
        return iter(self.__myTeam)

def main():
    classmates = Teams(['John', 'Steve', 'Tim'])
    print (len(classmates))
    
    # Will print True if __len__ is implemented
    print("is __len__ implemented? "+str(hasattr(classmates, '__len__')))  

    # Checking if 'Tim' and 'Sam' are part of our team
    print("Is Tim part of our team? "+str('Tim' in classmates))  
    print("Is Sam part of our team? "+str('Sam' in classmates))

    # Printing each member of the classmates object
    for member in classmates:
        print(member)

main()
