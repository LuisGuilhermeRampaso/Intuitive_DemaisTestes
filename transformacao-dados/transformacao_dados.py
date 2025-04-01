import tabula
import pandas as pd
import zipfile
import os

def executar_teste_completo():
    # Configurações
    pdf_path = "anexos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    output_csv = "transformacao-dados/rol_de_procedimentos.csv"
    output_zip = "transformacao-dados/Teste_GuilhermeRampaso.zip"
    
    try:
        print("🔄 Processo iniciado...")
        
        # Passo 2.1: Extrair dados do PDF
        print("📄 Extraindo tabelas do PDF...")
        dfs = tabula.read_pdf(
            pdf_path,
            pages='all',
            multiple_tables=True,
            lattice=True,
            pandas_options={'header': None}
        )
        
        # Combina todas as tabelas extraídas
        df = pd.concat(dfs, ignore_index=True)
        
        # Passo 2.4: Substituir abreviações (valores E nomes das colunas)
        print("✏️ Substituindo abreviações...")
        
       # Dicionário de substituições
        substituicoes = {
            'OD': 'Odontológico',
            'AMB': 'Ambulatorial'
        }
        
        # Substitui valores dentro do DataFrame
        df = df.replace(substituicoes)
        
        # Renomeia as colunas se necessário
        df = df.rename(columns=substituicoes)
        
        # Substitui os valores nas colunas (se existirem)
        if 'Odontológico' in df.columns:
            df['Odontológico'] = df['Odontológico'].apply(
                lambda x: 'Odontológico' if str(x).strip() == 'OD' else x
            )
        
        if 'Ambulatorial' in df.columns:
            df['Ambulatorial'] = df['Ambulatorial'].apply(
                lambda x: 'Ambulatorial' if str(x).strip() == 'AMB' else x
            )
        
        # Passo 2.2: Salvar como CSV
        df.to_csv(output_csv, index=False, encoding='utf-8-sig')
        print(f"✅ CSV gerado: {output_csv}")
        
        # Passo 2.3: Compactar o arquivo
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(output_csv, arcname=os.path.basename(output_csv))
        print(f"📦 Arquivo ZIP criado: {output_zip}")
        
        print("\n🎉 Processo concluído com sucesso!")
        return True
    
    except Exception as e:
        print(f"\n❌ Erro durante o processo: {str(e)}")
        return False

if __name__ == "__main__":
    executar_teste_completo()