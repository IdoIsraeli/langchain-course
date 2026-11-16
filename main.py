from dotenv import load_dotenv
#from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch
#from tavily import TavilyClient

load_dotenv()


# tavily = TavilyClient()

# @tool
# def search(query: str) -> str:
#     """
#     tool that serches the internet
#     Args:
#         query: query to search
#     Returns: 
#         the search result
#     """
#     print(f"searching for {query}")
#     return tavily.search(query=query)
#tools = [search]

tools=[TavilySearch()]
llm = ChatGoogleGenerativeAI(model= "gemini-3.5-flash" )
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course! please hold")
    res = agent.invoke(
        {
            "messages":HumanMessage(
                content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details?"
            )
        }
    )
    print(res)

if __name__ == "__main__":
    main()
