# Create Cursor Dev Template

A custom development template for Cursor/VS Code that provides a pre-configured development environment with optimized settings, recommended extensions, and AI assistant configurations.

## 🚀 Features

### Development Environment
- **Pre-configured VS Code/Cursor settings** for optimal development experience
- **Curated extension recommendations** for React, TypeScript, Python, and general development
- **Custom AI assistant configurations** supporting multiple providers (Claude, Gemini, OpenAI)
- **Optimized editor settings** with Fira Code font, ligatures, and smooth animations

### Included Extensions
- **React Development**: ES7+ React/Redux/React-Native snippets
- **Code Quality**: Prettier, Error Lens, Bracket Pair Colorizer
- **Styling**: Tailwind CSS IntelliSense, Styled Components
- **Productivity**: Auto Close Tag, Auto Rename Tag, Path Intellisense
- **Languages**: Python, Java, Jupyter support
- **Version Control**: GitLens
- **Themes**: Material Icon Theme, One Dark Pro, Material Theme

---

### 🧠 Agent Workflow (AI Development Automation)

A complete, interactive agent workflow for automating the software development lifecycle using the [Pocket Flow Framework](https://pypi.org/project/pocketflow/). This workflow guides you from problem definition to implementation, testing, and documentation—all powered by modular AI agents.

**Key Features:**
- 6-node agent network: Problem Acquisition, Clarification, Planning, Implementation, Testing, Documentation
- Interactive, step-by-step automation of real-world software projects
- Generates requirements, plans, code, tests, and documentation
- Integrates with Git for version control
- Easily extensible and customizable

**Location:** `template/src/agent_workflow.py`

#### Installation (Python)

1. Ensure you have Python 3.8+ installed.
2. Install the [pocketflow](https://pypi.org/project/pocketflow/) framework:
   ```bash
   pip install pocketflow
   ```

#### Usage

```bash
cd template/src
python agent_workflow.py
```

You will be guided through a series of prompts to define your project, clarify requirements, plan, implement, test, and generate documentation. Artifacts (requirements, plans, code, test reports, docs) are saved in the current directory.

---

### AI Assistant Configuration
- **Multi-provider support**: Claude, Gemini, and OpenAI
- **Custom API configurations** for each provider
- **Environment variable integration** for secure API key management
- **Default provider selection** (Claude)

## 📦 Installation

### Prerequisites
- Node.js (version 14 or higher)
- npm or yarn package manager

### Install the Template
```bash
npm install -g @singapore2022/create-cursor-dev
```

## 🛠️ Usage

### Create a New Project
```bash
# Create project in current directory
create-cursor-dev

# Create project in specific directory
create-cursor-dev my-project-name
```

### Manual Installation
If you prefer to install manually:
```bash
# Clone or download the template
git clone <repository-url>
cd cursor_dev_template

# Install dependencies (if any)
npm install

# Run the template
node index.js [target-directory]
```

## 🔧 Configuration

### AI Assistant Setup
The template includes pre-configured AI assistant settings. To use them:

1. **Set up API keys** as environment variables:
   ```bash
   export CLAUDE_API_KEY="your-claude-api-key"
   export GEMINI_API_KEY="your-gemini-api-key"
   export OPENAI_API_KEY="your-openai-api-key"
   ```

2. **Configure in Cursor/VS Code**:
   - The settings are automatically applied when you open the project
   - Default provider is set to Claude
   - You can switch between providers in the Cursor AI settings

### Customizing Settings
- **VS Code Settings**: Edit `template/.vscode/settings.json`
- **Extensions**: Modify `template/.vscode/extensions.json`
- **Cursor Rules**: Update `template/.cursor/.cursorrules`

## 🏗️ Build and Development

### Local Development
```bash
# Clone the repository
git clone <repository-url>
cd cursor_dev_template

# Install dependencies
npm install

# Test the template locally
node index.js test-project
```

### Building for Distribution
```bash
# Ensure all files are included
npm run build  # if you have a build script

# Test the package locally
npm pack
npm install -g ./singapore2022-create-cursor-dev-0.1.1.tgz
```

## 📤 Publishing

### Prepare for Publishing
1. **Update version** in `package.json`:
   ```json
   {
     "version": "0.1.2"
   }
   ```

2. **Verify package contents** in `package.json`:
   ```json
   {
     "files": [
       "template",
       "index.js"
     ]
   }
   ```

3. **Test the package**:
   ```bash
   npm pack
   npm install -g ./singapore2022-create-cursor-dev-0.1.2.tgz
   create-cursor-dev test-project
   ```

### Publish to npm
```bash
# Login to npm (if not already logged in)
npm login

# Publish the package
npm publish

# For scoped packages, ensure you have the right permissions
npm publish --access public
```

### Publishing Checklist
- [ ] Update version number in `package.json`
- [ ] Test the package locally with `npm pack`
- [ ] Verify all template files are included
- [ ] Check that the binary works correctly
- [ ] Run `npm publish`

## 📁 Project Structure

```
cursor_dev_template/
├── index.js              # Main template generator script
├── package.json          # Package configuration
├── template/             # Template files
│   ├── .vscode/         # VS Code/Cursor settings
│   │   ├── extensions.json
│   │   └── settings.json
│   ├── .cursor/         # Cursor-specific configuration
│   │   └── .cursorrules
│   └── src/             # Source code directory
│       └── agent_workflow.py  # AI agent workflow (Pocket Flow)
└── README.md            # This file
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Cursor team for the amazing AI-powered editor
- VS Code community for the excellent extensions
- All contributors who help improve this template

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](../../issues) page for existing solutions
2. Create a new issue with detailed information
3. Contact the maintainer at [your-email@example.com]

---

**Happy coding with Cursor! 🎉**
