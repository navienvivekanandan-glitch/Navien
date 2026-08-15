#Task 2

#Task 2.1

class Room:
    def __init__(self,north_exit,south_exit,east_exit,west_exit):
        self.north_exit = north_exit
        self.east_exit = east_exit
        self.south_exit = south_exit
        self.west_exit = west_exit

    def get_exit(self,door_character):
        if door_character == 'N':
            return self.north_exit
        if door_character == 'S':
            return self.south_exit
        if door_character == 'E':
            return self.east_exit
        if door_character == 'W':
            return self.west_exit


class Start(Room):
    def __init__(self,north_exit,east_exit,south_exit,west_exit,start_text):
        self.start_text = start_text
        super().__init__(north_exit,south_exit,east_exit,west_exit)
        
    def get_message(self):
        string = ''
        if self.north_exit != -1:
            string += " There is a door to the North."
        if self.south_exit != -1:
            string += " There is a door to the South."
        if self.east_exit != -1:
            string += " There is a door to the East."
        if self.west_exit != -1:
            string += " There is a door to the West."
        return (self.start_text,"Start",string)
    
class Finish(Room):
    def __init__(self,north_exit,east_exit,south_exit,west_exit,finish_text):
        self.finish_text = finish_text
        super().__init__(north_exit,south_exit,east_exit,west_exit)

    def get_message(self):
        return (self.finish_text,"Finish")

class Normal(Room):
    def __init__(self,north_exit,east_exit,south_exit,west_exit,question,answer):
        self.question = question
        self.answer = answer
        super().__init__(north_exit,south_exit,east_exit,west_exit)

    def get_question(self):
        return self.question

    def check_answer(self,user_answer):
        if user_answer == self.answer:
            return True
        else:
            return False

    def get_message(self):
        string = ''
        if self.north_exit != -1:
            string += " There is a door to the North."
        if self.south_exit != -1:
            string += " There is a door to the South."
        if self.east_exit != -1:
            string += " There is a door to the East."
        if self.west_exit != -1:
            string += " There is a door to the West."
        return (string,"Normal")






#Task 2.2

def read_file(filename):
    file = open(filename,'r')
    room_lst = []
    for line in file:
        line = line.strip()
        line = line.split(',')
        if line[0] != 'Normal':
            room_type,North,East,South,West,message = line[0],int(line[1]),int(line[2]),int(line[3]),int(line[4]),line[5]
        else:
            room_type,North,East,South,West,question,answer = line[0],int(line[1]),int(line[2]),int(line[3]),int(line[4]),line[5],line[6]
    
        if room_type == 'Start':
            room = Start(North,East,South,West,message)
            room_lst.append(room)
        elif room_type == 'Normal':
            room = Normal(North,East,South,West,question,answer)
            room_lst.append(room)
        elif room_type == 'Finish':
            room = Finish(North,East,South,West,message)
            room_lst.append(room)
    return room_lst

room_lst = read_file('rooms.txt')
for line in room_lst:
    print(line.get_message())


#Task 2.3
def play_game(room_lst):

    current_room = 0

    while True:

        room = room_lst[current_room]

        message = room.get_message()
        print(message)

        if message[1] == "Finish":
            break

        Valid = False

        while Valid == False:
            guess = input('Enter a valid door to go through: ')

            if guess == 'N' or guess == 'E' or guess == 'S' or guess == 'W':
                next_room = room.get_exit(guess)

                if next_room != -1:
                    Valid = True

        current_room = next_room

        room = room_lst[current_room]

        message = room.get_message()
        print(message)

        if message[1] == "Finish":
            break

        question = room.get_question()
        print(question)

        Valid = False

        while Valid == False:
            user_guess = input('Enter your answer to the question: ')

            if room.check_answer(user_guess) == True:
                Valid = True

print(play_game(room_lst))












    
