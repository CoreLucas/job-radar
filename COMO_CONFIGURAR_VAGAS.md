# 🎯 Como Configurar as Vagas que Você Quer Buscar

## 📌 Resumo Rápido

Existem **2 perfis** que podem rodar separados ou juntos:
- **brasil** - Vagas no Brasil (Nordeste + algumas cidades) ou remotas para Brasil/LATAM
- **internacional** - Vagas remotas fora do Brasil que aceitam português/espanhol

## 🇧🇷 Configurar Perfil BRASIL

### Arquivo: `core/config.py`

#### 1. Cargos que você quer (linhas 10-67)

**Cargos Fortes** - Aprovados sozinhos:
```python
KEYWORDS_CARGO_FORTE = [
    "Analista de Dados",
    "Analista BI",
    "Data Analyst",
    "Business Intelligence",
    # Adicione mais cargos aqui
]
```

**Cargos Ambíguos** - Precisam de qualificador junto (dados, BI, SQL, etc):
```python
KEYWORDS_CARGO_AMBIGUO = [
    "Business Analyst",
    "Analista de Negócios",
    # Adicione mais cargos aqui
]
```

#### 2. Ferramentas/Termos de busca (linhas 94-109)

**Termos extras de cargo:**
```python
TERMOS_CARGO_EXTRA = [
    "power bi",
    "inteligência de mercado",
    # Adicione mais termos aqui
]
```

**Ferramentas:**
```python
TERMOS_FERRAMENTA = [
    "sql",
    "python",
    "tableau",
    "qlik",
    "looker",
    "bigquery",
    # Adicione: "spark", "databricks", etc.
]
```

#### 3. Cidades aceitas (linhas 143-157)

```python
CIDADES = [
    "Remoto",
    "Campina Grande",
    "João Pessoa",
    "Recife",
    "Natal",
    "Caruaru",
    "Manaus",
    "Maceió",
    "Aracaju",
    # Adicione mais cidades aqui
]
```

---

## 🌎 Configurar Perfil INTERNACIONAL

### Arquivo: `core/config_intl.py`

#### 1. Cargos aceitos (linhas 18-48)

```python
KEYWORDS_INTL = [
    "Data Analyst",
    "Business Intelligence",
    "Analista de Dados",
    "Analista de Datos",  # espanhol
    # Adicione mais cargos aqui
]
```

#### 2. Termos de busca (linhas 54-115)

```python
TERMOS_BUSCA_INTL = [
    "data analyst spanish speaker",
    "business intelligence portuguese speaker",
    "remote data analyst latam",
    "analista de datos remoto",
    # Adicione mais combinações aqui
]
```

#### 3. Países pesquisados (linhas 138-147)

```python
LOCATIONS_INTL = [
    "Spain",
    "Portugal",
    "Mexico",
    "Colombia",
    "Argentina",
    "Chile",
    # Adicione mais países aqui
]
```

---

## 🚀 Como Rodar Depois de Configurar

### Rodar apenas perfil Brasil:
```bash
python main.py --perfil brasil --once
```

### Rodar apenas perfil Internacional:
```bash
python main.py --perfil internacional --once
```

### Rodar os dois perfis juntos:
```bash
python main.py --perfil brasil internacional --once
```

### Rodar em loop contínuo (checando a cada 3h):
```bash
python main.py --perfil brasil internacional
```

---

## 💡 Exemplos Práticos

### Exemplo 1: Adicionar cargo "Cientista de Dados"

No arquivo `core/config.py`, adicione em `KEYWORDS_CARGO_FORTE`:
```python
KEYWORDS_CARGO_FORTE = [
    "Analista de Dados",
    "Cientista de Dados",  # ← NOVO
    "Data Scientist",      # ← NOVO
    # ... resto da lista
]
```

### Exemplo 2: Adicionar cidade "Salvador"

No arquivo `core/config.py`, adicione em `CIDADES`:
```python
CIDADES = [
    "Remoto",
    "Campina Grande",
    "Salvador",  # ← NOVO
    # ... resto da lista
]
```

### Exemplo 3: Adicionar ferramenta "Spark"

No arquivo `core/config.py`, adicione em `TERMOS_FERRAMENTA`:
```python
TERMOS_FERRAMENTA = [
    "sql",
    "python",
    "spark",  # ← NOVO
    # ... resto da lista
]
```

---

## ⚙️ Configurações Avançadas

### Mudar quantidade de termos por ciclo (economizar tempo)

No `core/config.py`, linha 125:
```python
TERMOS_POR_CICLO = 10  # Mude para 5 ou 15
```
- **Menor** = ciclo mais rápido, mas leva mais ciclos para cobrir todos os termos
- **Maior** = cobre mais termos por ciclo, mas demora mais

### Mudar limiar de notificação imediata

No `core/config.py`, linha 340:
```python
LIMIAR_DIGEST_IMEDIATO = 7  # Vagas com score >= 7 notificam na hora
```
- **6** = mais vagas notificadas imediatamente (pode virar spam)
- **8** = só as melhores vagas notificam na hora

### Mudar hora do digest diário

No `core/config.py`, linha 359:
```python
DIGEST_HORA_UTC = 9  # 9 UTC = 6h da manhã no Brasil (UTC-3)
```

---

## 📝 Dicas Importantes

1. **Não delete** linhas existentes antes de entender o que fazem
2. **Teste localmente** com `--once` antes de deixar rodando em loop
3. **Mantenha backup** dos arquivos de configuração antes de grandes mudanças
4. **Use aspas duplas** (`"`) em strings Python
5. **Não esqueça vírgulas** entre itens da lista

---

## ❓ Precisa de Ajuda?

- Confira o arquivo `README.md` para mais detalhes
- Veja os logs em `jobradar.log`
- Rode os testes: `pytest tests/ -v`
