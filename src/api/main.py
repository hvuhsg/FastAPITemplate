from fastapi import APIRouter

from .v1 import api_v1_router


api_route = APIRouter(prefix="/api")
api_route.include_router(api_v1_router)
