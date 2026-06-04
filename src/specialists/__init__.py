from pydantic import BaseModel
from typing import List, Optional

class ResearchFinding(BaseModel):
    claim: str
    evidence_excerpt: str
    source_name_or_url: str
    publication_date: Optional[str] = "Unknown"

class SubagentResult(BaseModel):
    subtopic: str
    findings: List[ResearchFinding]
    errors: Optional[List[str]] = None