

import numpy as np

from slippage import SlippageModel
from trades import Trade, TradeType


class RandomSlippageModel(SlippageModel):
    "A uniform random slippage model."

    def __init__(self, max_price_slippage_percent: float = 3.0, max_amount_slippage_percent: float = 0.0):
        """
        Arguments:
            max_price_slippage_percent: The maximum random slippage to be applied to the fill price. Defaults to 3.0 (i.e. 3%).
            max_amount_slippage_percent: The maximum random slippage to be applied to the fill amount. Defaults to 0.
        """
        self.max_price_slippage_percent = max_price_slippage_percent
        self.max_amount_slippage_percent = max_amount_slippage_percent

    def fill_order(self, trade: Trade, current_price: float) -> Trade:
        amount_slippage = np.random.uniform(0, self.max_amount_slippage_percent / 100)
        price_slippage = np.random.uniform(0, self.max_price_slippage_percent / 100)

        fill_amount = trade.amount * (1 - amount_slippage)
        fill_price = current_price

        if trade.trade_type is TradeType.MARKET_BUY:
            fill_price = current_price * (1 + price_slippage)
        elif trade.trade_type is TradeType.LIMIT_BUY:
            fill_price = current_price * (1 + price_slippage)

            if fill_price > trade.price:
                fill_price = trade.price
                fill_amount *= trade.price / fill_price

        elif trade.trade_type is TradeType.MARKET_SELL:
            fill_price = current_price * (1 - price_slippage)
        elif trade.trade_type is TradeType.LIMIT_SELL:
            fill_price = current_price * (1 - price_slippage)

            if fill_price < trade.price:
                fill_price = trade.price
                fill_amount *= fill_price / trade.price

        return Trade(trade.symbol, trade.trade_type, amount=fill_amount, price=fill_price)
