

import pandas as pd

from abc import ABCMeta, abstractmethod

from trades import Trade


class RewardStrategy(object, metaclass=ABCMeta):

    def __init__(self):
        pass

    @property
    def exchange(self) -> 'InstrumentExchange':
        """The exchange being used by the current trading environment. Setting the exchange causes the strategy to reset."""
        return self._exchange

    @exchange.setter
    def exchange(self, exchange: 'InstrumentExchange'):
        self._exchange = exchange
        self.reset()

    def reset(self):
        """Optionally implementable method for resetting stateful strategies."""
        pass

    @abstractmethod
    def get_reward(self, current_step: int, trade: Trade) -> float:
        """
        Arguments:
            current_step: The environment's current timestep.
            trade: The trade executed and filled this timestep.

        Returns:
            A float corresponding to the benefit earned by the action taken this timestep.
        """
        raise NotImplementedError()
