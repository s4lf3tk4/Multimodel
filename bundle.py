from langchain_core.messages import BaseMessage
from typing import TypedDict, List, Literal
from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

#общее состояние
class SystemState(TypedDict):
    current_message: str
    messages: List[BaseMessage]
    message_type: str
    should_continue: bool
    code: str
    local: str
    dialog: str

#pydantic
class MessageClassify(BaseModel):
    message_type: Literal["code", "dialog", "local", "over"] = Field(
        description = "Тип сообщения: code - программирование, dialog - общение, local - российские реалии, over - завершение диалога"
    )
    confidence: float = Field(
        description = "Уверенность в классификации от 0.0 До 1.0",
        ge = 0.0, le = 1.0
    )

#классификация
classification_parser = JsonOutputParser(pydantic_object = MessageClassify)
classification_prompt = PromptTemplate(template = """Определи тип сообщения пользователя:
    CODE - сообщение про программирование, отладку, код, алгоритмы, технологии
    DIALOG - обычное сообщение, просьбы о помощи, общение, объяснения
    LOCAL - сообщение про Россию, российские законы, локальные особенности, госуслуги, вопросы по формлению каких-то документов(например: загранпаспорт или получение выписки по счету)
    OVER - пользователь прощается, явно говрит пока, до скидания, благодарит за предоставленные ответы (например: Спасибо за информативный диалог, было приятно пообщаться!)

    Сообщение: {user_input}

    {format_instructions}

    Верни ТОЛЬКО JSON!
""",
    input_variables = ["user_input"],
    partial_variables={"format_instructions": classification_parser.get_format_instructions()}
)

class AnalyzeDialog(BaseModel):

    key_topics: List[str] = Field(
        description="Ключевые темы диалога"
    )
    summary: str = Field(
        description="Краткое резюме в одном предложении",
        max_length=150
    )

analyzeDialog_parser = JsonOutputParser(pydantic_object = AnalyzeDialog)
analyzeDialog_prompt = PromptTemplate(template = """
    Проанализируй данные ответы:

    {combined}

    Выдели ключевые темы и дай краткое резюме в одном предложении.

    {format_instructions}

    Верни ТОЛЬКО JSON!
    """,
    input_variables = ["combined"],
    partial_variables={"format_instructions": analyzeDialog_parser.get_format_instructions()}
)
