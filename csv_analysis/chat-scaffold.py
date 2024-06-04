from openai import OpenAI
import pandas as pd
from comparisons import RaceComparison

OPENAI_API_KEY = 'your-api-key'

class Agent:
    def __init__(self, df1: pd.DataFrame, df1_tag: str, df2: pd.DataFrame, df2_tag: str) -> None:
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.df1 = df1
        self.df2 = df2
        self.race_comparator = RaceComparison()
        self.messages = [
            {"role": "system", "content": f"Given {df1_tag} with dataframe {df1} and {df2_tag} with dataframe {df2} answer questions."},
            {"role": "system", "content": "Initialize comparisons between two data sets."}
        ]
        self.context_window = []

    