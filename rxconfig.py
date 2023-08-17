import reflex as rx


class HelloreflexConfig(rx.Config):
    pass


config = HelloreflexConfig(
    app_name="chatapp",
    api_url="http://0gpt.diginori.com:8000",
    # api_url="http://0gpt.fly.dev:8000",

)
