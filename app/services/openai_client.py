import json
from openai import OpenAI
from app.config import settings

# Initialize client once
client = OpenAI(api_key=settings.OPENAI_API_KEY)


def generate_summary(transcript_text: str) -> dict:
    """
    Convert raw transcript to structured summary JSON.
    """
    prompt = f"""
    Extract structured info from this logistics call transcript:
    {transcript_text}
    Return JSON: call_outcome, driver_status, current_location, eta, emergency_type, emergency_location, escalation_status
    """

    try:
        resp = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        content = resp.choices[0].message.content
        return json.loads(content)
    except json.JSONDecodeError:
        return {"error": "Failed to parse summary"}
    except Exception as e:
        return {"error": str(e)}
