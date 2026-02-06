from uuid import UUID
from app.schemas import ProfileResponse, ProfileUpdate
from app.services import ProfileService
from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/profiles"
)

service = ProfileService()

@router.get("/me")
def get_user_profile() -> ProfileResponse:
    user_profile = service.get_profile('00000000-0000-0000-0000-000000000000')
    return user_profile

@router.put("/me")
def update_user_profile(req: ProfileUpdate) -> ProfileResponse:
    updated_profile = service.update_profile('00000000-0000-0000-0000-000000000000', req)
    return updated_profile

@router.get("/{user_id}")
def get_any_profile(user_id: UUID) -> ProfileResponse:
    user_profile = service.get_profile(user_id)
    return user_profile




