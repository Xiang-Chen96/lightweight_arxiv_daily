#!/usr/bin/env python3
"""
Test script to verify the chunk-based translation functionality.
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import translate_to_chinese

# Sample text for testing
sample_text = "This is the first sentence. This is the second sentence! Is this the third sentence? Yes, it is indeed the third sentence. We are testing chunk-based translation functionality."

print("Testing chunk-based translation...")
print(f"Original text: {sample_text}")
print()

translated = translate_to_chinese(sample_text)
print(f"Translated text: {translated}")
print()

# Test with a longer sample
longer_sample = """
This is a longer sample text to test chunk-based translation.
The goal is to break it into sentences and translate each one separately.
This helps avoid rate limits and potentially improves translation quality.
Each sentence should be processed individually.
The system should maintain the original structure and meaning.
Quality of translation is important for academic papers.
"""

print("Testing with longer sample...")
print(f"Original text: {longer_sample}")
print()

translated_long = translate_to_chinese(longer_sample)
print(f"Translated text: {translated_long}")
print()

print("Translation test completed!")