from fastapi import APIRouter, Depends, HTTPException, Query, Path
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from database import get_db, MovieModel
from database.models import CountryModel, GenreModel, ActorModel, LanguageModel

router = APIRouter()


@router.get("/movies")
async def list_movies():
    pass


@router.post("/movies")
async def create_movie():
    pass


@router.get("/movies/{movie_id}")
async def get_movie_details():
    pass


@router.delete("/movies/{movie_id}")
async def delete_movie():
    pass


@router.put("/movies/{movie_id}")
async def update_movie():
    pass
