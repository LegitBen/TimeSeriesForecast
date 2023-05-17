import pickle
import datetime
from typing import List
import pandas as pd
from abc import ABC, abstractmethod
class PricePredictor(ABC):
    def __init__(self, model_name) -> None:

        with open (f"models/fbmodel.bin", "rb",) as fin:
            try:
                self.model = pickle.load(fin)
            except (OSError, FileNotFoundError, TypeError):
                print("wrong path/ model not available")
                exit(-1)


def calculate_next_date(self, prev_date):

        self.next_date = datetime.datetime(
            *list(map(lambda x: int(x), prev_date.split("-")))
        ) + datetime.timedelta(
            days=1
        )  # next date


def get_next_date(self, prev_date):
        try:
            return self.next_date.strftime("%y-%m-%d")
        except NameError:
            self.calculate_next_date(prev_date)
@abstractmethod
def predict(self, prev_date) -> List:
        pass
@abstractmethod
def preprocess_inputs(self, prev_date):
        pass
@abstractmethod
def postprocess_outputs(self, output_from_model) -> List:
        pass


class FBProphetPredictor(PricePredictor):
    def get_next_date(self, prev_date):
        try:
            return self.next_date.strftime("%y-%m-%d")
        except NameError:
            self.calculate_next_date(prev_date)
    def calculate_next_date(self, prev_date):

        self.next_date = datetime.datetime(
            *list(map(lambda x: int(x), prev_date.split("-")))
        ) + datetime.timedelta(
            days=1
        )  #
    def __init__(self,) -> None:

        super().__init__("fbprophet")

    def preprocess_inputs(self, prev_date):

            self.calculate_next_date(prev_date)  # get the self.next_date var
            next_date_series = pd.DataFrame(
                {"ds": pd.date_range(start=self.next_date, end=self.next_date)}
            )
            return next_date_series

    def postprocess_outputs(self, output_from_model) -> List:

        return output_from_model["yhat"].tolist()

    def predict(self, prev_date) -> List:
        next_date_series = self.preprocess_inputs(prev_date)  # preprocess inp
        pred = self.model.predict(next_date_series)  # prediction
        pred = self.postprocess_outputs(pred)  # postprocess prediction
        return pred  # return prediction


class ArimaPredictor(PricePredictor):
    def __init__(self,) -> None:
        super().__init__("fbprophet")



