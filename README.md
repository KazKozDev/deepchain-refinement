# 🧠 DeepChain Refinement

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Ollama](https://img.shields.io/badge/Ollama-Compatible-orange.svg)](https://ollama.ai)
[![Model](https://img.shields.io/badge/Model-gemma2:9b-purple.svg)](https://ollama.ai)

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 320">
  <defs>
    <!-- Градиенты -->
    <linearGradient id="textGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ffffff"/>
      <stop offset="100%" style="stop-color:#e0e7ff"/>
    </linearGradient>
    
    <linearGradient id="accentGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#3b82f6"/>
      <stop offset="100%" style="stop-color:#2563eb"/>
    </linearGradient>

    <!-- Паттерн для фона -->
    <pattern id="gridPattern" x="0" y="0" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1e293b" stroke-width="0.5"/>
    </pattern>
  </defs>

  <!-- Тёмный фон -->
  <rect width="1280" height="320" fill="#0f172a"/>
  
  <!-- Сетка на фоне -->
  <rect width="1280" height="320" fill="url(#gridPattern)" opacity="0.3"/>

  <!-- Основные линии -->
  <path d="M0,160 L1280,160" stroke="#1e293b" stroke-width="1"/>
  <path d="M640,0 L640,320" stroke="#1e293b" stroke-width="1"/>

  <!-- Центральная группа элементов -->
  <g transform="translate(640, 160)">
    <!-- Декоративные круги -->
    <circle cx="0" cy="0" r="250" stroke="#1e293b" stroke-width="1" fill="none"/>
    <circle cx="0" cy="0" r="200" stroke="#1e293b" stroke-width="1" fill="none"/>
    <circle cx="0" cy="0" r="150" stroke="#1e293b" stroke-width="0.5" fill="none" opacity="0.5"/>
    
    <!-- Текстовый блок -->
    <g transform="translate(0, -20)">
      <text x="0" 
            y="0" 
            font-family="Arial, sans-serif" 
            font-size="82" 
            font-weight="800" 
            fill="url(#textGradient)" 
            text-anchor="middle" 
            dominant-baseline="middle"
            filter="drop-shadow(0 4px 6px rgba(0, 0, 0, 0.3))">DEEPCHAIN</text>
      
      <text x="0" 
            y="82" 
            font-family="Arial, sans-serif" 
            font-size="82" 
            font-weight="800" 
            fill="url(#accentGradient)" 
            text-anchor="middle" 
            dominant-baseline="middle"
            filter="drop-shadow(0 4px 6px rgba(0, 0, 0, 0.3))">REFINEMENT</text>
    </g>

    <!-- Декоративные линии -->
    <line x1="-300" y1="0" x2="-220" y2="0" stroke="url(#accentGradient)" stroke-width="4"/>
    <line x1="300" y1="0" x2="220" y2="0" stroke="url(#accentGradient)" stroke-width="4"/>
    
    <!-- Дополнительные декоративные элементы -->
    <circle cx="-260" cy="0" r="4" fill="url(#accentGradient)"/>
    <circle cx="260" cy="0" r="4" fill="url(#accentGradient)"/>
  </g>
</svg>

A sophisticated multi-stage prompt refinement system that leverages chain-of-thought reasoning to enhance AI responses and minimize hallucinations through progressive validation and synthesis.

## ✨ Features

- 🔄 **Chain-of-Thought Processing**: Implements logical reasoning chains for better understanding
- 🎯 **Multi-stage Prompting**: Uses three distinct stages of prompt refinement
- 📈 **Progressive Refinement**: Each stage builds upon and improves previous results
- 🔄 **Response Synthesis**: Combines multiple processing stages into coherent final output
- 🎯 **Integrated Intent Analysis**: Analyzes and refines user intent at each stage
- 🛡️ **Hallucination Mitigation**: Three-stage verification process helps identify and eliminate inconsistencies and hallucinations in AI responses

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

## 👨‍💻 Author

Artem Kazakov Kozlov

## 💬 Support

For questions and support, please open an issue in the GitHub repository.

---

**Note**: This project requires Ollama to be installed and running with the gemma2:9b model available.