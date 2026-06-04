from src.specialists import SubagentResult, ResearchFinding

def run_search_specialist(subtopic: str, context: str) -> SubagentResult:
    try:
        # Simulating a clean, traceable finding
        finding = ResearchFinding(
            claim=f"AI is deeply shifting the dynamics of {subtopic}.",
            evidence_excerpt="Data indicates a 30% increase in production efficiency...",
            source_name_or_url="https://creative-ai-insights.com/report"
        )
        return SubagentResult(subtopic=subtopic, findings=[finding])
    except Exception as e:
        # Handles errors gracefully with propagation context
        return SubagentResult(subtopic=subtopic, findings=[], errors=[str(e)])