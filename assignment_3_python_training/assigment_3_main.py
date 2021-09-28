from assigment_3_fuctions import whichone,category,Pet


def play():
    animals = []
    option = ''
    disclaimer = """
        Ignore the < > symbols
        For Adopting or adding, type --> adopt <pet_name> <category of pet, now available are [Dog,Bird,Cat]>
        For Greeting, type --> greet <pet_name>
        For Teaching, type --> teach <pet_name> <word you want to teach>
        For Feeding,  type  --> feed <pet_name>
        For Quiting,  type  --> quit

        Choice: """
    out = ""

    while True:
        action = input(out + '\n' + disclaimer)
        out = ''

        inputs = action.split()
        l = len(inputs)
        if l > 0:
            decisions = inputs[0]
        else:
            decisions = None
        if decisions == 'quit':
            print('Visit Again!')
            exit()
        elif decisions == 'adopt' and l > 1:
            if whichone(animals, inputs[1]):
                out += 'Sorry you already have a pet with same name\n'
            else:
                if l > 2:
                    cato = category(
                        inputs[2])  # to check if it belong to any category of classes which were defined before
                else:
                    cato = Pet

                animals.append(cato(inputs[1]))
        elif decisions == 'greet' and l > 1:
            pet = whichone(animals, inputs[1])
            if not pet:
                out += 'This pet name is not familiar, try again\n'
                print()
            else:
                pet.hi()

        elif decisions == 'feed' and l > 1:
            pet = whichone(animals, inputs[1])
            if not pet:
                out += 'This pet name is not familiar, try again\n'
            else:
                pet.feed()

        elif decisions == "teach" and l > 2:
            pet = whichone(animals, inputs[1])
            if not pet:
                out += 'This pet name is not familiar, try again\n'
            else:
                pet.teach(inputs[2])

        else:
            out += 'not recognizable, try again\n'

        for pet in animals:
            pet.clock_tick()
            out += '\n' + pet.__str__()

if __name__ == '__main__':
    play()

