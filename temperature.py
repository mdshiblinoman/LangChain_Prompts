from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model='gemini-2.5-flash', temperature=1.5)

result = model.invoke("Write a 5 line poem on cricket")

print(result)
