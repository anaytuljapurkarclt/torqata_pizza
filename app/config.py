import os
from dotenv import load_dotenv
from pathlib import Path
import urllib.parse

env_path = Path.home()/'.env'
load_dotenv(dotenv_path=env_path)


class loadSettings:
    username: str = os.getenv("username")
    password = urllib.parse.quote_plus(os.getenv("password"))
    hostname: str = os.getenv("hostname")
    portno: str = os.getenv("portno")
    dbnm: str = os.getenv("dbnm")
    conn_uri = "postgresql://{username}:{password}@{hostname}:{portno}/{dbnm}".format(
                username=username,
                password=password,
                hostname=hostname,
                portno=portno,
                dbnm=dbnm
                )

load_settings = loadSettings()
