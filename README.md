# AutoGen DSA Solver

An intelligent multi-agent system built with Microsoft AutoGen that solves Data Structures and Algorithms (DSA) problems through collaborative AI agents. The system uses a problem-solving expert agent and a code executor agent working together to understand problems, generate solutions, execute code safely in Docker containers, and provide detailed explanations.

## 🚀 Features

- **Multi-Agent Collaboration**: Two specialized agents work together to solve DSA problems
  - **ProblemSolverExpert**: Analyzes problems, devises solutions, and generates Python code
  - **CodeExecutorAgent**: Safely executes code in isolated Docker containers
- **Safe Code Execution**: All code runs in Docker containers for security and isolation
- **Interactive Web Interface**: Streamlit-based web UI for easy interaction
- **Command-Line Interface**: Simple CLI for programmatic usage
- **Automatic Solution Saving**: Solutions are automatically saved to `solutions.py`
- **Comprehensive Testing**: Includes test cases with each solution
- **Real-time Streaming**: Watch agents collaborate in real-time

## 📋 Prerequisites

- Python 3.8 or higher
- Docker Desktop installed and running
- OpenAI API key

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Monish-Nallagondalla/Autogen_DSA_Solver.git
   cd Autogen_DSA_Solver
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```bash
   cp .env_example .env
   ```
   
   Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Ensure Docker is running**
   
   Make sure Docker Desktop is installed and running on your system.

## 🎯 Usage

### Web Interface (Streamlit)

Launch the interactive web interface:

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501` and enter your DSA problem in the text input field.

### Command-Line Interface

Run the solver from the command line:

```bash
python main.py
```

By default, it solves: "Write a Python Code to add 2 numbers"

To solve a custom problem, edit the `task` variable in `main.py`:

```python
task = 'Your DSA problem here'
```

## 🏗️ Project Structure

```
Autogen_DSA_Solver/
├── agents/
│   ├── problem_solver_agent.py    # Problem-solving expert agent
│   └── code_executor_agent.py     # Code execution agent
├── config/
│   ├── constants.py               # Configuration constants
│   ├── docker_utils.py            # Docker executor utilities
│   └── model_client.py            # OpenAI model client setup
├── team/
│   ├── dsa_solver_team.py         # Team configuration
│   └── data_engineer_expert.py    # Additional expert (if needed)
├── app.py                         # Streamlit web application
├── main.py                        # CLI entry point
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## 🤖 How It Works

1. **Problem Input**: User provides a DSA problem or coding task
2. **Problem Analysis**: ProblemSolverExpert analyzes the problem and devises a solution approach
3. **Code Generation**: ProblemSolverExpert generates Python code with test cases
4. **Code Execution**: CodeExecutorAgent executes the code in a Docker container
5. **Error Handling**: If errors occur, ProblemSolverExpert corrects the code and resubmits
6. **Solution Saving**: Once successful, the solution is saved to `solutions.py`
7. **Explanation**: ProblemSolverExpert provides a detailed explanation of the solution
8. **Termination**: The process ends when the agent says "STOP"

## ⚙️ Configuration

Key configuration options can be modified in `config/constants.py`:

- `MODEL`: The OpenAI model to use (default: 'gpt-4o')
- `DOCKER_WORK_DIR`: Working directory in Docker container (default: 'tmp')
- `DOCKER_TIMEOUT`: Code execution timeout in seconds (default: 120)
- `MAX_TURNS`: Maximum conversation turns between agents (default: 15)

## 📝 Example

**Input:**
```
Can you give me a solution to add 2 numbers?
```

**Process:**
1. ProblemSolverExpert analyzes the problem
2. Generates Python code with test cases
3. CodeExecutorAgent runs the code in Docker
4. Results are displayed
5. Solution is saved to `solutions.py`
6. Detailed explanation is provided

## 🔒 Security

- All code execution happens in isolated Docker containers
- No direct access to your system files
- Timeout protection prevents infinite loops
- Container cleanup after execution

## 📦 Dependencies

Key dependencies include:
- `autogen-agentchat`: Microsoft AutoGen framework
- `autogen-ext`: AutoGen extensions for code execution
- `streamlit`: Web interface framework
- `python-dotenv`: Environment variable management
- `openai`: OpenAI API client

See `requirements.txt` for the complete list.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Microsoft AutoGen](https://github.com/microsoft/autogen) for the multi-agent framework
- OpenAI for the GPT models

## 📧 Contact

For questions or issues, please open an issue on the [GitHub repository](https://github.com/Monish-Nallagondalla/Autogen_DSA_Solver).

---

**Note**: Make sure Docker is running before executing any code. The system requires Docker to safely execute code in isolated containers.
