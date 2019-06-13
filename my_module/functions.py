"""A collection of functions for the game Green Glass Door."""

# Code Imports
import string
import random

def get_player_guess(num):
    """Asks the player to make a guess.
    
    Parameters
    ----------
    num : int
        Running total amount of times the player has made a guess
    
    Returns
    -------
    player_input : str
        The guess that is input by the player.
    """
    
    # The initial question is the same for every new game
    if num == 0:
        player_input = input(first_question) 
    # Subsequent questions are variations of the first question 
    else: 
        player_input = input(random.choice(questions))
        
    return player_input

def need_assistance(input_string):
    """Checks if player needs a hint.
    
    Parameters
    ----------
    input_string : str
        String that is input by the player.
        
    Returns 
    -------
    output_hint : boolean
        Returns whether the player has typed 'hint' or not.
    """
    
    if 'hint' in input_string:
        output_hint = True
    else:
        output_hint = False
        
    return output_hint

def check_double_letter(input_string):
    """Determines if an input string contains double letters inside of it and returns True or False.
    
    Parameters
    ----------
    input_string : str
        The guess that the player makes.
        
    Returns
    -------
    double_letter : boolean
        Returns whether the guess contains two letters in a row.
    """
    
    previous_letter = ''
    double_letter = False
    
    for letter in input_string:
        # Check equality by comparing the current letter to the previous letter
        if letter == previous_letter:
            double_letter = True
        # Update the 'previous' letter for the next iteration
        else:
            previous_letter = letter
                    
    return double_letter

def quit_game(player_input):
    """Determines if player inputs 'quit' to prematurely end the game.
    Modified from 'end_chat' method in Lecture 23 - Code Projects.
    Link: https://cogs18.github.io/materials/23-CodeProjects
    
    Parameters
    ----------
    input_string : str
        String that is input by the player.
        
    Returns
    -------
    end_game : boolean
        Returns whether to continue the game or not. 
        If TRUE, continue the game. If FALSE, end the game.
    """
    
    if 'quit' in player_input:
        end_game = True 
    else:
        end_game = False
        
    return end_game

def win_game(consecutive_streak):
    """Displays the answer to the riddle if the player is correct 5 times in a row.
    
    Parameters
    ----------
    consecutive_streak : int
        The amount of times the player has correctly guessed in a row
    
    Returns
    -------
    display_answer : boolean
        Boolean that denotes if the moderator should display the answer to the riddle.
    """
    
    # Assumes player has not yet guessed correctly 5 times in a row.
    display_answer = False
    winning_answer = 'Any word that contains double letters can go through the GREEN GLASS DOOR.'
    
    # When player does reach 5 correct guesses, updates status to show answer.
    if consecutive_streak == 5:
        display_answer = True
        print('\n> Congratulations on making 5 correct guesses in a row!' + \
             '\n> The answer to the riddle is: ' + winning_answer)

    return display_answer

def remove_nonalpha(input_string):
    """Remove all numbers and punctuation from an input string.
    
    Parameters
    ----------
    input_string : str
        The guess that is input by the player.
        
    Returns
    -------
    alpha_string : str
        The guess that is input by the player, without numbers or punctuation.
    """
    
    alpha_string = ''
    
    for character in input_string:
        # Skips over numbers and punctuation so they are not included
        if character.isalpha():
            alpha_string += character
    
    return alpha_string

def check_empty_string(input_string):
    """Determines if an input string is empty.
    
    Parameters
    ----------
    input_string : str
        The player's input guess.
    
    Returns
    -------
    empty : boolean
        TRUE if the player did not type anything, FALSE if their input is greater than 0. 
    """
    
    # Assumes status that the player's string is not empty
    empty = False
    
    # Updates status if player's string is empty
    if len(input_string) == 0:
        empty = True
        
    return empty

def get_player_name():
    """Ask player for their name.
    
    Returns
    -------
    player_input : str
        The 'name' entered by the player. 
    """
    
    player_input = input('> What is your name? \n')
    
    # Checks length of string to see if no response is given
    while check_empty_string(player_input):
        player_input = input('> Please enter your name: \n')
        
    # Uses the 'isalpha' method to ensure all characters are from the alphabet
    while not player_input.isalpha():
        player_input = input('> Letters only, please. Please enter your name: \n')
    
    return player_input.capitalize()

def get_game_length():
    """Determine the length of the game based off of player input.
    
    Returns
    -------
    game_length : int
        The amount of chances that the player has to make a guess.
        This number determines the duration of the game. 
    """
    
    game_length = 0
    my_response = ''
    
    print('\n> How much time do you have to play?' + \
          'This will determine the length of your game.\n' 
          'A. A short amount of time (15 attempts)\n' + \
          'B. A medium amount of time (25 attempts)\n' + \
          'C. A long amount of time (Indefinite attempts)\n')
    
    # Player's input choice is capitalized to maintain consistency
    player_input = input('Your choice: ').capitalize()
    
    # Checks length of string to see if no response is given
    while check_empty_string(player_input):
        my_response = input('> Please make a choice: \n')
    
    # Updates game length based off of the player's choice
    if 'A' in player_input:
        game_length = 15
    elif 'B' in player_input:
        game_length = 25
    elif 'C' in player_input:
        # -1 for indefinite game length
        game_length = -1
    else:
        print('You didn\'t choose A. or B. (10 attempts)')
        game_length = 10
        
    return game_length

