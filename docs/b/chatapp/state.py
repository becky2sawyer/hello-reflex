# state.py
import reflex as rx
import os
import openai
import numpy as np
import random


openai.api_key = os.environ["OPENAI_API_KEY"]

cat_meow_list = [
    "야옹",
    "meow",
    "miaou",
    "miau",
    "miau",
    "miao",
    "喵喵",
    "ニャーニャー",
    "мяу",
    "miau",
    "مواء",
    "מיאו",
    "meong",
    "เหมียว",
    "meo meo"
]


class State(rx.State):

    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    def answer(self):
        # Our chatbot has some brains now!
        # session = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     messages=[
        #         {"role": "user", "content": self.question}
        #     ],
        #     stop=None,
        #     temperature=0.7,
        #     stream=True,
        # )

        answers = random.choices(cat_meow_list, k=1)

        self.chat_history.append((self.question, answers))
        self.chat_history[-1] = (
            self.question,
            ",".join(answers),
        )
        yield
        # for item in session:
        #     if hasattr(item.choices[0].delta, "content"):
        #         answer += item.choices[0].delta.content
        #         self.chat_history[-1] = (
        #             self.question,
        #             answer,
        #         )
        #         yield
