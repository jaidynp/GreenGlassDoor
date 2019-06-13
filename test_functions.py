"""Test for my functions."""

import pytest 
from functions import *

##
##

    
def test_need_assistance():
    """ Tests for the 'need_assistance' function."""
    
    assert callable(need_assistance)
    assert isinstance(need_assistance('help'), bool)
    
    # Test when 'hint' is incorrectly spelled
    assert need_assistance('hifnt') == False
    
    # Test when 'hint' is correctly input
    assert need_assistance('hint') == True

    # Test when 'hint' is capitalized
    assert need_assistance('Hint') == False
    
def test_check_double_letter():
    """ Tests for the 'check_double_letter' function."""

    assert callable(check_double_letter)
    assert isinstance(check_double_letter('happy'), bool)
    
    # Test when string doesn't have double letters
    assert check_double_letter('banana') == False
    
    # Test when string does have double letters
    assert check_double_letter('apple') == True
    
    # Test for repeated numbers
    assert check_double_letter('11') == True
    
    # Test for multiple words in string
    assert check_double_letter('double letters') == True
    
def test_quit_game():
    """ Tests for the 'quit_game' function."""

    assert callable(quit_game)
    assert isinstance(quit_game('quit'), bool)
    assert quit_game('quit') == True
    
    #Test for capitalization
    assert quit_game('Quit') == False
    
def test_win_game():
    """ Tests for the 'win_game' function."""

    assert callable(win_game)
    assert isinstance(win_game(5), bool)
    
    # Test for required amount of consecutive guesses
    assert win_game(4) == False
    assert win_game(5) == True
    
def test_remove_nonalpha():
    """ Tests for the 'remove_nonalpha' function."""

    assert callable(remove_nonalpha)
    assert isinstance(remove_nonalpha('hi'), str)
    assert remove_nonalpha(';l0111') == 'l'
    
    # Test for blank input
    assert remove_nonalpha('') == ''
    
def test_check_empty_string():
    """Tests for the 'check_empty_string' function."""
    
    assert callable(check_empty_string)
    assert isinstance(check_empty_string(''), bool)
    assert check_empty_string('hi') == False
    
    # Test for blank input
    assert check_empty_string('') == True
    
def test_count_hints():
    """Tests for the 'count_hints' function."""
    
    assert callable(count_hints)
    assert isinstance(count_hints(4), bool)
    assert count_hints(5) == True
    assert count_hints(0) == False
    
def test_generate_example():
    """Tests for the 'generate_example' function."""
    
    assert callable(generate_example)
    assert isinstance(generate_example(['a','b']), str)
    assert generate_example(['dog']) == '\n> I can bring dog through the door.'
    assert generate_example(['']) == '\n> I can bring  through the door.'
    
def test_welcome_message():
    """Tests for the 'welcome_message' function."""
    
    assert callable(welcome_message)
    assert isinstance(welcome_message('a', 5, 12), str)