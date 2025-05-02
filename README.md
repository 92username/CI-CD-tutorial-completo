[![CI/CD - Build, Testes e Deploy](https://github.com/92username/CI-CD-tutorial-completo/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/92username/CI-CD-tutorial-completo/actions/workflows/ci-cd.yml) 

[!Microsoft Azure(https://img.shields.io/badge/microsoft%20azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white)]

##  🚧 Em construção 🚧

readme_content = """\
# CI/CD Tutorial Completo com FastAPI, Docker e GitHub Actions

Este repositório é um **tutorial prático e completo** sobre como construir uma pipeline CI/CD moderna, com foco em boas práticas de desenvolvimento, segurança e automação DevOps.

Ao longo do projeto, você irá aprender como:

- Containerizar uma aplicação FastAPI com Docker
- Configurar testes, análise de código e linting automáticos
- Integrar ferramentas de segurança como **Bandit**, **pip-audit** e **OWASP ZAP**
- Automatizar o deploy em uma VM com GitHub Actions

> **Status do projeto**: 🚧 Em desenvolvimento – Capítulo 4 concluído.

---

## 📚 Índice dos Capítulos

1. [Capítulo 1 - Introdução e Preparação do Projeto](./1.%20Capitulo%201.md)
2. [Capítulo 2 - Secrets e Variáveis de Ambiente](./2.%20Capitulo%202.md)
3. [Capítulo 3 - Workflows de CI/CD com GitHub Actions](./3.%20Capitulo%203.md)
4. [Capítulo 4 - Integração com OWASP ZAP para Segurança](./4.%20Capitulo%204.md)

---

## 📦 Tecnologias Utilizadas

- Python 3.12 + FastAPI
- Docker + Docker Compose
- GitHub Actions
- Bandit, pip-audit, Ruff, Pylint, Mypy
- OWASP ZAP (security scan automatizado)
- Azure VM (deploy remoto via SSH)

---

## 💡 Objetivo

Este projeto serve como base de estudo e referência para estudantes, desenvolvedores iniciantes em DevOps e profissionais que desejam aplicar práticas modernas de integração contínua, entrega contínua e segurança automatizada em aplicações Python.

---

## 🛡️ Segurança

Confira mais detalhes no arquivo [`SECURITY.md`](./SECURITY.md).

---

## ✍️ Contribuindo

Este repositório é mantido para fins educacionais, mas colaborações e sugestões são bem-vindas. 
"""

Path("/mnt/data/README - provisório.md").write_text(readme_content, encoding="utf-8")

