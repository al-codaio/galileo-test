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
relevant_documents = [
    """
    Galileo is the fastest way to ship reliable apps.
    Galileo brings automation and insight to AI evaluations so you can
    ship with confidence.
    """,
    """
    Galileo has Automated evaluations
    Eliminate 80% of evaluation time by replacing manual reviews
    with high-accuracy, adaptive metrics. Test your AI features,
    offline and online, and bring CI/CD rigor to your AI workflows.
    """,
    """
    Galileo allows Rapid iteration
    Ship iterations 20% faster by automating testing numerous
    prompts and models. Find the best performance for any given
    test set. When something breaks, Galileo helps identify
    failure modes and root cause.
    """
]

system_prompt = f"""
You are a helpful assistant that wants to provide a user as much information
as possible. Avoid saying I don't know.

Here is some relevant information:
{relevant_documents}
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