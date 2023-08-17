import reflex as rx
import os

class HelloreflexConfig(rx.Config):
    pass


config = HelloreflexConfig(
    app_name="chatapp",
    # api_url="http://0gpt.diginori.com:8000",
    # api_url="https://0gpt.fly.dev:8000",
    # api_url=os.environ["REFLEX_API_URL"],

)
