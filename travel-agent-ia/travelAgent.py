import os
from langchain_openai import ChatOpenAI
from langchain_community.agent.toolkits.load_tools import load_tools # Carrega as ferramentas para que o agente tenha acesso a elas
from langchain.agents import initialize_agent # Inicializa o agente

llm = ChatOpenAI(model="gpt-3.5-turbo")

tools = load_tools(['ddg-search', 'wikipedia'], llm=llm)

agent = initialize_agent(
  tools,
  llm,
  agent='zero-shot-react-description',
  verbose = True
)

query = """
Vou viajar para Londres em agosto de 2024. Quero que faça um roteiro de viagens para mim com eventos que irão ocorrer na data da viagem e com o preço de passagem de São Paulo para Londres.
"""

agent.run(query)