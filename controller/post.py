from sqlalchemy.orm import Session
from models.post import PostModel
from models.sql_models import Post
from models.user import SignUp


def get_users_posts(user: SignUp, session: Session):
    posts = session.query(Post).filter_by(owner_id=user.id).all()
    return posts


def create_post_in_db(user: SignUp, post: PostModel, session: Session):
    db_post = Post(title=post.title, content=post.content, owner_id=user.id)
    session.add(db_post)
    session.commit()
    session.refresh(db_post)
