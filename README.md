# 🤖 The second shot in the leg with an AI (Chainlit, LangChain, Ollama, Mistral)

This project serves as a basic example of integrating [Chainlit](https://chainlit.io/) and [LangChain](https://www.langchain.com/) with the Mistral Large Language Model (LLM). Ensure that the `data/test.pdf` file contains the necessary context for the LLM. Additionally, you may want to customize the `PROMPT_TEMPLATE` to suit your needs. 🙃

[preview](https://github.com/dev5c32373043/ai-genesis-part-2/assets/13788002/92afb332-8729-4778-abc5-870c57c6919a)

## 🚀 Getting started

To start the project, install all dependencies in the requirements section.

Download `mistral:instruct` model (if needed):

```bash
ollama pull mistral:instruct
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

And finally, start the server:

```bash
chainlit run app.py -w -h
```

That's it! 🎉
Now visit [http://localhost:8000](http://localhost:8000) to play with it! 😏

## Requirements

- [Python][python] 3.8.10+
- [Ollama][ollama] 0.2.17+
- [Qdrant][qdrant] 1.7.3+

[python]: https://www.python.org/
[ollama]: https://ollama.ai/
[qdrant]: https://qdrant.tech/
