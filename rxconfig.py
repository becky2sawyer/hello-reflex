import reflex as rx


class HelloreflexConfig(rx.Config):
    pass


config = HelloreflexConfig(
    app_name="chatapp",
    api_url="https://app.example.com:8000",
)