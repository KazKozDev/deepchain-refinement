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

DeepChain features thought chain processing to build logical reasoning chains, multi-stage cue processing using three separate stages of cue refinement, and progressive refinement where each stage builds on and improves upon previous results. In addition, the system includes response synthesis to combine multiple processing steps into a consistent final result, integrated intent analysis to analyze and refine user intent at each step, and hallucination reduction.

### 📋 Demo

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

### Technical Details

### System Architecture

The system operates in three main stages:
1. 🔍 **Basic Analysis**: Initial prompt processing and response generation
2. 🔎 **Detailed Refinement**: Enhanced analysis with context consideration and fact verification
3. 🎯 **Comprehensive Synthesis**: Final stage with complete topic analysis and cross-validation

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
