from src.specialists import SubagentResult

def run_report_specialist(subtopic: str, context: str) -> SubagentResult:
    # Formats findings into the final traceable markdown file
    return SubagentResult(subtopic=subtopic, findings=[])