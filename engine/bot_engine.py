import time
from data.data_feed import DataFeed
from strategy.ema_strategy import EMAStrategy
from execution.broker import Broker
from config.settings import SHORT_EMA, LONG_EMA, LOOP_DELAY


class BotEngine:

    def __init__(self):

        self.feed = DataFeed()
        self.strategy = EMAStrategy(SHORT_EMA, LONG_EMA)
        self.broker = Broker()

        self.last_signal = None

    def run(self):

        print("🚀 EMA Bot Started...")

        while True:

            try:

                data = self.feed.fetch()
                signals = self.strategy.apply(data)

                latest = signals.iloc[-1]

                price = float(latest["Close"])
                signal = int(latest["Signal"])

                action = self.broker.execute(signal, price)

                if signal != self.last_signal:

                    print("\n===================")
                    print(f"Price: {price}")
                    print(f"Signal: {signal}")
                    print("Action:", action)

                    self.last_signal = signal

                time.sleep(LOOP_DELAY)

            except Exception as e:
                print("Error:", e)
                time.sleep(5)