from sqlalchemy.orm import Session
from models.post import PostIn
from models.sql_models import Post, User
from cachetools import TTLCache, cached


@cached(cache=TTLCache(maxsize=10, ttl=60 * 5))
def get_users_db_posts(user: User, session: Session):
    posts = session.query(Post).filter_by(owner_id=user.id).all()
    return posts


def create_post_in_db(user: User, post: PostIn, session: Session):
    db_post = Post(title=post.title, content=post.content, owner_id=user.id)
    session.add(db_post)
    session.commit()
    session.refresh(db_post)


def get_post_by_id(post_id: int, session: Session):
    post = session.query(Post).filter_by(id=post_id).first()
    return post


def delete_post_by_id(post_id: int, session: Session):
    session.query(Post).filter_by(id=post_id).delete()
    session.commit()
