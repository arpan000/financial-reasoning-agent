from mongodb.mongo_connection import (
    conversation_collection
)

def add_message(

    session_id,

    role,

    content
):

    conversation_collection.insert_one({

        "session_id": session_id,

        "role": role,

        "content": content
    })

def get_conversation(session_id):

    messages = conversation_collection.find({

        "session_id": session_id
    })

    conversation = []

    for msg in messages:

        conversation.append({

            "role": msg["role"],

            "content": msg["content"]
        })

    return conversation

def clear_conversation(session_id):

    conversation_collection.delete_many({

        "session_id": session_id
    })


if __name__ == "__main__":

    add_message(
        "user001",
        "user",
        "Hello Financial AI"
    )

    result = get_conversation(
        "user001"
    )

    print(result)