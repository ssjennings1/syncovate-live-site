# CLAUDE.md

This file provides guidance for AI assistants (Claude and others) working in this repository.

## Repository

- **Name**: syncovate-11
- **Remote**: `ssjennings1/syncovate-11`
- **Status**: Initial setup — no source files committed yet.

> **Note**: This repository was analyzed on 2026-03-11 and contained no source code. The sections below are structured to be filled in as the project evolves. Update this file whenever the project structure, tooling, or conventions change.

---

## Project Overview

<!-- Fill in once the project purpose is established -->
<!-- Example: "Syncovate is a real-time data synchronization service built with..." -->

---

## Repository Structure

<!-- Update this section once files are added -->
```
syncovate-11/
├── CLAUDE.md          # This file
└── (project files TBD)
```

---

## Development Setup

### Prerequisites

<!-- List required tools, language runtimes, package managers, etc. -->
<!-- Example:
- Node.js >= 20
- pnpm >= 9
- Docker (for local services)
-->

### Getting Started

```bash
# Clone the repository
git clone <repo-url>
cd syncovate-11

# Install dependencies (update command to match actual package manager)
# npm install / pnpm install / pip install -r requirements.txt / cargo build / go mod download

# Start development environment
# npm run dev / make dev / etc.
```

### Environment Variables

<!-- Document required environment variables here -->
<!-- Example:
Copy `.env.example` to `.env` and fill in values:
- `DATABASE_URL` — connection string for the primary database
- `API_KEY` — external service API key
-->

---

## Commands

<!-- Update these to reflect actual scripts once package.json / Makefile / etc. are added -->

| Command | Description |
|---------|-------------|
| `<build command>` | Build the project |
| `<test command>` | Run the test suite |
| `<lint command>` | Lint and format code |
| `<dev command>` | Start local development server |

---

## Testing

<!-- Describe the testing strategy and how to run tests -->
<!-- Example:
- Unit tests live alongside source files as `*.test.ts`
- Integration tests are in `tests/integration/`
- Run all tests: `npm test`
- Run a single test file: `npm test -- path/to/file.test.ts`
-->

---

## Code Conventions

<!-- Document project-specific conventions as they emerge -->

### General

- Prefer explicit over implicit.
- Keep functions small and focused on a single responsibility.
- Write tests for any non-trivial logic.

### Naming

<!-- Example:
- Files: `kebab-case`
- Functions/variables: `camelCase`
- Types/classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
-->

### Commits

- Use the [Conventional Commits](https://www.conventionalcommits.org/) format:
  ```
  <type>(<scope>): <short summary>
  ```
  Types: `feat`, `fix`, `chore`, `docs`, `refactor`, `test`, `style`, `perf`, `ci`
- Keep the subject line under 72 characters.
- Reference issue numbers where relevant (`fixes #123`).

---

## Branch Strategy

- `main` — production-ready code; protected, requires PR + review.
- `feat/<description>` — new features.
- `fix/<description>` — bug fixes.
- `chore/<description>` — maintenance tasks.

---

## Pull Requests

- Every PR should have a clear description of **what** changed and **why**.
- Link to the relevant issue.
- Ensure CI passes before requesting review.
- Keep PRs focused — one logical change per PR.

---

## Architecture Notes

<!-- Add architectural decisions, ADRs, or key design patterns here as they are established -->

---

## AI Assistant Guidelines

When working in this repository:

1. **Read before editing** — always read a file before modifying it.
2. **Minimal changes** — only change what is directly required by the task; avoid refactoring unrelated code.
3. **No speculative additions** — do not add error handling, abstractions, or features that are not explicitly requested.
4. **Test coverage** — when adding logic, add or update corresponding tests.
5. **Security** — do not introduce OWASP Top 10 vulnerabilities (XSS, SQL injection, command injection, etc.).
6. **Commit hygiene** — write descriptive commit messages following the Conventional Commits format above.
7. **Branch discipline** — develop on the designated feature branch; never push directly to `main`.
8. **Update this file** — when you discover or establish new conventions, tooling, or architectural patterns, update the relevant section of this CLAUDE.md.
