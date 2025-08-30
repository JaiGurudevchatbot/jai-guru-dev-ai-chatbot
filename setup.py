#!/usr/bin/env python3
"""
Enhanced setup script for JAI GURU DEV AI Chatbot
Handles dependency conflicts and provides multiple installation options.
Now optimized for Railway free tier with in-memory vector database.
"""

import os
import sys
import subprocess
from pathlib import Path
import yaml
from dotenv import load_dotenv

def install_requirements_with_fallback():
    """Install requirements with fallback options for dependency conflicts"""
    print("🔧 Installing required packages...")
    
    # Try method 1: Install with updated requirements
    try:
        print("📦 Attempting installation with specific versions...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Method 1 failed: {e}")
    
    # Try method 2: Install packages individually
    try:
        print("📦 Installing packages individually...")
        essential_packages = [
            "streamlit",
            "langchain", 
            "langchain-openai",
            "langchain-community",
            "faiss-cpu",
            "python-dotenv",
            "pyyaml",
            "openai>=1.10.0",
            "pandas",
            "numpy"
        ]
        
        for package in essential_packages:
            print(f"   Installing {package}...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package], 
                                    capture_output=True, text=True)
            except subprocess.CalledProcessError:
                print(f"   ⚠️ Failed to install {package}, continuing...")
        
        print("✅ Essential packages installed!")
        return True
        
    except Exception as e:
        print(f"❌ All installation methods failed: {e}")
        return False

