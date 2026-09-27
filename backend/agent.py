import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

async def analyze_competitor(scraped_text: str) -> str:
    
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.3, # Low temperature (0.0 to 1.0) means the AI will be more factual and less "creative/hallucinatory".
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    
    prompt = f"""
    You are an expert business analyst. 
    I have scraped the following text from a competitor's website.
    
    TEXT:
    {scraped_text[:10000]} 
    *(Note: We limit to 10,000 characters to save time/tokens, but Gemini can handle much more!)*
    
    TASK:
    Analyze this text and provide a brief, high-level strategic summary.
    Format your response in Markdown with the following headers:
    ### 🎯 Core Value Proposition
    ### 💰 Pricing & Tiers (if mentioned)
    ### 🚀 New Features or Updates
    ### 💡 Strategic Insight (One sentence on how we can beat them)
    """
    
    response = await llm.ainvoke(prompt)
    
    return response.content