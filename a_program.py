"""
 Matthew Janzen
 Module 08 Lab Assignment
 Part B
 
 This program simulates a football game's score, but it's really here to be
 committed to a repo.
"""

print("This is a change that I will commit to the repo")

class FootballGame:
    def __init__(self):
        self.__location = 'Avondale'
        self.__home_score = 0
        self.__away_score = 0
    
    def get_location(self):
        return self.__location

    def get_home_score(self):
        return self.__home_score
    
    def get_away_score(self):
        return self.__away_score
    
    def touchdown_home(self):
        self.__home_score += 6
    
    def touchdown_away(self):
        self.__away_score += 6
    
    def field_goal_home(self):
        self.__home_score += 3
    
    def field_goal_away(self):
        self.__away_score += 3
    
    def conversion_home(self):
        self.__home_score += 2
    
    def conversion_away(self):
        self.__away_score += 2
    
    def safety_home(self):
        self.__home_score += 2
    
    def safety_away(self):
        self.__away_score += 2
    
    def extra_point_home(self):
        self.__home_score += 1
    
    def extra_point_away(self):
        self.__away_score += 1
    
    def print_game_info(self):
        print(self.__location)
        print(self.__home_score)
        print(self.__away_score)

game = FootballGame()

game.print_game_info()

game.touchdown_home()
game.extra_point_home()

game.print_game_info()

game.field_goal_away()

game.print_game_info()

game.safety_home()
game.touchdown_away()

game.print_game_info()

game.conversion_away()
game.field_goal_home()

game.print_game_info()