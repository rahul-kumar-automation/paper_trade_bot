class EMAStrategy:

    def __init__(self, short, long):
        self.short = short
        self.long = long

    def apply(self, data):

        data = data.copy()

        data[f"EMA{self.short}"] = data["Close"].ewm(
            span=self.short,
            adjust=False
        ).mean()

        data[f"EMA{self.long}"] = data["Close"].ewm(
            span=self.long,
            adjust=False
        ).mean()

        short_col = f"EMA{self.short}"
        long_col = f"EMA{self.long}"

        data["Signal"] = 0

        data.loc[data[short_col] > data[long_col], "Signal"] = 1
        data.loc[data[short_col] < data[long_col], "Signal"] = -1

        return data