from fizzbuzz import Fizzbuzz

def test_says_fizz():
    fb = Fizzbuzz.says(3)
    assert fb == 'fizz'

def test_says_buzz():
    fb = Fizzbuzz.says(5)
    assert fb == 'buzz'

def test_says_fizzbuzz():
    fb = Fizzbuzz.says(15)
    assert fb == 'fizzbuzz'

def test_says_number():
    fb = Fizzbuzz.says(2)
    assert fb == 2
