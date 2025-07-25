#!/usr/bin/env python3
"""
Startup script for the AI PR Reviewer API server
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src', 'api'))

# Import and run the API server
if __name__ == '__main__':
    from api_server import app
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True) 