from flask import Flask, request, jsonify
import pandas as pd
from fuzzywuzzy import fuzz

app = Flask(__name__)

# Carregar os dados do CSV
df = pd.read_csv('dados_cadastrais_ativos.csv', sep=';', encoding='utf-8')

@app.route('/api/search', methods=['GET'])
def search_operadoras():
    query = request.args.get('q', '')
    limit = int(request.args.get('limit', 10))
    
    if not query:
        return jsonify([])
    
    # Função para calcular a relevância
    def calculate_relevance(row):
        name = str(row['Razao_Social']) if pd.notna(row['Razao_Social']) else ''
        fantasy = str(row['Nome_Fantasia']) if pd.notna(row['Nome_Fantasia']) else ''
        city = str(row['Cidade']) if pd.notna(row['Cidade']) else ''
        state = str(row['UF']) if pd.notna(row['UF']) else ''
        
        # Calcular scores para diferentes campos
        score_name = fuzz.token_set_ratio(query.lower(), name.lower())
        score_fantasy = fuzz.token_set_ratio(query.lower(), fantasy.lower())
        score_city = fuzz.token_set_ratio(query.lower(), city.lower())
        score_state = fuzz.token_set_ratio(query.lower(), state.lower())
        
        # Ponderar os scores (dando mais peso para nome e nome fantasia)
        total_score = (score_name * 0.5 + score_fantasy * 0.3 + score_city * 0.1 + score_state * 0.1)
        return total_score
    
    # Aplicar a função de relevância a cada linha
    df['relevance'] = df.apply(calculate_relevance, axis=1)
    
    # Ordenar por relevância e pegar os top N resultados
    results = df.sort_values('relevance', ascending=False).head(limit)
    
    # Converter para formato JSON
    response = results.to_dict(orient='records')
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)