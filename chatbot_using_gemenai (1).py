

!pip install google-generativeai

import google.generativeai as genai

genai.configure(
    api_key='YOUR API KEY'
)

model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])

while(True):
  question=input("VIR:")
  if(question.strip()==''):
    break
  print('\n')
  response=chat.send_message(question)
  print(f"Vir: {response.text}")
  print('\n')

