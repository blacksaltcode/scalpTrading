

import numpy as np

from typing import Union
from abc import ABCMeta, abstractmethod
from gym.spaces import Space

from trades import Trade

DTypeString = Union[type, str]
TradeActionUnion = Union[int, float, tuple]


class ActionStrategy(object, metaclass=ABCMeta):
    """An abstract strategy for determining the action to take at each timestep within a trading environment."""

    @abstractmethod
    def __init__(self, action_space: Space, dtype: DTypeString = np.float16):
        """
        Arguments:
            action_space: The shape of the actions produced by the strategy.
            dtype: A type or str corresponding to the dtype of the `action_space`. Defaults to `np.float16`.
        """

        self._action_space = action_space
        self._dtype = dtype

    @property
    def action_space(self) -> Space:
        """The shape of the actions produced by the strategy."""
        return self._action_space

    @action_space.setter
    def action_space(self, action_space: Space):
        self._action_space = action_space

    @property
    def dtype(self) -> DTypeString:
        """A type or str corresponding to the dtype of the `action_space`."""
        return self._dtype

    @dtype.setter
    def dtype(self, dtype: DTypeString):
        self._dtype = dtype

    @property
    def exchange(self) -> 'InstrumentExchange':
        """The exchange being used by the current trading environment.

        This will be set by the trading environment upon initialization. Setting the exchange causes the strategy to reset.
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange: 'InstrumentExchange'):
        self._exchange = exchange
        self.reset()

    def reset(self):
        """Optionally implementable method for resetting stateful strategies."""
        pass

    @abstractmethod
    def get_trade(self, action: TradeActionUnion) -> Trade:
        """Get the trade to be executed on the exchange based on the action provided.

        Arguments:
            action: The action to be converted into a trade.

        Returns:
            The trade to be executed on the exchange this timestep.
        """
        raise NotImplementedError
