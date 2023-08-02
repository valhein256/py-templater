from typing import List
from pydantic import BaseModel, validator


class StrictInt(int):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, float):
            raise TypeError("Will not coerce float to int")
        return v


class Input(BaseModel):
    """
    Input model
    """
    num_list: List[StrictInt]
    top_n: StrictInt

    @validator('num_list')
    def is_int_list(cls, v):
        if not isinstance(v, list):
            raise ValueError(f'num_list must be list, but got {type(v)}')
        for i in v:
            if not isinstance(i, int):
                raise ValueError(f'num_list must be list of int, but got {i}')
        return v

    @validator('top_n')
    def is_positive_number(cls, v):
        if v < 0 or not isinstance(v, int):
            raise ValueError(f'top_n must be positive number, but got {v}')
        return v


class Output(BaseModel):
    """
    Output model
    """
    result: List[int]
