from models.user import User
from core.security import hash_password

def register_user(db, email, password):

    user = User(
        email=email,
        password_hash=hash_password(password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user