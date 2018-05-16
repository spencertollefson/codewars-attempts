"""
https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
2018-05-14 Mon
Description:

In this kata you are required to, given a string, replace every letter with
its position in the alphabet. If anything in the text isn't a letter,
ignore it and don't return it.

a being 1, b being 2, etc.
"""


def alphabet_position(text: str) -> str:
    text = text.lower()
    letters_only = ""
    for i in text:
        if i.isalpha():
            letters_only += i
    position_list = ''
    for i in letters_only:
        position_list += " " + str((ord(i) - ord('a') + 1))
    return position_list.strip()


if __name__== "__main__":
    print("Let's see how this goes: Here are the answers:")
    print(alphabet_position("cat!juice a&d SYRUP"))




#Tests
def test_1():
    assert alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

def test_2():
    assert alphabet_position("The narwhal bacons at midnight.") == "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"