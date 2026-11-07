from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

class User(Base):
    __tablename__ ="users"
    id:Mapped[int]=mapped_column(primary_key=True)
    name: Mapped[str]=mapped_column(String(100))
    posts: Mapped[list["Post"]]= relationship(back_populates="owner")
    
class Post(Base):
    __tablename__ ="posts"
    id:Mapped[int]= mapped_column(primary_key=True)
    title: Mapped[str]=mapped_column(String(200))
    user_id: Mapped[int]=mapped_column(ForeignKey("users.id"))
    owner: Mapped["User"]=relationship(back_populates="posts")
    