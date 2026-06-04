from src.specialists import SubagentResult

def run_synthesis_specialist(subtopic: str, context: str) -> SubagentResult:
    # Compares different sources to isolate data contradictions
    return SubagentResult(subtopic=subtopic, findings=[])