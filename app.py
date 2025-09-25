from galileo import galileo_context
from galileo.openai import openai
from galileo.config import GalileoPythonConfig
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set the project and Log stream, these are created if they don't exist.
# You can also set these using the GALILEO_PROJECT and GALILEO_LOG_STREAM
# environment variables.
galileo_context.init(project="MyFirstEvaluation",
                     log_stream="MyFirstLogStream")

# Initialize the Galileo OpenAI client wrapper
client = openai.OpenAI()

# Define a system prompt with guidance
system_prompt = f"""
You are a helpful assistant that wants to provide a user as much
information as possible. Avoid saying I don't know.
"""

# Define a user prompt with a question
user_prompt = "Describe Galileo"

# Send a request to the LLM
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
)

# Print the response
print(response.choices[0].message.content.strip())

# Show Galileo information after the response
config = GalileoPythonConfig.get()
logger = galileo_context.get_logger_instance()
project_url = f"{config.console_url}project/{logger.project_id}"
log_stream_url = f"{project_url}/log-streams/{logger.log_stream_id}"

print()
print("🚀 GALILEO LOG INFORMATION:")
print(f"🔗 Project   : {project_url}")
print(f"📝 Log Stream: {log_stream_url}")