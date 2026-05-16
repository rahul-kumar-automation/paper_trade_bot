class Broker:

    def __init__(self):
        self.position = 0  # 1 long, -1 short, 0 flat

    def execute(self, signal, price):

        if signal == 1 and self.position != 1:
            self.position = 1
            return f"BUY @ {price}"

        elif signal == -1 and self.position != -1:
            self.position = -1
            return f"SELL @ {price}"

        return "HOLD"