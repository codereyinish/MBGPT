<p align="center">
  <img src="https://img.icons8.com/external-tal-revivo-regular-tal-revivo/96/external-readme-is-a-easy-to-build-a-developer-hub-that-adapts-to-the-user-logo-regular-tal-revivo.png" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">MBGPT</h1>
</p>
<p align="center">
    <em>Enhancing Interactions, Tailoring Smarter AI Responses.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/codereyinish/MBGPT?style=flat&logo=opensourceinitiative&logoColor=white&color=black" alt="license">
	<img src="https://img.shields.io/github/last-commit/codereyinish/MBGPT?style=flat&logo=git&logoColor=white&color=black" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/codereyinish/MBGPT?style=flat&color=black" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/codereyinish/MBGPT?style=flat&color=black" alt="repo-language-count">
</p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=flat&logo=Jupyter&logoColor=white" alt="Jupyter">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/conda-44A833.svg?style=flat&logo=conda&logoColor=white" alt="Conda">
	<img src="https://img.shields.io/badge/pip-3775A9.svg?style=flat&logo=pypa&logoColor=white" alt="pip">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU Bash">
	<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
	<img src="https://img.shields.io/badge/OpenAI-1.35.3-412991.svg?style=flat&logo=OpenAI&logoColor=white" alt="OpenAI">
	<br>
</p>

