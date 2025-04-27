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

async def main():
    # History of the agent
    history = []
    
    while True:
        # Infinite loop to keep the agent running
        user_input = input("User input: ")
        if user_input.lower() == "exit":
            print("Exiting the agent.")
            break
        history.append({"role": "user", "content": user_input})

        result = await Runner.run(
            agent,
            history
        )
        # append the agent's response to the history
        history.append({"role": "assistant", "content": result.final_output})
        print(result.final_output)



if __name__ == "__main__":
    asyncio.run(main())