def install_groq_separately():
    """Install Groq separately as it might have conflicts"""
    try:
        print("📦 Installing Groq API client...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "groq"])
        return True
    except subprocess.CalledProcessError:
        print("⚠️ Groq installation failed - you'll only be able to use OpenAI models")
        return False

def verify_installation():
    """Verify that core packages are installed"""
    print("🔍 Verifying installation...")
    
    required_packages = [
        'streamlit',
        'langchain', 
        'openai',
        'faiss',  # Changed from chromadb to faiss
        'yaml',
        'pandas',
        'numpy'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            if package == 'yaml':
                import yaml
            elif package == 'faiss':
                import faiss
            else:
                __import__(package)
            print(f"✅ {package} - OK")
        except ImportError:
            print(f"❌ {package} - MISSING")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️ Missing packages: {', '.join(missing_packages)}")
        return False
    
    print("✅ All core packages verified!")
    return True

def verify_environment():
    """Verify environment variables"""
    print("🔍 Verifying environment setup...")
    
    load_dotenv()
    
    openai_key = os.getenv('OPENAI_API_KEY')
    groq_key = os.getenv('GROQ_API_KEY')
    
    if not openai_key:
        print("⚠️  Warning: OPENAI_API_KEY not found in environment")
    else:
        print("✅ OpenAI API key found")
    
    if not groq_key:
        print("⚠️  Warning: GROQ_API_KEY not found in environment")
    else:
        print("✅ Groq API key found")
    
    if not openai_key and not groq_key:
        print("❌ No API keys found! Please check your .env file")
        return False
    
    return True

def verify_knowledge_base():
    """Verify knowledge base files"""
    print("📚 Verifying knowledge base...")
    
    kb_path = Path("Knowledge_Base")
    if not kb_path.exists():
        print(f"❌ Knowledge base directory not found: {kb_path}")
        return False
    
    md_files = list(kb_path.glob("*.md"))
    if not md_files:
        print("❌ No markdown files found in Knowledge_Base directory")
        return False
    
    print(f"✅ Found {len(md_files)} markdown files:")
    for file in md_files:
        print(f"   - {file.name}")
    
    return True

def test_document_processor():
    """Test the document processor"""
    print("🧪 Testing document processor...")
    
    try:
        from document_processor import DocumentProcessor
        
        processor = DocumentProcessor("Knowledge_Base")
        teachings = processor.load_all_teachings()
        
        if teachings:
            print(f"✅ Successfully loaded {len(teachings)} teachings")
            print(f"   First teaching: #{teachings[0].number} - {teachings[0].title}")
            return True
        else:
            print("❌ No teachings loaded")
            return False
            
    except Exception as e:
        print(f"❌ Error testing document processor: {e}")
        return False

def test_config():
    """Test configuration file"""
    print("⚙️  Testing configuration...")
    
    try:
        with open("config.yaml", 'r') as f:
            config = yaml.safe_load(f)
        
        required_sections = ['model_provider', 'rag', 'embeddings', 'ui', 'chatbot']
        for section in required_sections:
            if section not in config:
                print(f"❌ Missing configuration section: {section}")
                return False
        
        print("✅ Configuration file is valid")
        return True
        
    except FileNotFoundError:
        print("❌ config.yaml file not found")
        return False
    except yaml.YAMLError as e:
        print(f"❌ Error parsing config.yaml: {e}")
        return False

def test_vector_database():
    """Test in-memory vector database creation"""
    print("🧠 Testing in-memory vector database...")
    
    try:
        import faiss
        import numpy as np
        
        # Create a simple test vector database
        dimension = 10
        test_vectors = np.random.random((5, dimension)).astype('float32')
        
        # Create FAISS index
        index = faiss.IndexFlatL2(dimension)
        index.add(test_vectors)
        
        # Test search
        query_vector = np.random.random((1, dimension)).astype('float32')
        distances, indices = index.search(query_vector, 2)
        
        print(f"✅ In-memory vector database test successful!")
        print(f"   Created index with {index.ntotal} vectors")
        return True
        
    except Exception as e:
        print(f"❌ Vector database test failed: {e}")
        return False

def main():
    """Main setup function"""
    print("🙏 JAI GURU DEV AI Chatbot - Railway-Optimized Setup")
    print("=" * 60)
    print("🧠 Now using in-memory vector database for Railway free tier!")
    print("=" * 60)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required")
        return False
    
    print(f"✅ Python {sys.version.split()[0]} detected")
    
    # Installation steps
    print(f"\n📦 Step 1: Installing Dependencies")
    if not install_requirements_with_fallback():
        print("❌ Failed to install core dependencies")
        print("💡 Try running manually: pip install streamlit langchain langchain-openai faiss-cpu python-dotenv pyyaml openai")
        return False
    
    # Install Groq separately
    print(f"\n📦 Step 2: Installing Groq (optional)")
    install_groq_separately()
    
    # Verification steps
    verification_steps = [
        ("Verify Installation", verify_installation),
        ("Test Vector Database", test_vector_database),
        ("Verify Environment", verify_environment),
        ("Verify Knowledge Base", verify_knowledge_base),
        ("Test Configuration", test_config),
        ("Test Document Processor", test_document_processor)
    ]
    
    all_passed = True
    for step_name, step_func in verification_steps:
        print(f"\n🔍 {step_name}...")
        if not step_func():
            all_passed = False
            print(f"❌ {step_name} failed!")
        else:
            print(f"✅ {step_name} completed!")
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 Setup completed successfully!")
        print("\n🚀 Ready for Railway deployment!")
        print("\n🔥 Benefits of in-memory vector database:")
        print("   • ✅ Works on Railway free tier")
        print("   • ⚡ Faster startup after first load")  
        print("   • 💾 No persistent storage needed")
        print("   • 🔄 Fresh index on each deployment")
        print("\n🚀 To start the chatbot locally:")
        print("   python start_chatbot.py")
        print("   OR")
        print("   streamlit run chatbot.py")
        print("\n💡 Note: First run takes 30-60 seconds to build in-memory vector database")
    else:
        print("❌ Setup encountered some issues.")
        print("💡 The chatbot may still work if core dependencies are installed.")
        print("💡 Try running: python start_chatbot.py")
    
    return all_passed

if __name__ == "__main__":
    main()
