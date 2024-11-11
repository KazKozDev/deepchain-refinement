![Project Banner - DeepChain Refinement Architecture](https://github.com/kazkozdev/deepchain-refinement/blob/main/project-banner.png)

# 🧠 DeepChain Refinement

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Ollama](https://img.shields.io/badge/Ollama-Compatible-orange.svg)](https://ollama.ai)
[![Model](https://img.shields.io/badge/Model-gemma2:9b-purple.svg)](https://ollama.ai)

A sophisticated multi-stage prompt refinement system that leverages chain-of-thought reasoning to enhance AI responses and minimize hallucinations through progressive validation and synthesis.

## ✨ Features

- 🔄 **Chain-of-Thought Processing**: Implements logical reasoning chains for better understanding
- 🎯 **Multi-stage Prompting**: Uses three distinct stages of prompt refinement
- 📈 **Progressive Refinement**: Each stage builds upon and improves previous results
- 🔄 **Response Synthesis**: Combines multiple processing stages into coherent final output
- 🎯 **Integrated Intent Analysis**: Analyzes and refines user intent at each stage
- 🛡️ **Hallucination Mitigation**: Three-stage verification process helps identify and eliminate inconsistencies and hallucinations in AI responses

## 🎬 Demo Preview

![DeepChain Refinement movie](https://github.com/kazkozdev/deepchain-refinement/blob/main/deepchain-refinement-movie.gif)

In this example, the user submits an ambiguous query "How many discs does Madonna have?" Through a refinement process, the system demonstrates its analytical capabilities by providing a comprehensive response that breaks down Madonna's discography into studio albums, live recordings, and compilations. The response includes key information about her most significant releases, offering relevant context to fully address the query."

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