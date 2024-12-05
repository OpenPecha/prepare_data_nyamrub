import re 
import os 
import anthropic
from pathlib import Path 


ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not ANTHROPIC_API_KEY:
    raise ValueError("Please set ANTHROPIC_API_KEY environment variable")

def get_claude_response(prompt: str):
    # Initialize the client with your API key
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    # Create a message request
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",  # Specify the model version
        max_tokens=1000,  # Set maximum tokens for the response
        temperature=0.5,  # Adjust randomness of responses (0.0 for deterministic)
        system="You are a helpful assistant.",  # System message for context
        messages=[{"role": "user", "content": prompt}],
    )

    # Print the response content
    return response.content[0].text