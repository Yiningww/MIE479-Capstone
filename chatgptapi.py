import openai
import os
import pandas as pd
import time
openai.api_key = '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'

def get_completion(prompt, model="gpt-4"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=0,
    )
    return response.choices[0].message["content"]

prompt = "Explain PCA to me?"
response = get_completion(prompt)
print(response)