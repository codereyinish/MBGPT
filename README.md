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
  - [Current Limitations 🛑](#-current-limitations)
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
<details closed> <summary> Initial implementation using OpenAI's Assistant API with now few shots prompting. Source: <a href="https://github.com/codereyinish/MBGPT/blob/main/Results/Result_Pure_AI_Assistant.txt%20">Result_Pure_AI_Assistant.txt</a> </summary>
<br>
This stage represents the baseline functionality of the AI assistant. It relies entirely on OpenAI's API to generate responses, which are typically broad and generalized. Even for simple comments, the responses are too detailed and doesnt feel like a huamn replying, instead it seems like a writer is replying.. For context-specific questions, the answers become even more excessively long without RAG implementation. While this approach provides a wide range of capabilities, it lacks specificity to your particular use case. 

</details>


#### 2. Few-Shot Learning Enhancement :
<details closed> <summary> Improved generic replies using few-shot examples for more context-aware responses. Source: <a href="https://github.com/codereyinish/MBGPT/blob/main/Results/Result_Pure_Assistant_FewShots.txt%20">Result_Pure_Assistant_FewShots.txt</a></summary>
<br>
In this phase, we introduced few-shot learning techniques to guide the assistant model towards more YouTube-like responses. By providing examples of typical comments, we improved the AI's ability to imitate few shot examples and generate  appropriate HUMAN ALIKE, SHORT replies for simple comments to some extent .

 However, for context-specific questions, the AI still tended to give overly detailed explanations rather than concise, YouTube-style replies which guide us to implement RAG.
	
</details>

#### 3. RAG Implementation
<details closed> <summary> Integrated OpenAI's out of the box Retrieval-Augmented Generation (RAG) by uploading document  to the Assistant api, resulting in more specific, document-based responses. Source: <a href= "https://github.com/codereyinish/MBGPT/blob/main/Results/Result_Pure_Assistant_RAG_FewShots.txt">Result_Pure_Assistant_RAG_FewShots.txt</a> </summary>
<br> 
By uploading files to OpenAI's API storage, creating a vector store, and equipping the assistant with the files' knowledge resources and tools to retrieve details using the OpenAI's built-in RAG implementation, we implemented RAG. The successfuly managed to train the assistant to answer the questin by referring from the given document instead of generating generic answer by itself. 
</details>

#### 4. Fine-Tune Implementation
<details closed > <summary> Imporivng the Style/TONE of Human-Like AI Responses Through Fine-Tuning.  Source: <a href= "https://github.com/codereyinish/MBGPT/blob/main/Fine_Tune/Result_fine_tuned.txt"> Result_fine_tuned.txt</a>
</summary>
<br>
We fine-tuned the model using conversation examples, achieving more human-like responses. So far, we have successfully managed to get short, human-like replies for simple comments with good sentiment understanding from the model. We also managed to get context-specific answers by referring to the documents we uploaded. However, something is still missing—the human touch. Despite our efforts, it still feels somewhat artificial. There's a saying that we should switch to fine-tuning from detailed prompting when it's easier to "show, not tell." And guess what? We managed to get almost perfect human-like comment responses, which I think you will find hard to believe.</details>


---


### 🚧 Limitations and Future Plans of Project 



#### Current Limitations 🛑

1. **API Lock-in 🔒**: The assistant is accessible only through the OpenAI API, limiting flexibility and control.

2. **Cost Considerations 💸**: 
   - API usage costs can escalate rapidly, especially when scaling for widespread business applications.
   - Cost of training the the base model(which I dont think is a big issue, because even fine-tuning the open source cost compuational resources,      and given the Open_AI hyper -parametric  control, fine-tuning becomes more easier and out of the box with no need to worry about       	       configuration.
   - Even after fine-tuning, continued API calls are required, incurring ongoing expenses.

3. **Scalability Challenges 📈**: Integrating the assistant into external platforms (e.g., websites) poses scalability and security concerns.

4. **Fine-Tuning Constraints 🔧**: While fine-tuning is streamlined via OpenAI's API, the resulting model remains tied to OpenAI's infrastructure and pricing model, This the biggest issue in comparison to fine-tuning open source model, but it fine-tuning the open-source requires more work from our side which will learn later.

  


#### Future Plans 🌱

To address current limitations and enhance the AI Note Assistant, we have two main paths:

- **Continue with OpenAI**:Improve the fine-tuned model through better prompts and implementing additional tools

- **Fine-tuning Open Source LLMs**: Developing and integrating Open Source Language Model (LLM) solutions, which can offer cost-effective alternatives to proprietary APIs like OpenAI.
  
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
