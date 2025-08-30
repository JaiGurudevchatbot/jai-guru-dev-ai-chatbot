# 🙏 JAI GURU DEV AI Chatbot

A spiritual guidance chatbot powered by Sri Sri Ravi Shankar's teachings, built using RAG (Retrieval Augmented Generation) technology with Streamlit UI. **Now optimized for Railway free tier deployment!**

## ✨ Features

- **Intelligent Retrieval**: Advanced RAG system with in-memory FAISS vector database
- **Context-Aware**: Gathers user context (emotional state, life situation, guidance type) for personalized responses
- **Multiple AI Models**: Configurable support for OpenAI GPT and Groq Llama models
- **Beautiful UI**: Saffron-themed Streamlit interface inspired by spiritual aesthetics
- **Comprehensive Knowledge Base**: Contains structured teachings with metadata (topics, keywords, emotional states, etc.)
- **Source Attribution**: Shows which specific teachings were used to generate responses
- **Railway Free Tier Compatible**: In-memory vector database that works on free hosting tiers

## 🚀 Quick Deploy to Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/your-template-id)

### ⚡ Railway Free Tier Benefits

- **✅ No Persistent Storage**: In-memory vector database eliminates storage costs
- **🚀 Fast Startup**: FAISS vector database loads quickly into memory
- **💰 Cost-Effective**: Designed specifically for Railway's free tier
- **🔄 Fresh Start**: Database rebuilds on each deployment with latest teachings

### Environment Variables for Railway:

```bash
OPENAI_API_KEY=your_openai_api_key_here
GROQ_API_KEY=your_groq_api_key_here  # Optional
ENVIRONMENT=production
```

## 📁 Project Structure

```
jai-guru-dev-ai-chatbot/
├── .env.example           # Environment variables template  
├── .gitignore            # Git ignore rules
├── railway.toml          # Railway deployment config
├── config.yaml           # Application configuration
├── requirements.txt      # Python dependencies (FAISS optimized)
├── setup.py             # Setup and testing script
├── chatbot.py           # Main Streamlit application
├── rag_system.py        # In-memory RAG system with FAISS
├── document_processor.py # Markdown file processor
├── start_chatbot.py     # Enhanced launcher script
├── test_system.py       # Component testing script
└── Knowledge_Base/      # Teaching files directory
    ├── README.md        # Format documentation
    └── sample_teachings.md # Example teachings
```

## 🏗️ Local Development

### Prerequisites

- Python 3.8 or higher
- OpenAI API key and/or Groq API key

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/JaiGurudevchatbot/jai-guru-dev-ai-chatbot.git
   cd jai-guru-dev-ai-chatbot
   ```

2. **Set up environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run setup script** to verify everything is working:
   ```bash
   python setup.py
   ```

5. **Start the chatbot**:
   ```bash
   python start_chatbot.py
   # OR
   streamlit run chatbot.py
   ```

### First Run

1. The application will automatically build the in-memory vector database on startup (30-60 seconds)
2. Select your preferred AI model provider (OpenAI or Groq) in the sidebar
3. Answer the initial context questions to personalize your experience
4. Start asking questions about life, spirituality, relationships, and more!

## ⚙️ Configuration

### Model Provider Selection

Edit `config.yaml` to change default settings:

```yaml
model_provider:
  default: "openai"  # or "groq"
  
  openai:
    model: "gpt-4o-mini"
    temperature: 0.7
    max_tokens: 1500
    
  groq:
    model: "llama-3.3-70b-versatile"
    temperature: 0.7
    max_tokens: 1500
```

### RAG Settings

```yaml
rag:
  chunk_size: 1000
  chunk_overlap: 200
  top_k_results: 5
  similarity_threshold: 0.7
```

## 📚 Knowledge Base Structure

Each teaching in the markdown files follows this structure:

```markdown
## Teaching #XXX: [Title]
**Date:** [Date if available]
**Location:** [Location if mentioned]
**Topics:** [main themes - comma separated]
**Keywords:** [specific words for exact matching - comma separated]
**Problem Categories:** [user problems this addresses - comma separated]
**Emotional States:** [emotions this helps with - comma separated]
**Life Situations:** [when to apply - comma separated]

