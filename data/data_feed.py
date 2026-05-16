import yfinance as yf
import pandas as pd
from config.settings import SYMBOL, INTERVAL, LOOKBACK


class DataFeed:

    def fetch(self):

        data = yf.download(
            SYMBOL,
            period=LOOKBACK,
            interval=INTERVAL,
            progress=False
        )

        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)

        return data