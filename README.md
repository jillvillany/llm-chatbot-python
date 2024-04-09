# Build an Neo4j-backed Chatbot using Python

This repository accompanies the link:https://graphacademy.neo4j.com/courses/llm-chatbot-python/?ref=github[Build an Neo4j-backed Chatbot using Python^] course on link:https://graphacademy.neo4j.com/?ref=github[Neo4j GraphAcademy^].

For a complete walkthrough of this repository, link:https://graphacademy.neo4j.com/courses/llm-chatbot-python/?ref=github[enrol now^].

# Setup
## Create OpenAI and NEO4J Environment Variables
- Create a `.streamlit/secrets.toml` file
- Add the following values:
```
OPENAI_API_KEY = ""
OPENAI_MODEL = "gpt-3.5-turbo"

NEO4J_URI = ""
NEO4J_USERNAME = ""
NEO4J_PASSWORD = ""
```
**NOTE:** You must create an OpenAI account to generate an OpenAI API Key. The Neo4j login info is a sandbox account from the graphacademy course.

## Create IBM Cloud API Key
- Login to the IBM Cloud console: https://cloud.ibm.com/login?state=%2Fdocs%2Faccount%3Ftopic%3Daccount-userapikey%26interface%3Dui
- Select Manage > Access (IAM)
- On the IAM page, select API keys from the side menu
- Click "Create" button
- Name the API Key "llm-chatbot-python" and click the "Create" button
- Click the "Copy" button to copy the API Key that is generated
    - Add to the `.streamlit/secrets.toml` file `IBM_CLOUD_API_KEY=""`

## Create Watsonx Project
- Navigate to the Watsonx Projects Page: https://dataplatform.cloud.ibm.com/projects/?context=wx
- Click the "New Project" button
- Name it "llm-chatbot-python"
- Click the "Create" button
- Navigate to the "Manage" tab and copy the "Project ID"
    - Add to the `.streamlit/secrets.toml` file `WATSONX_PROJECT_ID=""`
- Navigate to the "Services & integrations" side tab
- Click the "Associate service" button
- Select WatsonMachineLearning and click the "Associate" button

## Create Python Environment
```
conda create -n neo_llm python=3.11
conda activate neo_llm
poetry install
```

# Run Streamlit App
Enter the command `streamlit run bot.py` to start the app on: http://localhost:8501/[http://localhost:8501/^].

# Lessons Learned
- Context window of LLM may impact ability of langchain agent executor to function properly - i.e. instructions may get cut off