

import pandas as pd
import numpy as np

from typing import Union, List, Tuple
from sklearn.preprocessing import MinMaxScaler

from features.transformer import Transformer, TransformableList


class MinMaxNormalizer(Transformer):
    """A transformer for normalizing values within a feature pipeline by the column-wise extrema."""

    def __init__(self, feature_range: Tuple[int, int] = (0, 1), columns: Union[List[str], str] = None):
        """
        Arguments:
            feature_range (optional): A tuple containing the new `(minimum, maximum)` values to scale to.
            columns (optional): A list of column names to normalize.
        """
        self._columns = columns
        self._scaler = MinMaxScaler(feature_range=feature_range)

    def transform(self, X: TransformableList, y: TransformableList = None):
        if self._columns is None:
            return self._scaler.fit_transform(X, y)

        return self._scaler.fit_transform(X[self._columns], y)
