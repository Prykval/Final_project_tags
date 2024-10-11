from typing import List

from sqlalchemy.orm import Session

from src.entity.models import Tag
from src.schemas.schemas import TagModel
from src.entity.models import Hashtag


async def get_tags(skip: int, limit: int, db: Session) -> List[Tag]:
    return db.query(Tag).offset(skip).limit(limit).all()


async def get_tag(tag_id: int, db: Session) -> Tag:
    return db.query(Tag).filter(Tag.id == tag_id).first()


async def create_tag(body: TagModel, db: Session) -> Tag:
    tag = Tag(name=body.name)
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag


async def update_tag(tag_id: int, body: TagModel, db: Session) -> Tag | None:
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if tag:
        tag .name = body.name
        db.commit()
    return tag


async def remove_tag(tag_id: int, db: Session)  -> Tag | None:
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if tag:
        db.delete(tag)
        db.commit()
    return tag


async def get_or_create_tag(db: Session, name: str):
    """
    The get_or_create_tag function retrieves a tag from the database with the given name, or creates a new tag if it doesn't exist.

    :param db: Session: Pass the database session to the function
    :param name: str: Specify the name of the tag
    :return: A tag
    :doc-author: Trelent
    """
    tag = db.query(Hashtag).filter(Hashtag.name == name).first()
    if not tag:
        tag = Hashtag(name=name)
        db.add(tag)
        db.commit()
        db.refresh(tag)
    return tag