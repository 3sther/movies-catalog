from fastapi import (
    FastAPI,
    Request,
)

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
