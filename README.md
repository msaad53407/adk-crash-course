# 🤖 Google ADK (Agent Development Kit) & Multi-Agent Systems Crash Course

A comprehensive, hands-on repository demonstrating modern autonomous AI agent architectures using the **Google Agent Development Kit (ADK)**, **LiteLLM**, **Gemini**, and **Pydantic**.

This course progressively builds from simple prompt-based agents up to distributed, stateful, multi-agent orchestrations with persistent memory backends.

---

## 📚 Curriculum & Module Overview

| Module | Topic | Core Concepts |
| :--- | :--- | :--- |
| **`01_basic_agent`** | **Foundational Agents** | Direct model invocation, prompt formatting, system instructions with Google ADK. |
| **`02_tool_agent`** | **Tool Calling & Execution** | Equipping agents with custom Python functions, tool schemas, and dynamic execution loops. |
| **`03_litellm_agent`** | **Model Agnostic Routing** | Leveraging LiteLLM to swap between Gemini, OpenAI, Claude, and local models seamlessly. |
| **`04_structured_output_agent`** | **Deterministic Schemas** | Enforcing strict JSON outputs and validation contracts using **Pydantic v2**. |
| **`05_sessions_state_runners`** | **Session Runners & Context** | Managing stateful conversation flows, step execution, and runner lifecycles. |
| **`06_persistent_memory`** | **Long-term Memory** | Persisting agent memory and conversation history across sessions with PostgreSQL. |
| **`07_multi_agent`** | **Multi-Agent Collaboration** | Hierarchical delegation, task handoffs, and multi-agent coordination pipelines. |
| **`08_stateful_multi_agent`** | **Advanced Multi-Agent Workflows** | Complex multi-agent topologies maintaining shared state and dynamic branching logic. |

---

## 🛠️ Tech Stack

* **Agent Framework:** `google-adk`
* **LLM Engine & Routing:** `google-generativeai`, `litellm`
* **Validation & Schemas:** `pydantic`
* **Storage & Memory:** PostgreSQL (`psycopg2-binary`)
* **Tool Integrations:** `yfinance`, `psutil`
* **Environment & Package Management:** `uv`, Python 3.13+

---

## 🚀 Getting Started

### Prerequisites
* Python `>= 3.13`
* [uv](https://github.com/astral-sh/uv) (recommended fast package manager)
* Gemini API Key (or LiteLLM supported provider keys)

### Installation
```bash
# Clone the repository
git clone https://github.com/msaad53407/adk-crash-course.git
cd adk-crash-course

# Install dependencies with uv
uv sync
```

### Environment Configuration
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
DATABASE_URL=postgresql://user:password@localhost:5432/agent_memory
```

### Running a Module
Navigate into any module directory or run directly using `uv`:
```bash
uv run python 01_basic_agent/main.py
uv run python 07_multi_agent/main.py
```

---

## 📜 License
MIT
