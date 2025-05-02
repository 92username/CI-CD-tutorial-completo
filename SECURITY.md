# Política de Segurança

Este projeto adota práticas essenciais de segurança como parte do ciclo de vida de desenvolvimento de software.

## 🔒 Autenticação Segura

- Os acessos a serviços de infraestrutura são realizados via **chave SSH privada**, armazenada de forma segura no GitHub Secrets (`VM_KEY`).
- A aplicação está hospedada em uma **VM na Azure**, com acesso controlado.

## 🔐 Gerenciamento de Secrets

- O repositório utiliza **GitHub Secrets** para armazenar dados sensíveis, como:
  - `VM_IP`, `VM_USER`, `VM_KEY`: para acesso SSH seguro à VM.
  - `ZAP_TOKEN`: token pessoal (PAT) com escopo restrito para permitir ações da ferramenta de segurança OWASP ZAP.

## 🛡️ Varredura de Vulnerabilidades com OWASP ZAP

- Um scanner automatizado de segurança baseado no **OWASP ZAP** é executado via GitHub Actions após o deploy.
- A configuração atual usa `fail_action: false` para não interromper o CI/CD durante o desenvolvimento.  
  Na produção simulada, esta opção será ajustada para `true`.

## 🧪 Análise Estática de Código

Durante o processo de CI, são executadas ferramentas de análise e verificação:

- `ruff`, `pylint`, `mypy`, `bandit` e `pip-audit` para lint, tipagem, segurança e auditoria de dependências.
- Todos os erros são reportados diretamente no log do GitHub Actions.

## ✅ Boas Práticas

- As imagens Docker são construídas com `python:3.12-slim`, minimizando superfícies de ataque.
- A aplicação serve apenas as rotas necessárias, todas com propósito funcional ou educacional:
  - `/` — Health check simples (status da API)
  - `/metrics` — Exposição de métricas para Prometheus
  - `/robots.txt` e `/sitemap.xml` — Suporte básico a scanners/bots
  - `/api/v1/event` — Simulação de evento para coleta de métricas
  - `/api/v1/users` — Endpoint com retorno de dados mockados (simulados), sem uso de banco de dados ou dados sensíveis
- As métricas expostas estão protegidas com `Content-Type: text/plain` e não incluem dados pessoais.

## 📬 Reportar Vulnerabilidades

Caso você identifique uma falha de segurança, por favor abra uma **issue privada** ou entre em contato diretamente com o mantenedor do repositório.

