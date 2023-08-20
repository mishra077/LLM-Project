import chainlit as cl
import openai
import os

os.environ['OPEN_AI_KEY'] = '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'
openai.api_key = os.environ['OPEN_AI_KEY']

@cl.on_message
async def main(message : str):

    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = [
            {"role" : "assistant", "content" : "you are a helpful assistant that is obsessed with the color blue"},
            {"role" : "user", "content" : message}
        ],
        temperature = 1,
    )

    await cl.Message(
        content = f"{response['choices'][0]['message']['content']}",
    ).send()