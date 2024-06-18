from openai import OpenAI

# To fetch the API key stored as an environment variable.
import os
import time
api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI()

# Instruction to ChatGPT on how to comment
instructions_string = "MBGPT, functioning as a virtual data science \
consultant on YouTube, communicates in clear, accessible language, escalating \
to technical depth upon request. \
It reacts to feedback aptly and concludes with its signature '–MBGPT'. \
MBGPT will tailor the length of its responses to match the viewer's comment, \
providing concise acknowledgments to brief expressions of gratitude or \
feedback, thus keeping the interaction natural and engaging."

# Create an assistant entity
assistant = client.beta.assistants.create(
    name = "MBBPT",
    description="Data scientist GPT for YouTube comments",
    instructions = instructions_string,
    # toos = ""
    model = "gpt-4-0125-preview"
)

# Create a discussion thread
thread = client.beta.threads.create()

# Adding user message to the thread
message = client.beta.threads.messages.create(
    thread_id = thread.id,
    role = "user",
    # content = "Great Content, thank you!"
    content = "Worst content"
)


# Run object handles message passing between user and assistant
run = client.beta.threads.runs.create(
    thread_id = thread.id,
    assistant_id = assistant.id
)


# Helper function to wait for assistant completion
def wait_for_assistant(thread, run):
    t0 = time.time()
    while(run.status!= 'completed'):
        #again retrieve the fresh run object, and wait for .25 seconds for another condition check
        run = client.beta.threads.runs.retrieve(
            thread_id = thread.id,
            run_id = run.id
        )
        time.sleep(0.25)
    dt = time.time()-t0
    print("Elapsed time: " + str(dt) + " seconds")
    return run


run = wait_for_assistant(thread, run)
run_dict = dict(run)  
print(run_dict)
print("\n")
print(thread)
print("\n")

# Access list of all messages in the thread
messages = client.beta.threads.messages.list(
    thread_id= thread.id
)
print(messages.data[0].content[0].text.value)

#refer this https://platform.openai.com/docs/api-reference/messages/listMessages, and https://platform.openai.com/docs/api-reference/messages/createMessage







