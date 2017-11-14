# Create the class so the quizzes work
class Questions:
    def __init__(self, question, a1, a2, a3, a4, answer):
        self.__question = question
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3
        self.__a4 = a4
        self.__answer = answer

    def set_questions(self, question):
        self.__question = question

    def set_a1(self, a1):
        self.__a1 = a1

    def set_a2(self, a2):
        self.__a2 = a2

    def set_a3(self, a3):
        self.__a3 = a3

    def set_a4(self, a4):
        self.__a4 = a4

    def set_answer(self,answer):
        self.__answer = answer

    def get_question(self):
        return self.__question

    def get_a1(self):
        return self.__a1

    def get_a2(self):
        return self.__a2

    def get_a3(self):
        return self.__a3

    def get_a4(self):
        return self.__a4

    def get_answer(self):
        return self.__answer

# Now Lets Start the game
def main():
    print('Oh Goody two new mortals are here to play a new game, you know i love games as much as i love CHEESE!')
    q0 = Questions('Who was the man that conquered all of tameriel?',
            'a: Tiber Septim',
            'b: Reymond Cyrodiil',
            'c: Umbriel the unfeathered',
            'd: Titus Mede II',
            'a')
    q1 = Questions('How many daedric princes are their after Oblivion?',
         'a: 12',
         'b: 8',
         'c: 16',
         'd: 17',
         'd')
    q2 = Questions('What are the three clans in the elder scrolls online?',
        "a: Ebonheart, Aldmeri dominion, Daggerfall Convenant",
        "b: Daerdric, Aerdra, Imperial', ",
        "'c: Dwarven, Snow elves, Nords', ",
        'd: Deep Ones, Dark Brotherhood, Morang tong', 'a')
    q3 = Questions('Who is SHOR?',

         'a: Azura',
         'b: Lorkhan',
         'c: Akotash',
         'd: Boethia',
         'b')

    q4 = Questions('Which daedric prince is the youngest?',

         'a: Azura',
         'b: Sheogorath',
         'c: Malacath',
         'd: Naemeria',
                  'b')

    q5 = Questions('What is the afterlife to the nords?',
                  'a: skyrim',
                  'b:ashlands',
                   'c: Sovngarde',
                  'd: Shivering Isles',
                  'c')
    q6 = Questions('What does Aerdra mean?',
                  'a: of our end time',
                  'b: of our ancestors',
                  'c: not of our ancestors',
                  'd: of our time begins',
                  'b')
    q7 = Questions('How many continents are in tamerial?',
                  'a: 7',
                  'b: 11',
                  'c: 9',
                  'd: 8',
                  'c')
    q8 = Questions('Who loves CHEESE?',
                  'a: SHEOGORATH',
                  'b: Haskill',
                  'c: Talos',
                  'd: Martin',
                  'a')
    q9 = Questions('What is the most recent war in the elder scrolls series',
                  'a: The Great War',
                  'b: The Civil War',
                  'c: The Slave Rebbellion',
                  'd: the oblivion crisis',
                  'a')
    # Make Counter for Player and get their names
    player1 = input('Whats your name first mortal: ')
    player_1 = 0
    player2 = input('And you other mortal you know what im gonna ask: ')
    player_2 = 0
    # Put questions in set since its easier
    set_1 = [q1, q3, q5, q7, q9]
    set_2 = [q0, q2, q4, q6, q8]
    # time to have fun and go through my quiz
    print(player1)
    for quest in set_1:
        print('\n')
        print(quest.get_question())
        print(quest.get_a1())
        print(quest.get_a2())
        print(quest.get_a3())
        print(quest.get_a4())
        guess = input('Guess the answer: ')
        if guess.lower() == quest.get_answer():
            print('Congrats your right')
            player_1 += 1
        else:
            print('WRONG!!, now to punish you puny mortal.')
            player_1 -= 1
    print('You', player1,  'Earned: ' + str(player_1), 'points')

    print(player2)
    for quest in set_2:
        print('\n')
        print(quest.get_question())
        print(quest.get_a1())
        print(quest.get_a2())
        print(quest.get_a3())
        print(quest.get_a4())
        guess = input('Guess the answer: ')
        if guess.lower() == quest.get_answer():
            print('Congrats your right')
            player_2 += 1
        else:
            print('WRONG!!, now to punish you puny mortal.')
            player_2 -= 1
    print('You', player2, 'Earned: ' + str(player_2), 'points')
    # To Compare scores and see which mortal dies
    print(' Now which of you mortals die!')
    if player_1 > player_2:
        print('the first one wins by', player_1 - player_2,  'scores, time to end you pathetic mortal life second thing.')
        print(player2, 'has been executed')
    elif player_1 == player_2:
        print('Well great no one gets killed they both tied, well actually lets just kill both.')
        print(player1, ' and', player2, 'have been executed')

    else:
        print('The Second one won well that is not much of a surprise', player_1 - player_2, 'scores, lets just kill the first one already.')
        print(player1, 'has been executed')



main()
