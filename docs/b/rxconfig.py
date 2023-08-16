import reflex as rx


class HelloreflexConfig(rx.Config):
    pass


config = HelloreflexConfig(
    app_name="chatapp",
    api_url="https://slide.diginori.com/hello-reflex",
)