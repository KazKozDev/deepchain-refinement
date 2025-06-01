<p align="center">
   <img src="https://github.com/user-attachments/assets/958180f9-798a-442c-b93d-4e561358f33e" width="600" alt="banner">
</p>

<p align="center">
   <a href="https://www.python.org"><img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python"></a>
   <a href="https://ollama.ai"><img src="https://img.shields.io/badge/Model-gemma2:9b-purple.svg" alt="Model"></a>
</p>

DeepChain is a Python-based pipeline that applies a three-stage refinement process to LLM outputs (using gemma2:9b via Ollama). By combining chain-of-thought prompting, context-aware improvements, and fact‐checking, it produces more accurate and in-depth answers from a compact model.

---

## Key Features

- **Three-Stage Refinement Pipeline**  
  1. **Basic Analysis:** Generates an initial (“naive”) response to your prompt.  
  2. **Contextual Refinement:** Adds context, performs intent analysis, and fact-checks the initial output.  
  3. **Final Synthesis:** Integrates and cross-validates information from earlier stages into a polished, comprehensive answer.

- **Hallucination Reduction**  
  Intermediate checks and cross-validation between stages reduce misinformation and incorrect facts.

- **Easy Setup & Lightweight**  
  Just Python 3.8+ + Ollama + gemma2:9b. No heavyweight frameworks are required.

- **Simple, Clear Code**  
  All core logic lives in a single `src/main.py`, making it easy to understand and extend.

---

## Demo / Usage Example

![DeepChain Refinement movie](https://github.com/kazkozdev/deepchain-refinement/blob/main/deepchain-refinement-movie.gif)

> In this example, the user sends the ambiguous query "How many disks does Madonna have?". Through DeepChain's refinement process, the system demonstrates how a small Gemma2:9B model is enhanced with multi-stage reasoning capabilities. The system showcases improved analytical performance by providing a comprehensive answer that categorizes Madonna's discography into studio albums, live recordings, and compilations. The answer includes key information about her most significant releases, offering the appropriate context for a complete answer to the query - all achieved by applying refinement techniques to a relatively compact 9B parameter model that wouldn't typically exhibit such sophisticated reasoning on its own.

1. **Clone and Install**  
   ```bash
   git clone https://github.com/KazKozDev/deepchain-refinement.git
   cd deepchain-refinement
   pip install -r requirements.txt
   ```

2. **Run the Pipeline**  
   ```bash
   python src/main.py --prompt "How many discs does Madonna have?"
   ```

---

## Installation

1. **Ensure Python 3.8+ is installed**.  
2. **Install Ollama** and confirm it is running locally.  
3. **Clone this repository**:  
   ```bash
   git clone https://github.com/KazKozDev/deepchain-refinement.git
   cd deepchain-refinement
   ```
4. **Install Python dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```

---

## Project Structure

```text
deepchain-refinement/
├── src/
│   └── main.py        # Core implementation with three refinement stages
├── requirements.txt   # Python dependencies
├── LICENSE            # MIT license text
└── README.md          # This file
```

---

If you like this project, please give it a star ⭐

For questions, feedback, or support, reach out to:

[Artem KK](https://www.linkedin.com/in/kazkozdev/) | MIT [LICENSE](LICENSE) 
