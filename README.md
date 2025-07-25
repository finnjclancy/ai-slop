so we want an llm to approve / reject a pr

so to do this we will:

1. use github actions to get PRs on a repo
2. extract and format this PR
3. send this info to an LLM
4. get an approve / reject response from this LLM
5. use github API to approve / reject PR