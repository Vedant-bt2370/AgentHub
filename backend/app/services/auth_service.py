from models.user import User
from core.security import hash_password, verify_password


def register_user(db, email, password):

    user = User(
        email=email,
        password_hash=hash_password(password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def authenticate_user(db, email, password):

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if user is None:
        return None

    if not verify_password(
        password,
        user.password_hash
    ):
        return None

    return user