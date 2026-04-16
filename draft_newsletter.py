import sys, os
from datetime import date
from openai import OpenAI

# 1. Setup Topic
topic = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "AI trends"

# 2. Initialize OpenAI Client 
# (It will automatically look for the OPENAI_API_KEY environment variable)
client = OpenAI()

try:
    response = client.chat.completions.create(
        model="gpt-5.4", # Using the 2026 flagship model
        messages=[
            {
                "role": "system", 
                "content": "You are a professional newsletter editor."
            },
            {
       
                "role": "user",
                "content": f"""Write a short, engaging newsletter edition about: {topic}

Format it like this:
# [Catchy headline]

**This week:** One sentence summary

## The story
2-3 paragraphs covering the key points, written in a friendly, readable tone.

## Why it matters
1-2 sentences on the bigger picture.

## Quick takeaway
One actionable insight the reader can use.

---
*Drafted by OpenClaw Newsletter Skill*"""
            }
        ]
    )

    content = response.choices[0].message.content

    # 3. Handle File Saving
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "newsletters")
    os.makedirs(output_dir, exist_ok=True)

    filename = f"{date.today()}-{topic[:30].replace(' ', '-').lower()}.md"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w") as f:
        f.write(content)

    print(f"Newsletter saved to: {filepath}")
    print(f"Preview:\n{content[:200]}...")

except Exception as e:
    print(f"Error generating newsletter: {e}")

