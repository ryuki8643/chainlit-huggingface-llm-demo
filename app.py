import chainlit as cl


import models.facebook_blenderbot_400m as model

#falcon models are big and need a lot of ram and gpu and disk space especially 40b
# import models.tiiuae_falcon_7b as model
# import models.tiiuae_falcon_40b as model


@cl.on_chat_start
def main():

    cl.Message(
        content=f"My name is {model.name()}",
    ).send()

@cl.on_message
def main(message: str):

    model_output_message=model.chat_message(message)

    cl.Message(
        content=model_output_message,
    ).send()