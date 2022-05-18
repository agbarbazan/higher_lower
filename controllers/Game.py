from game_data import data
from random import randint
import os
import art
import re

def a_or_an(str):
    first_letter = str.lower()[0]
    return 'an' if re.search("[aeiou]", first_letter) else 'a'


class Game:
    def __init__(self):
        self.score = 0
        self.choices = []
        self.user_choice = None
        self.correct_answer = None
        self.game_over = False

    def set_choices(self, game_data):
        a = game_data[randint(0,len(game_data) - 1)]
        game_data.remove(a)
        b = game_data[randint(0,len(game_data) - 1)]
        self.choices = [a,b]
    
    def set_correct_answer(self):
        a = self.choices[0]['follower_count']
        b = self.choices[1]['follower_count']
        self.correct_answer = 'A' if a > b else 'B' 
    
    def get_user_input(self):
        self.user_choice = input("Who has more followers? Type 'A' or 'B': ")

    def compare(self):
        if self.user_choice == self.correct_answer:
            self.score += 1
            return False
        else:
            return True

    def game_round(self):
           self.set_choices(data)
           self.set_correct_answer()

    def clear_console(self):
        os.system('cls')
           
    def play_game(self):
        while not self.game_over:
            if self.score > 0:
                print(f"You're right! Current score:{self.score}\n")  
            
            self.game_round()
            a = self.choices[0]
            b = self.choices[1]
            print(f"Compare A: {a['name']}, {a_or_an(a['description'])} {a['description']}, from {a['country']}.")
            print(f"{art.vs}\n")
            print(f"Compare B: {b['name']}, {a_or_an(b['description'])} {b['description']}, from {b['country']}.")
            self.get_user_input()
            self.game_over = self.compare()
        self.clear_console()
        print(f"Sorry, that's wrong. Final score: {self.score}")
