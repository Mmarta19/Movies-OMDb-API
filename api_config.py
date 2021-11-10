import os


class API_Config:
    def __init__(self) -> None:
        self.PORT = 5000
        self.OMDB_API_URL = "http://www.omdbapi.com/"
        self.OMDB_KEY = self.getOMDBKey()
        self.DEBUG = True

    def getOMDBKey(self):
        OMDB_KEY = os.getenv('OMDB_KEY')
        if OMDB_KEY is None:
            raise ValueError("OMDB_KEY is not set.")
        else:
            return OMDB_KEY
