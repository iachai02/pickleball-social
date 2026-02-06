from app.schemas import ProfileCreate, ProfileUpdate, ProfileResponse
from uuid import UUID
from supabase import create_client, Client
from app.core.config import settings

supabase_url: str = settings.SUPABASE_URL
supabase_key: str = settings.SUPABASE_SERVICE_ROLE_KEY

supabase: Client = create_client(supabase_url, supabase_key)

class ProfileService:
    def get_profile(self, user_id: UUID) -> ProfileResponse:
        try:
            response = supabase.table("profiles").select("*").eq("id", user_id).execute()
            if response.data:
                return ProfileResponse(**response.data[0])

        except Exception as e:
            print("Failed to get profile:", e)
    
    def create_profile(self, user_id: UUID, req: ProfileCreate) -> ProfileResponse:
        try:
            data = req.model_dump()
            data['id'] = str(user_id)
            response = supabase.table("profiles").insert(data).execute()
            if response.data:
                return ProfileResponse(**response.data[0])
        except Exception as e:
            print("Failed to create profile:", e)
    
    def update_profile(self, user_id: UUID, req: ProfileUpdate) -> ProfileResponse:
        try:
            response = supabase.table("profiles").update(req.model_dump(exclude_unset=True)).eq("id", user_id).execute()
            if response.data:
                return ProfileResponse(**response.data[0])
        except Exception as e:
            print("Failed to update profile:", e)
    
