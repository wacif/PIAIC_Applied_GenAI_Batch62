
import os
from crewai import Flow, start, listen, route

api_key = os.getenv("API_KEY")
print(f"API Key: {api_key}")


class RouteFlow(Flow):
    @start()
    def greeting(self):
        print("Hey there! Welcome")
        return "Welcome from greeting function"

    @listen(greeting)
    def task_to_select (self, greeting):
        list_of_tasks = [
            "1. Get a random city name",
            "2. Get a fun fact about the city",
            "3. Shorten the fun fact to one line",
        ]
        print(f"Please select a task from the list below: {list_of_tasks}")
        

    @listen(fun_fact)
    def shortner(self, fun_fact):
        return "shortner"