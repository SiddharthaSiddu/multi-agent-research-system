from src.specialists import SubagentResult

def run_analysis_specialist(subtopic: str, context: str) -> SubagentResult:
    # Focused strictly on analyzing trends
    return SubagentResult(subtopic=subtopic, findings=[])