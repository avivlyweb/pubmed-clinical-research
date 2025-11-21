# 🔧 Installation Guide

**Complete setup guide for PubMed Clinical Research Extension**

## 🎯 **Quick Start**

### Option 1: Gemini CLI (Recommended)
```bash
gemini extensions install https://github.com/avivlyweb/pubmed-clinical-research.git
```

### Option 2: Manual Installation
```bash
# Clone repository
git clone https://github.com/avivlyweb/pubmed-clinical-research.git
cd pubmed-clinical-research

# Install dependencies
pip install httpx biopython

# Test installation
python3 pubmed_server.py
```

## 📋 **Detailed Installation Steps**

### **Step 1: System Requirements**

#### **Python Setup**
```bash
# Check Python version (3.8+ required)
python3 --version

# If Python 3.8+ not installed:
# macOS: brew install python3
# Ubuntu: sudo apt install python3
# Windows: Download from python.org
```

#### **Gemini CLI Setup**
```bash
# Check if Gemini CLI is installed
gemini --version

# If not installed, follow Gemini CLI installation guide
# Visit: https://github.com/google/gemini-cli
```

### **Step 2: Install Python Dependencies**

#### **Using pip (Recommended)**
```bash
pip install httpx biopython
```

#### **Using conda (Alternative)**
```bash
conda install -c conda-forge httpx biopython
```

#### **Using virtual environment (Best Practice)**
```bash
# Create virtual environment
python3 -m venv pubmed-env
source pubmed-env/bin/activate  # On Windows: pubmed-env\Scripts\activate

# Install dependencies
pip install httpx biopython

# Test
python3 pubmed_server.py

# Deactivate when done
deactivate
```

### **Step 3: Optional Configuration**

#### **Set Environment Variables**
```bash
# Add to ~/.bashrc, ~/.zshrc, or ~/.profile
export ENTREZ_EMAIL="your-email@example.com"
export ENTREZ_API_KEY="your-ncbi-api-key"

# Apply changes
source ~/.bashrc  # or ~/.zshrc
```

#### **Get NCBI API Key (Optional)**
1. Visit [NCBI Account Settings](https://account.ncbi.nlm.nih.gov/settings/)
2. Go to "API Key Management"
3. Generate new API key
4. Add to environment variable above

**Benefits:**
- Higher rate limits (10 requests/second vs 3)
- Better reliability
- Access to additional features

### **Step 4: Test Installation**

#### **Quick Test**
```bash
# Test server startup
python3 pubmed_server.py

# Expected output:
# 🔬 PubMed Clinical Research MCP Server
# ==================================================
# ✅ All dependencies available
# ℹ️  Using default Entrez settings (no API key)
# 📚 Server ready with 9 clinical research tools
# 🚀 Starting MCP server...
```

#### **Functionality Test**
```bash
# Run comprehensive test
python3 comprehensive_test.py
```

#### **Quick API Test**
```bash
python3 -c "
import asyncio
from pubmed_server import search_pubmed
result = asyncio.run(search_pubmed('cancer', 1))
print('✅ Installation successful!' if 'Found' in result else '❌ Installation failed')
print(result[:100])
"
```

## 🐛 **Troubleshooting Installation**

### **Problem: ModuleNotFoundError: No module named 'httpx'**

#### **Solution 1: Install dependencies**
```bash
pip install httpx biopython
```

#### **Solution 2: Use system packages (Ubuntu/Debian)**
```bash
sudo apt update
sudo apt install python3-httpx python3-biopython
```

#### **Solution 3: Check Python path**
```bash
# Find where Python looks for modules
python3 -c "import sys; print(sys.path)"

# Install to user directory
pip install --user httpx biopython
```

### **Problem: "python3: command not found"**

#### **Solution: Use python instead**
```bash
python --version  # Try this first
python3 --version  # If above doesn't work

# Install Python 3
# macOS: brew install python3
# Ubuntu: sudo apt install python3
# Windows: Download from python.org
```

### **Problem: "Permission denied"**

#### **Solution: Use appropriate permissions**
```bash
# For system-wide installation
sudo pip install httpx biopython

# For user installation
pip install --user httpx biopython

# For virtual environment
python3 -m venv myenv
source myenv/bin/activate
pip install httpx biopython
```

### **Problem: Network/Connection Issues**

#### **Behind Corporate Firewall**
```bash
# Set proxy variables
export HTTP_PROXY=http://proxy.company.com:8080
export HTTPS_PROXY=https://proxy.company.com:8080

# Or install without proxy
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org httpx biopython
```

#### **Connection Timeout**
```bash
# Increase timeout for pip
pip install --default-timeout=300 httpx biopython

# Or use specific mirror
pip install -i https://pypi.python.org/simple/ httpx biopython
```

### **Problem: BioPython Installation Issues**

#### **If BioPython fails to install**
```bash
# Install biopython without dependencies
pip install --no-deps biopython

# Or use conda
conda install -c conda-forge biopython

# Or install from source
pip install git+https://github.com/biopython/biopython.git
```

## 🔧 **Advanced Configuration**

### **Custom Email Configuration**
```bash
# For NCBI compliance (required for production use)
echo 'export ENTREZ_EMAIL="your-name@your-domain.com"' >> ~/.bashrc
source ~/.bashrc
```

### **Rate Limiting**
```python
# Add to your scripts to respect NCBI limits
import time
import asyncio

async def rate_limited_search(query, delay=0.34):
    # NCBI allows 3 requests/second without API key
    await asyncio.sleep(delay)
    return await search_pubmed(query, 10)

# With API key (10 requests/second)
async def fast_search(query):
    await asyncio.sleep(0.1)  # 10 requests/second
    return await search_pubmed(query, 10)
```

### **Logging Configuration**
```python
# Enable detailed logging
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

## 📱 **Platform-Specific Notes**

### **macOS**
```bash
# Install with Homebrew
brew install python3

# Or use the system Python
python3 -m pip install httpx biopython
```

### **Ubuntu/Debian**
```bash
# Update package list
sudo apt update

# Install Python and pip
sudo apt install python3 python3-pip

# Install dependencies
pip3 install httpx biopython
```

### **Windows**
```powershell
# Using Command Prompt or PowerShell
# Download Python from python.org

# Install dependencies
pip install httpx biopython

# Or use conda
conda install -c conda-forge httpx biopython
```

### **Docker (Optional)**
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install httpx biopython

EXPOSE 8000
CMD ["python3", "pubmed_server.py"]
```

## ✅ **Verification Checklist**

- [ ] Python 3.8+ installed and working
- [ ] `httpx` module imports successfully
- [ ] `Bio.Entrez` module imports successfully
- [ ] Server starts without errors
- [ ] Test query returns results
- [ ] Environment variables set (optional)

## 🆘 **Still Having Issues?**

### **Debug Information**
```bash
# Collect system info
python3 -c "
import sys, platform
print('Python version:', sys.version)
print('Platform:', platform.platform())
print('Architecture:', platform.architecture())
"

# Test imports
python3 -c "
try:
    import httpx
    print('✅ httpx available')
except ImportError as e:
    print('❌ httpx missing:', e)

try:
    from Bio import Entrez
    print('✅ Bio.Entrez available')
except ImportError as e:
    print('❌ Bio.Entrez missing:', e)
"
```

### **Get Help**
1. **Check [GitHub Issues](https://github.com/avivlyweb/pubmed-clinical-research/issues)**
2. **Create a new issue with:**
   - Operating system and version
   - Python version
   - Error message (full output)
   - Steps to reproduce

---

**Installation successful? Time to explore the clinical research tools!** 🔬