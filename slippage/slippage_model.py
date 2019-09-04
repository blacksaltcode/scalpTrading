

from abc import ABCMeta, abstractmethod

from trades import Trade


class SlippageModel(object, metaclass=ABCMeta):
    """A model for simulating slippage on an exchange trade."""

    def __init__(self):
        pass

    @abstractmethod
    def fill_order(self, trade: Trade, **kwargs) -> Trade:
        """Simulate slippage on a trade ordered on a specific exchange.

        Arguments:
            trade: The trade executed on the exchange.
            **kwargs: Any other arguments necessary for the model.

        Returns:
            A filled `Trade` with the `price` and `amount` adjusted for slippage.
        """

        raise NotImplementedError()
