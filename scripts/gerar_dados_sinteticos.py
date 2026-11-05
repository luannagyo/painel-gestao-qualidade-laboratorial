"""
Script: Gerador de Dados Sintéticos de Qualidade Laboratorial
Autora: Luanna Oliveira (Biomédica & Graduanda em Sistemas de Informação)
Setores: Urinálise, Microbiologia, Parasitologia, Micologia
Foco: Recoletas, Atrasos de TAT e Resultados Errados (Retificações)
"""

import os
import random
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

# Definir semente para reprodutibilidade científica (o mesmo código sempre gera os mesmos dados)
np.random.seed(42)
random.seed(42)

# Garantir que a pasta data/raw exista
os.makedirs('data/raw', exist_ok=True)
os.makedirs('scripts', exist_ok=True)

print("Iniciando geração de dados sintéticos para o laboratório...")

# ==============================================================================
# 1. TABELA DIMENSÃO: EXAMES (dim_exame.csv)
# ==============================================================================
dados_exames = [
    {"id_exame": "EX01", "nome_exame": "Urinálise Completa (EAS / Sumário de Urina)", "setor": "Urinálise", "tipo_amostra": "Urina Jato Médio", "tat_alvo_horas": 4},
    {"id_exame": "EX02", "nome_exame": "Urocultura com TSA / Antibiograma", "setor": "Microbiologia", "tipo_amostra": "Urina Estéril", "tat_alvo_horas": 48},
    {"id_exame": "EX03", "nome_exame": "Parasitológico de Fezes (EPF 3 amostras)", "setor": "Parasitologia", "tipo_amostra": "Fezes com Conservante", "tat_alvo_horas": 24},
    {"id_exame": "EX04", "nome_exame": "Micológico Direto e Cultura de Raspado", "setor": "Micologia", "tipo_amostra": "Escamas de Unha / Pele", "tat_alvo_horas": 360}, # 15 dias
    {"id_exame": "EX05", "nome_exame": "Cultura de Secreção com Antibiograma", "setor": "Microbiologia", "tipo_amostra": "Swab com Meio Stuart", "tat_alvo_horas": 72},
    {"id_exame": "EX06", "nome_exame": "Hemocultura Automatizada Pareada", "setor": "Microbiologia", "tipo_amostra": "Sangue Total em Frasco Específico", "tat_alvo_horas": 120}
]
df_dim_exame = pd.DataFrame(dados_exames)
df_dim_exame.to_csv('data/raw/dim_exame.csv', index=False, encoding='utf-8-sig')
print("✓ Dimensão Exames salva com sucesso em data/raw/dim_exame.csv")

# ==============================================================================
# 2. TABELA DIMENSÃO: SETORES DE ORIGEM / POSTOS (dim_origem.csv)
# ==============================================================================
dados_origem = [
    {"id_origem": "LOC01", "nome_origem": "Posto de Coleta Central", "tipo_unidade": "Ambulatorial", "cidade": "Sede"},
    {"id_origem": "LOC02", "nome_origem": "Posto de Coleta Shopping", "tipo_unidade": "Ambulatorial", "cidade": "Sede"},
    {"id_origem": "LOC03", "nome_origem": "Pronto Atendimento / Emergência (PA)", "tipo_unidade": "Hospitalar", "cidade": "Sede"},
    {"id_origem": "LOC04", "nome_origem": "Unidade de Terapia Intensiva (UTI Adulto)", "tipo_unidade": "Hospitalar", "cidade": "Sede"},
    {"id_origem": "LOC05", "nome_origem": "UTI Neonatal e Pediátrica", "tipo_unidade": "Hospitalar", "cidade": "Sede"},
    {"id_origem": "LOC06", "nome_origem": "Enfermaria de Internação", "tipo_unidade": "Hospitalar", "cidade": "Sede"}
]
df_dim_origem = pd.DataFrame(dados_origem)
df_dim_origem.to_csv('data/raw/dim_origem.csv', index=False, encoding='utf-8-sig')
print("✓ Dimensão Origem salva com sucesso em data/raw/dim_origem.csv")

