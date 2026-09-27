import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq 

load_dotenv()

async def analyze_competitor(scraped_text: str) -> str:
    
    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.7, 
        groq_api_key=os.getenv("GROQ_API_KEY") 
    )
    
    prompt = f"""
    You are an expert business analyst. 
    I have scraped the following text from a competitor's website.
    
    TEXT:
    {scraped_text[:2000]}  # <--- CHANGED FROM 10000 TO 2000 TO PREVENT CONTEXT ERRORS
    
    TASK:
    Analyze this text and provide a brief, high-level strategic summary.
    CRITICAL: Do not just output a number or a single word. You must write a full text report.
    Format your response in Markdown with the following headers:
    ### 🎯 Core Value Proposition
    ### 💰 Pricing & Tiers (if mentioned)
    ### 🚀 New Features or Updates
    ### 💡 Strategic Insight (One sentence on how we can beat them)
    """
    
    response = await llm.ainvoke(prompt)
    
    return response.content