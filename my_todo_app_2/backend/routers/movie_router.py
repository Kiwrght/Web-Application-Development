from fastapi import APIRouter, Path, HTTPException, status

from backend.models.movie import Movie, MovieRequest
from models.todo_model import Todo, MovieRequest

movie_router = APIRouter()

movie_list = []
max_id: int = 0


@movie_router.post("", status_code=status.HTTP_201_CREATED)
async def add_todo(todo: MovieRequest) -> Movie:
    global max_id
    max_id += 1  # auto increment ID

    newMovie = MovieRequest(id=max_id, title=todo.title, description=todo.description)
    await Movie.insert_one(newMovie)
    return newMovie


@movie_router.get("")
async def get_movie() -> list[Movie]:
    return await Movie.find_all().to_list()


@movie_router.get("/{id}")
async def get_movie_by_id(id: int = Path(..., title="default")) -> Movie:
    movie = Movie.get(id)
    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"The Movie with ID={id} is not found.",
    )


@movie_router.put("/{id}")
async def update_movie(movie: MovieRequest, id: int) -> dict:
    for x in movie_list:
        if x.id == id:
            x.title = movie.title
            x.year = movie.year
            return {"message": "Todo updated successfully"}

    return {"message": f"The movie with ID={id} is not found."}


@movie_router.delete("/{id}")
async def delete_movie(id: int) -> dict:
    for i in range(len(movie_list)):
        movie = movie_list[i]
        if movie.id == id:
            movie_list.pop(i)
            return {"message": f"The movie with ID={id} has been deleted."}

    return {"message": f"The movie with ID={id} is not found."}
