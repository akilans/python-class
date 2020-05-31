class Friends:
    training = "Python"

    def __init__(self, name, location):
        print("Created Instance")
        self.name = name
        self.location = location

    def get_info(self):
        return f"Friend name is {self.name} and he is in {self.location}"

    @staticmethod
    def say_hello():
        return "Hello Python"

class Bp_friends(Friends):

    company = "BP"
    
    def __init__(self,name,location,exp):
        super().__init__(name,location)
        self.experience = exp
    
    def get_info(self):
        return f"Friend name is {self.name} and he is in {self.location} and working in BP"
    

bp_fnd_1 = Bp_friends("Durga","UK",10)
print(bp_fnd_1.get_info())
print(bp_fnd_1.say_hello())
print(bp_fnd_1.experience)
print(bp_fnd_1.company)

'''
fnd_1 = Friends("Durga","UK")
fnd_2 = Friends("Gopal","India")
'''
'''
print(fnd_1.training)
print(fnd_2.training)
'''
'''
print(fnd_1.get_info())
print(fnd_2.get_info())

print(fnd_1.say_hello())
print(Friends.say_hello())
'''
