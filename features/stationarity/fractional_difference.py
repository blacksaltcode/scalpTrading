
#
# Reference Source: https://towardsdatascience.com/preserving-memory-in-stationary-time-series-6842f7581800

import pandas as pd
import numpy as np

from typing import Union, List, Tuple

from features.transformer import Transformer, TransformableList


class FractionalDifference(Transformer):
    """A transformer for differencing values within a feature pipeline by a fractional order."""

    def __init__(self, columns: Union[List[str], str] = None, lag_cutoff: int = 0, difference_order: float = 0.5):
        """
        Arguments:
            columns (optional): A list of column names to normalize.
        """
        self._columns = columns
        self._lag_cutoff = lag_cutoff
        self._difference_order = difference_order

    def _weights(self):
        weights = [1]

        for k in range(1, self._lag_cutoff):
            weights.append(-weights[-1] * ((self._difference_order - k + 1)) / k)

        weights = np.array(weights).reshape(-1, 1)

        return weights

    def _difference(self, column: Union[int, str]):
        weights = self._weights()
        res = 0

        for k in range(self._lag_cutoff):
            res += weights[k] * column.shift(k).fillna(0)

        return res[self._lag_cutoff:]

    def transform(self, X: TransformableList):
        columns = self._columns

        if columns is None:
            columns = X.columns if hasattr(X, 'columns') else range(len(X))

        for column in columns:
            X[column] = self._difference(X[column])

        return X
