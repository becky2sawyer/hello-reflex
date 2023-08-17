# state.py
import reflex as rx
import os
import openai
import numpy as np
import random


# openai.api_key = os.environ["OPENAI_API_KEY"]
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

word = ['공산전체주의 세력', '맹종', '자유', '한·미·일 3국 공조', '조작선동', '반국가세력', '일본은 파트너', '위장', '야비', '패륜']


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

        meows = random.choices(cat_meow_list, k=2)
        words = random.choices(word, k=3)
        meows_words = meows + words
        random.shuffle(meows_words)
        answers = " ".join(meows_words)
        self.chat_history.append((self.question, answers))
        self.chat_history[-1] = (
            self.question,
            answers,
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
