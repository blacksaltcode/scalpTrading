

import pandas as pd
import numpy as np

from typing import Union, List, Tuple
from sklearn.preprocessing import StandardScaler

from features.transformer import Transformer, TransformableList


class StandardNormalizer(Transformer):
    """A transformer for normalizing values within a feature pipeline by removing the mean and scaling to unit variance."""

    def __init__(self, columns: Union[List[str], str] = None):
        """
        Arguments:
            columns (optional): A list of column names to normalize.
        """
        self._columns = columns
        self._scaler = StandardScaler()

    def transform(self, X: TransformableList, y: TransformableList = None):
        if self._columns is None:
            return self._scaler.fit_transform(X, y)

        return self._scaler.fit_transform(X[self._columns], y)
