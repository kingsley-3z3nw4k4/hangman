class Human():
    def __init__(self,name,age,gender='',status='Single',spouse='',spousetyp=''):
        self.name = name
        self.age = age
        self.status = status
        self.gender = gender
        self.spousetyp = spousetyp

    def bio(self): #polymorphism
        if (self.status == 'Married'):
            print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Status: {self.status}, {self.spousetyp}'s name: {self.spouse.name}")
        elif (self.gender != ''):
            print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Status: {self.status}")
        else:
            print(f"Name: {self.name}, Age: {self.age}, Status: {self.status}")

    def weds(self,spouse): #encapsulation(?)
        self.status = 'Married'
        self.spouse = spouse

def marriage(bride=Human, groom=Human): #abstraction
    bride.weds(groom)
    groom.weds(bride)
    print(f"\n{bride.name} weds {groom.name}! Happy Wedluck!!\n")

class Man(Human): #inheritance
        def __init__(self,name,age,gender='Male',status='Single',spouse='',spousetyp='Wife'):
            self.name = name
            self.age = age
            self.status = status
            self.gender = gender
            self.spousetyp = spousetyp

class Woman(Human):#inheritance
        def __init__(self,name,age,gender='Female',status='Single',spouse='',spousetyp='Husband'):
            self.name = name
            self.age = age
            self.status = status
            self.gender = gender
            self.spousetyp = spousetyp

human1 = Man('John Doe',35)
human2 = Woman('Mary Lyn', 33)
print("Bio:")
human1.bio()
human2.bio()

do_marriage = input(f"\nDo {human1.name} and {human2.name} fall in love and get married? Y/N...").lower()

marriage(human1,human2)

print("New Bio:")
human1.bio()
human2.bio()
