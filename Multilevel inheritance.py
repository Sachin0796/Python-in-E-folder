# ALl the attributes will be carry forwarded to the child class which inheritate the parent class

class Dad:
    basketball = 1

class Son(Dad):

    dance=3
    def isDance(self):
        print(f"I know {self.dance} types of dance forms !!")

class GrandSon(Son):
    # pass
    dance=6
    def isDance(self):
        print(f"I know {self.dance} types of dance forms !!. Woohoo !!")

carry=Dad()
larry=Son()
harry=GrandSon()
print("Before commmenting isDance function in Grandson class")
harry.isDance()
# print("After commmenting isDance function in Grandson class")
# harry.isDance()

# print("After commmenting isDance function and dance variable in Grandson class")
# harry.isDance()
print(harry.basketball)