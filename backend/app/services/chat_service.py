from models.chat import Chat


def save_chat(
        db,
        user_id,
        question,
        answer
):

    chat = Chat(
        user_id=user_id,
        question=question,
        answer=answer
    )

    db.add(chat)
    db.commit()

    return chat