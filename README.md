# AI PR Reviewer

An AI-powered pull request reviewer that automatically approves or rejects PRs using OpenAI GPT-4o.

## How it Works

1. **GitHub Action** triggers on PR events (opened, synchronize, reopened)
2. **Extract PR Data** - Gets the PR title, description, and code diff
3. **AI Review** - Sends data to OpenAI GPT-4o for analysis
4. **Decision** - AI returns APPROVE or REJECT with reasoning
5. **GitHub API** - Automatically approves or requests changes based on AI decision

## Quick Start

```bash
# 1. Setup
git clone <your-repo>
cd ai-slop
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp config/env.example .env
# Edit .env with your API keys

# 2. Test locally
python run_server.py        # Start server
python run_tests.py         # Test API (in another terminal)

# 3. Connect to GitHub (optional)
ngrok http 5001             # Expose server
# Add ngrok URL to GitHub secrets
# Create a PR and watch AI review it!
```

## Setup

### 1. Prerequisites

- Python 3.7+
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- GitHub personal access token ([Create one here](https://github.com/settings/tokens))
- ngrok account ([Sign up here](https://dashboard.ngrok.com/signup)) for GitHub integration

### 2. Local Development Setup

1. **Clone and setup environment:**
```bash
git clone <your-repo-url>
cd ai-slop
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Create environment file:**
```bash
cp config/env.example .env
```

3. **Add your API keys to `.env`:**
```
OPENAI_API_KEY=your_openai_api_key_here
GITHUB_TOKEN=your_github_token_here
LOCAL_SERVER_URL=http://localhost:5001
```

4. **Test locally:**
```bash
# Start the server
python run_server.py

# In another terminal, run tests
python run_tests.py
```

The server will run on `http://localhost:5001` and you should see successful API tests.

### 3. GitHub Integration Setup

To enable automatic PR reviews, you need to expose your local server to GitHub:

1. **Start your local server:**
```bash
python run_server.py
```

2. **In a separate terminal, start ngrok:**
```bash
# Install ngrok first: brew install ngrok (or download from ngrok.com)
ngrok config add-authtoken YOUR_NGROK_TOKEN
ngrok http 5001
```

3. **Copy the ngrok URL** (something like `https://abc123.ngrok-free.app`)

4. **Add GitHub Secrets** in your repository settings (Settings → Secrets and variables → Actions):
   - `PERSONAL_ACCESS_TOKEN` - Your GitHub personal access token
   - `LOCAL_SERVER_URL` - Your ngrok URL (e.g., `https://abc123.ngrok-free.app`)

### 4. GitHub Token Setup

Create a fine-grained personal access token with these permissions:
- **Repository access**: Select your repository
- **Permissions needed**:
  - Pull requests: Read and write
  - Contents: Read-only  
  - Metadata: Read-only

### 5. Test End-to-End

1. **Make sure both are running:**
   - Local server: `python run_server.py`
   - ngrok tunnel: `ngrok http 5001`

2. **Create a test PR** with some code changes

3. **Watch the magic happen:**
   - GitHub Action triggers automatically
   - AI analyzes your code with GPT-4o
   - PR gets approved/rejected with detailed feedback

### 6. Troubleshooting

**Local server won't start?**
- Make sure you're in the virtual environment: `source venv/bin/activate`
- Check that all dependencies are installed: `pip install -r requirements.txt`

**GitHub Action fails?**
- Verify your ngrok tunnel is active and accessible
- Check that GitHub secrets are set correctly
- Ensure your GitHub token has the right permissions

**AI not responding?**
- Verify your OpenAI API key is correct and has billing set up
- Check the GitHub Action logs for detailed error messages

## API Endpoints

- `GET /health` - Health check
- `POST /review` - Review a PR (expects JSON with `title`, `body`, `diff`)

## Example PR Data Format

```json
{
  "title": "Add new feature",
  "body": "This PR adds a new feature to improve user experience",
  "diff": "@@ -1,3 +1,5 @@\n function hello() {\n-  console.log('Hello');\n+  console.log('Hello World');\n+  console.log('New feature added');\n }"
}
```

## Response Format

```json
{
  "ai_response": "APPROVE - Code looks good, follows best practices",
  "decision": "approve",
  "reason": "Code looks good, follows best practices"
}
```

## Customization

- Modify the AI prompt in `api_server.py` to change review criteria
- Adjust the OpenAI model or parameters
- Add additional PR data fields for more context

## Security Notes

- Keep your API keys secure
- Consider rate limiting for the API
- Review AI decisions before enabling auto-merge
- Monitor the AI's decisions to ensure quality

## Troubleshooting

1. **GitHub Action fails**: Check that your local server is accessible
2. **OpenAI errors**: Verify your API key and billing
3. **Permission errors**: Ensure GitHub token has proper permissions
4. **Network issues**: Use ngrok or deploy to cloud for public access