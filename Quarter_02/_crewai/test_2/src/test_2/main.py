import os
from crewai.flow import Flow, start, listen
from litellm import completion

api_key = os.getenv("API_KEY")

class TestFlow(Flow):

    @start()
    def topic_generator(self):
        response = completion(
            model="gemini/gemini-1.5-flash",
            api_key=api_key,
            messages=[
                {
                    "role": "user",
                    "content": "Generate a topic for a blog post about Franz Kafka."
                }
            ],
            temperature=0.5,    
            max_tokens=50,
        )
        topics = response["choices"][0]["message"]["content"]
        print(f"Generated Topics: {topics}")
        return topics
    
    @listen("topic_generator")
    def blog_post_generator(self, topics):
        response = completion(
            model="gemini/gemini-1.5-flash",
            api_key=api_key,
            messages=[
                {
                    "role": "user",
                    "content": f"Generate a blog post about {topics}."
                }
            ],
            temperature=0.5,    
            max_tokens=1000,
        )
        blog_post = response["choices"][0]["message"]["content"]
        print(f"Generated Blog Post: {blog_post}")

def kickoff():
    flow = TestFlow()
    flow.kickoff()