import chainlit as cl


import torch

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("facebook/blenderbot-400M-distill")

model = AutoModelForSeq2SeqLM.from_pretrained("facebook/blenderbot-400M-distill")

def chat_message(message: str):

    input_ids = tokenizer(message, return_tensors="pt").input_ids
    generation_output = model.generate(
            input_ids=input_ids
        )
    model_output_message=tokenizer.decode(generation_output[0])
    model_output_message=model_output_message.replace("<s>","").replace("</s>","")

    return model_output_message
