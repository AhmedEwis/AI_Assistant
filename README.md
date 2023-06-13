# AI-chatbot 🤖

[![Twitter Follow](https://img.shields.io/twitter/follow/sor3a95?style=social)](https://twitter.com/sor3a95)
[![Last Commit](https://img.shields.io/github/last-commit/AhmedEwis/AI_Assistant)](https://github.com/AhmedEwis/AI_Assistant/commits/main)


### An AI chatbot featuring conversational memory, designed to enable users to discuss their CSV, PDF and TXT data in a more intuitive manner. 📄
![AI_Assistant](AI_Assistant.png)

By integrating the strengths of Langchain and OpenAI, AI_Assistant employs large language models to provide users with seamless, 
context-aware natural language interactions for a better understanding of their data.🧠
## Quick Start 🚀

[![AI_Assistant](https://img.shields.io/static/v1?label=AI_Assistant&message=Visit%20Website&color=ffffff&labelColor=ADD8E6&style=for-the-badge)](https://ahmedewis-ai-assistant-srchome-jfcir5.streamlit.app/)


## TO-DO :
- [x] enable print tokens utilizations for the conversation
- [x] Use CSV Agent for chat with the entire csv file
- [ ] Add lots of files accepted like GitHub repo, Excel etc...
- [ ] Run falcon-40b-instruct and falcon-40b on a custom dataset
- [ ] Add free models like vicuna and free embeddings
- [ ] Replace chain of the chatbot by a custom agent for handling more features | memory + vectorstore + custom prompt

## Running Locally 💻
Follow these steps to set up and run the service locally :

### Prerequisites
- Python 3.8 or higher
- Git

### Installation
Clone the repository :

`git clone https://github.com/AhmedEwis/AI_Assistant.git`


Navigate to the project directory :

`cd AI_Assistant`


Create a virtual environment :
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

Install the required dependencies in the virtual environment :

`pip install -r requirements.txt`


Launch the chat service locally :

`streamlit run src/Home.py`

#### That's it! The service is now up and running locally. 🤗

## Contributing 🙌
Contributions are always welcome! If you want to contribute to this project, please open an issue, submit a pull request or contact me at ahmed.ewis.ml@gmail.com (:


