# Jenix

Jenix is an agentic coding assistant that works directly in your terminal, leveraging local LLMs from Ollama. It simplifies coding tasks, provides intelligent suggestions, and supports advanced AI models like Google Gemini and Anthropic Claude.

![Version](https://img.shields.io/badge/version-0.1.0-blue)

---

## 🚀 Features

- **Interactive Chat Mode**: Have conversations with AI models for coding assistance.
- **Agent Mode**: Generate, edit, and manage code files with ease.
- **Advanced AI Support**:
  - Google Gemini (Jenix Pro Agent)
  - Anthropic Claude
  - Local Ollama models
- **Enhanced Tools**: File operations, code analysis, and terminal commands.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

---

## 🛠️ Prerequisites

Before using Jenix, ensure the following:

1. **Python**: Version 3.6 or higher.
2. **Ollama**: Installed and running. [Download Ollama](https://ollama.ai/).
3. **Language Models**: Pull one or more models into Ollama (e.g., `codellama:13b`, `mistral:7b`).
4. **Optional API Keys**:
   - Google API key (for Jenix Pro Agent with Gemini).
   - Anthropic API key (for Claude Agent).

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Abhijeetsingh610/Jenix.git
cd Jenix
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
   This creates a PowerShell module that allows you to use the `Jenix` command directly in PowerShell.

## Usage

### Basic Commands

```
Jenix --model MODEL_NAME --chat       # Start a chat session
jenix --model MODEL_NAME --agent      # Start an agent for coding tasks
jenix --claude-agent                  # Start Claude Agent (requires API key)
jenix --jenix-pro-agent            # Start Jenix Pro Agent (Gemini integration)
jenix --list-models                   # Show available models
jenix --no-color                      # Disable colored output
jenix help                            # Show help information
```

### Windows Users

**CMD Users**: Run `run_jenix.bat` for a convenient menu interface.

**PowerShell Users**: After running `install_powershell.bat`, you can use `jenix` commands directly in PowerShell. 
Alternatively, use `.\Use-Jenix.ps1` with arguments (the simplest approach).

### Chat Mode

Chat mode allows you to have a conversation with the LLM:

```
jenix --model llama2:7b --chat
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
jenix --model codellama:13b --agent
```

#### How Agent Mode Works

1. Describe what you want to build
2. The agent will generate code and list files it plans to create
3. You can view the full LLM response if needed
4. You'll be asked to confirm each file creation
5. The agent checks for existing files and handles directories automatically
6. After file creation, you can run executable files directly

### Jenix Pro Agent

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
git clone https://github.com/Abhijeetsingh610/Jenix.git
cd jenix-pro-agent

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
jenix --model llama3:8b --jenix-pro-agent
```

Or with Google Gemini:

```bash
jenix --model gemini-pro --jenix-pro-agent
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
jenix --jenix-pro-setup YOUR_API_KEY
```

## Using Ollama Models

To use local Ollama models, make sure Ollama is installed and running on your system, then:

```bash
jenix --model llama3:8b --jenix-pro-agent --use-ollama
```

You can also set the jenix_OLLAMA_MODEL environment variable to specify the model:

```bash
set Jenix_OLLAMA_MODEL=llama3:8b
jenix --jenix-pro-agent --use-ollama
```

## Available Commands

Start the agent:
```bash
jenix --jenix-pro-agent
```

Specify a model:
```bash
jenix --jenix-pro-model gemini-1.5-pro --jenix-pro-agent
```

List available Gemini models:
```bash
jenix --jenix-pro-list-models
```

Set default model:
```bash
jenix --jenix-pro-set-default-model gemini-1.5-pro
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
jenix --list-models
```

### Starting Chat Mode

```
jenix --model mistral:7b --chat
```

### Using Agent Mode to Create and Run a Python Script

```
jenix --model codellama:13b --agent
```

Then describe your coding task when prompted, such as: "Create a simple weather API client in Python"

### Using Jenix Pro Agent with Gemini

```
jenix --jenix-pro-agent
```

### Using Claude Agent with a Local Model

```
jenix --model llama3:8b --local --claude-agent
```

### Automatic Model Selection

If you don't specify a model, Jenix will automatically use the first available model in your Ollama installation:

```
jenix --chat
jenix --agent
```

## Advanced Agents

Jenix includes two advanced AI coding agents:

### Jenix Pro Agent

Powered by Google's Gemini models with support for local Ollama models. Features include:
- Advanced code understanding and generation
- File system operations and terminal commands
- Rich terminal UI with syntax highlighting
- Support for both cloud and local models

See [Jenix_PRO_README.md](Jenix_PRO_README.md) for more details.

### Claude Agent

Powered by Anthropic's Claude with support for local Ollama models. Features include:
- Deep codebase understanding
- File editing and git integration
- Context-aware code generation
- Support for both API and local models

See [CLAUDE_AGENT_README.md](CLAUDE_AGENT_README.md) for more details.

## License

MIT