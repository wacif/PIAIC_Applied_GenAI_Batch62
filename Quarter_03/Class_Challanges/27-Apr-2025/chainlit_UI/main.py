import chainlit as cl
import os
import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from dotenv import load_dotenv

load_dotenv()
# Set the API key for Gemini

gemini_api_key = os.getenv("GEMINI_API_KEY")
if gemini_api_key is None:
    raise ValueError("GEMINI_API_KEY environment variable is not set")
else:
    print("GEMINI_API_KEY is set.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_tracing_disabled(disabled=True)

# Create an agent with a name and instructions
# This agent will use the custom LLM provider
agent = Agent(
        name="Assistant",
        instructions="You are a smart assistant.",
        model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
        )

# Store conversation history
conversation_history = {}


@cl.on_chat_start
async def on_chat_start():
    # Initialize conversation history for the new chat session
    conversation_history[cl.user_session.get("id")] = []

@cl.on_message
async def main(message: cl.Message):
    # Get the current user's session ID
    session_id = cl.user_session.get("id")
    
    # Initialize history if it doesn't exist for this session
    if session_id not in conversation_history:
        conversation_history[session_id] = []
    
    # Get user input from the message
    user_input = message.content
    
    # Add user message to history
    conversation_history[session_id].append({"role": "user", "content": user_input})
    
    # Thinking...
    msg = cl.Message(content="Thinking...")
    await msg.send()

    # Get response from the agent
    result = Runner.run_sync(
        agent,
        conversation_history[session_id]
    )
    
    # Add agent's response to history
    conversation_history[session_id].append({"role": "assistant", "content": result.final_output})
    
    # Send the response back to the user
    msg.content = result.final_output
    await msg.update()

    # Debugging: Print the conversation history
    print(f"Conversation history for session {session_id}:")
    for message in conversation_history[session_id]:
        print(f"{message['role']}: {message['content']}")