### Content:
[The actual teaching content]
```

This rich metadata enables sophisticated retrieval based on:
- **Topics**: Broad themes like relationships, spiritual practice, etc.
- **Keywords**: Specific terms for exact matching
- **Problem Categories**: Types of problems the teaching addresses
- **Emotional States**: Emotions the teaching helps with
- **Life Situations**: Contexts where the teaching applies

## 🎯 How It Works

### 1. Context Gathering
- User provides information about their situation, emotional state, and what type of guidance they seek
- This context is stored and used to enhance all subsequent queries

### 2. Intelligent Retrieval (In-Memory)
- User's question is enhanced with their context
- FAISS vector similarity search finds relevant teachings in memory
- Metadata filtering ensures contextually appropriate results
- Custom retriever combines multiple signals for optimal results

### 3. Response Generation
- Selected teachings are provided as context to the AI model
- AI generates compassionate, wisdom-filled responses in Gurudev's spirit
- Sources are provided for transparency and further study

## 🎨 UI Features

- **Saffron Theme**: Beautiful spiritual aesthetic with saffron colors
- **Context Display**: Shows your gathered context throughout the session
- **Chat History**: Maintains conversation flow with full history
- **Source Attribution**: Expandable sections showing which teachings were referenced
- **Random Wisdom**: Get random spiritual insights
- **Configurable Models**: Switch between AI providers on the fly

## 🔧 Troubleshooting

### Common Issues

1. **"No API key found"**
   - Check that your .env file contains valid API keys
   - For Railway: Set environment variables in the Railway dashboard

2. **"Error loading teachings"**
   - Verify that the Knowledge_Base folder contains .md files
   - Check that the markdown files follow the expected format

3. **"System initialization failed"**
   - Run `python setup.py` to diagnose issues
   - Check your internet connection for API calls
   - Verify Python version is 3.8+

### Performance Tips

- First run takes 30-60 seconds to build in-memory vector database
- Subsequent queries are very fast with FAISS in-memory search
- Use Groq models for faster response times
- Use OpenAI models for higher quality responses

## 🚀 Railway Deployment

This application is optimized for Railway's free tier:

1. **Fork this repository**
2. **Connect to Railway**: 
   - Go to [Railway](https://railway.app)
   - Create new project from GitHub repo
3. **Set Environment Variables**:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `GROQ_API_KEY`: Your Groq API key (optional)
   - `ENVIRONMENT`: Set to `production`
4. **Deploy**: Railway will automatically deploy using `railway.toml`

The application will be accessible at your Railway-provided URL.

### 🧠 Why In-Memory Vector Database?

- **Cost-Effective**: No persistent storage costs on Railway
- **Fast Performance**: FAISS is extremely fast for similarity search
- **Simple Deployment**: No database setup or configuration needed
- **Fresh Updates**: Database rebuilds with each deployment
- **Memory Efficient**: Optimized for small to medium knowledge bases

## 🤝 Usage Examples

### Example Conversations

**User Context:**
- Life Aspect: Relationships
- Emotional State: Confused
- Guidance Type: Specific Situation Help

**Query:** "I'm having conflicts with my family members. How do I handle this?"

**Response:** The chatbot will find relevant teachings about family relationships, conflict resolution, and provide compassionate guidance based on Gurudev's wisdom.

### Question Types That Work Well

- Emotional guidance: "How do I deal with anger?"
- Relationship advice: "What is true love?"
- Spiritual practice: "How do I meditate properly?"
- Life purpose: "What is my purpose in life?"
- General wisdom: "What brings happiness?"

## 🙏 Spiritual Disclaimer

This chatbot is a technological tool created to share the wisdom of Sri Sri Ravi Shankar's teachings. While it provides guidance based on authentic spiritual content, it is not a replacement for:
- Personal spiritual practice
- Direct guidance from qualified teachers
- Professional counseling when needed
- Your own inner wisdom and intuition

Use this tool as a complement to your spiritual journey, not as the sole source of guidance.

## 🛠️ Development

### Testing

Run the comprehensive test suite:

```bash
python test_system.py
```

### Adding New Teachings

1. Create new .md files in the `Knowledge_Base` folder
2. Follow the exact metadata structure shown above
3. Restart the application to reindex the new content (in-memory rebuild)

### Customizing

- **Model**: Edit `rag_system.py` for prompt templates and retrieval logic
- **UI**: Modify `chatbot.py` for interface changes
- **Configuration**: Update `config.yaml` for settings

## 📊 System Requirements

- Python 3.8+
- OpenAI API key (required)
- Groq API key (optional)
- 512MB+ RAM for in-memory vector database
- Internet connection for AI APIs

## 🔒 Security & Privacy

- Environment variables for API keys
- No sensitive data in repository
- In-memory vector database (no persistent storage)
- Railway environment variable management

## 📞 Support & Contributing

- **Issues**: Create GitHub issues for bugs
- **Documentation**: README.md and inline comments
- **Testing**: Comprehensive test suite included
- **Setup**: Automated dependency management

---

**🙏 "In the depth of silence is the source of love" - Sri Sri Ravi Shankar**

**Built with love and devotion • Optimized for Railway Free Tier • Jai Guru Dev! 🙏**

---

## 🏷️ Version Info

- **Version**: Release 1.1 (Railway Optimized)
- **Vector Database**: In-Memory FAISS (Railway Free Tier Compatible)
- **Last Updated**: August 30, 2025
- **Repository**: https://github.com/JaiGurudevchatbot/jai-guru-dev-ai-chatbot
- **Deployment**: Railway-ready with automatic deployment on free tier
