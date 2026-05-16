import pandas as pd

class Portfolio:

    def __init__(self):
        self.equity = []
        self.cash = 100000
        self.position = 0

    def update(self, price, signal):

        if signal == 1:
            self.position = 1

        elif signal == -1:
            self.position = -1

        value = self.cash + (self.position * price * 1)

        self.equity.append(value)

        return self.equity