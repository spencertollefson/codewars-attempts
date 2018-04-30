"""
https://www.codewars.com/kata/57fb44a12b53146fe1000136/train/python
2018-04-30 Fri
Description:
Each exclamation mark weight is 2; Each question mark weight is 3. Put two string left and right to the balance, Are they balanced?

If the left side is more heavy, return "Left"; If the right side is more heavy, return "Right"; If they are balanced, return "Balance".
"""

def balance(left: str, right: str) -> str:
    weight_left = left.count("?") * 3 + left.count("!") * 2
    weight_right = right.count("?") * 3 + right.count("!") * 2
    if weight_left == weight_right:
        return "Balance"
    elif weight_left > weight_right:
        return "Left"
    else:
        return "Right"

#Tests
def test_blank():
    assert balance("", "") == "Balance"

def test_1():
    assert balance("!!", "??") == "Right"

def test_2():
    assert balance("!??", "?!!") == "Left"

def test_3():
    assert balance("!?!!", "?!?") == "Left"

def test_4():
    assert balance("!!???!????", "??!!?!!!!!!!") == "Balance"

if __name__== "__main__":
    print(balance("!!???!????", "??!!?!!!!!!!"))
    print(balance("!??", "?!!"))
