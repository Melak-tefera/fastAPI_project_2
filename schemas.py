from pydantic import BaseModel, ConfigDict

class Usercreate(BaseModel):
    name: str

class Userread(BaseModel):
    id: int
    name: str
    model_config=ConfigDict(from_attributes=True)

class Postcreate(BaseModel):
    title: str

class Postread(BaseModel):
    id:int
    title:str
    user_id:int
    model_config=ConfigDict(from_attributes=True)
    
