import os
import chainlit as cl
from litellm import completion


api_key = os.getenv("GEMINI_API_KEY")
print(f"api_key: {api_key}")

@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="Classical Mechanics",
            message="The study of motion and forces in macroscopic systems, excluding very small or very fast objects.  Think of Newton's laws governing the trajectory of a ball thrown in the air",
            # icon="/public/idea.svg",
            ),

        cl.Starter(
            label="Exploring the Laws of Nature",
            message="Physics seeks to uncover the fundamental laws that govern the universe and explain the behavior of everything from atoms to stars. This ongoing quest for knowledge continues to expand our understanding of the cosmos. Example:  The theory of relativity revolutionized our understanding of space, time, and gravity.",
            # icon="/public/learn.svg",
            ),
        cl.Starter(
            label="Understanding Motion, Energy, and Matter",
            message="Physics investigates the principles governing motion, energy transformations, and the properties of matter. It encompasses diverse fields like mechanics, thermodynamics, and electromagnetism. Example: Physics describes how a car accelerates (Newton's laws) and how electricity powers our homes (electromagnetism).",
            # icon="/public/terminal.svg",
            ),
        cl.Starter(
            label="The Study of the Universe",
            message="Physics explores the fundamental constituents of the universe and how they interact, from the smallest subatomic particles to the largest galaxies.  It uses observation, experimentation, and mathematical models to understand natural phenomena. Example:  Physics explains why apples fall from trees (gravity) and how stars shine (nuclear fusion).",
            # icon="/public/write.svg",
            )
        ]
# ...

@cl.on_message
async def main(message: cl.Message):

    # Send a thinking message
    msg = cl.Message(content="Thinking...")
    await msg.send()

    # Get the chat history from the user session or initialize it if it doesn't exist
    history = cl.user_session.get('chat_history', [])
    if not history:
        # Initialize with the system message only if history is empty
        history.append({"role": "system", "content": "You are a helpful Physics Teacher. You are very friendly and helpful. You are very good at explaining complex concepts in simple terms. You always give an example to illustrate your point. Your resonse is in fully structured and in markdown."})

    # Append the user message to the chat history
    history.append({"role": "user", "content": message.content})

    try:
        response = completion(
            model="gemini/gemini-1.5-flash",
            api_key=api_key,
            messages=history,
            temperature=0.7,
            # stream=True,
        )   

        # async for part in stream_:
        #     print(f"Received part: {part}")
        #     if part.choices and part.choices[0].delta.content:
        #         token = part.choices[0].delta.content
        #         await msg.stream_token(token)

        msg.content = response.choices[0].message.content
        # Append the response to the chat history
        history.append({"role": "assistant", "content": msg.content})
        cl.user_session.set('chat_history', history)
        # Send the response message
        await msg.update()

    except Exception as e:
        print(f"Error: {e}")
        msg.content = "Sorry, there was an error processing your request."
        await msg.update()


# litellm._turn_on_debug()
@cl.on_chat_start
def on_chat_start():
    print("A new chat session has started!")
