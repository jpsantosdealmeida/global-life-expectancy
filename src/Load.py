
# Exportando o df para o caminho passado

def exportar_csv(df, caminho):
    caminho.parent.mkdir(parents=True,exist_ok=True)
    df.to_csv(caminho,index=False)

