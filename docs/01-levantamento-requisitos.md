# 📋 Levantamento de Requisitos: Painel de Qualidade Laboratorial Integrada

**Autora:** Luanna Oliveira (Biomédica & Graduanda em Sistemas de Informação)  
**Escopo do Setor:** Microbiologia · Urinálise · Parasitologia · Micologia  
**Amostra de Maior Volume:** Urina (EAS / Urocultura)  
**Referência Técnica:** Manuais de Microbiologia Clínica / Controle de Infecção (ANVISA) e Diretrizes da SBPC/ML

---

## 1. 🎯 Objetivos de Negócio

O objetivo do painel é transformar os registros de desvios operacionais em inteligência acionável para:
1. **Reduzir Recoletas e Descarte de Amostras** (melhorando a experiência do paciente e reduzindo custos);
2. **Controlar o Turnaround Time (TAT)** (garantindo que atrasos por complexidade biológica sejam diferenciados de gargalos operacionais);
3. **Eliminar Erros de Laudo e Retificações** (reforçando a segurança diagnóstica e conformidade para acreditações ONA/PALC).

---

## 2. 👥 Matriz de Stakeholders e Perguntas de Decisão

| Nível | Papel / Usuário | Foco de Decisão | Perguntas Respondidas pelo Painel |
| :--- | :--- | :--- | :--- |
| **Operacional** | Analistas e Técnicos de Bancada | Priorização da rotina e registro ágil de desvios. | *Quais amostras de urina precisam de repique/reteste hoje? Houve rejeição por tubo rachado na centrifugação?* |
| **Tático** | Supervisora de Setor (Micro/Urina/Parasito/Mico) | Eficiência da equipe, motivos de desvios e cumprimento de SLA. | *Quantas recoletas foram causadas por cadastro errado da recepção? Qual setor tem maior atraso de TAT?* |
| **Estratégico** | Gestão da Qualidade & RT | Conformidade, auditoria e segurança do paciente. | *Qual a taxa mensal de retificação de laudo? Quais planos de ação preventiva estão pendentes?* |
| **Interface / Atendimento** | Coordenação de Coleta e Recepção | Melhoria no atendimento e logística de amostras. | *Quais unidades/postos têm maior índice de frascos com vazamento ou falta de conservante?* |

---

## 3. 🔬 Catálogo de Desvios por Especialidade

### 3.1 🔄 Recoletas / Rejeições (Fase Pré-Analítica)
* **Cadastro de Exame Errado (Recepção):** Ex.: atendimento cadastrou apenas EAS quando a requisição médica solicitava EAS + Urocultura, ou cadastrou cultura sem antibiograma.
* **Amostra Não Vedada / Vazamento:** Frasco de urina ou fezes com tampa mal rosqueada/frouxa, extravasando líquido no transporte e gerando perda de volume e risco biológico.
* **Tubo Rachado / Quebrado:** Tubo cônico de urina trincado no transporte ou quebrado na centrifugação por desbalanceamento ou fadiga de material.
* **Conservante Inadequado / Ausente:** Amostra de fezes para parasitologia sem líquido conservante (MIF/SAF) para fixação de trofozoítos de protozoários.
* **Volume Insuficiente:** Urina com volume < 10 mL (insuficiente para fita bioquímica e sedimento) ou escamas dérmicas insuficientes em raspados de micologia.
* **Contaminação de Amostra:** Urocultura polimicrobiana (> 3 espécies) decorrente de falha de assepsia ou tempo prolongado sem refrigeração (> 2h).

### 3.2 ⏳ Atrasos na Liberação de Laudo / TAT (Analítica e Pós-Analítica)
* **Necessidade de Repique (Cultura Mista):** Urocultura ou secreção com colônias mistas que necessitam de 24h a 48h adicionais para isolamento de colônia pura antes do TSA.
* **Crescimento Fúngico Lento:** Culturas de micologia de unhas/pele que exigem acompanhamento de 15 a 30 dias em estufa.
* **Gargalo de Microscopia:** Dúvida diagnóstica em elementos raros (cilindros hemáticos, cristais atípicos ou trofozoítos duvidosos) retendo a validação técnica.
* **Falha de Equipamento:** Pane em analisador de urinálise ou carrossel de hemocultura.

### 3.3 🚨 Resultados Errados / Retificações de Laudo (Segurança do Paciente)
* **Inversão de Tubos / Amostras:** Troca acidental de tubos de urina no momento da leitura do sedimento ou da semeadura.
* **Confusão Diagnóstica Microscópica:** Confundir cisto de comensal (*Entamoeba coli*) com patógeno (*Entamoeba histolytica*) em fezes.
* **Inconsistência de Perfil Fenotípico:** Laudo emitido com perfil de sensibilidade biologicamente incompatível com as regras de resistência intrínseca.
* **Erro de Digitação / Transcrição:** Digitação invertida de resultados de fita urinária ou de contagem de leucócitos/hemácias no LIS.

---

## 4. 🗄️ Modelagem Conceitual para Power BI (Data Warehouse)

Para permitir análises multidimensionais de alto desempenho no Power BI:
* **Tabela Fato (`fato_ocorrencias`):** Registra cada evento de desvio individual (data, hora, protocolo da amostra, tempo de resolução).
* **Dimensão Motivo (`dim_motivo`):** Catálogo com motivo, especialidade, pilar (recoleta, TAT, retificação), gravidade e SLA.
* **Dimensão Amostra (`dim_amostra`):** Tipo de fluido/espécime (Urina, Fezes, Raspado de Unha, Swab, Sangue).
* **Dimensão Local / Origem (`dim_origem`):** Posto de coleta, ambulatório, UTI, enfermaria ou recepção.
* **Dimensão Tempo (`dim_calendario`):** Data, mês, ano, dia da semana, turno de trabalho.
