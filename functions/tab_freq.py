# Tabela de frequência aprimorada
def tab_freq(df, col):
    tab_freq = df[col].value_counts().reset_index()
    tab_freq.columns = [col, 'Freq. Absoluta']

    # Freq. Relativa
    tab_freq['Freq. Relativa'] = (100 * (tab_freq['Freq. Absoluta'] / tab_freq['Freq. Absoluta'].sum())).round(2)
    
    # Contagem Acumulada
    tab_freq['Freq. Acumulada'] = tab_freq['Freq. Absoluta'].cumsum()

    # Percentual Acumulado
    tab_freq['% Acumulado'] = tab_freq['Freq. Relativa'].cumsum().round(2)

    return tab_freq