from ai.huggingface_service import (
    ask_huggingface
)

from services.mongo_memory_service import (

    get_conversation,

    add_message
)

SYSTEM_CONTEXT = """
You are an AI financial reasoning assistant.

You maintain conversational continuity.

You remember:
- user goals
- portfolio discussions
- previous financial context

You provide:
- personalized investment reasoning
- conversational financial guidance
- follow-up support
"""

def conversational_financial_agent(

    session_id,

    user_message
):

    add_message(
        session_id,
        "user",
        user_message
    )

    history = get_conversation(
        session_id
    )

    conversation_text = SYSTEM_CONTEXT + "\n\n"

    for msg in history:

        conversation_text += (
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )

    response = ask_huggingface(
        conversation_text
    )

    add_message(
        session_id,
        "assistant",
        response
    )

    return response


if __name__ == "__main__":

    session_id = "user001"

    result = conversational_financial_agent(

        session_id,

        "I want retirement planning"
    )

    print(result)