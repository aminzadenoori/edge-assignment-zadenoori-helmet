"""
This module contains Enviroment bluprint.
Author: Stefano Ravagnan <stefano.ravagnan@nphysis.com>
"""
from pydantic import BaseSettings, Field

class Environment(BaseSettings):
    """Class that represents enviroment variables"""

    # General config 

    # Camera and shot config
    RESIZE: tuple = Field( default = (300, 300))
    SCORE_TH: float = Field(min_value=0, max_value=1, default=.5)
    SHOT_DELAY: int = Field(default = 2)  # seconds between each shot
    CAMERA_INIT_DELAY: int = Field(default = 10)
    
    # rasp pi4 config
    DEVICE_ID: int = Field(default = 12345)
    AUTH_KEY: str  =  Field(default = 'mnbvcxzlkjhgfdsapoiuytrewq')
    
    #slack
    #SLACK_TOKEN: str
    #SLACK_ERROR_LINK: str
    #SLACK_ERROR_LINK_NAME: str

    
    class Config:
        """Class that represents confi for parsing .env file"""

        env_file = ".env"
        env_file_encoding = "utf-8"

        def __repr__(self) -> str:
            return "<Config Enviroment Class>"

    def __repr__(self) -> str:
        return "<Enviroment Class>"


ENVIRONMENT = Environment(_env_file="config/.env", _env_file_encoding="utf-8")