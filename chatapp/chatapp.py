# chatapp.py
import reflex as rx

from chatapp import style
from chatapp.state import State


def polar() -> rx.Component:
    return rx.box(
        rx.chart(
            rx.polar(),
            rx.line(
                data=rx.data(
                    "line", x=["민주", "고양이", "공산당", "검찰", "자유"], y=[1, 2, 8, 10, 10]
                ),
            ),
            polar=True,
        ),
        rx.image(
            src="https://img.freepik.com/free-photo/adorable-kitty-looking-like-it-want-to-hunt_23-2149167099.jpg?w=2000",
            width="100px",
            height="auto",
            border_radius="15px 50px",
            border="5px solid #555",
            box_shadow="lg",
        )
    )


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, text_align="right"),
            style=style.question_style,
        ),
        rx.box(
            rx.text(answer, text_align="left"),
            style=style.answer_style,
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.text_area(
            id="question",
            placeholder="여기에 프롬프트 입력",
            on_blur=State.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_click=State.answer,
            style=style.button_style,
        ),
    )


def index() -> rx.Component:
    return rx.container(
        polar(),
        chat(),
        action_bar(),
    )


app = rx.App()
app.add_page(index)
app.compile()
