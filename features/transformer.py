

import numpy as np
import pandas as pd

from typing import Union
from abc import abstractmethod
from sklearn.base import TransformerMixin

TransformableList = Union[np.ndarray, pd.DataFrame]


class Transformer(TransformerMixin):
    """An abstract transformer for use within feature pipelines."""

    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def transform(self, X: TransformableList, y: TransformableList = None):
        """Transform the data set with the pre-fit model.

        Arguments:
            X: The set of data to transform.
            y (optional): The target output to train on.
        """
        raise NotImplementedError
