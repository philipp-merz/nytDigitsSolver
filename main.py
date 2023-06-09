#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 22:23:04 2023

@author: pm
"""

import random

class solver:

    def __init__(self, numbers = [0, 0, 0, 0, 0, 0], target = 0):
        self.nums = numbers

        self.numsOriginal = numbers

        self.target = target

        self.operands = ['+', '-', '*', '/']

        self.usedOperations = []


    def compute(self, availableValues):
        numbers = availableValues
        pickedNums = random.sample(numbers, 2) # pick two numbers from list


        # calculate random operation, if random operation not possible on integers (divide 10/4),
        # pick another operand

        operandNOK = True

        while operandNOK:
            operand = random.choice(self.operands)

            if operand == '+':
                result = pickedNums[0] + pickedNums[1]
                operandNOK = (False)

            elif operand == '*':
                result = pickedNums[0] * pickedNums[1]
                operandNOK = (False)

            elif operand == '-':
                result = pickedNums[0] - pickedNums[1]

                if result > 0:
                    operandNOK = False

            elif operand == '/':
                result = pickedNums[0] / pickedNums[1]

                if result % 1 == 0:
                    operandNOK = False

            else:
                raise ValueError("There was an unsupported Operator... I think")

        # add used operation to list, remove numbers, add result
        self.usedOperations.append([pickedNums[0], operand, pickedNums[1]])
        numbers.remove(pickedNums[0])
        numbers.remove(pickedNums[1])
        numbers.append(result)

        if result == self.target:
            return result
        elif len(numbers) >= 2:
            return self.compute(numbers)
        else:
            print("failed to find correct operations")
            return False

        # now check if result is number we look for, if no, return false


        return False

    def solve(self):
        success = False
        while success==False:
            numbs = []
            for el in self.nums:
                numbs.append(el)
            self.usedOperations=[]
            success = self.compute(numbs)
            print(success)

if __name__ == '__main__':
    solve = solver(numbers=[9,11,14,21,23,25], target=493)
    solve.solve()
    print("The following Operations were used:")
    print(solve.usedOperations, '/n')
    print("The following numbers are still available:")
    print(solve.nums)
