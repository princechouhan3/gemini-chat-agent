# tools.py

def search_web(query):
    # Placeholder for a real search or dummy logic
    return f"Web search result for: {query}"

def calculate(expression):
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error in calculation: {str(e)}"

# Optional: collect tools in a dictionary if needed
available_tools = {
    "search_web": search_web,
    "calculate": calculate
}
