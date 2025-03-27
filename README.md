<p align="center">
  <img src="https://github.com/user-attachments/assets/958180f9-798a-442c-b93d-4e561358f33e" width="600" alt="banner">
</p>

<p align="center">
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python"></a>
  <a href="https://ollama.ai"><img src="https://img.shields.io/badge/Model-gemma2:9b-purple.svg" alt="Model"></a>
</p>

<p align="center">DeepChain is a Python-based system that automatically applies refinement techniques to LLM.</p>
<p align="center">One script. Three iterations.</p>

The tool helps engineers visualize how each refinement enhances the quality and depth of LLM outputs.

DeepChain uses a structured, three-stage refinement pipeline to enhance LLM responses. It begins with Basic Analysis, which performs initial prompt processing and baseline generation. The second stage, Detailed Refinement, adds context-aware improvements, intent analysis, and fact verification. Finally, Comprehensive Synthesis integrates and cross-validates information from previous stages into a consistent, in-depth result.

The system combines chain-of-thought reasoning, multi-stage cue refinement, and progressive enhancement, where each stage builds on the last. It also includes hallucination reduction and automated synthesis to ensure clarity, depth, and accuracy.

### 🎬 Demo

![DeepChain Refinement movie](https://github.com/kazkozdev/deepchain-refinement/blob/main/deepchain-refinement-movie.gif)

In this example, the user submits an ambiguous query "How many discs does Madonna have?" Through a refinement process, the system demonstrates its analytical capabilities by providing a comprehensive response that breaks down Madonna's discography into studio albums, live recordings, and compilations. The response includes key information about her most significant releases, offering relevant context to fully address the query.

### 📋 Requirements

- Python 3.8 or higher
- Ollama installed and running
- gemma2:9b model
- Required Python packages (see requirements.txt)

### Quick Start

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
### Project Structure
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

**Note**: This project requires Ollama to be installed and running with the gemma2:9b model available.
