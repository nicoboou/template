import argparse
import os

from src.models import NewModelGenerator
from src.utils import Params

parser = argparse.ArgumentParser()

parser.add_argument(
    "--config_path",
    default="./config/batch_all.json",
    help="Path to the config file for trainning",
)


if __name__ == "__main__":
    args = parser.parse_args()

    json_path = args.config_path
    assert os.path.isfile(json_path), f"No config file found at {json_path}"
    params = Params(json_path)

    model_gen = NewModelGenerator(**params.__dict__)
