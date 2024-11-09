import ollama
import re
from datetime import datetime, timedelta
from typing import List, Tuple, Dict

def get_current_date():
    """Returns the current date in YYYY-MM-DD format."""
    return datetime.now().strftime("%Y-%m-%d")

def analyze_user_intent(input_text: str, cycle_num: int) -> str:
    """
    Analyzes user intent based on input text.
    Different approaches for different cycles.
    
    :param input_text: User's text
    :param cycle_num: Cycle number (1, 2, or 3)
    :return: String with user intent
    """
    prompts = {
        1: f"""
        Analyze the user's text and determine their main intent.
        Focus on the basic goal of the request.
        
        Main steps:
        1. Find key words
        2. Determine request type (informational, analytical, creative)
        3. Determine main topic
        4. Formulate goal in one sentence
        
        Don't repeat the request text, create a new intent formulation.
        
        User text: {input_text}
        Intent:
        """,
        
        2: f"""
        Consider the following user text from an expert's perspective
        and determine the deeper intent of the request.
        
        In analysis consider:
        1. Request context
        2. Possible implicit goals
        3. Expected response format
        4. Level of detail
        5. Potential related interests
        
        Formulate intent differently than in the explicit request.
        
        User text: {input_text}
        Deep intent:
        """,
        
        3: f"""
        Conduct a comprehensive analysis of the user's request.
        Determine the broadest possible context of the request.
        
        Consider:
        1. Explicit and implicit goals
        2. Possible request prerequisites
        3. Related topics
        4. Potential follow-up questions
        5. Practical application of information
        
        Provide an expanded interpretation of user intent.
        
        User text: {input_text}
        Expanded intent:
        """
    }
    
    try:
        intent_response = ollama.generate(
            model='gemma2:9b', 
            prompt=prompts[cycle_num]
        )
        return intent_response['response'].strip()
    except Exception:
        return None

def generate_llm_prompt(input_text: str, user_intent: str, cycle_num: int) -> str:
    """
    Generates an effective prompt for LLM.
    Different generation approaches for different cycles.
    
    :param input_text: User's text
    :param user_intent: User's intent
    :param cycle_num: Cycle number (1, 2, or 3)
    :return: Generated prompt
    """
    current_date = datetime.now()
    
    templates = {
        1: f"""
        Create a basic prompt to get a direct answer to the user's request.
        
        Rules:
        1. Clear formulation of the main question
        2. Specification of desired response format
        3. Minimum necessary clarifications
        
        Text: {input_text}
        Intent: {user_intent}
        Date: {current_date.strftime("%Y-%m-%d")}
        
        Generate prompt:
        """,
        
        2: f"""
        Create a detailed prompt to get an elaborate response.
        
        Requirements:
        1. Information structuring
        2. Request for additional context
        3. Clarification of related aspects
        4. Indication of need for explanations
        
        Text: {input_text}
        Intent: {user_intent}
        Date: {current_date.strftime("%Y-%m-%d")}
        
        Generate prompt:
        """,
        
        3: f"""
        Create a comprehensive prompt for complete topic analysis.
        
        Include requirements:
        1. Coverage of all topic aspects
        2. Examples and illustrations
        3. Practical application
        4. Connection with other topics
        5. Perspectives and trends
        
        Text: {input_text}
        Intent: {user_intent}
        Date: {current_date.strftime("%Y-%m-%d")}
        
        Generate prompt:
        """
    }
    
    try:
        prompt_response = ollama.generate(
            model='gemma2:9b',
            prompt=templates[cycle_num]
        )
        return prompt_response['response'].strip()
    except Exception:
        return None

def get_llm_response(prompt: str, cycle_num: int) -> str:
    """
    Gets response from the language model.
    Different approaches for different cycles.
    
    :param prompt: Prepared prompt
    :param cycle_num: Cycle number
    :return: Model response
    """
    try:
        # Add cycle-specific instructions
        cycle_instructions = {
            1: "Provide a direct and concise answer to the question.",
            2: "Provide a detailed response with explanations.",
            3: "Create a complete topic analysis with examples and context."
        }
        
        full_prompt = f"{cycle_instructions[cycle_num]}\n\n{prompt}"
        
        response = ollama.generate(
            model='gemma2:9b',
            prompt=full_prompt
        )
        return response['response'].strip()
    except Exception as e:
        return f"Error getting response from model: {str(e)}"

def post_process_prompt(prompt: str) -> str:
    """Processes the received prompt."""
    prompt = prompt.strip('"').strip("'")
    prompt = re.sub(r'^(prompt:)\s*', '', prompt, flags=re.IGNORECASE)
    prompt = re.sub(r'\s+', ' ', prompt)
    return prompt.strip()

