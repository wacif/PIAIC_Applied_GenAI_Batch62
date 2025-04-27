import os
from dotenv import load_dotenv
from agents import Agent, Runner, set_tracing_disabled

# Set tracing disabled to False
set_tracing_disabled(disabled=True)

# Load environment variables from .env file
load_dotenv()

# Now set the API key from the loaded environment
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("OPENAI_API_KEY environment variable is not set")
os.environ["OPENAI_API_KEY"] = api_key

def test_agent():

    while True:
        # Infinite loop to keep the agent running
        user_input = input("User input: ")
        if user_input.lower() == "exit":
            print("Exiting the agent.")
            break
        # Create an agent with a name and instructions
        agent = Agent(name="TestAgent", instructions="You are a test agent.")
        
        # Run the agent with a sample input
        result = Runner.run_sync(agent, user_input)
        # Print the agent's response
        print(f"Agent response: {result.final_output}")


# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.


if __name__ == "__main__":
    # Run the agent with a sample input
    test_agent()
    # Print the final output
    print("Test completed.")