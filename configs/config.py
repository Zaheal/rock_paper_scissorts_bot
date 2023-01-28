from environs import Env
from dataclasses import dataclass


@dataclass
class Config:
    token: str


def load_config(path: str | None) -> Config:

    env: Env = Env()
    env.read_env(path)

    return Config(token=env('BOT_TOKEN'))
