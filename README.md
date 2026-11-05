# 🧪 Painel de Gestão da Qualidade Laboratorial

> Plataforma de Business Intelligence (BI) para controle e redução de Não Conformidades nos setores de **Microbiologia, Urinálise, Parasitologia e Micologia**.

![status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![pandas](https://img.shields.io/badge/Pandas-2.3-150458?logo=pandas)
![git](https://img.shields.io/badge/Git-GitHub-F05032?logo=git)

---

## 📌 Contexto e Problema de Negócio

Em laboratórios clínicos e hospitalares, falhas nas fases **Pré-Analítica, Analítica e Pós-Analítica** resultam em:
- **Recoletas desnecessárias** (desconforto para o paciente, risco biológico e desperdício de insumos);
- **Atrasos na entrega de laudos (TAT)** que impactam o início de tratamentos e o tempo de internação;
- **Retificações de laudo** decorrentes de inversão de tubos, erros de digitação ou divergências fenotípicas.

Este projeto aplica técnicas de **Engenharia de Dados** e **Business Intelligence** para centralizar esses desvios, gerar indicadores automatizados e subsidiar planos de ação corretiva para acreditação (PALC, ONA, RDC 786/ANVISA).

---

## 🎯 Objetivos

- [x] Mapear stakeholders e dores da rotina (Microbiologia, Urinálise, Parasitologia, Micologia)
- [x] Catalogar causas-raiz de recoletas, atrasos e erros de laudo com regras da ANVISA
- [ ] Construir o pipeline de ETL em Python (Pandas) gerando base sintética realista
- [ ] Modelar o Data Warehouse em **Star Schema** (Tabela Fato e Dimensões)
- [ ] Desenvolver dashboard interativo no **Power BI** com métricas DAX de qualidade

---

## 👥 Stakeholders

| Nível | Stakeholder | Papel no Projeto |
| :--- | :--- | :--- |
| **Operacional** | Analistas e Técnicos de Bancada | Consulta a pendências de retestes/repiques e registro ágil de desvios. |
| **Tático** | Supervisora Técnica de Setor | Monitoramento de taxas de recoleta, gargalos de TAT e controle de SLA. |
| **Estratégico** | Gestão da Qualidade & RT | Acompanhamento de indicadores para auditorias e reuniões de análise crítica. |
| **Interface Clínica** | CCIH / SCIH e Postos de Coleta | Alertas rápidos de amostras inadequadas e monitoramento de infecções. |

---

## 🛠️ Tecnologias Utilizadas

- **Python (Pandas):** Limpeza, estruturação e geração de dados sintéticos baseados em regras clínicas.
- **Jupyter Notebook:** Prototipação interativa, exploração e documentação do raciocínio analítico.
- **Modelagem Dimensional (Star Schema):** Tabelas Fato e Dimensões otimizadas para BI.
- **Power BI & DAX:** Visualização de dados, storytelling e cálculos de indicadores (KPIs).
- **Git & GitHub:** Versionamento de código e documentação contínua.

---

## 📂 Estrutura do Repositório

```text
📁 painel-gestao-qualidade-laboratorial/
│
├── 📁 docs/                             # Documentação técnica e regras de negócio
│   └── 01-levantamento-requisitos.md   # Mapeamento completo de stakeholders e dores
│
├── 📁 notebooks/                        # Cadernos Jupyter de prototipação e análise
│   └── 00_levantamento_e_referencias.ipynb # Catálogo de desvios em Python/Pandas
│
├── 📁 data/                             # Bases de dados
│   ├── raw/                            # Dados brutos / sintéticos
│   └── processed/                      # Dados tratados para o Power BI
│
├── .gitignore                          # Arquivos e pastas ignorados pelo Git
└── README.md                           # Visão geral do projeto
```

---

## 📚 Documentação do Projeto

- 📄 [Levantamento de Requisitos e Matriz de Falhas](docs/01-levantamento-requisitos.md)
- 📓 [Caderno de Prototipação em Python](notebooks/00_levantamento_e_referencias.ipynb)

---

## ⚠️ Aviso sobre Dados

Todos os dados gerados e utilizados neste repositório são **100% sintéticos e simulados**. Nenhuma informação real de pacientes, prontuários ou instituições de saúde é utilizada.

---

## 👩‍💻 Autora

**Luanna Oliveira**  
Biomédica & Graduanda em Sistemas de Informação  
- GitHub: [@luannagyo](https://github.com/luannagyo)
