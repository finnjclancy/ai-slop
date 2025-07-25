#!/usr/bin/env python3
"""
Test runner for the AI PR Reviewer API
"""

import sys
import os

# Add the tests directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'tests'))

if __name__ == '__main__':
    from test_api import test_health, test_api
    
    print("Testing AI PR Reviewer API...")
    print("-" * 40)
    
    test_health()
    print()
    test_api() 