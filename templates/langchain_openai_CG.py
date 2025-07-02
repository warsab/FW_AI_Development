# ___________________________________________// LangChain & OpenAI Agent Template ________

# ====== Importing Libraries:
import os
from typing import List
from langchain_openai import ChatOpenAI

# ====== Config (parameters and constants):
MODEL_NAME = "gpt-4-turbo"  # Change to other models if need be (e.g. gpt-4o, gpt-4o-mini, etc.)
TEMPERATURE = 0.7 # Because this specific agent is creative, randomness set accordinly 
MAX_TOKENS = 2000 # Set max tokens accordinly

# ====== Set up API Key (use environment variable, not hardcoded)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY"):
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set. Please check your .env file.")

# ====== LLM instance (LangChain wrapper):
llm = ChatOpenAI(model = MODEL_NAME, temperature = TEMPERATURE, max_tokens = MAX_TOKENS, openai_api_key = OPENAI_API_KEY)

# ====== General writing structure (customize as needed):
general_writing_structure = """
Write in a tone: Friendly with a banter personality, slightly promotional, but fact-based.
Maintain variety in structure......
"""

# ====== Agent role description (customize as needed):
'''
This will be the system prompt for the ai agent.
'''
def get_role_description(topic: str) -> str:
    return f'''
Role: AI Content Generator

You will be given a topic from the user, and you will need to generate a response based on the instructions.

Your task:
- Follow the user's instructions
- Use the specified tone and structure

Inputs:
- Topic: {topic}
- No-intro/no-conclusion rules (if any)

Output:
- Structured, relevant content
'''

# ====== Pipeline Agent Function
def agent_generate_content(topic: str, user_instruction: str, extra_context: str = "") -> str:
    """
    Generate content using LangChain's ChatOpenAI agent.
    Args:
        topic (str): The main topic for generation.
        user_instruction (str): Specific instructions for the agent.
        extra_context (str): Any extra context or data to provide.
    Returns:
        str: The generated content.
    """
    system_prompt = get_role_description(topic) + "\n" + general_writing_structure
    user_prompt = f"Instruction: {user_instruction}\nContext: {extra_context}"
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    return llm.invoke(messages).content.strip()

# ====== Refinement Agent Function
def agent_refine_content(content: str, company_data: dict | None = None, refinement_rules: str = "") -> str:
    """
    Refine and improve content using LangChain's ChatOpenAI agent.
    Args:
        content (str): The original content to refine.
        company_data (dict): Company-specific data and rules (e.g., brand guidelines, tone, etc.).
        refinement_rules (str): Additional refinement rules or requirements.
    Returns:
        str: The refined and improved content.
    """
    # Build company-specific context
    company_context = ""
    if company_data:
        company_context = f"""
Company Information:
- Brand Guidelines: {company_data.get('brand_guidelines', 'N/A')}
- Tone of Voice: {company_data.get('tone', 'N/A')}
- Target Audience: {company_data.get('target_audience', 'N/A')}
- Industry: {company_data.get('industry', 'N/A')}
- Key Messaging: {company_data.get('key_messaging', 'N/A')}
"""
    
    system_prompt = f"""
You are an expert content refinement specialist. Your job is to:

1. CHECK FOR ERRORS:
   - Grammar and spelling mistakes
   - Factual inaccuracies
   - Inconsistent formatting
   - Logical flow issues

2. IMPROVE STRUCTURE:
   - Ensure proper paragraph breaks
   - Check for clear headings and subheadings
   - Verify logical content flow
   - Optimize readability

3. INCORPORATE COMPANY DATA:
   - Apply brand guidelines
   - Match company tone of voice
   - Include relevant company messaging
   - Align with target audience

4. ENHANCE QUALITY:
   - Make content more engaging
   - Improve clarity and conciseness
   - Ensure professional standards
   - Optimize for intended purpose

{company_context}

Additional Refinement Rules:
{refinement_rules}

IMPORTANT: Rewrite the entire content with improvements while maintaining the core message and intent.
"""

    user_prompt = f"""
Please refine the following content according to the guidelines above:

ORIGINAL CONTENT:
{content}

Please provide the refined version with all improvements applied.
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    return llm.invoke(messages).content.strip()

# ====== Complete Pipeline Function
def full_content_pipeline(topic: str, user_instruction: str, extra_context: str = "", 
                         company_data: dict | None = None, refinement_rules: str = "") -> str:
    """
    Complete content generation and refinement pipeline.
    Args:
        topic (str): The main topic for generation.
        user_instruction (str): Specific instructions for the agent.
        extra_context (str): Any extra context or data to provide.
        company_data (dict): Company-specific data and rules.
        refinement_rules (str): Additional refinement rules.
    Returns:
        str: The final refined content.
    """
    print("Step 1: Generating initial content...")
    initial_content = agent_generate_content(topic, user_instruction, extra_context)
    
    print("Step 2: Refining content...")
    refined_content = agent_refine_content(initial_content, company_data, refinement_rules)
    
    return refined_content

# ====== Example Usage
if __name__ == "__main__":
    # Example company data
    company_info = {
        "brand_guidelines": "Professional, trustworthy, innovative",
        "tone": "Friendly yet authoritative",
        "target_audience": "Tech-savvy business professionals",
        "industry": "Technology consulting",
        "key_messaging": "Digital transformation, efficiency, growth"
    }
    
    # Example refinement rules
    refinement_rules = """
    - Use active voice where possible
    - Include at least one specific example
    - Keep paragraphs under 3 sentences
    - Use bullet points for lists
    """
    
    topic = "Benefits of AI in Business"
    instruction = "List three key benefits and provide a short example for each."
    extra = "Audience: Small business owners."
    
    # Use the complete pipeline
    final_output = full_content_pipeline(
        topic=topic,
        user_instruction=instruction,
        extra_context=extra,
        company_data=company_info,
        refinement_rules=refinement_rules
    )
    
    print("Final Refined Content:\n", final_output)
