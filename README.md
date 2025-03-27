<p align="center">
  <img src="https://github.com/user-attachments/assets/958180f9-798a-442c-b93d-4e561358f33e" width="600" alt="banner">
</p>

<p align="center">
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"></a>
  <a href="https://ollama.ai"><img src="https://img.shields.io/badge/Model-gemma2:9b-purple.svg" alt="Model"></a>
</p>

This Python-based system automatically improves the quality of LLM responses by applying a multi-step process of prompt refinement and information verification, which greatly reduces the likelihood of hallucinations.

## Features

- **Chain-of-Thought Processing**: Implements logical reasoning chains for better understanding
- **Multi-stage Prompting**: Uses three distinct stages of prompt refinement
- **Progressive Refinement**: Each stage builds upon and improves previous results
- **Response Synthesis**: Combines multiple processing stages into coherent final output
- **Integrated Intent Analysis**: Analyzes and refines user intent at each stage
- **Hallucination Mitigation**: Three-stage verification process helps identify and eliminate inconsistencies and hallucinations in AI responses

## 🎬 Demo Preview

![DeepChain Refinement movie](https://github.com/kazkozdev/deepchain-refinement/blob/main/deepchain-refinement-movie.gif)

In this example, the user submits an ambiguous query "How many discs does Madonna have?" Through a refinement process, the system demonstrates its analytical capabilities by providing a comprehensive response that breaks down Madonna's discography into studio albums, live recordings, and compilations. The response includes key information about her most significant releases, offering relevant context to fully address the query.

## 📋 Requirements

- Python 3.8 or higher
- Ollama installed and running
- gemma2:9b model
- Required Python packages (see requirements.txt)

## 🚀 Quick Start

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

## 🔧 Technical Details

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

### Key Components

- 🧩 Intent Analysis System
- 🔄 Multi-stage Prompt Generator
- ⚙️ Response Processing Engine
- 🎯 Final Synthesis Module
- 🛡️ Cross-validation System for Hallucination Prevention

## 👥 Contributing

Contributions are welcome! 

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💬 Support

For questions and support, please open an issue in the GitHub repository.

---

**Note**: This project requires Ollama to be installed and running with the gemma2:9b model available.
