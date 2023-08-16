# chatapp.py
import reflex as rx


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(question, text_align="rigth"),
        rx.box(answer, text_align="left"),
        margin_y="1em",
    )


def chat() -> rx.component:
    qa_pairs = [
        (
            "Reflex란 무엇입니까?",
            "순수한 파이썬으로 웹 앱을 만드는 방법!",
        ),
        (
            "그것으로 무엇을 만들 수 있을까요?",
            "단순한 웹사이트에서 복잡한 웹 앱까지!",
        )
    ]
    return rx.box(
        *[
            qa(question, answer)
            for question, answer in qa_pairs
        ]
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="질문을 던져라!"),
        rx.button("질문 받아라 ~")
    )


def index() -> rx.Component:
    return rx.container(chat(), action_bar())


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
