from src.coordinator import ResearchCoordinator

def main():
    print("=== Initializing Multi-Agent Research System ===")
    
    # Initialize the supervisor agent
    coordinator = ResearchCoordinator()
    
    # Define a broad research prompt
    topic = "Impact of AI on Creative Industries"
    print(f"Starting parallel research execution for topic: '{topic}'...\n")
    
    # Execute parallel research loops
    research_results = coordinator.run_parallel_research(topic)
    
    # Print the clean, structured output summary
    print("=== Research Cycle Completed Successfully ===")
    for result in research_results:
        print(f"\nSubtopic: {result.subtopic}")
        for finding in result.findings:
            print(f"  - Claim: {finding.claim}")
            print(f"    Source: {finding.source_name_or_url}")
            print(f"    Excerpt: {finding.evidence_excerpt}")

if __name__ == "__main__":
    main()