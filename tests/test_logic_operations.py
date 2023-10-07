# -*- coding:utf-8 -*-
# author : duqi


from src.logic_operations.logic_operations import logical_and, logical_or, logical_not

def test_logical_and():
    assert logical_and(True, True) == True
    assert logical_and(True, False) == False
    assert logical_and(False, False) == False

def test_logical_or():
    assert logical_or(True, True) == True
    assert logical_or(True, False) == True
    assert logical_or(False, False) == False


def test_logical_not():
    assert logical_not(True) == False
    assert logical_not(False) == True

def test_not_and():
    assert logical_and(logical_not(True), False) == False