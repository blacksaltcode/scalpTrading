

from enum import Enum


class TradeType(Enum):
    """A trade type for use within trading environments."""

    HOLD = 0
    LIMIT_BUY = 1
    MARKET_BUY = 2
    LIMIT_SELL = 3
    MARKET_SELL = 4

    @property
    def is_hold(self) -> bool:
        """
        Returns:
            Whether the trade type is non-existent (i.e. hold).
        """
        return self == TradeType.HOLD

    @property
    def is_buy(self) -> bool:
        """
        Returns:
            Whether the trade type is a buy offer.
        """
        return self == TradeType.MARKET_BUY or self == TradeType.LIMIT_BUY

    @property
    def is_sell(self) -> bool:
        """
        Returns:
            Whether the trade type is a sell offer.
        """
        return self == TradeType.MARKET_SELL or self == TradeType.LIMIT_SELL