def get_game_difficulty():
    """Determine the difficulty of the game: Easy, Medium, or Hard, based off of player input.
    
    Returns
    -------
    num_hints : int
        The amount of hints that will be available to the player to use throughout the game
    """

    num_hints = 0
    my_response = ''
    
    print('\n> Choose the difficulty you wish to play at.' + \
          ' This will determine the amount of hints given.\n' + \
          'A. Easy (5 hints)\n' + \
          'B. Medium (3 hints)\n' + \
          'C. Hard (2 hints)\n')
    
    player_input = input('Your choice: ').capitalize()
    
    # Checks length of string to see if no response is given
    while check_empty_string(player_input):
        my_response = input('> Please make a choice: \n')
    
    # Updates amount of available hints based off of the player's choice
    if 'A' in player_input:
        num_hints = 5
    elif 'B' in player_input:
        num_hints = 3
    else:
        num_hints = 2
        
    return num_hints

def count_hints(hints_available):
    """Keeps track of and alerts player of their remaining hints
    
    Parameters
    ----------
    hints_available : int
        The amount of hints that the player has. This amount varies with game difficulty.
        
    Returns
    -------
    hints_left : boolean
        True or False, depending on if the player has hints still available.
    """
    
    remaining_hints = hints_available
    
    # Determines if player has more than 0 hints left.
    if remaining_hints != 0:
        hints_left = True
        print('> You have ' + str(remaining_hints) + ' left.')
        # Subtracts 1 from the remaining total after a hint is given. 
        remaining_hints = remaining_hints - 1
    else:
        hints_left = False
    
    return hints_left

def generate_example(my_examples):
    """Generate a random example of an object that follows the game's rules.
    
    Parameters
    ----------
    my_examples : list
        List of possible examples stating what can and cannot go through the door.
    
    Returns
    -------
    my_example : str
        A sentence containing an example for the player. 
    """
    
    # Gets a random example from my defined list of examples
    random_example = random.choice(my_examples)
    
    # Uses the random example to construct a full sentence for the player.
    my_example = '\n> I can bring ' + random_example + ' through the door.'
    
    return my_example

def welcome_message(player_name, game_length, hint_amount):
    """Generates a Welcome Message for the player that includes instructions on how to play.
    
    Parameters
    ----------
    player_name : str
        The string representing the player's name
    game_length : int
        The amount of attempts the player has to guess
    hint_amount : int
        The amount of hints available for the player's use
    
    Returns
    -------
    welcome : str
        The welcome message that is displayed to the player, combines the parameters into sentences.
    """
    
    # If 'game length' is an integer that can be plugged into the welcome message
    if game_length > 0:
        welcome = (
            '\n> Welcome ' + player_name + '! There exists a GREEN GLASS DOOR' + \
            ' that allows only specific objects to pass through.'+ \
            '\nYou have ' + str(game_length) + ' attempts to correctly guess what you can' + \
            ' bring through the door.' + \
            '\nIf you guess correctly 5 times in a row, you can win!' + \
            '\nTo ask for a hint, type, \'hint.\' You have ' + str(hint_amount) + ' left.'
        )
    # Else, the message replaces 'str(game_length)' with 'indefinite attempts.''
    # This is because game_length, when indefinite, is equal to -1. 
    else:
         welcome = (
            '\n> Welcome ' + player_name + '! There exists a GREEN GLASS DOOR' + \
            ' that allows only specific objects to pass through.'+ \
            '\nYou have indefinite attempts to correctly guess what you can' + \
            ' bring through the door.' + \
            '\nIf you guess correctly 5 times in a row, you can win!'
            '\nTo ask for a hint, type \'hint.\' You have ' + str(hint_amount) + ' hints left.'
        )
    return welcome

# This cell defines phrases that will be used throughout the game. 
# A list of examples for objects that can and cannot go through the door.
examples = ['a pineapple, but not an orange', 'a cheeto, but not a chip', 
            'a kettle, but not a pot', 'a kitten, but not a cat', 'a stripper, but not a pole', 
            'chess, but not checkers', 'a macbook, but not a windows', 
            'a bottle, but not a cup', 'summer, but not spring', 
            'vanilla, but not chocolate', 'a hill, but not a mountain', 
            'pepper, but not salt', 'a queen, but not a king', 'a smell, but not a taste', 
            'a llama, but not a donkey', 'good, but not god', 'mommy, but not mom', 
            'Jill, but not Jane', 'Twitter, but not Instagram', 'the moon, but not the sun', 
            'a professor, but not a teacher', 'a poodle, but not a dog', 
            'pizza, but not breadsticks', 'streets, but not roads',
            'a lollipop, but not a popsicle', 'a mattress, but not a bed', 
            'glasses, but not the case', 'Harry Potter, but not Ron Weasley']

# A list of hints to give the player.
hints = ['Notice the title of the game: GREEN GLASS DOOR', 
         'Try not to focus on the relationship between objects.',
         'Look for similarities between the objects that can go through the door.', 
         'Ask yourself: What do the words of the title all contain?', 
         'Notice the spelling of the objects.']

# Questions to ask the player to make a guess.
first_question = '\n> What do you want to bring? \n'
questions = ['\n> What else do you want to bring?\n', 
             '\n> Make another guess.\n', 
             '\n> What else?\n',
             '\n> Anything else?\n', 
             '\n> Any other guesses?\n', 
             '\n> Do you have another guess in mind?\n']

# A list of phrases to respond to the player's guess.
pos_responses = ['> Yes, you can bring that!', 
                 '> Sure! You can bring that.', 
                 '> That\'ll work! You can bring that.']
neg_responses = ['> Sorry, you can\'t bring that.', 
                 '> Guess again. You can\'t bring that.']
