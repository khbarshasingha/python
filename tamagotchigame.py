# from random import randrange

# class Pet():
# 	sounds="Meow"
# 	def __init__(self, name="kitty"):
# 		self.name=name
# 		self.hunger=randrange(10)
# 		self.boredom=randrange(10)
# 		self.sounds=self.sounds[]

# 	def clock_tick(self):

# 		self.boredom+=1
# 		self.hunger+=1

# 	def mood(self):
# 		if self.hunger<=5 and self.boredom<=6:
# 			return "happy"
# 		elif self.hunger>5 :
# 			return "hungry"
# 		else:
# 			return "bored"

# 	def __str__(self):
# 		state =" I am "+self.name+ "."
# 		state+="I am "+self.mood() + " ."
# 		return state

# 	def teach(self,word):
# 		self.sounds.append(word)
# 		self.boredom -=1

# 	def hi(self):
# 		print(self.sounds[])




# print("------------WELCOME TO TAMGOTCHI GAME------------")
# print("1. Adopt a pet [adopt <name>] \n 2. Feed the pet [feed name] \n 3.Teach the pet \n 4.Quit")
# x= int(input())
# if x==1:
# 	print("Enter the name of the pet ")
# 	name=input()
# 	
import sys
sys.setExecutionLimit(60000)

def whichone(petlist, name):
    for pet in petlist:
        if pet.name == name:
            return pet
    return None # no pet matched

def play():
    animals = []

    option = ""
    base_prompt = """
        Quit
        Adopt <petname_with_no_spaces_please>
        Greet <petname>
        Teach <petname> <word>
        Feed <petname>

        Choice: """
    feedback = ""
    while True:
        action = input(feedback + "\n" + base_prompt)
        feedback = ""
        words = action.split()
        if len(words) > 0:
            command = words[0]
        else:
            command = None
        if command == "Quit":
            print("Exiting...")
            return
        elif command == "Adopt" and len(words) > 1:
            if whichone(animals, words[1]):
                feedback += "You already have a pet with that name\n"
            else:
                animals.append(Pet(words[1]))
        elif command == "Greet" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again.\n"
                print()
            else:
                pet.hi()
        elif command == "Teach" and len(words) > 2:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.teach(words[2])
        elif command == "Feed" and len(words) > 1:
            pet = whichone(animals, words[1])
            if not pet:
                feedback += "I didn't recognize that pet name. Please try again."
            else:
                pet.feed()
        else:
            feedback+= "I didn't understand that. Please try again."

        for pet in animals:
            pet.clock_tick()
            feedback += "\n" + pet.__str__()



play()
