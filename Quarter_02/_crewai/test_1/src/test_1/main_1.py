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
                    "content": "Give me a city name."
                }
            ]

        )
        city_name = response.choices[0].message.content
        print(f"City name: {city_name}")
        time.sleep(4)
        return city_name
    
    @listen(city_name)
    def fun_fact(self):
        response = completion(
            model="gemini/gemini-2.0-flash",
            api_key=api_key,
            messages=[
                {
                    "role": "user",
                    "content": f"Tell me a fun fact about {self.city_name}."
                }
            ]
        )
        fun_fact = response.choices[0].message.content
        print(f"Fun fact: {fun_fact}")
        time.sleep(4)
        return fun_fact
    
    @listen(fun_fact)
    def urdu_lang(self):
        response = completion(
            model="gemini/gemini-2.0-flash",
            api_key=api_key,
            messages=[
                {
                    "role": "user",
                    "content": f"Translate this to Urdu: {self.fun_fact}."
                }
            ]
        )
        urdu_lang = response.choices[0].message.content
        print(f"Urdu translation: {urdu_lang}")
        time.sleep(4)
        return urdu_lang

    

def kickoff():
    obj = CityFunFact()
    obj.city_name()