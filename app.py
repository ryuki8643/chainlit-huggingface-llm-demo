import chainlit as cl


import models.facebook_blenderbot_400m as model

@cl.on_message
def main(message: str):

    model_output_message=model.chat_message(message)
    
    cl.Message(
        content=model_output_message,
    ).send()