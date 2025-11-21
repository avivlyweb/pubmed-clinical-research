#!/usr/bin/env python3
"""
Comprehensive test script to debug the PubMed MCP server
"""

import asyncio
import httpx
import json
from pubmed_server import (
    search_pubmed, get_article_details, get_article_abstract, 
    search_by_author, clinical_search, pico_analysis, 
    evidence_quality_assessment, analyze_author_credibility_tool,
    citation_network_analysis, enhanced_article_with_links
)

async def test_comprehensive():
    """Test all PubMed MCP functionality"""
    print("Testing comprehensive PubMed MCP functionality...")
    
    # Test 1: Basic search
    print("\n=== Test 1: Basic Search ===")
    try:
        result = await search_pubmed("machine learning diabetes", 3)
        print("✅ Basic search successful")
        print(f"Found articles (preview): {result[:150]}...")
    except Exception as e:
        print(f"❌ Basic search failed: {e}")
    
    # Test 2: Abstract retrieval
    print("\n=== Test 2: Abstract Retrieval ===")
    try:
        result = await get_article_abstract("35412731")
        print("✅ Abstract retrieval successful")
        print(f"Abstract preview: {result[:200]}...")
    except Exception as e:
        print(f"❌ Abstract retrieval failed: {e}")
    
    # Test 3: Author search
    print("\n=== Test 3: Author Search ===")
    try:
        result = await search_by_author("Schneider JK", 2)
        print("✅ Author search successful")
        print(f"Author results preview: {result[:150]}...")
    except Exception as e:
        print(f"❌ Author search failed: {e}")
    
    # Test 4: Clinical search (enhanced analysis)
    print("\n=== Test 4: Clinical Search ===")
    try:
        result = await clinical_search("blood pressure meditation", 2)
        print("✅ Clinical search successful")
        print(f"Clinical analysis preview: {result[:300]}...")
    except Exception as e:
        print(f"❌ Clinical search failed: {e}")
    
    # Test 5: PICO analysis
    print("\n=== Test 5: PICO Analysis ===")
    try:
        result = await pico_analysis("35412731", "Does meditation reduce blood pressure?")
        print("✅ PICO analysis successful")
        print(f"PICO analysis preview: {result[:250]}...")
    except Exception as e:
        print(f"❌ PICO analysis failed: {e}")
    
    # Test 6: Evidence quality assessment
    print("\n=== Test 6: Evidence Quality ===")
    try:
        result = await evidence_quality_assessment("35412731")
        print("✅ Evidence quality assessment successful")
        print(f"Quality assessment preview: {result[:250]}...")
    except Exception as e:
        print(f"❌ Evidence quality assessment failed: {e}")
    
    # Test 7: Author credibility analysis
    print("\n=== Test 7: Author Credibility ===")
    try:
        result = await analyze_author_credibility_tool("Schneider JK", 3)
        print("✅ Author credibility analysis successful")
        print(f"Credibility analysis preview: {result[:200]}...")
    except Exception as e:
        print(f"❌ Author credibility analysis failed: {e}")
    
    # Test 8: Citation network analysis
    print("\n=== Test 8: Citation Network ===")
    try:
        result = await citation_network_analysis("35412731")
        print("✅ Citation network analysis successful")
        print(f"Citation analysis preview: {result[:200]}...")
    except Exception as e:
        print(f"❌ Citation network analysis failed: {e}")
    
    # Test 9: Enhanced article with links
    print("\n=== Test 9: Enhanced Article Links ===")
    try:
        result = await enhanced_article_with_links("35412731")
        print("✅ Enhanced article with links successful")
        print(f"Enhanced article preview: {result[:200]}...")
    except Exception as e:
        print(f"❌ Enhanced article with links failed: {e}")

async def test_error_handling():
    """Test error handling scenarios"""
    print("\n=== Testing Error Handling ===")
    
    # Test with invalid PMID
    print("\n--- Invalid PMID Test ---")
    try:
        result = await get_article_abstract("invalid_pmid")
        print(f"Invalid PMID result: {result}")
    except Exception as e:
        print(f"Invalid PMID handled correctly: {e}")
    
    # Test with empty search
    print("\n--- Empty Search Test ---")
    try:
        result = await search_pubmed("", 1)
        print(f"Empty search result: {result}")
    except Exception as e:
        print(f"Empty search handled correctly: {e}")

async def main():
    print("🔬 PubMed MCP Server Comprehensive Debug Test")
    print("=" * 60)
    
    await test_comprehensive()
    await test_error_handling()
    
    print("\n" + "=" * 60)
    print("🎯 Debug test completed!")

if __name__ == "__main__":
    asyncio.run(main())