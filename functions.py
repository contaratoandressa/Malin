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
