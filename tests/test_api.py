#!/usr/bin/env python3
"""
Test script for the AI PR Reviewer API
"""

import requests
import json

def test_api():
    """Test the API with sample PR data"""
    
    # Sample PR data
    test_pr_data = {
        "title": "Add user authentication feature",
        "body": "This PR adds user authentication with JWT tokens and password hashing for security.",
        "diff": """
@@ -1,3 +1,15 @@
+import jwt
+import bcrypt
+
+def hash_password(password):
+    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
+
+def verify_password(password, hashed):
+    return bcrypt.checkpw(password.encode('utf-8'), hashed)
+
+def create_token(user_id):
+    return jwt.encode({'user_id': user_id}, 'secret', algorithm='HS256')
+
 class User:
-    def __init__(self, name):
+    def __init__(self, name, password):
         self.name = name
+        self.password_hash = hash_password(password)
     """
    }
    
    # Test the API
    try:
        response = requests.post(
            'http://localhost:5001/review',
            json=test_pr_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ API Test Successful!")
            print(f"AI Response: {result['ai_response']}")
            print(f"Decision: {result['decision']}")
            print(f"Reason: {result['reason']}")
        else:
            print(f"❌ API Test Failed: {response.status_code}")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API server. Make sure it's running on localhost:5001")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_health():
    """Test the health endpoint"""
    try:
        response = requests.get('http://localhost:5001/health')
        if response.status_code == 200:
            print("✅ Health check passed")
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API server")

if __name__ == "__main__":
    print("Testing AI PR Reviewer API...")
    print("-" * 40)
    
    test_health()
    print()
    test_api() 