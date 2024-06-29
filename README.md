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

The MBGPT project introduces an advanced AI assistant designed specifically for enhancing user engagement on YouTube through personalized interactions. This software utilizes OpenAIs platform to manage and respond to user comments effectively, ensuring each interaction is tailored to the users needs and the complexity of their inquiries. Key components of the project include fine-tuning the AI model to improve its accuracy and relevance in communication, as evidenced through dedicated notebooks for API interactions and model customization. The MBGPT project not only boosts user interaction but also streamlines the integration and customization process, making it a valuable tool for creators aiming to establish a responsive and engaging online presence.

---

## 🧩 Features

|    | Feature           | Description                                                                                                     |
|----|-------------------|-----------------------------------------------------------------------------------------------------------------|
| ⚙️  | **Architecture**  | Utilizes Jupyter Notebooks for modular development of AI functionalities, focusing on interaction via OpenAI.    |
| 🔩 | **Code Quality**  | The code is maintained within notebooks, offering clear, iterative examples of usage and fine-tuning approaches. |
| 📄 | **Documentation** | Documentation is mainly in the form of inline comments within notebooks, explaining processes and configurations.|
| 🔌 | **Integrations**  | Integrates with OpenAI's API for AI model interactions and enhancements.                                         |
| 🧩 | **Modularity**    | Highly modular with distinct notebooks for different functionalities like API integration and model fine-tuning.|
| 🧪 | **Testing**       | No explicit testing frameworks or tools mentioned; testing methodologies are not clarified.                      |
| ⚡️  | **Performance**   | Efficiency in API usage and model optimization discussed, but no specific metrics or performance data provided.   |
| 🛡️ | **Security**      | Basic security by handling sensitive credentials for API access; further security practices are not detailed.    |
| 📦 | **Dependencies**  | Relies on Python, JupyterLab, and specific libraries like Notebook and OpenAI accessible via Conda and pip.       |
```

---

## 🗂️ Repository Structure

```sh
└── MBGPT/
    ├── AI_Assistant.ipynb
    ├── AI_Assistant_FineTune.ipynb
    ├── README.md
    ├── assistant_env.yml
    └── docs
        └── rag.docx
```

---

## 📦 Modules

<details closed><summary>.</summary>

| File                                                                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---                                                                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [AI_Assistant.ipynb](https://github.com/codereyinish/MBGPT.git/blob/master/AI_Assistant.ipynb)                   | AI_Assistant.ipynb establishes an AI-powered assistant designed for interacting with users on YouTube. It manages responses to user comments, tailoring engagement based on the contents complexity and user feedback. The notebook also handles API interactions and demonstrates efficient message management through OpenAIs platform.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [AI_Assistant_FineTune.ipynb](https://github.com/codereyinish/MBGPT.git/blob/master/AI_Assistant_FineTune.ipynb) | The file `AI_Assistant_FineTune.ipynb` within the MBGPT repository plays a crucial role in the configuration and enhancement of the AI assistant developed in this project. This Jupyter notebook specifically focuses on fine-tuning the underlying machine learning model, leveraging the OpenAI platform. Through the initial code snippets, its evident that the notebook handles environment setup and credentials configuration essential for accessing OpenAI's API.The primary goal of this notebook is to adapt the AI model to better suit specific tasks or improve performance by optimizing its responses. This customization is integral to evolving the AI Assistant's capabilities, ensuring it aligns more closely with user expectations and the functional requirements stipulated in the broader project scope.This fine-tuning process is a key component of the repositorys architecture, suggesting a sophisticated use of machine learning techniques to refine the assistant's interaction quality. The other files in the repository, such as `AI_Assant.ipynb`, likely utilize the enhanced model developed here, making this notebook a foundational piece in the overall functionality of the AI assistant system hosted in the MBGPT repository. |
| [assistant_env.yml](https://github.com/codereyinish/MBGPT.git/blob/master/assistant_env.yml)                     | Defines the environment setup for the MBGPT project, specifying necessary software dependencies such as JupyterLab, Python, and specific versions of Notebook and OpenAI libraries through Conda and pip, ensuring consistent development and execution conditions across different setups.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

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
> $ git clone https://github.com/codereyinish/MBGPT.git
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


---

### 🚧 Limitations and Future Plans of Project 

#### Limitations 🛑
1. **💸Cost of OpenAI API**: Utilizing the OpenAI Assistant API can become expensive, particularly if scaling the application. This cost consideration is important for long-term sustainability.
   
2. **📈Scalability Issues**: Integrating the AI Note Assistant into a website or scaling it for broader use may pose challenges due to resource demands and performance considerations.

3. **🤖 Potential for Generic Responses**: While ChatGPT effectively references notebook content for responses, the answers might sometimes appear too similar or copy-pasted, lacking personalized engagement.

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