# ==============================================================================
# 3. TABELA DIMENSÃO: CATÁLOGO DE MOTIVOS DE FALHA (dim_motivo_desvio.csv)
# ==============================================================================
dados_motivos = [
    # Recoletas (Pré-Analítica)
    {"id_motivo": "REC01", "pilar": "Recoleta / Rejeição", "setor_alvo": "Urinálise", "motivo": "Amostra Não Vedada / Vazamento", "fase": "Pré-Analítica", "gravidade": "Alta", "sla_investigacao_dias": 1},
    {"id_motivo": "REC02", "pilar": "Recoleta / Rejeição", "setor_alvo": "Urinálise", "motivo": "Tubo Rachado / Quebrado na Centrifugação", "fase": "Pré-Analítica", "gravidade": "Alta", "sla_investigacao_dias": 1},
    {"id_motivo": "REC03", "pilar": "Recoleta / Rejeição", "setor_alvo": "Geral / Recepção", "motivo": "Cadastro de Exame Errado", "fase": "Pré-Analítica", "gravidade": "Crítica", "sla_investigacao_dias": 1},
    {"id_motivo": "REC04", "pilar": "Recoleta / Rejeição", "setor_alvo": "Parasitologia", "motivo": "Conservante Inadequado / Ausente", "fase": "Pré-Analítica", "gravidade": "Média", "sla_investigacao_dias": 2},
    {"id_motivo": "REC05", "pilar": "Recoleta / Rejeição", "setor_alvo": "Micologia", "motivo": "Volume Insuficiente de Raspado", "fase": "Pré-Analítica", "gravidade": "Média", "sla_investigacao_dias": 2},
    {"id_motivo": "REC06", "pilar": "Recoleta / Rejeição", "setor_alvo": "Microbiologia", "motivo": "Contaminação da Amostra na Coleta", "fase": "Pré-Analítica", "gravidade": "Alta", "sla_investigacao_dias": 3},
    {"id_motivo": "REC07", "pilar": "Recoleta / Rejeição", "setor_alvo": "Urinálise", "motivo": "Volume Insuficiente de Urina (<10mL)", "fase": "Pré-Analítica", "gravidade": "Média", "sla_investigacao_dias": 1},

    # Atrasos de Laudo / TAT (Analítica e Pós)
    {"id_motivo": "TAT01", "pilar": "Atraso de Laudo (TAT)", "setor_alvo": "Microbiologia", "motivo": "Necessidade de Repique (Cultura Mista)", "fase": "Analítica", "gravidade": "Média", "sla_investigacao_dias": 2},
    {"id_motivo": "TAT02", "pilar": "Atraso de Laudo (TAT)", "setor_alvo": "Micologia", "motivo": "Crescimento Fúngico Lento", "fase": "Analítica", "gravidade": "Baixa", "sla_investigacao_dias": 5},
    {"id_motivo": "TAT03", "pilar": "Atraso de Laudo (TAT)", "setor_alvo": "Urinálise", "motivo": "Gargalo de Microscopia / Sedimento Duvidoso", "fase": "Analítica", "gravidade": "Média", "sla_investigacao_dias": 1},
    {"id_motivo": "TAT04", "pilar": "Atraso de Laudo (TAT)", "setor_alvo": "Geral / Bancada", "motivo": "Falha Mecânica de Equipamento", "fase": "Analítica", "gravidade": "Alta", "sla_investigacao_dias": 1},
    {"id_motivo": "TAT05", "pilar": "Atraso de Laudo (TAT)", "setor_alvo": "Supervisão", "motivo": "Retenção de Laudo para Conferência Clínica", "fase": "Pós-Analítica", "gravidade": "Média", "sla_investigacao_dias": 1},

    # Resultados Errados / Retificações (Segurança do Paciente)
    {"id_motivo": "ERR01", "pilar": "Resultado Errado / Retificação", "setor_alvo": "Urinálise", "motivo": "Inversão de Tubos na Bancada / Centrífuga", "fase": "Analítica", "gravidade": "Crítica", "sla_investigacao_dias": 1},
    {"id_motivo": "ERR02", "pilar": "Resultado Errado / Retificação", "setor_alvo": "Parasitologia", "motivo": "Confusão Diagnóstica de Cisto (Comensal vs Patógeno)", "fase": "Analítica", "gravidade": "Alta", "sla_investigacao_dias": 1},
    {"id_motivo": "ERR03", "pilar": "Resultado Errado / Retificação", "setor_alvo": "Microbiologia", "motivo": "Inconsistência de Perfil Fenotípico (Resistência Intrínseca)", "fase": "Pós-Analítica", "gravidade": "Crítica", "sla_investigacao_dias": 1},
    {"id_motivo": "ERR04", "pilar": "Resultado Errado / Retificação", "setor_alvo": "Geral / Bancada", "motivo": "Erro de Digitação / Transcrição no LIS", "fase": "Pós-Analítica", "gravidade": "Alta", "sla_investigacao_dias": 1}
]
df_dim_motivo = pd.DataFrame(dados_motivos)
df_dim_motivo.to_csv('data/raw/dim_motivo_desvio.csv', index=False, encoding='utf-8-sig')
print("✓ Dimensão Motivos salva com sucesso em data/raw/dim_motivo_desvio.csv")

