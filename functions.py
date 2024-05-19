# bibliotecas
import pandas as pd # data analysis
import numpy as np # data analysis
from google.colab import drive # connection from googlle drive
from os import listdir # listar arquivos
from os.path import isfile, join # listar arquivos

# base: Fazenda - Empresas
def dwl_database(mypath = '/content/drive/MyDrive/CONSULTORIAS/UFF - Projeto Niterói/Bases de Dados/bases_fazenda/', compl = 'cnae/', name = 'cnae', **kwargs):
    """Download databases.
    mypath = list of the path that the sheets are.
    compl = de exatc path.
    name = to rename the dataset.
    """
    # local
    mypath = mypath+compl
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    # download
    if len(onlyfiles) == 1:
      df = pd.read_csv(mypath+onlyfiles[0], **kwargs, sep=';',encoding='ISO-8859-1',header=None)
    else:
      df = pd.DataFrame()
      for list in range(0, len(onlyfiles)):
        result = pd.read_csv(mypath+onlyfiles[list], **kwargs, sep=';',encoding='ISO-8859-1',header=None)
        df = pd.concat([df, result], axis=0)
    #rename
    if name == 'cnae':
      df = df.rename(columns={0: "Codigo", 1: "Descricao"})
    elif name == 'empresas':
      df = df.rename(columns={0: "CnpjBasico", 1: "RazaoSocial", 2: "NaturezaJuridica", 3: "QualificacaoResponsavel", 4: "CapitalSocial", 5: "Porte",
                              6: "EnteFederativoResponsavel"})
    elif name == 'estabelecimentos':
      df = df.rename(columns={0: "CnpjBasico", 1: "CnpjOrdem", 2: "CnpjDv", 3: "IdMatrizFilial", 4: "NomeFantasia",
                              5: "SituacaoCadastral", 6: "DataSituacaoCadastral", 7: "MotivoSituacaoCadastral", 8: "NomeCidadeExterior",
                              9: "Pais", 10: "DataIniAtv", 11: "CnaeFiscalPrincipal", 12: "CnaeFiscalSecundaria", 13: "TipoLogradouro",
                              14: "Logradouro", 15: "Numero", 16: "Complemento", 17: "Bairro", 18: "CEP", 19: "UF", 20: "Municipio",
                              21: "ddd1", 22: "Tel1", 23: "ddd2", 24: "Tel2", 25: "dddFax", 26: "Fax", 27: "CorreioEletronico",
                              28: "SituacaoEspecial", 29: "DataSituacaoEspecial"})

    # save into drive
    df.to_csv(mypath+name+'.csv')

    # return
    return(df)


# databases
cnae = dwl_database()
estabelecimentos = dwl_database(compl = 'estabelecimentos/', name = 'estabelecimentos')
empresas = dwl_database(compl = 'empresas/', name = 'empresas')
mypath = '/content/drive/MyDrive/CONSULTORIAS/UFF - Projeto Niterói/Bases de Dados/bases_fazenda/empresas/empresas1.csv'
empresas = pd.read_csv(mypath)

# orgao por municipio
# 103-1 - Órgão Público do Poder Executivo Municipal
# 106-6 - Órgão Público do Poder Legislativo Municipal
# 118-0 - Órgão Público Autônomo Municipal
orgao_muni = empresas[empresas.NaturezaJuridica.isin([1031, 1066, 1180])]
orgao_muni.to_csv(mypath+'orgao_muni.csv')

# orgao por estado
# 102-3 - Órgão Público do Poder Executivo Estadual ou do Distrito Federal
# 105-8 - Órgão Público do Poder Legislativo Estadual ou do Distrito Federal
# 108-2 - Órgão Público do Poder Judiciário Estadual
# 117-1 - Órgão Público Autônomo Estadual ou do Distrito Federal
orgao_est = empresas[empresas.NaturezaJuridica.isin([1023, 1058, 1082, 1171])]
orgao_est.to_csv(mypath+'orgao_est.csv')

# orgao por federacao
# 101-5 - Órgão Público do Poder Executivo Federal
# 104-0 - Órgão Público do Poder Legislativo Federal
# 107-4 - Órgão Público do Poder Judiciário Federal
# 116-3 - Órgão Público Autônomo Federal
orgao_fed = empresas[empresas.NaturezaJuridica.isin([1015, 1040, 1074, 1163])]
orgao_fed.to_csv(mypath+'orgao_fed.csv')

# fundacao publica por municipio
# 115-5 - Fundação Pública de Direito Público Municipal
# 127-9 - Fundação Pública de Direito Privado Municipal
funda_muni = empresas[empresas.NaturezaJuridica.isin([1031, 1066, 1180])]
funda_muni.to_csv(mypath+'funda_muni.csv')

# fundacao publica por estado
# 114-7 - Fundação Pública de Direito Público Estadual ou do Distrito Federal
# 126-0 - Fundação Pública de Direito Privado Estadual ou do Distrito Federal
funda_est = empresas[empresas.NaturezaJuridica.isin([1147, 1260])]
funda_est.to_csv(mypath+'funda_est.csv')

# fundacao publica por federacao
# 113-9 - Fundação Pública de Direito Público Federal
# 125-2 - Fundação Pública de Direito Privado Federal
funda_fed = empresas[empresas.NaturezaJuridica.isin([1139, 1252])]
funda_fed.to_csv(mypath+'funda_fed.csv')

# empresas

# empresas por municipio
# 201-1 - Empresa Pública
# 203-8 - Sociedade de Economia Mista
# 204-6 - Sociedade Anônima Aberta
# 205-4 - Sociedade Anônima Fechada
# 206-2 - Sociedade Empresária Limitada
# 207-0 - Sociedade Empresária em Nome Coletivo
# 208-9 - Sociedade Empresária em Comandita Simples
# 209-7 - Sociedade Empresária em Comandita por Ações
# 212-7 - Sociedade em Conta de Participação
# 213-5 - Empresário (Individual)
# 215-1 - Consórcio de Sociedades
# 216-0 - Grupo de Sociedades
# 223-2 - Sociedade Simples Pura
# 224-0 - Sociedade Simples Limitada
# 225-9 - Sociedade Simples em Nome Coletivo
# 226-7 - Sociedade Simples em Comandita Simples
# 228-3 - Consórcio de Empregadores
# 229-1 - Consórcio Simples
# 230-5 - Empresa Individual de Responsabilidade Limitada (de Natureza Empresária)
# 231-3 - Empresa Individual de Responsabilidade Limitada (de Natureza Simples)
# 232-1 – Sociedade Unipessoal de Advogados
# 233-0 – Cooperativas de Consumo
# 234-8 – Empresa Simples de Inovação - Inova Simples
# 235-6 – Investidor Não Residente
empresas = dwl_database(compl = 'empresas/', name = 'empresas')
empresas = empresas[empresas.NaturezaJuridica.isin([2011, 2038, 2046, 2054, 2062, 2070, 2089, 2097, 2127, 2135, 2151, 
                                                    20160, 2232, 2240, 2259, 2267, 2283, 2291, 2305, 2313, 2321, 2330, 
                                                    2348, 2356])]
