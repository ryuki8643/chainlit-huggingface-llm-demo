#If you use only cpu throw error https://huggingface.co/tiiuae/falcon-40b/discussions/3
#you have to have enough ram and gpu to run this model

from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

model = "tiiuae/falcon-7b"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
"text-generation",
model=model,
tokenizer=tokenizer,
torch_dtype=torch.bfloat16,
trust_remote_code=True,

#if you didn't configure your gpu you delete this line but too many ram will be used so it is not recommended
#you should setup to use gpu by pytorch
device_map="auto",
)



def name():
    return __file__.split("/")[-1].replace(".py","")


def chat_message(message: str):

    sequences = pipeline(
    message,
    max_length=200,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
    )

    return sequences[0]['generated_text']