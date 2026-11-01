import argparse
import logging
import os
import json

from pathlib import Path
from typing import Annotated
from pydantic import BaseModel, ConfigDict, Field, ValidationError, EmailStr

parser = argparse.ArgumentParser(
    prog='cli',
    description='Parses and validates the given json file. Additionally applying flags if given',
    epilog='The program should follow as python3(whichever compiler version you are using) <file name> [--flags](check the README file for acceptable flags) ')

parser.add_argument('filename')
# parser.add_argument('-s', '--strict')

args = parser.parse_args()
log_file = os.path.join(os.getcwd(), 'errors.log')

try:
    Path(log_file).touch(exist_ok=True)
    logging.basicConfig(
        filename = log_file,
        filemode='a',
        level = logging.DEBUG,
       )
    logger = logging.getLogger(__name__)

except Exception as err:
    print("couldn't create a log file.")


class Company(BaseModel):
    """Company information"""
    id: Annotated[int, Field(gt = 0)]
    email: EmailStr | None = None
    contact_info: list[str] | str
    mobile: str | None = None
    owner: str | list[str]
    has_app: bool = False
    contact_permits: bool | None = None


try:
    with open(args.filename, "r") as file:
        json_payload = json.load(file)
except (FileNotFoundError, Exception) as err:
    print("Please give a proper existing json file. For more details check your errors.log file if present")
    if logger: logger.debug("Bad JSON: {0}".format(err))
    else: raise


try:
    company = Company.model_validate(json_payload)
    print(company)
except ValidationError as err:
    print(err)
except NameError as exc:
    pass