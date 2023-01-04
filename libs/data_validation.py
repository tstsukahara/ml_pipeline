import pandas as pd
from typing import Type

from pandera import SchemaModel


def validate(df: pd.DataFrame, schema: Type[SchemaModel]) -> None:
    schema.validate(df)
    print(f"{schema.Config.name} validated.")
