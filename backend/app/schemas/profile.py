from pydantic import BaseModel, model_validator, ConfigDict
from typing import Optional, List
from uuid import UUID
from datetime import datetime
from enum import Enum

class SkillLevelEnum(Enum):
    beginner = 'beginner'
    intermediate = 'intermediate'
    advanced = 'advanced'

class PlayStyleEnum(Enum):
    casual = 'casual'
    competitive = 'competitive'

class ProfileCreate(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    skill_level: SkillLevelEnum
    play_style: Optional[PlayStyleEnum] = None
    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    home_courts: Optional[List[str]] = None

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'first_name': 'John',
                'last_name': 'Doe',
                'skill_level': 'beginner',
                'play_style': 'casual',
                'bio': 'Hello I am an avid pickleball player',
                'avatar_url': '...',
                'home_courts': ['san diego court', 'cypress court']
            }
        }
    )

class ProfileUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    skill_level: Optional[SkillLevelEnum] = None
    play_style: Optional[PlayStyleEnum] = None
    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    home_courts: Optional[List[str]] = None

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'first_name': 'John',
                'last_name': 'Doe',
                'skill_level': 'beginner',
                'play_style': 'casual',
                'bio': 'Hello I am an avid pickleball player',
                'avatar_url': '...',
                'home_courts': ['san diego court', 'cypress court']
            }
        }
    )

class ProfileResponse(BaseModel):
    full_name: str
    first_name: str
    last_name: Optional[str] = None
    skill_level: SkillLevelEnum
    play_style: Optional[PlayStyleEnum] = None
    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    home_courts: Optional[List[str]] = None
    reliability_score: Optional[float] = 100.0
    user_id: UUID
    created_at: datetime

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'full_name': 'John Doe',
                'first_name': 'John',
                'last_name': 'Doe',
                'skill_level': 'beginner',
                'play_style': 'casual',
                'bio': 'Hello I am an avid pickleball player',
                'avatar_url': '...',
                'home_courts': ['san diego court', 'cypress court'],
                'reliability_score': 98.2,
                'user_id': 'user_id',
                'created_at': '...'
            }
        }
    )

    @model_validator(mode='after')
    def create_full_name(self) -> 'ProfileResponse':
        self.full_name = ''
        if self.first_name is not None:
            self.full_name += self.first_name
        if self.last_name is not None:
            self.full_name += " " + self.last_name
        return self

