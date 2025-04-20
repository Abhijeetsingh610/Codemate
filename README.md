# Codemate

Codemate is an agentic coding assistant that works directly in your terminal, leveraging local LLMs from Ollama. It simplifies coding tasks, provides intelligent suggestions, and supports advanced AI models like Google Gemini and Anthropic Claude.

![Version](https://img.shields.io/badge/version-0.3.0-blue)

---

## 🚀 Features

- **Interactive Chat Mode**: Have conversations with AI models for coding assistance.
- **Agent Mode**: Generate, edit, and manage code files with ease.
- **Advanced AI Support**:
  - Google Gemini (Codemate Pro Agent)
  - Anthropic Claude
  - Local Ollama models
- **Enhanced Tools**: File operations, code analysis, and terminal commands.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

---

## 🛠️ Prerequisites

Before using Codemate, ensure the following:

1. **Python**: Version 3.6 or higher.
2. **Ollama**: Installed and running. [Download Ollama](https://ollama.ai/).
3. **Language Models**: Pull one or more models into Ollama (e.g., `codellama:13b`, `mistral:7b`).
4. **Optional API Keys**:
   - Google API key (for Codemate Pro Agent with Gemini).
   - Anthropic API key (for Claude Agent).

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Codemate-Offiicial/Codemate-Pair-coder-in-terminal--Alpha.git
cd codemate
```

2. Choose one of the installation methods:

   **Option 1: Pip installation**
   ```
   pip install -e .
   ```
   
   **Option 2: Windows batch file**
   ```
   install.bat
   ```
   
   **Option 3: PowerShell users (recommended for PowerShell)**
   ```
   .\install_powershell.bat
   ```
   This creates a PowerShell module that allows you to use the `codemate` command directly in PowerShell.

## Usage

### Basic Commands

```
codemate --model MODEL_NAME --chat       # Start a chat session
codemate --model MODEL_NAME --agent      # Start an agent for coding tasks
codemate --claude-agent                  # Start Claude Agent (requires API key)
codemate --codemate-pro-agent            # Start Codemate Pro Agent (Gemini integration)
codemate --list-models                   # Show available models
codemate --no-color                      # Disable colored output
codemate help                            # Show help information
```

### Windows Users

**CMD Users**: Run `run_codemate.bat` for a convenient menu interface.

**PowerShell Users**: After running `install_powershell.bat`, you can use `codemate` commands directly in PowerShell. 
Alternatively, use `.\Use-Codemate.ps1` with arguments (the simplest approach).

### Chat Mode

Chat mode allows you to have a conversation with the LLM:

```
codemate --model llama2:7b --chat
```

#### Chat Commands

While in chat mode, you can use these special commands:
- `exit` or `quit` - End the session
- `clear` - Clear chat history
- `save` - Save conversation to file
- `help` - Show available commands

### Agent Mode

Agent mode helps you generate code based on your requirements:

```
codemate --model codellama:13b --agent
```

#### How Agent Mode Works

1. Describe what you want to build
2. The agent will generate code and list files it plans to create
3. You can view the full LLM response if needed
4. You'll be asked to confirm each file creation
5. The agent checks for existing files and handles directories automatically
6. After file creation, you can run executable files directly

### Codemate Pro Agent

AI coding assistant supporting Google Gemini and local Ollama models.

## Features

- Interactive chat interface with AI models
- Local file system access for reading and writing code
- Terminal command execution
- Support for both Google Gemini and local Ollama models

## Installation

### Basic Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/codemate-pro-agent.git
cd codemate-pro-agent

# Install the package
pip install -e .
```

### Windows-specific Installation

For Windows users, you'll need the `pyreadline3` package:

```bash
pip install -e ".[windows]"
```

### Gemini Support

To use Google Gemini models:

```bash
pip install -e ".[gemini]"
```

## Usage

Run the agent with a local Llama model:

```bash
codemate --model llama3:8b --codemate-pro-agent
```

Or with Google Gemini:

```bash
codemate --model gemini-pro --codemate-pro-agent
```

## Configuration

The agent can be configured via a `config.yaml` file in your home directory:

```yaml
api_key: your_gemini_api_key  # Required for Gemini models
model: llama3:8b  # Default model
```

## Requirements

- Python 3.8 or higher
- Ollama (for local models)
- Google API key (for Gemini models)

## Setting Up Google API Key

To use the Gemini models, you'll need to set up a Google API key:

```bash
codemate --codemate-pro-setup YOUR_API_KEY
```

## Using Ollama Models

To use local Ollama models, make sure Ollama is installed and running on your system, then:

```bash
codemate --model llama3:8b --codemate-pro-agent --use-ollama
```

You can also set the CODEMATE_OLLAMA_MODEL environment variable to specify the model:

```bash
set CODEMATE_OLLAMA_MODEL=llama3:8b
codemate --codemate-pro-agent --use-ollama
```

## Available Commands

Start the agent:
```bash
codemate --codemate-pro-agent
```

Specify a model:
```bash
codemate --codemate-pro-model gemini-1.5-pro --codemate-pro-agent
```

List available Gemini models:
```bash
codemate --codemate-pro-list-models
```

Set default model:
```bash
codemate --codemate-pro-set-default-model gemini-1.5-pro
```

## Chat Commands

- `/exit` or `/quit` - Exit the chat session
- `/help` - Show help information

## Troubleshooting

### Windows-specific Issues
- If you encounter `ModuleNotFoundError: No module named 'readline'`, run the Windows fix script as described above.

### Ollama Connection Issues
- Make sure Ollama is running locally at http://localhost:11434
- Check that the requested model is available in your Ollama installation

### API Key Issues
- Verify that your Google API key is correctly set up
- Check your API quota limits if you receive API error responses

## Examples

### Listing Available Models

```
codemate --list-models
```

### Starting Chat Mode

```
codemate --model mistral:7b --chat
```

### Using Agent Mode to Create and Run a Python Script

```
codemate --model codellama:13b --agent
```

Then describe your coding task when prompted, such as: "Create a simple weather API client in Python"

### Using Codemate Pro Agent with Gemini

```
codemate --codemate-pro-agent
```

### Using Claude Agent with a Local Model

```
codemate --model llama3:8b --local --claude-agent
```

### Automatic Model Selection

If you don't specify a model, Codemate will automatically use the first available model in your Ollama installation:

```
codemate --chat
codemate --agent
```

## Advanced Agents

Codemate includes two advanced AI coding agents:

### Codemate Pro Agent

Powered by Google's Gemini models with support for local Ollama models. Features include:
- Advanced code understanding and generation
- File system operations and terminal commands
- Rich terminal UI with syntax highlighting
- Support for both cloud and local models

See [CODEMATE_PRO_README.md](CODEMATE_PRO_README.md) for more details.

### Claude Agent

Powered by Anthropic's Claude with support for local Ollama models. Features include:
- Deep codebase understanding
- File editing and git integration
- Context-aware code generation
- Support for both API and local models

See [CLAUDE_AGENT_README.md](CLAUDE_AGENT_README.md) for more details.

## License

MIT