# -*- coding: utf-8 -*-
import operator
from collections import deque


class PrefixCalc:
    prefix_input = ''
    operators = deque()
    operands = deque()
    ops = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul,
           '/': operator.div}

    def getInput(self):
        return self.prefix_input

    def setInput(self, input):
        self.prefix_input = input
        self.operators.clear()
        self.operands.clear()
        if input != '':
            for i in self.prefix_input.split(' '):
                if i in self.ops:
                    self.operators.appendleft(i)
                elif i.isdigit():
                    self.operands.append(float(i))
            check = len(self.operands) - len(self.operators)
            if check <= 0 or check > 1:
                raise ValueError

    def calculate(self):
        while self.operators:
            o = self.operators.popleft()
            one = self.operands.popleft()
            two = self.operands.popleft()
            self.operands.appendleft(self.ops[o](one, two))
        return self.operands.popleft()
