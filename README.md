# Jenix

Jenix is an agentic coding assistant that works directly in your terminal, leveraging local LLMs from Ollama. It simplifies coding tasks, provides intelligent suggestions.

![Version](https://img.shields.io/badge/version-0.1.3-blue)

---

## 🚀 Features

- **Interactive Chat Mode**: Have conversations with AI models for coding assistance.
- **Agent Mode**: Generate, edit, and manage code files with ease.
- **Advanced AI Support**:
  - Local Ollama models
- **Enhanced Tools**: File operations, code analysis, and terminal commands.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

---

## 🛠️ Prerequisites

Before using Jenix, ensure the following:

1. **Python**: Version 3.6 or higher.
2. **Ollama**: Installed and running. [Download Ollama](https://ollama.ai/).
3. **Language Models**: Pull one or more models into Ollama (e.g., `codellama:13b`, `mistral:7b`).

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


## Usage

Run the agent with a local Llama model:

```bash
jenix --model llama3:8b --jenix-pro-agent
```



## Requirements

- Python 3.8 or higher
- Ollama (for local models)



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


## Chat Commands

- `/exit` or `/quit` - Exit the chat session
- `/help` - Show help information

## Troubleshooting

### Windows-specific Issues
- If you encounter `ModuleNotFoundError: No module named 'readline'`, run the Windows fix script as described above.

### Ollama Connection Issues
- Make sure Ollama is running locally at http://localhost:11434
- Check that the requested model is available in your Ollama installation


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

```

### Automatic Model Selection

If you don't specify a model, Jenix will automatically use the first available model in your Ollama installation:

```
jenix --chat
jenix --agent
```

## License

MIT