def validate_prompt(prompt: str) -> bool:
    """Checks prompt validity."""
    return bool(prompt) and len(prompt.split()) >= 3

def process_single_cycle(user_input: str, cycle_num: int) -> Dict[str, str]:
    """
    Executes one complete request processing cycle.
    
    :param user_input: User's text
    :param cycle_num: Cycle number
    :return: Dictionary with cycle results
    """
    print(f"\nCycle {cycle_num}:")
    
    # Intent analysis considering cycle number
    print("Analyzing intent...")
    intent = analyze_user_intent(user_input, cycle_num)
    if not intent:
        raise Exception("Failed to determine user intent")
    print(f"Intent: {intent}")

    # Prompt generation
    print("Generating prompt...")
    llm_prompt = generate_llm_prompt(user_input, intent, cycle_num)
    if not llm_prompt:
        raise Exception("Failed to generate prompt")
    final_prompt = post_process_prompt(llm_prompt)
    if not validate_prompt(final_prompt):
        raise Exception("Generated prompt is incorrect")
    print(f"Prompt: {final_prompt}")

    # Getting response
    print("Getting response...")
    response = get_llm_response(final_prompt, cycle_num)
    if not response:
        raise Exception("Failed to get model response")
    print(f"Response: {response}")

    return {
        "intent": intent,
        "prompt": final_prompt,
        "response": response
    }

def synthesize_final_answer(cycles: List[Dict[str, str]], original_query: str) -> str:
    """
    Creates final synthesized answer based on three cycles.
    
    :param cycles: List of dictionaries with results from each cycle
    :param original_query: Original user query
    :return: Synthesized answer
    """
    synthesis_prompt = f"""
    Based on the provided information, create a complete but well-structured response 
    to the user's question: "{original_query}"

    Answer creation rules:
    1. Start with a brief, direct answer to the question (main figures/facts)
    2. Structure information by sections:
       - Basic information
       - Chronology and evolution
         * Early period
         * Development period
         * Modern stage
       - Significant works and achievements
       - Impact and significance
       - Interesting facts and details
    3. Provide detailed information in each section
    4. Use subheadings for better navigation
    5. Include all significant aspects from provided sources
    
    Information from sources:
    ---
    Basic answer:
    {cycles[0]['response']}
    ---
    Detailed answer:
    {cycles[1]['response']}
    ---
    Complete analysis:
    {cycles[2]['response']}
    ---

    Answer requirements:
    - Use markdown formatting for better readability
    - Preserve all important information from sources
    - Organize information logically
    - Use lists and subheadings
    - Highlight key points
    
    Don't mention the analysis process or information sources - 
    just provide a complete, well-organized answer.
    """

    try:
        synthesis_response = ollama.generate(model='gemma2:9b', prompt=synthesis_prompt)
        return synthesis_response['response'].strip()
    except Exception as e:
        return f"Error synthesizing final answer: {str(e)}"

def process_user_input(user_input: str) -> Tuple[List[Dict[str, str]], str]:
    """
    Processes user input with three responses and final synthesis.
    
    :param user_input: User's text
    :return: Tuple[list of cycle results, synthesized answer]
    """
    if not user_input:
        return [], "Please enter text for prompt creation."

    # Execute three independent cycles
    cycles = []
    for i in range(3):
        cycle_results = process_single_cycle(user_input, i + 1)
        cycles.append(cycle_results)

    # Create final synthesis
    final_synthesis = synthesize_final_answer(cycles, user_input)

    return cycles, final_synthesis

def main():
        
    print("\nDeepChain Refinement LLM v1.0.0:")
    print("Using chain-of-thought, multi-step prompting,")
    print("progressive refinement and response synthesis")
    print("Built on Ollama architecture. Powered by 'Gemma2:9B'\n")
    
    while True:
        try:
            user_input = input("\nEnter text to create prompt (or 'exit' to quit): ").strip()
            if user_input.lower() == 'exit':
                print("Terminating program.")
                break
                
            # Get cycle results and final synthesis
            cycles, final_synthesis = process_user_input(user_input)
            
            # Output results of each cycle
            for i, cycle in enumerate(cycles, 1):
                print(f"\nCycle {i}:")
                print(f"Intent: {cycle['intent']}")
                print(f"Prompt: {cycle['prompt']}")
                print(f"Response: {cycle['response']}")
            
            # Output final synthesis
            print("\nFinal synthesized answer:\n")
            print(final_synthesis)
                
        except KeyboardInterrupt:
            print("\nTerminating program.")
            break
        except Exception as e:
            print(f"An error occurred: {str(e)}. Please try again.")

if __name__ == "__main__":
    main()