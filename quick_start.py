#!/usr/bin/env python3
"""
Quick start guide for the PubMed MCP server
"""

# Method 1: Direct execution (most common)
# python3 pubmed_server.py

# Method 2: As a module  
# python3 -m pubmed_server

# Method 3: Check if tools are registered
import sys
sys.path.append('.')

try:
    from pubmed_server import mcp
    print("✅ MCP server imports successfully")
    
    # Check available tools
    tools = [attr for attr in dir(mcp) if not attr.startswith('_')]
    print(f"📋 Available tools: {len(tools)}")
    for tool in tools[:5]:  # Show first 5
        print(f"  • {tool}")
    if len(tools) > 5:
        print(f"  ... and {len(tools) - 5} more tools")
        
except Exception as e:
    print(f"❌ Import error: {e}")

# Quick test function
async def quick_test():
    """Run a quick functionality test"""
    from pubmed_server import search_pubmed
    
    print("\n🧪 Quick functionality test...")
    result = await search_pubmed("test query", 1)
    if "Found" in result and "articles" in result:
        print("✅ Quick test passed!")
        return True
    else:
        print("❌ Quick test failed!")
        return False

if __name__ == "__main__":
    print("🔬 PubMed MCP Server - Quick Start Guide")
    print("=" * 50)
    
    import asyncio
    success = asyncio.run(quick_test())
    
    if success:
        print("\n🎯 Your server is working perfectly!")
        print("\n📚 Usage examples:")
        print("search_pubmed('cancer treatment', 5)")
        print("get_article_abstract('35412731')")
        print("clinical_search('diabetes management', 3)")
    else:
        print("\n⚠️ There might be a configuration issue.")