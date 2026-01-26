<div align="center">

# ⚡ IAcriolla

> **Inteligencia Artificial y soluciones de datos con viveza criolla 💫**
>
> [iacriolla.com](https://iacriolla.com)

[![Test Template](https://github.com/lilidl-nft/AI/actions/workflows/test-template.yml/badge.svg)](https://github.com/lilidl-nft/AI/actions/workflows/test-template.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Agentic: Ready](https://img.shields.io/badge/Agentic-Ready-blueviolet)](llms.txt)

<br />

**The Stack**

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi&logoColor=white)
![uv](https://img.shields.io/badge/uv-Dependency%20Manager-purple)
![Pydantic](https://img.shields.io/badge/Pydantic-Settings-e92063?logo=pydantic&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Coverage-green?logo=pytest&logoColor=white)

</div>

---

## 🗺️ Navigation

| 🏗️ **Templates & Configs** | 📚 **Development Guides** | 🏛️ **Architecture & AI** |
| :--- | :--- | :--- |
| [**Python Starter**](templates/python-starter/)<br>_FastAPI + uv + Structlog_ | [**Best Practices**](guides/python_best_practices.md)<br>_Zen of Python, PEP 8, Typing_ | [**RAG Systems**](architecture/rag_best_practices.md)<br>_Vectors, Chunking, Retrieval_ |
| [**Enforceable Configs**](configs/)<br>_Ruff, Mypy, Pre-commit_ | [**API Design**](guides/api_rules.md)<br>_REST, Versioning, Security_ | [**MCP Servers**](architecture/mcp_best_practices.md)<br>_Tool Design & Safety_ |
| | [**Definition of Done**](guides/testing_and_dod.md)<br>_Testing Pyramid & Quality_ | [**Agent Context**](llms.txt)<br>_Optimized for LLMs_ |

---

## 🚀 Workflow: Ship It.

Follow this checklist to go from idea to production-ready code.

### 1. Scaffold
Start your project with our battle-tested template.
```bash
# Requires cookiecutter (uv tool install cookiecutter)
cookiecutter https://github.com/lilidl-nft/AI --directory templates/python-starter
```

### 2. Enforce
Don't debate style. Enforce it from day one.
```bash
cp configs/pyproject.toml .              # The Rules
cp configs/pre-commit-config.yaml .      # The Gatekeeper
mkdir -p .github/workflows && cp configs/ci.yml .github/workflows/ # The Judge
```

### 3. Contextualize
Give your AI assistant the rules of engagement.
```bash
cp guides/gemini_rules.md .cursorrules   # Or gemini_rules.md
```

### 4. Verify
Run the quality gates. If this fails, do not commit.
```bash
uv run pytest        # Test Logic
uv run ruff check    # Fix Style
uv run mypy .        # Check Types
```

---

## 🤖 Agentic Usage

This repository is **machine-readable**.

*   **For RAG**: Feed `llms.txt` to your model for instant context.
*   **For Chat**: Use `prompts/system_prompt.md` as the System Message.
*   **For Agents**: Read `agent_manifest.json` to discover tools and templates programmatically.

---

## ⚖️ Decision Log (ADR)
*Why we do what we do.*

*   [**001: Use `uv`**](adr/001-use-uv-for-dependency-management.md) - Speed & Determinism.
*   [**002: Pragmatic Typing**](adr/002-pragmatic-strict-typing.md) - Safety without the toil.
*   [**003: `src/` Layout**](adr/003-src-layout.md) - No import hacks.
*   [**004: Async I/O**](adr/004-async-by-default.md) - Concurrency by default.