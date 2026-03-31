from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from app.core.config import settings
from app.core.database import get_schema_info, execute_query
from pathlib import Path
import re


# Grok is OpenAI-compatible, so we use ChatOpenAI with custom base_url
def get_llm():
    return ChatOpenAI(
        model=settings.GROQ_MODEL,
        api_key=settings.GROQ_API_KEY,
        base_url="https://api.groq.com/openai/v1",
        temperature=0,
    )


_prompt_path = Path(__file__).parent.parent.parent / "prompts" / "sql_generation.md"
_prompt_template = _prompt_path.read_text(encoding="utf-8")

SQL_GENERATION_PROMPT = PromptTemplate(
    input_variables=["schema", "question"],
    template=_prompt_template,
)


def clean_sql(raw: str) -> str:
    """Strip markdown fences and whitespace from LLM output."""
    raw = raw.strip()
    # Remove ```sql ... ``` or ``` ... ```
    raw = re.sub(r"```(?:sql)?", "", raw, flags=re.IGNORECASE).strip("`").strip()
    return raw


def validate_sql(sql: str) -> None:
    """
    Basic safety check — only allow SELECT statements.
    Raises ValueError if the query is not a SELECT.
    """
    normalized = sql.strip().upper()
    forbidden = ["INSERT", "UPDATE", "DELETE", "DROP", "TRUNCATE", "ALTER", "CREATE"]
    for keyword in forbidden:
        if normalized.startswith(keyword) or f" {keyword} " in normalized:
            raise ValueError(f"Unsafe SQL detected: '{keyword}' is not allowed.")
    if not normalized.startswith("SELECT"):
        raise ValueError("Only SELECT queries are allowed.")


async def natural_language_to_sql(question: str) -> dict:
    """
    Full pipeline:
    1. Get DB schema
    2. Send question + schema to Grok via LangChain
    3. Clean and validate the generated SQL
    4. Execute the SQL
    5. Return results
    """
    # Step 1: Get schema
    schema = get_schema_info()

    # Step 2: Generate SQL using Grok
    llm = get_llm()
    chain = LLMChain(llm=llm, prompt=SQL_GENERATION_PROMPT)
    raw_sql = await chain.arun(schema=schema, question=question)

    # Step 3: Clean SQL
    sql = clean_sql(raw_sql)

    # Step 4: Validate SQL (safety check)
    validate_sql(sql)

    # Step 5: Execute
    results = execute_query(sql)

    return {
        "question": question,
        "generated_sql": sql,
        "results": results,
        "row_count": len(results),
    }
