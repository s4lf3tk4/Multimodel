from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, BaseMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List, Literal
from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os


class SystemState(TypedDict):
    current_message: str
    messages: List[BaseMessage]
    message_type: str
    should_continue: bool

#pydantic

class MessageClassify(BaseModel):
    message_type: Literal["code", "dialog", "local"] = Field(
        description = "Тип задачи: code - программирование, dialog - общение, local - российские реалии"
    )
    confidence: float = Field(
        description = "Уверенность в классификации от 0.0 До 1.0",
        ge = 0.0, le = 1.0
    )

#классификация
classification_parser = JsonOutputParser(pydantic_object = MessageClassify)
classification_prompt = PromptTemplate(template = """Определи тип задачи пользователя:
    CODE - вопросы про программирование, отладку, код, алгоритмы, технологии
    DIALOG - обычные вопросы, просьбы о помощи, общение, объяснения
    LOCAL - вопросы про Россию, российские законы, локальные особенности, госуслуги

    Вопрос: {user_input}

    {format_instructions}

    Верни ТОЛЬКО JSON!
""",
    input_variables = ["user_input"],
    partial_variables={"format_instructions": classification_parser.get_format_instructions()}
)

#llm
llm = ChatOllama(
    model="mistral",
    num_predict=2000
)
