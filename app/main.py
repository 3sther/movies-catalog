from typing import Annotated

from fastapi import (
    FastAPI,
    Request,
    HTTPException,
    status,
    Depends,
)

from schemas.movies import Movie

app = FastAPI(
    title="Movies Catalog",
)


@app.get("/")
def root_informer(
    # Get incoming url obj to adjust
    request: Request,
):
    path_to_docs = request.url.replace(
        path="/docs",
    )
    return {"Our catalog is currently empty, please go to our docs": str(path_to_docs)}


MOVIES_CATALOG = [
    Movie(
        id=0,
        title="The Shawshank Redemption",
        description="A banker convicted of uxoricide forms a friendship over a"
        "quarter century with a hardened convict, while maintaining his innocence"
        "and trying to remain hopeful through simple compassion.",
        released="14 Oct 1994",
        budget="$28,767,189",
        director="Frank Darabont",
    ),
    Movie(
        id=1,
        title="The Godfather",
        description="The aging patriarch of an organized crime dynasty transfers"
        "control of his clandestine empire to his reluctant son.",
        released="24 Mar 1972",
        budget="$136,381,073",
        director="Francis Ford Coppola",
    ),
]


def find_movie_by_id(movie_id: int) -> Movie | None:
    movie: Movie | None = next(
        (movie for movie in MOVIES_CATALOG if movie.id == movie_id), None
    )
    if movie:
        return movie

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@app.get(
    "/movies/",
    response_model=list[Movie],
)
def list_catalog() -> list[Movie]:
    return MOVIES_CATALOG


@app.get(
    "/movies/{movie_id}/",
    response_model=Movie,
)
def get_movie(
    movie: Annotated[Movie, Depends(find_movie_by_id)],
) -> Movie:
    return movie
