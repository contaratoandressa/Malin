# bibliotecas
import pandas as pd # data analysis
import numpy as np # data analysis
from google.colab import drive # connection from googlle drive
from os import listdir # listar arquivos
from os.path import isfile, join # listar arquivos

# base: Fazenda - Empresas
def dwl_database(mypath = '.../', compl = 'cnae/', name = 'cnae'):
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
      df = pd.read_csv(mypath+onlyfiles[0], sep=';',encoding='ISO-8859-1',header=None)
    else:
      df = pd.DataFrame()
      for list in range(0, len(onlyfiles)):
        result = pd.read_csv(mypath+onlyfiles[list], sep=';',encoding='ISO-8859-1',header=None)
        df = pd.concat([df, result], axis=0)
    #rename
    if name == 'cnae':
      df = df.rename(columns={0: "Codigo", 1: "Descricao"})
    elif name == 'empresas':
      df = df.rename(columns={0: "CnpjBasico", 1: "RazaoSocial", 2: "NaturezaJuridica", 4: "QualificacaoResponsavel", 5: "CapitalSocial", 6: "Porte", 
                              7: "EnteFederativoResponsavel"})
    # return
    return(df)
