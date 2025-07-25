# Project Structure

```
ai-slop/
├── src/                    # Source code
│   ├── api/               # API server
│   │   └── api_server.py  # Main Flask API server
│   └── utils/             # Utility functions
│       ├── math_utils.py  # Math utilities
│       └── utils.py       # General utilities
├── tests/                 # Test files
│   └── test_api.py       # API tests
├── config/               # Configuration files
│   └── env.example       # Environment variables template
├── docs/                 # Documentation
│   └── project-structure.md  # This file
├── .github/              # GitHub Actions workflows
│   └── workflows/
│       └── pr-review.yml # AI PR reviewer workflow
├── run_server.py         # Server startup script
├── run_tests.py          # Test runner script
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
└── README.md            # Main documentation
```

## How to Run

### Start the API Server
```bash
python run_server.py
```

### Run Tests
```bash
python run_tests.py
```

### Setup Environment
```bash
cp config/env.example .env
# Edit .env with your API keys
```

## Key Components

- **API Server**: `src/api/api_server.py` - Main Flask app that handles PR reviews
- **Utilities**: `src/utils/` - Helper functions and utilities
- **Tests**: `tests/` - API tests and validation
- **Config**: `config/` - Configuration templates
- **Workflows**: `.github/workflows/` - GitHub Actions for automated PR review 