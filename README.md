<p align="center">
  <img src="https://github.com/user-attachments/assets/958180f9-798a-442c-b93d-4e561358f33e" width="600" alt="banner">
</p>

<p align="center">
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python"></a>
  <a href="https://ollama.ai"><img src="https://img.shields.io/badge/Model-gemma2:9b-purple.svg" alt="Model"></a>
</p>

<p align="center">DeepChain is a Python-based system that automatically applies refinement techniques to LLM.</p>
<p align="center">One input. Three iterations.</p>

The tool helps engineers visualize how refinement prompts enhances the quality and depth of LLM outputs. The project is of practical value to developers working with language models and users.

DeepChain uses a structured, three-stage refinement pipeline. It begins with basic analysis, which performs initial prompt processing and baseline generation. The second stage, detailed refinement, adds context-aware improvements, intent analysis, and fact verification. Finally, comprehensive synthesis integrates and cross-validates information from previous stages into a consistent, in-depth result.

The system combines chain-of-thought reasoning, multi-stage cue refinement, and progressive enhancement, where each stage builds on the last. It also includes hallucination reduction and automated synthesis to ensure clarity, depth, and accuracy.<br><br>

### 🎬 Demo

![DeepChain Refinement movie](https://github.com/kazkozdev/deepchain-refinement/blob/main/deepchain-refinement-movie.gif)

> In this example, the user sends the ambiguous query "How many disks does Madonna have?". Through DeepChain's refinement process, the system demonstrates how a small Gemma2:9B model is enhanced with multi-stage reasoning capabilities. The system showcases improved analytical performance by providing a comprehensive answer that categorizes Madonna's discography into studio albums, live recordings, and compilations. The answer includes key information about her most significant releases, offering the appropriate context for a complete answer to the query - all achieved by applying refinement techniques to a relatively compact 9B parameter model that wouldn't typically exhibit such sophisticated reasoning on its own.

<p></p>

### 📋 Requirements

- Python 3.8 or higher
- Ollama installed and running
- gemma2:9b model
- Required Python packages (see requirements.txt)

### 🚩 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/KazKozDev/deepchain-refinement.git
cd deepchain-refinement
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python src/main.py
```
### ➤ Project Structure
```
deepchain-refinement/
    ├── src/
    │   └── main.py        # Core implementation
    ├── requirements.txt   # Project dependencies
    ├── LICENSE           # MIT license
    └── README.md         # This documentation
```

### 📄 License

MIT License - [LICENSE](LICENSE).

---
If you like this project, please give it a star ⭐

For questions, feedback, or support, reach out to:

[Artem KK](https://www.linkedin.com/in/kazkozdev/)
