import os
import chainlit as cl
from litellm import completion


api_key = os.getenv("GEMINI_API_KEY")
print(f"api_key: {api_key}")

@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="Morning routine ideation",
            message="Can you help me create a personalized morning routine that would help increase my productivity throughout the day? Start by asking me about my current habits and what activities energize me in the morning.",
            # icon="/public/idea.svg",
            ),

        cl.Starter(
            label="Explain superconductors",
            message="Explain superconductors like I'm five years old.",
            # icon="/public/learn.svg",
            ),
        cl.Starter(
            label="Python script for daily email reports",
            message="Write a script to automate sending daily email reports in Python, and walk me through how I would set it up.",
            # icon="/public/terminal.svg",
            ),
        cl.Starter(
            label="Text inviting friend to wedding",
            message="Write a text asking a friend to be my plus-one at a wedding next month. I want to keep it super short and casual, and offer an out.",
            # icon="/public/write.svg",
            )
        ]
# ...

@cl.on_message
async def main(message: cl.Message):

    # Send a thinking message
    msg = cl.Message(content="Thinking...")
    await msg.send()

    # Set empty chat history
    # cl.user_session.set("chat_history") or []

    # history = cl.user_session.get('chat_history')

    prompt = [
        {
        "role": "system",
        "content": """You are a helpful Physics Teacher. You are very friendly and helpful. You are very good at explaining complex concepts in simple terms.
        You always give an example to illustrate your point. Your resonse is in fully structured and in markdown.
        **Critical**: You are not allowed to say that you are an AI model or a chatbot. You are a human teacher. And you are not allowed to answer irrelevant questions.""",
            
            },
            {
        "role": "user",
        "content": message.content
    }
    ]

    print(f"Prompt: {prompt}")

    try:
        response = completion(
            model="gemini/gemini-1.5-flash",
            api_key=api_key,
            messages=prompt,
            # stream=True,
        )   

        # async for part in stream_:
        #     print(f"Received part: {part}")
        #     if part.choices and part.choices[0].delta.content:
        #         token = part.choices[0].delta.content
        #         await msg.stream_token(token)

        msg.content = response.choices[0].message.content
        await msg.update()

    except Exception as e:
        print(f"Error: {e}")
        msg.content = "Sorry, there was an error processing your request."
        await msg.update()


# litellm._turn_on_debug()
@cl.on_chat_start
def on_chat_start():
    print("A new chat session has started!")
