"""Regras de negocio da usuaria, escritas como teste executavel.

Estas regras foram definidas por escrito e sao a especificacao do que o
JobRadar deve ou nao notificar. Ate aqui elas viviam so no config.py -- e
a lista CIDADES tinha divergido em dois sentidos ao mesmo tempo (faltava
Manaus, sobravam quatro cidades fora da regra) sem que nenhum dos 76
testes existentes percebesse.

Regra, resumida:
  BRASIL   -> remoto de qualquer lugar do pais;
              hibrido/presencial SO nas cidades de CIDADES.
  EXTERIOR -> SO remoto, e so em mercado de lingua portuguesa/espanhola.
              Nunca hibrido, nunca presencial, nunca mercado de lingua
              inglesa.
"""

import pytest

from core.job import Job
from core.perfis import PERFIL_BR


def _vaga(titulo, local, modalidade):
    return Job(
        titulo=titulo, empresa="Empresa Teste", local=local,
        link=f"https://exemplo.com/{abs(hash((titulo, local, modalidade)))}",
        site="Teste", modalidade=modalidade,
    )


# As seis cidades obrigatorias do requisito, mais as duas mantidas por
# decisao explicita da usuaria (Maceio e Aracaju).
CIDADES_ACEITAS = [
    "Campina Grande", "João Pessoa", "Recife", "Natal", "Caruaru",
    "Manaus", "Maceió", "Aracaju",
]


# ---------------------------------------------------------------- BRASIL

@pytest.mark.parametrize("modalidade", ["Híbrido", "Presencial"])
@pytest.mark.parametrize("cidade", CIDADES_ACEITAS)
def test_br_hibrido_e_presencial_nas_cidades_aceitas(cidade, modalidade):
    assert _vaga("Analista de Dados", f"{cidade} - PB", modalidade).combina_com(PERFIL_BR.regras)


# Variacoes de escrita que as fontes realmente usam -- separador, acento e
# caixa nao podem mudar o resultado.
@pytest.mark.parametrize("local", [
    "Campina Grande", "Campina Grande - PB", "Campina Grande, PB",
    "Campina Grande/PB", "CAMPINA GRANDE - PB", "campina grande, pb",
    "João Pessoa - PB", "Joao Pessoa - PB",
    "Manaus - AM", "Manaus, AM", "Manaus/AM",
    "Recife - PE", "Caruaru, PE", "Natal/RN",
])
def test_br_variacoes_de_escrita_da_cidade(local):
    assert _vaga("Analista de Dados", local, "Híbrido").combina_com(PERFIL_BR.regras)


@pytest.mark.parametrize("modalidade", ["Híbrido", "Presencial"])
@pytest.mark.parametrize("local", [
    "São Paulo - SP", "Belo Horizonte, MG", "Salvador - BA",
    "Rio de Janeiro, RJ", "Curitiba - PR", "Brasília, DF",
    "Fortaleza - CE", "Porto Alegre - RS",
    # Estavam em CIDADES por engano e aceitavam hibrida/presencial
    # fora da regra -- ver MEDIDO em config.py.
    "Jaboatão dos Guararapes - PE", "Teresina - PI",
    "São Luís - MA", "Petrolina - PE",
])
def test_br_hibrido_e_presencial_fora_das_cidades_e_rejeitado(local, modalidade):
    assert not _vaga("Analista de Dados", local, modalidade).combina_com(PERFIL_BR.regras)


@pytest.mark.parametrize("local", [
    "Remoto", "Remoto (São Paulo, SP)", "Remoto (Manaus, AM)",
    "Remoto - Brasil", "Remote, Brazil", "Remoto (Belo Horizonte, MG)",
])
def test_br_remoto_no_brasil_e_aceito_de_qualquer_cidade(local):
    """Remoto nao tem restricao de cidade -- a regra de CIDADES vale so
    pra hibrido/presencial."""
    assert _vaga("Analista de Dados", local, "Remoto").combina_com(PERFIL_BR.regras)


@pytest.mark.parametrize("local", [
    "Remote - US only", "Remote, United States", "Remote (Austin, TX)",
    "Remote - India",
])
def test_br_remoto_de_mercado_nao_aceito_e_rejeitado(local):
    assert not _vaga("Analista de Dados", local, "Remoto").combina_com(PERFIL_BR.regras)


# ------------------------------------------------------------------ CARGO

@pytest.mark.parametrize("titulo, esperado", [
    ("Analista de Dados Pleno", True),
    ("Analista de BI", True),
    ("Business Intelligence Analyst", True),
    ("Business Analyst", False),               # ambiguo, sem qualificador
    ("Business Analyst com SQL", True),        # ambiguo + qualificador
    ("Analista de Power BI", True),            # ferramenta + cargo
    ("Desenvolvedor Power BI", False),         # ferramenta sem cargo de analise
    ("Vendedor Externo", False),
    ("Engenheiro de Dados", False),
])
def test_cargo_no_titulo(titulo, esperado):
    assert _vaga(titulo, "Recife - PE", "Presencial").combina_com(PERFIL_BR.regras) is esperado
