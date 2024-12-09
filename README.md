# Gen-Fix Cycle

A Python package for generating, evaluating, and fixing AP-level assessment questions using LLMs.

## Features

- Question generation with subject-specific criteria
- Quality checking against multiple criteria
- Automated fixing of identified issues
- Browser-based testing infrastructure
- Support for multiple AP subjects and courses

## Project Structure

```
src/
├── gen_fix_cycle/
│   ├── prompts/
│   │   ├── criteria/
│   │   │   ├── bloom.py      # Bloom's taxonomy levels
│   │   │   ├── examples.py   # Example questions
│   │   │   └── criteria.py   # Subject criteria
│   │   ├── gen.py           # Generation prompts
│   │   ├── qc.py            # Quality check prompts
│   │   └── fix.py           # Fix prompts
│   ├── models.py            # Data models
│   ├── config.py            # Configuration
│   ├── cycle.py             # Main orchestration
│   ├── llm.py              # LLM integration
│   └── browser.py          # Browser testing
```

## Running in Google Colab

1. Open this link in your browser: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/InceptTrilogy/colab-example/blob/master/src/notebooks/gen_fix_cycle.ipynb)

2. Run these setup cells at the start of your notebook:

```python
# Clone repo
!git clone https://github.com/InceptTrilogy/colab-example.git
%cd colab-example

# Install package
!pip install -e .

# Add src to Python path
import sys
sys.path.append('/content/colab-example/src')

# Install OpenAI for LLM integration
!pip install openai
```

3. Important Notes:
- Use absolute imports in notebook cells (e.g., `from gen_fix_cycle.models import Question`)
- Keep working directory as repo root
- If import errors occur, verify sys.path includes '/content/colab-example/src'

## Development

1. Clone the repository:
```bash
git clone https://github.com/InceptTrilogy/colab-example.git
cd colab-example
```

2. Install in development mode:
```bash
pip install -e .
```

3. Run tests:
```bash
pytest
```

## License

[Add your license information here]