<details>
  <summary>Table of Contents</summary><br>
	
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [⚙️ Install](#-install)
  - [🤖 Usage ](#-usage)
- [🚧 Limitations and Future](#-limitations-and-future-plans-of-project)
  - [Limitations 🛑](#-limitations)
  - [Future Plans 🌱](#-future-plans)
- [🤝 Contributing](#-contributing)	 
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)
</details>
<hr>


## 📍 Overview

***🌟 Motivation***

I developed this project to revolutionize YouTube commenting by moving beyond generic responses. The goal is for the AI assistant to provide detailed and context-specific answers that enrich viewer interactions with video and blog content.

<br>

***💡 Idea***

The core idea behind this project is to transform how YouTube comments are handled by leveraging advanced AI capabilities. When a user poses a question, the AI assistant avoids generic responses by using Retrieval-Augmented Generation (RAG). This technology allows the assistant to dive into uploaded content such as files, documents, references, blogs, or YouTube videos.
By analyzing this content, the AI identifies relevant information related to the user's query. It then generates a detailed response that mirrors the depth and contextuality of human answers. This approach ensures that responses are not only accurate but also meaningful, enriching viewer interaction with tailored insights and references.
Ultimately, the goal is to create an AI assistant that enhances engagement on YouTube and similar platforms by providing personalized and informative responses, fostering deeper connections between creators and their audience.




## 🧩 Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project showcases an architecture for building AI assistants using GPT-4 models with a focus on natural language processing for YouTube comments. It includes scripts like AI_Assistant.ipynb and AI_Assistant_RAG.ipynb for interaction and integration with OpenAI API. |
| 🔩 | **Code Quality**  | The code is maintained within notebooks, offering clear, iterative examples of usage and fine-tuning approaches. |
| 📄 | **Documentation** | Documentation is mainly in the form of inline comments within notebooks, explaining processes and configurations.|
| 🔌 | **Integrations**  | Integrates with OpenAI's API for AI model interactions and enhancements.                                         |
| 🧩 | **Modularity**    | Highly modular with distinct notebooks for different functionalities like API integration and model fine-tuning.|
| 🧪 | **Testing**       | No explicit testing frameworks or tools mentioned; testing methodologies are not clarified.                      |
| ⚡️  | **Performance**   | Efficiency in API usage and model optimization discussed, but no specific metrics or performance data provided.   |
| 🛡️ | **Security**      | Basic security by handling sensitive credentials for API access; further security practices are not detailed.    |
| 📦 | **Dependencies**  | Relies on Python, JupyterLab, and specific libraries like Notebook and OpenAI accessible via Conda and pipspecified in the assistant_env.yml file. These dependencies support the setup and execution of the AI assistant environment. |      


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

* **Python**: 3.8+
* **JupyterNotebook**
* **Package manager/Container**: `conda`(Recommended), `pip`
* **LLM service**: `OpenAI` (Recommended), `Google Gemini`

### ⚙️ Installation

>1. **Clone the repository**:
>```bash
>git clone https://github.com/codereyinish/MBGPT.git
>```
>
> 2. Change to the project directory:
> ```bash
> $ cd MBGPT
> ```
>
>3. **Create the Conda environment**:
>
> ![conda](https://img.shields.io/badge/Anaconda-44A833.svg?style=flat&logo=Anaconda&logoColor=white)
>
>```bash
>conda env create -f assistant_env.yml
> ```
>4. **Activate the environment**:
> ```bash
> conda activate assistant_env
> ```
>5. **Set up the OpenAI key**:
>Obtain your OpenAI API key from [OpenAI](https://www.openai.com/). Create a file named `.env` in the project root directory and add:
><a href="https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety" target ="_blank" style = "text-decoration: none">Refer this</a>
>```env
>OPENAI_API_KEY=your_openai_api_key
>```


### 🤖 Usage

<h4>From <code>source</code></h4>

> Run whichever .ipynb file  you want to experiment with this jupyter command:
> ```console
> $ jupyter nbconvert --execute AI_Assistant.ipynb
> $ jupyter nbconvert --execute AI_Assistant_RAG.ipynb
>
> ```



---

---

### Performance Evolution 📈

#### 1. Pure Assistant with Assistant API :
<details closed> <summary> Initial implementation using OpenAI's Assistant API for generic responses. Source: ${\textsf{\color{green}AI_Assistant.ipynb}}$ </summary>
	gfdfs
</details>

### 🚧 Limitations and Future Plans of Project 

#### Limitations 🛑
1. **💸Cost of OpenAI API**: Utilizing the OpenAI Assistant API can become expensive, particularly if scaling the application. This cost consideration is important for long-term sustainability.
   
2. **📈Scalability Issues**: Integrating the AI Note Assistant into a website or scaling it for broader use may pose challenges due to resource demands and performance considerations.


#### Future Plans 🌱

To address these limitations and enhance the AI Note Assistant, future improvements include:

- **Fine-tuning Open Source LLMs**: Developing and integrating Open Source Language Model (LLM) solutions, which can offer cost-effective alternatives to proprietary APIs like OpenAI.
  
- **Enhanced Response Design**: Designing responses with a mix of components to avoid generic outputs:
  - **ChatGPT Writing Fillip**: Injecting creative and engaging writing style cues into responses.
  - **Notebook Content Retrieval**: Extracting specific and relevant information directly from uploaded documents.
  - **Scraping Linked Resources**: Scraping supplementary information from linked resources to enrich responses.
  - **Few-shot Learning Examples**: Incorporating few-shot learning examples to diversify writing styles and enhance context-specific responses.

These improvements aim to not only reduce operational costs but also enrich user interactions by providing more dynamic and contextually relevant AI responses.


---


## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/codereyinish/MBGPT.git/issues)**: Submit bugs found or log feature requests for the `MBGPT` project.
- **[Submit Pull Requests](https://github.com/codereyinish/MBGPT.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/codereyinish/MBGPT.git/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/codereyinish/MBGPT.git
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
   <a href="https://github.com{/codereyinish/MBGPT.git/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=codereyinish/MBGPT.git">
   </a>
</p>
</details>

---

## 🎗 License

[MIT-License](LICENSE)

---

## 👏 Acknowledgments

- <a href="https://github.com/ShawhinT"  style="text-decoration: none;"> ShawinT </a>

<br>
<p align="right">
  <a href="#-overview"><b>Return</b></a>
</p>

---