# ==============================================================================
# 4. TABELA FATO: AMOSTRAS RECEBIDAS (fato_amostras.csv)
# ==============================================================================
# Vamos simular 2.500 amostras processadas nos últimos 90 dias
TOTAL_AMOSTRAS = 2500
data_fim = datetime.now()
data_inicio = data_fim - timedelta(days=90)

# Pesos de frequência dos exames: Urina (EX01 + EX02) representa ~65% do total!
exames_ids = ["EX01", "EX02", "EX03", "EX04", "EX05", "EX06"]
pesos_exames = [0.45, 0.20, 0.15, 0.08, 0.07, 0.05]

origens_ids = ["LOC01", "LOC02", "LOC03", "LOC04", "LOC05", "LOC06"]
pesos_origens = [0.35, 0.25, 0.15, 0.10, 0.05, 0.10]

lista_amostras = []
lista_ocorrencias = []

id_desvio_contador = 1001

for i in range(1, TOTAL_AMOSTRAS + 1):
    id_amostra = f"AMO-{i:05d}"
    id_paciente = f"PAC-{random.randint(1000, 9999)}"
    
    # Escolha de exame e origem respeitando as distribuições
    exame_escolhido = np.random.choice(exames_ids, p=pesos_exames)
    origem_escolhida = np.random.choice(origens_ids, p=pesos_origens)
    
    # Data aleatória dentro da janela de 90 dias
    segundos_aleatorios = random.randint(0, int((data_fim - data_inicio).total_seconds()))
    data_coleta = data_inicio + timedelta(seconds=segundos_aleatorios)
    # Recebimento entre 30 min e 4 horas após a coleta
    data_recebimento = data_coleta + timedelta(minutes=random.randint(30, 240))
    
    # Obter dados do exame
    info_exame = next(item for item in dados_exames if item["id_exame"] == exame_escolhido)
    tat_alvo = info_exame["tat_alvo_horas"]
    
    # Decidir se a amostra sofreu algum desvio (Taxa global de falhas ~ 7%)
    # Probabilidades clínicas:
    # 93% Conforme
    # 3.5% Recoleta (amostra inadequada, vazamento, quebra, etc.)
    # 2.5% Atraso de TAT (extrapolou o prazo)
    # 1.0% Retificação (resultado com erro corrigido após liberação)
    sorteio_qualidade = random.random()
    
    status_amostra = "Conforme"
    houve_desvio = False
    tipo_desvio_escolhido = None
    
    if sorteio_qualidade < 0.035:
        status_amostra = "Recoleta Solicitada"
        houve_desvio = True
        categoria_desvio = "Recoleta / Rejeição"
    elif sorteio_qualidade < 0.060:
        status_amostra = "Atraso no Laudo (TAT)"
        houve_desvio = True
        categoria_desvio = "Atraso de Laudo (TAT)"
    elif sorteio_qualidade < 0.070:
        status_amostra = "Laudo Retificado (Erro)"
        houve_desvio = True
        categoria_desvio = "Resultado Errado / Retificação"
    
    # Cálculo da data de liberação do laudo
    if status_amostra == "Conforme":
        # Liberado dentro do TAT alvo (com variação normal de 50% a 95% do prazo)
        tempo_real_horas = round(tat_alvo * random.uniform(0.5, 0.95), 1)
        data_liberacao = data_recebimento + timedelta(hours=tempo_real_horas)
        dentro_do_prazo = "Sim"
    elif status_amostra == "Atraso no Laudo (TAT)":
        # Liberado com atraso (120% a 250% do prazo alvo)
        tempo_real_horas = round(tat_alvo * random.uniform(1.2, 2.5), 1)
        data_liberacao = data_recebimento + timedelta(hours=tempo_real_horas)
        dentro_do_prazo = "Não"
    elif status_amostra == "Recoleta Solicitada":
        # Amostra rejeitada precocemente (dentro de 2 a 6 horas)
        tempo_real_horas = round(random.uniform(2.0, 6.0), 1)
        data_liberacao = None
        dentro_do_prazo = "Não Aplicável"
    else: # Laudo Retificado
        # Liberado inicialmente, depois retificado
        tempo_real_horas = round(tat_alvo * random.uniform(0.8, 1.1), 1)
        data_liberacao = data_recebimento + timedelta(hours=tempo_real_horas)
        dentro_do_prazo = "Sim"
    
    # Registrar amostra
    lista_amostras.append({
        "id_amostra": id_amostra,
        "id_paciente": id_paciente,
        "id_exame": exame_escolhido,
        "id_origem": origem_escolhida,
        "data_coleta": data_coleta.strftime("%Y-%m-%d %H:%M:%S"),
        "data_recebimento": data_recebimento.strftime("%Y-%m-%d %H:%M:%S"),
        "data_liberacao": data_liberacao.strftime("%Y-%m-%d %H:%M:%S") if data_liberacao else "",
        "tat_alvo_horas": tat_alvo,
        "tat_real_horas": tempo_real_horas,
        "status_amostra": status_amostra,
        "dentro_do_prazo": dentro_do_prazo
    })
    
    # Se gerou Não Conformidade, alimentar a TABELA FATO DE OCORRÊNCIAS
    if houve_desvio:
        # Filtrar motivos compatíveis com a categoria sorteada
        motivos_possiveis = [m for m in dados_motivos if m["pilar"] == categoria_desvio]
        
        # Ajustar para priorizar o setor se houver compatibilidade
        setor_do_exame = info_exame["setor"]
        motivos_setor = [m for m in motivos_possiveis if m["setor_alvo"] in [setor_do_exame, "Geral / Recepção", "Geral / Bancada", "Supervisão"]]
        if motivos_setor:
            motivo_sorteado = random.choice(motivos_setor)
        else:
            motivo_sorteado = random.choice(motivos_possiveis)
            
        id_ocorrencia = f"NC-{id_desvio_contador}"
        id_desvio_contador += 1
        
        data_registro_nc = data_recebimento + timedelta(hours=random.randint(1, 4))
        sla_dias = motivo_sorteado["sla_investigacao_dias"]
        
        # Simular resolução da investigação e plano de ação:
        # 80% resolvidas no prazo, 15% resolvidas com atraso, 5% ainda em aberto/investigação
        sorteio_sla = random.random()
        if sorteio_sla < 0.80:
            dias_gasto = round(random.uniform(0.3, sla_dias), 1)
            status_acao = "Concluída no Prazo"
            data_conclusao = (data_registro_nc + timedelta(days=dias_gasto)).strftime("%Y-%m-%d %H:%M:%S")
        elif sorteio_sla < 0.95:
            dias_gasto = round(sla_dias + random.uniform(0.5, 3.0), 1)
            status_acao = "Concluída com Atraso"
            data_conclusao = (data_registro_nc + timedelta(days=dias_gasto)).strftime("%Y-%m-%d %H:%M:%S")
        else:
            dias_gasto = round((data_fim - data_registro_nc).total_seconds() / 86400, 1)
            status_acao = "Em Investigação / Aberta"
            data_conclusao = ""
            
        lista_ocorrencias.append({
            "id_ocorrencia": id_ocorrencia,
            "id_amostra": id_amostra,
            "id_motivo": motivo_sorteado["id_motivo"],
            "data_registro_nc": data_registro_nc.strftime("%Y-%m-%d %H:%M:%S"),
            "data_conclusao_acao": data_conclusao,
            "dias_resolucao": dias_gasto,
            "sla_permitido_dias": sla_dias,
            "status_plano_acao": status_acao,
            "investigador_responsavel": random.choice(["Luanna Oliveira (Biomédica)", "Supervisora Técnica", "Comitê da Qualidade"])
        })

