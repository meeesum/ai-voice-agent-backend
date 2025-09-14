import openai
from ..config import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_summary(transcript_text: str) -> dict:
    """
    Convert raw transcript to structured summary JSON.
    """
    prompt = f"""
    Extract structured info from this logistics call transcript:
    {transcript_text}
    Return JSON: call_outcome, driver_status, current_location, eta, emergency_type, emergency_location, escalation_status
    """

    resp = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    content = resp.choices[0].message.content
    try:
        import json
        return json.loads(content)
    except:
        return {"error": "Failed to parse summary"}
