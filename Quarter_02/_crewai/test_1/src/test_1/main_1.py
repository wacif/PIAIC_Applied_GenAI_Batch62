from crewai.flow import Flow, start, listen
from litellm import completion
import os
import time

api_key = os.getenv("API_KEY")
print(f"API Key: {api_key}")


class CityFunFact(Flow):

    @start()
    def city_name(self):
        response = completion(
            model="gemini/gemini-2.0-flash",
            api_key=api_key,
            messages=[
                {
                    "role": "user",
                    "content": "Give me a random city name."
                }
            ]

        )
        city_name = response.choices[0].message.content
        print(f"City name: {city_name}")
        time.sleep(4)
        return city_name
    
    @listen(city_name)
    def fun_fact(self, city_name):
        response = completion(
            model="gemini/gemini-2.0-flash",
            api_key=api_key,
            messages=[
                {
                    "role": "user",
                    "content": f"Tell me a fun fact about {city_name}."
                }
            ]
        )
        fun_fact = response.choices[0].message.content
        print(f"Fun fact: {fun_fact}")
        time.sleep(4)
        return fun_fact
    
    @listen(fun_fact)
    def shortner(self, fun_fact):
        response = completion(
            model="gemini/gemini-2.0-flash",
            api_key=api_key,
            messages=[
                {
                    "role": "user",
                    "content": f"Make this fun fact one liner: {fun_fact}."
                }
            ]
        )
        one_line = response.choices[0].message.content
        print(f"The one liner of the fun fact is: {one_line}")
        time.sleep(4)
        return one_line

    

def kickoff():
    obj = CityFunFact()
    obj.kickoff()

def plot():
    obj = CityFunFact()
    obj.plot()