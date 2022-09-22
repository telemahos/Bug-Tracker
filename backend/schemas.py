from typing import List, Optional, Union
from datetime import date
# datetime, time
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# User
# ------------------------------------
class User(BaseModel):
    id: int
    name: str
    email: str
    password: Union[str, None] = None
    user_role: int

class ShowUser(BaseModel):
    id: int
    name: Union[str, None] = None 
    email: Union[str, None] = None
    user_role: Union[int, None] = None
    class Config():
        orm_mode = True


# Case
# ------------------------------------
class CaseBase(BaseModel):
    id: int
    start_date: Optional[date]
    due_date: Optional[date]
    title: Optional[str] = None
    description: Optional[str] = None
    tags:  Optional[str] = None
    status:  Optional[int] = 0
    priority: Optional[int] = 0
    case_type: Optional[int] = 0
    project_id: Optional[int] = None
    owner_id: Optional[int] = None

class Case(CaseBase):
    class Config():
        orm_mode = True

class ShowCase(CaseBase):
    id: int
    start_date: Optional[date]
    due_date: Optional[date]
    title: Optional[str] = None
    description: Optional[str] = None
    tags:  Optional[str] = None
    status:  Optional[int] = 0
    priority: Optional[int] = 0
    case_type: Optional[int] = 0
    project_id: Optional[int] = None
    owner_id: Optional[int] = None

    class Config():
        orm_mode = True

    # bar_income_2: Optional[float] = None
    # pos: float = 0
    # shift_id: Optional[str]
    # the_shift: Optional[Shift] 
    
# Project
# ------------------------------------
class ProjectBase(BaseModel):
    id: int
    start_date: date
    due_date : date
    title: Optional[str] = None
    description: Optional[str] = None
    tags:  Optional[str] = None
    active:  Optional[bool] = False
    status:  Optional[int] = 0
    priority: Optional[int] = 0
    # team_id: Optional[int] = 0
    owner_id: Optional[int] = None

class Project(ProjectBase):
    class Config():
        orm_mode = True

class ShowProject(ProjectBase):
    id: int
    start_date: date
    due_date : date
    title: Optional[str] = None
    description: Optional[str] = None
    tags:  Optional[str] = None
    active:  Optional[bool] = False
    status:  Optional[int] = 0
    priority: Optional[int] = 0
    # team_id: Optional[int] = 0
    owner_id: Optional[int] = 0

    class Config():
        orm_mode = True

# Team
# ------------------------------------
# class TeamBase(BaseModel):
#     id: int
#     project_id: Optional[str] = 0
#     active:  Optional[bool] = False
#     note:  Optional[str] = None

# class Team(TeamBase):
#     class Config():
#         orm_mode = True

# class ShowTeam(TeamBase):
#     id: int
#     project_id: Optional[str] = 0
#     active:  Optional[bool] = False
#     note:  Optional[str] = None
#     the_team_members: Optional[Team] 
#     class Config():
#         orm_mode = True
        
# Team
# ------------------------------------
class TeamMemberBase(BaseModel):
    id: int
    project_id: int 
    user_id: int
    team_role: Optional[int] = 0
    assign_date: date
    active:  Optional[bool] = True
    note:  Optional[str] = None
    
class TeamMember(TeamMemberBase):
    class Config():
        orm_mode = True
        
class ShowTeamMember(TeamMemberBase):
    id: int
    project_id: int 
    user_id: int
    team_role: Optional[int] = 0
    assign_date: date
    active:  Optional[bool] = True
    note:  Optional[str] = None

    class Config():
        orm_mode = True