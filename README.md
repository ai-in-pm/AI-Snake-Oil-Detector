# AI SnakeOil Detector

A collaborative AI system designed to evaluate AI products and services for authenticity and transparency. The system employs six specialized AI agents to provide comprehensive analysis of AI claims, transparency, ethics, applicability, marketing, and risks.

The development of this repository was inspired by the book "AI Snake Oil".  Visit https://www.aisnakeoil.com/about to learn more about the book.

## Agents

1. **Claims Validator Agent (CVA)**
   - Analyzes capabilities claims
   - Cross-references with industry benchmarks
   - Flags exaggerated results

2. **Transparency Auditor Agent (TAA)**
   - Assesses system transparency
   - Reviews documentation and methodology
   - Identifies documentation gaps

3. **Ethics and Fairness Agent (EFA)**
   - Evaluates ethical design
   - Checks for biases
   - Assesses societal impact

4. **Applicability Assessor Agent (AAA)**
   - Validates domain appropriateness
   - Verifies technology alignment
   - Flags misapplications

5. **Marketing Claims Evaluator Agent (MCEA)**
   - Analyzes marketing language
   - Identifies misleading claims
   - Detects misrepresented capabilities

6. **Risk Analyst Agent (RAA)**
   - Assesses adoption risks
   - Evaluates potential issues
   - Analyzes broader consequences

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure API keys in `.env` file:
```
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
COHERE_API_KEY=your_key_here
EMERGENCEAI_API_KEY=your_key_here
```

## Usage

Run the example script:
```bash
python example.py
```

## Output
```bash

AI SnakeOil Detection Results
=============================
Analysis Date: 2025-01-22 18:32:51
Product: AI SuperBrain 3000
Company: TechCorp Inc.

Executive Summary
-----------------
Category: AI Snake Oil
Confidence Score: 0.37/1.00
Risk Level: 0.00/1.00

Detailed Analysis
-----------------

Claims Validation:
- Confidence Score: 0.12

Transparency Assessment:
- Documentation Score: 0.34

Applicability Analysis:
- Suitability Score: 0.49

Marketing Claims Review:
- Transparency Score: 0.51

Red Flags
---------
[HIGH] 100% accurate predictions in all scenarios
[HIGH] Can read and understand human emotions perfectly
[MEDIUM] Eliminates all biases automatically
[LOW] Marketing claim contains buzzword: revolutionary
[LOW] Marketing claim contains buzzword: first-ever
[LOW] Marketing claim contains buzzword: quantum

Recommendations
---------------
[MEDIUM] High Priority: Should obtain necessary medical certifications

Risk Mitigation Steps

```

## Contributing

Feel free to submit issues and enhancement requests!
