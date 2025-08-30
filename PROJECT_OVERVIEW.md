# 🙏 JAI GURU DEV AI Chatbot - Project Overview

## 📋 Project Summary

**JAI GURU DEV AI** is a sophisticated spiritual guidance chatbot powered by Sri Sri Ravi Shankar's teachings, built using advanced RAG (Retrieval Augmented Generation) technology with a beautiful Streamlit interface.

### ✨ Key Features

- **Context-Aware Responses**: Gathers user context (emotional state, life situation) for personalized spiritual guidance
- **Advanced RAG System**: Uses ChromaDB vector database with custom retrieval logic
- **Multiple AI Providers**: Supports both OpenAI GPT and Groq Llama models
- **Beautiful UI**: Saffron-themed interface inspired by spiritual aesthetics
- **Rich Metadata**: Structured teachings with topics, keywords, emotional states, and life situations
- **Source Attribution**: Shows which specific teachings were referenced in responses

## 🏗️ Architecture

### Core Components

1. **chatbot.py** - Main Streamlit application with elegant UI
2. **rag_system.py** - RAG system with custom retriever and LLM integration
3. **document_processor.py** - Parses structured markdown teachings
4. **config.yaml** - Centralized configuration management
5. **start_chatbot.py** - Enhanced launcher with dependency management
6. **setup.py** - Comprehensive setup and validation script
7. **test_system.py** - Component testing and validation

### Technology Stack

- **Frontend**: Streamlit with custom CSS theming
- **Vector Database**: ChromaDB for semantic search
- **LLM Integration**: LangChain with OpenAI GPT / Groq Llama
- **Document Processing**: Custom markdown parser with metadata
- **Deployment**: Railway-optimized with railway.toml

## 📁 File Structure

```
jai-guru-dev-ai-chatbot/
├── 📄 README.md                 # Comprehensive documentation
├── 📄 .env.example              # Environment variables template  
├── 📄 .gitignore                # Git ignore rules
├── 📄 railway.toml              # Railway deployment config
├── 📄 requirements.txt          # Python dependencies
├── ⚙️ config.yaml               # Application configuration
├── 🐍 chatbot.py                # Main Streamlit application
├── 🤖 rag_system.py             # RAG system with LLM integration
├── 📚 document_processor.py     # Teaching parser and processor
├── 🚀 start_chatbot.py          # Enhanced launcher script
├── 🔧 setup.py                  # Setup and validation script
├── 🧪 test_system.py            # Component testing script
└── 📖 Knowledge_Base/           # Spiritual teachings directory
    ├── README.md                # Format documentation
    └── sample_teachings.md      # Example teachings
```

## 🚀 Quick Deployment

### Local Development
```bash
git clone https://github.com/JaiGurudevchatbot/jai-guru-dev-ai-chatbot.git
cd jai-guru-dev-ai-chatbot
cp .env.example .env  # Add your API keys
pip install -r requirements.txt
python setup.py      # Validate installation
python start_chatbot.py
```

### Railway Deployment
1. Fork the repository
2. Connect to Railway
3. Set environment variables (OPENAI_API_KEY, GROQ_API_KEY)
4. Deploy automatically with railway.toml

## 🎯 How It Works

### 1. Context Gathering
- User provides life situation, emotional state, and guidance preferences
- Context is stored and used to enhance all subsequent queries

### 2. Intelligent Retrieval
- Questions are enhanced with user context
- Vector similarity search finds relevant teachings
- Custom retriever combines multiple signals for optimal results

### 3. Wisdom Generation
- Selected teachings provide context to the LLM
- AI generates compassionate responses in Gurudev's spirit
- Sources are shown for transparency and further study

## 🔧 Configuration

### Model Providers
- **OpenAI GPT**: High-quality responses, slower
- **Groq Llama**: Faster responses, good quality
- Configurable via config.yaml

### RAG Parameters  
- Chunk size: 1000 characters
- Overlap: 200 characters
- Top-k results: 5 teachings
- Similarity threshold: 0.7

## 📚 Knowledge Base Format

Each teaching follows this structure:

```markdown
## Teaching #XXX: [Title]
**Date:** [Date if available]
**Location:** [Location if mentioned]  
**Topics:** [main themes - comma separated]
**Keywords:** [specific words - comma separated]
**Problem Categories:** [user problems - comma separated]
**Emotional States:** [emotions - comma separated]
**Life Situations:** [contexts - comma separated]

### Content:
[The actual spiritual teaching content]
```

## 🎨 UI Features

- **Saffron Theme**: Inspired by spiritual traditions
- **Context Cards**: Display user's gathered context
- **Chat History**: Full conversation flow
- **Source Attribution**: Expandable teaching references
- **Random Wisdom**: Get surprise insights
- **API Testing**: Built-in connection validation

## 🛠️ Development

### Testing
```bash
python test_system.py  # Validate components
python setup.py        # Full system check
```

### Adding Teachings
1. Create .md files in Knowledge_Base/
2. Follow the exact metadata format
3. Restart application to reindex

### Customization
- **Prompts**: Edit rag_system.py
- **UI**: Modify chatbot.py  
- **Config**: Update config.yaml

## 🙏 Spiritual Philosophy

This chatbot is a technological tool to share Sri Sri Ravi Shankar's wisdom. It complements but doesn't replace:
- Personal spiritual practice
- Direct teacher guidance  
- Professional counseling
- Inner wisdom and intuition

## 📊 System Requirements

- Python 3.8+
- OpenAI API key (required)
- Groq API key (optional)
- 1GB+ RAM for vector database
- Internet connection for AI APIs

## 🔒 Security & Privacy

- Environment variables for API keys
- No sensitive data in repository
- Local vector database storage
- Railway environment variable management

## 📞 Support & Contributing

- **Issues**: Create GitHub issues for bugs
- **Documentation**: README.md and inline comments
- **Testing**: Comprehensive test suite included
- **Setup**: Automated dependency management

---

**🙏 "In the depth of silence is the source of love" - Sri Sri Ravi Shankar**

**Built with love and devotion • Jai Guru Dev! 🙏**

---

## 🏷️ Version Info

- **Version**: Release 1.0
- **Last Updated**: August 30, 2025
- **Repository**: https://github.com/JaiGurudevchatbot/jai-guru-dev-ai-chatbot
- **Deployment**: Railway-ready with automatic deployment
