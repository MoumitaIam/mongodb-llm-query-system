from langchain.llms import LlamaCpp
import json
import re

# Initialize model with chat=True for llama-2 style chat models
model_path = "mistral-7b.gguf"  # update with your actual model path
llm = LlamaCpp(model_path=model_path, n_ctx=4096, temperature=0.1, max_tokens=512, chat=True)

def clean_and_parse_json(raw_text):
    """
    Extract JSON substring from raw text, remove markdown fences, and parse it.
    Raises ValueError if no valid JSON is found.
    """
    # Remove markdown code fences if any
    raw_text = re.sub(r"```json|```", "", raw_text).strip()
    
    # Extract JSON object from text
    json_match = re.search(r"\{.*\}", raw_text, re.DOTALL)
    if json_match:
        json_str = json_match.group(0)
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            raise ValueError(f"JSON decoding error: {e}")
    else:
        raise ValueError("No valid JSON found in the response.")

def generate_mongo_query(user_input):
    messages = [
        {
            "role": "system",
            "content": (
                "You are an AI assistant that ONLY outputs a MongoDB query filter dictionary in valid JSON format. "
                "Use exact field names: 'Rating', 'ReviewCount', and 'Brand'. "
                "Combine ALL conditions using '$and'. "
                "Do NOT include explanations, markdown, or extra text."
            )
        },
        {"role": "user", "content": user_input},
    ]

    response = llm.invoke(messages)

    try:
        mongo_query_filter = clean_and_parse_json(response)
        return mongo_query_filter
    except ValueError as e:
        print(f"Error parsing JSON from model response: {e}\nRaw model output:\n{response}")
        return None

if __name__ == "__main__":
    while True:
        user_input = input("Enter your natural language query (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting program.")
            break
        print("Generating MongoDB query...")
        mongo_query_filter = generate_mongo_query(user_input)
        if mongo_query_filter:
            print("\nGenerated MongoDB query filter:")
            print(json.dumps(mongo_query_filter, indent=2))
        else:
            print("Failed to generate a valid MongoDB query filter. Please try rephrasing your query.")

