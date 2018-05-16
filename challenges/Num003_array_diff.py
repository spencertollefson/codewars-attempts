#!/usr/bin/env python
# coding=utf-8
"""
Created on 15-May-18
Author: Spencer Tollefson
Num003_array_diff.py
Description:
Codewars challenge
https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
6kyu
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b.
"""


def array_diff(a, b):
    for i in b:
        if i in a:
            while i in a:
                a.remove(i)
    return a

# Tests

def test_1():
    assert array_diff([1, 2], [1]) == [2], "a was [1,2], b was [1], expected [2]"

def test_2():
    assert array_diff([1, 2, 2], [1]) == [2, 2], "a was [1,2,2], b was [1], expected [2,2]"
def test_3():
    assert array_diff([1, 2, 2], [2]) == [1], "a was [1,2,2], b was [2], expected [1]"
def test_4():
    assert array_diff([1, 2, 2], []) == [1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]"
def test_5():
    assert array_diff([], [1, 2]) == [], "a was [], b was [1,2], expected []"