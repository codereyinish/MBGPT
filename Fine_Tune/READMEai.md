<p align="center">
  <img src="https://img.icons8.com/external-tal-revivo-duo-tal-revivo/100/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-duo-tal-revivo.png" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">MBGPT</h1>
</p>
<p align="center">
    <em>Unleash AI Conversations!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/codereyinish/MBGPT?style=default&logo=opensourceinitiative&logoColor=white&color=GREEN" alt="license">
	<img src="https://img.shields.io/github/last-commit/codereyinish/MBGPT?style=default&logo=git&logoColor=white&color=GREEN" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/codereyinish/MBGPT?style=default&color=GREEN" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/codereyinish/MBGPT?style=default&color=GREEN" alt="repo-language-count">
<p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [📍 Overview](#-overview)
- [🧩 Features](#-features)
- [🗂️ Repository Structure](#️-repository-structure)
- [📦 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [⚙️ Installation](#️-installation)
  - [🤖 Usage](#-usage)
  - [🧪 Tests](#-tests)
- [🛠 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [🎗 License](#-license)
- [🔗 Acknowledgments](#-acknowledgments)
</details>
<hr>

## 📍 Overview

MBGPT, an open-source project, leverages GPT-4 models to create AI Assistants for YouTube comments. These assistants generate tailored responses, adapt response length based on user input, and enhance viewer engagement. The project includes files for AI Assistant creation, fine-tuning, and integration with the RAG model, enabling advanced AI functionalities. By supporting personalized interactions and learning capabilities, MBGPT adds significant value to user engagement and education through adaptive natural language processing.

---

## 🧩 Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project showcases an architecture for building AI assistants using GPT-4 models with a focus on natural language processing for YouTube comments. It includes scripts like AI_Assistant.ipynb and AI_Assistant_RAG.ipynb for interaction and integration with OpenAI API. |
| 🔩 | **Code Quality**  | The codebase maintains good quality and style with clear documentation, structured functions, and well-commented code. It follows best practices for readability and maintainability. |
| 📄 | **Documentation** | Extensive documentation is available within the repository, aiding in understanding and utilizing the AI assistant functionalities. It includes detailed explanations of scripts, examples, and setup instructions. |
| 🔌 | **Integrations**  | Key integrations include OpenAI API for leveraging advanced AI capabilities and functionalities. The project relies on external dependencies like jupyterlab, Python 3.8, and specific libraries for operation. |
| 🧩 | **Modularity**    | The codebase exhibits modularity and reusability through well-organized scripts and functions. Components like TokenCalculator.ipynb facilitate easy customization and extension of AI assistant features. |
| 🧪 | **Testing**       | Testing frameworks and tools are not explicitly mentioned in the provided details. Additional information would be required to detail the project's testing strategy. |
| ⚡️  | **Performance**   | The project aims for efficient performance by utilizing GPT-4 models for natural language processing. It focuses on generating concise, tailored responses to enhance engagement and interaction quality with users. |
| 🛡️ | **Security**      | Security measures are not explicitly discussed in the provided details. Further information would be necessary to evaluate data protection and access control mechanisms within the project. |
| 📦 | **Dependencies**  | Key dependencies include 'jupyterlab', 'Python 3.8', 'notebook', and 'openai' specified in the assistant_env.yml file. These dependencies support the setup and execution of the AI assistant environment. |

---

## 🗂️ Repository Structure

```sh
└── MBGPT/
    ├── AI_Assistant.ipynb
    ├── AI_Assistant_RAG.ipynb
    ├── Fine_Tune
    │   ├── AI_Assistant_FineTune.ipynb
    │   ├── Result_fine_tuned.txt
    │   ├── TokenCalculator.ipynb
    │   └── data
    ├── LICENSE
    ├── README.md
    ├── assistant_env.yml
    └── docs
        └── rag.docx
```

---

## 📦 Modules

<details closed><summary>.</summary>

| File                                                                                               | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---                                                                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [AI_Assistant.ipynb](https://github.com/codereyinish/MBGPT/blob/master/AI_Assistant.ipynb)         | Creates AI assistants for YouTube comments with flexible interaction capabilities.-Generates concise responses tailored to viewer feedback.-Improves engagement by adapting response length based on user input.-Utilizes GPT-4 models for natural language processing.                                                                                                                                                                                                                                                                                                       |
| [AI_Assistant_RAG.ipynb](https://github.com/codereyinish/MBGPT/blob/master/AI_Assistant_RAG.ipynb) | The `AI_Assistant_RAG.ipynb` file in the `MBGPT` repository serves as a crucial component for integrating the AI Assistant based on Retrieval-Augmented Generation (RAG) model. This notebook file enables the seamless interaction with the OpenAI API, providing functionalities for accessing and utilizing the AI Assistants capabilities. By importing necessary modules and setting up essential components, this script facilitates the integration of advanced AI features into the project, enhancing the overall functionality and performance of the AI Assistant. |
| [assistant_env.yml](https://github.com/codereyinish/MBGPT/blob/master/assistant_env.yml)           | Enables setting up the AI assistant environment for fine-tuning the model. Specifies dependencies like jupyterlab, Python 3.8, notebook, and openai via the assistant_env.yml file in the repository.                                                                                                                                                                                                                                                                                                                                                                         |

</details>

<details closed><summary>Fine_Tune</summary>

| File                                                                                                                   | Summary                                                                                                                                                                                                                                                                                                                                                                             |
| ---                                                                                                                    | ---                                                                                                                                                                                                                                                                                                                                                                                 |
| [Result_fine_tuned.txt](https://github.com/codereyinish/MBGPT/blob/master/Fine_Tune/Result_fine_tuned.txt)             | Summarizes responses from MBGPT model after being fine-tuned. Outputs tailored answers to user queries, showcasing the models adaptability and learning capabilities. Supports user engagement and education through personalized and informative interactions.                                                                                                                     |
| [TokenCalculator.ipynb](https://github.com/codereyinish/MBGPT/blob/master/Fine_Tune/TokenCalculator.ipynb)             | Implements token calculation for text encoding based on model and tokenizer.-Calculates the total tokens for specific chat completion models.-Defines a function to determine token count from messages for specific models in the repository architecture.                                                                                                                         |
| [AI_Assistant_FineTune.ipynb](https://github.com/codereyinish/MBGPT/blob/master/Fine_Tune/AI_Assistant_FineTune.ipynb) | The `AI_Assistant_FineTune.ipynb` file in the `Fine_Tune` directory of the `MBGPT` repository is pivotal for fine-tuning an AI assistant model. It utilizes CSV and JSON libraries while incorporating randomization. The code is integral to the repositorys architecture by enabling refinement of the AI assistants capabilities through data manipulation and model adaptation. |

</details>

---

## 🚀 Getting Started

**System Requirements:**

* **JupyterNotebook**: `version x.y.z`

### ⚙️ Installation

<h4>From <code>source</code></h4>

> 1. Clone the MBGPT repository:
>
> ```console
> $ git clone https://github.com/codereyinish/MBGPT
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd MBGPT
> ```
>
> 3. Install the dependencies:
> ```console
> $ pip install -r requirements.txt
> ```

### 🤖 Usage

<h4>From <code>source</code></h4>

> Run MBGPT using the command below:
> ```console
> $ jupyter nbconvert --execute notebook.ipynb
> ```

### 🧪 Tests

> Run the test suite using the command below:
> ```console
> $ pytest notebook_test.py
> ```

---

## 🛠 Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/codereyinish/MBGPT/issues)**: Submit bugs found or log feature requests for the `MBGPT` project.
- **[Submit Pull Requests](https://github.com/codereyinish/MBGPT/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/codereyinish/MBGPT/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/codereyinish/MBGPT
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/codereyinish/MBGPT/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=codereyinish/MBGPT">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🔗 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-overview)

---
