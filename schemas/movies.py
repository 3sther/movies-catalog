from pydantic import BaseModel


class MovieBaseModel(BaseModel):
    id: int
    title: str
    description: str
    released: str
    budget: str
    director: str


class Movie(MovieBaseModel):
    """
    This is core data for a movie.
    """

    pass
