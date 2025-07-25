import os
import json
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

def call_openai_for_review(pr_data):
    """Send PR data to OpenAI and get review decision"""
    
    # Format the prompt
    prompt = f"""
    Review this pull request and respond with either 'APPROVE' or 'REJECT' followed by a brief reason.
    
    PR Title: {pr_data.get('title', 'No title')}
    PR Description: {pr_data.get('body', 'No description')}
    
    Code Changes:
    {pr_data.get('diff', 'No diff provided')}
    
    Respond with format: APPROVE/REJECT - [reason]
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a code reviewer. Analyze pull requests for code quality, security, and best practices."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.1
        )
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        print(f"Error calling OpenAI: {e}")
        return "REJECT - Error processing request"

def parse_ai_response(response):
    """Parse AI response to extract decision and reason"""
    response = response.upper()
    
    if response.startswith('APPROVE'):
        return {
            'decision': 'approve',
            'reason': response.replace('APPROVE', '').strip(' -')
        }
    elif response.startswith('REJECT'):
        return {
            'decision': 'reject', 
            'reason': response.replace('REJECT', '').strip(' -')
        }
    else:
        return {
            'decision': 'reject',
            'reason': 'Unable to parse AI response'
        }

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})

@app.route('/review', methods=['POST'])
def review_pr():
    """Main endpoint to review a PR"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Call OpenAI for review
        ai_response = call_openai_for_review(data)
        
        # Parse the response
        result = parse_ai_response(ai_response)
        
        return jsonify({
            'ai_response': ai_response,
            'decision': result['decision'],
            'reason': result['reason']
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True) 