df_fato_amostras = pd.DataFrame(lista_amostras)
df_fato_amostras.to_csv('data/raw/fato_amostras.csv', index=False, encoding='utf-8-sig')
print(f"✓ Fato Amostras salva com {len(df_fato_amostras)} registros em data/raw/fato_amostras.csv")

df_fato_ocorrencias = pd.DataFrame(lista_ocorrencias)
df_fato_ocorrencias.to_csv('data/raw/fato_ocorrencias.csv', index=False, encoding='utf-8-sig')
print(f"✓ Fato Ocorrências de Qualidade salva com {len(df_fato_ocorrencias)} desvios em data/raw/fato_ocorrencias.csv")

print("\n" + "="*60)
print("RESUMO ESTATÍSTICO DA MASSA DE DADOS GERADA:")
print("="*60)
print("Distribuição das Amostras por Status:")
print(df_fato_amostras["status_amostra"].value_counts(normalize=True).mul(100).round(1).astype(str) + "%")
print("\nTop 5 Motivos de Desvio Mais Frequentes:")
df_merge_motivo = df_fato_ocorrencias.merge(df_dim_motivo, on="id_motivo")
print(df_merge_motivo["motivo"].value_counts().head(5))
print("="*60)
print("Geração concluída com 100% de sucesso!")
