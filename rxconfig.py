import reflex as rx


class HelloreflexConfig(rx.Config):
    pass


config = HelloreflexConfig(
    app_name="chatapp",
    frontend_port=3000,
    backend_port=8000,
)