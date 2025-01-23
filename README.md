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

The system provides:
- Detailed analysis from each agent
- Overall confidence score (0-100%)
- Product categorization:
  - Legitimate AI Solution
  - AI Snake Oil
  - Unverified AI Solution
- Red flags and recommendations

## Contributing

Feel free to submit issues and enhancement requests!
