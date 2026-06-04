import concurrent.futures
from src.specialists.search_agent import run_search_specialist

class ResearchCoordinator:
    def __init__(self):
        self.allowed_tools = ["Task"]

    def run_parallel_research(self, topic: str):
        # Decompose the topic broadly
        subtopics = [f"{topic} - Art", f"{topic} - Music", f"{topic} - Writing", f"{topic} - Film"]

        # Run subagents in parallel far faster than one-at-a-time
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(lambda sub: run_search_specialist(sub, "Context"), subtopics))

        return results