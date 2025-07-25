# AI PR Reviewer

An AI-powered pull request reviewer that automatically approves or rejects PRs using OpenAI GPT-4o.

## How it Works

1. **GitHub Action** triggers on PR events (opened, synchronize, reopened)
2. **Extract PR Data** - Gets the PR title, description, and code diff
3. **AI Review** - Sends data to OpenAI GPT-4o for analysis
4. **Decision** - AI returns APPROVE or REJECT with reasoning
5. **GitHub API** - Automatically approves or requests changes based on AI decision

## Setup

### 1. Local API Server

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create environment file:
```bash
cp env.example .env
```

3. Add your API keys to `.env`:
```
OPENAI_API_KEY=your_openai_api_key_here
GITHUB_TOKEN=your_github_token_here
LOCAL_SERVER_URL=http://localhost:5000
```

4. Start the server:
```bash
python api_server.py
```

The server will run on `http://localhost:5000`

### 2. GitHub Repository Setup

1. **Add GitHub Secrets** in your repository settings:
   - `GITHUB_TOKEN` - GitHub personal access token with repo permissions
   - `LOCAL_SERVER_URL` - URL of your local server (e.g., `http://localhost:5000`)

2. **Make your local server accessible** to GitHub Actions:
   - Use ngrok: `ngrok http 5000`
   - Or deploy to a cloud service (Heroku, Railway, etc.)
   - Update the `LOCAL_SERVER_URL` secret with the public URL

### 3. Test the Setup

1. Create a test PR in your repository
2. The GitHub Action should trigger automatically
3. Check the Action logs to see the AI review process
4. The PR should be approved or rejected based on the AI decision

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