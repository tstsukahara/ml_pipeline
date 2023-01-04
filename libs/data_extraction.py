from pydantic import BaseModel, validator, validate_arguments
import pandas as pd


class SQL(BaseModel):
    query: str

    @validator('query')
    def query_must_end_with_semicolon(cls, v):
        if v[-1] != ';':
            raise ValueError("query must end with ';'")
        return v


@validate_arguments
def extract(sql: SQL) -> pd.DataFrame:
    print(f"query={sql.query}")
    df = pd.DataFrame({'name': ['hoge', 'foo'], 'price': [1000, 2000]})
    print(df.head())
    return df
