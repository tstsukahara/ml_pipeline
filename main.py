import pandas as pd
from prefect import flow, task
from libs import data_extraction, data_validation, model_training
from libs.data_extraction import SQL
from schemas.item import ItemSchema
import hydra
from omegaconf import DictConfig, OmegaConf


@task
# @task(persist_result=True)
def data_extract():
    sql = SQL.parse_obj({'query': 'select hoge;'})
    return data_extraction.extract(sql)


@task
def data_validate(df: pd.DataFrame):
    data_validation.validate(df, ItemSchema)
    return df
    
    
@task
def model_train(df: pd.DataFrame):
    params = {'model_name': 'modelA'}
    model_training.train(df, params)
           

@flow(name="example")
def my_flow():
    df = data_extract()
    df = data_validate(df)
    model_train(df)


@hydra.main(version_base=None, config_path="conf", config_name="config")
def main(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    my_flow()


if __name__ == '__main__':
    main()