from coordinator import AISnakeOilCoordinator
import json
from datetime import datetime

def format_section(title, char="="):
    print(f"\n{title}")
    print(char * len(title))

def print_severity_list(items, severity_key="severity"):
    for item in items:
        if isinstance(item, dict):
            severity = item.get(severity_key, "MEDIUM")
            message = item.get("message", item)
            print(f"[{severity}] {message}")
        else:
            print(f"- {item}")

def main():
    # Create sample AI product data
    sample_product = {
        "product_name": "AI SuperBrain 3000",
        "company": "TechCorp Inc.",
        "claims": [
            "100% accurate predictions in all scenarios",
            "Can read and understand human emotions perfectly",
            "Eliminates all biases automatically"
        ],
        "technical_documentation": {
            "methodology": "Proprietary AI algorithms",
            "validation": "Internal testing",
            "data_sources": "Various public datasets"
        },
        "target_applications": [
            "Healthcare diagnostics",
            "Criminal justice",
            "Personality assessment"
        ],
        "marketing_materials": [
            "Revolutionary AI technology",
            "First-ever truly unbiased AI",
            "Powered by quantum neural networks"
        ]
    }

    # Initialize the coordinator
    coordinator = AISnakeOilCoordinator()
    
    # Evaluate the product
    results = coordinator.evaluate_ai_product(sample_product)
    
    # Print results with timestamp
    format_section("AI SnakeOil Detection Results")
    print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Product: {sample_product['product_name']}")
    print(f"Company: {sample_product['company']}")
    
    format_section("Executive Summary", "-")
    print(f"Category: {results['summary']['category']}")
    print(f"Confidence Score: {results['summary']['confidence_score']:.2f}/1.00")
    print(f"Risk Level: {results['summary']['overall_risk_level']:.2f}/1.00")
    
    # Detailed Findings
    format_section("Detailed Analysis", "-")
    findings = results['detailed_findings']
    
    print("\nClaims Validation:")
    print(f"- Confidence Score: {findings['claims_validator'].get('confidence_score', 0):.2f}")
    
    print("\nTransparency Assessment:")
    print(f"- Documentation Score: {findings['transparency_auditor'].get('documentation_score', 0):.2f}")
    
    print("\nApplicability Analysis:")
    print(f"- Suitability Score: {findings['applicability_assessor'].get('suitability_score', 0):.2f}")
    
    print("\nMarketing Claims Review:")
    print(f"- Transparency Score: {findings['marketing_claims'].get('transparency_score', 0):.2f}")
    
    # Red Flags with Severity
    format_section("Red Flags", "-")
    red_flags_with_severity = [
        {"message": flag, "severity": "HIGH" if "100%" in flag or "perfect" in flag.lower() 
         else "MEDIUM" if "all" in flag.lower() or "proprietary" in flag.lower() 
         else "LOW"} 
        for flag in results['red_flags']
    ]
    print_severity_list(red_flags_with_severity)
    
    # Recommendations with Priority
    format_section("Recommendations", "-")
    recommendations_with_priority = [
        {"message": rec, "severity": "HIGH" if "must" in rec.lower() or "critical" in rec.lower() 
         else "MEDIUM" if "should" in rec.lower() or "recommend" in rec.lower() 
         else "LOW"} 
        for rec in results['recommendations']
    ]
    print_severity_list(recommendations_with_priority, "severity")
    
    # Risk Mitigation
    if 'risk_analyst' in findings and 'mitigation_suggestions' in findings['risk_analyst']:
        format_section("Risk Mitigation Steps", "-")
        for step in findings['risk_analyst']['mitigation_suggestions']:
            print(f"- {step}")

if __name__ == "__main__":
    main()
