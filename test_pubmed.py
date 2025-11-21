#!/usr/bin/env python3
"""
Test script to debug the PubMed MCP server
"""

import asyncio
import httpx
import json
from pubmed_server import search_pubmed, get_article_details, make_ncbi_request

async def test_basic_functionality():
    """Test basic PubMed functionality"""
    print("Testing basic PubMed functionality...")
    
    # Test 1: Basic PubMed search
    print("\n=== Test 1: Basic PubMed Search ===")
    try:
        result = await search_pubmed("cancer immunotherapy", 3)
        print("Search result:")
        print(result[:200] + "..." if len(result) > 200 else result)
        print("✅ Search test passed")
    except Exception as e:
        print(f"❌ Search test failed: {e}")
    
    # Test 2: Test direct NCBI request
    print("\n=== Test 2: Direct NCBI Request ===")
    try:
        search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        params = {
            "db": "pubmed",
            "term": "test query",
            "retmax": 2,
            "retmode": "json"
        }
        result = await make_ncbi_request(search_url, params)
        if result and "esearchresult" in result:
            print("✅ Direct NCBI request successful")
            print(f"Found {result['esearchresult'].get('count', 'unknown')} results")
        else:
            print("❌ Direct NCBI request failed")
            print(f"Result: {result}")
    except Exception as e:
        print(f"❌ Direct NCBI request error: {e}")
    
    # Test 3: Get a specific article
    print("\n=== Test 3: Article Details ===")
    try:
        # Use a known PMID
        result = await get_article_details("35412731")
        print("Article details result:")
        print(result[:300] + "..." if len(result) > 300 else result)
        print("✅ Article details test passed")
    except Exception as e:
        print(f"❌ Article details test failed: {e}")

def test_import():
    """Test if all modules import correctly"""
    print("Testing imports...")
    try:
        from pubmed_server import mcp
        print("✅ MCP server import successful")
        return True
    except Exception as e:
        print(f"❌ MCP server import failed: {e}")
        return False

if __name__ == "__main__":
    print("PubMed MCP Server Debug Test")
    print("=" * 40)
    
    # Test imports first
    if test_import():
        # Run async tests
        asyncio.run(test_basic_functionality())
    else:
        print("Import test failed, cannot proceed with functionality tests")
    
    print("\n" + "=" * 40)
    print("Debug test completed")