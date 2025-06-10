import os
import openai
from dotenv import load_dotenv

# Load environment
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY") or ""

def summarize_measurements(measurements, filename):
    prompt = f"""
Image: {filename}
Detected nails (JSON):
{measurements}

Write a concise report:
- Total count
- Average length & weight
- List each nail with length & weight
- Final summary sentence.
"""
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system","content":"Format JSON into a human-friendly report."},
            {"role":"user","content":prompt}
        ],
        temperature=0.7
    )
    return resp.choices[0].message.content.strip()
