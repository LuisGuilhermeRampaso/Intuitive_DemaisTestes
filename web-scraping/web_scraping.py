import requests
from bs4 import BeautifulSoup
import os
import zipfile
from urllib.parse import urljoin

def download_pdfs_and_zip():
    # URL base do site
    base_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    
    print("🔍 Acessando o site para encontrar os PDFs...")
    
    try:
        response = requests.get(base_url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao acessar o site: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Lista dos PDFs que queremos baixar (com base nos links que você encontrou)
    target_pdfs = [
        "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",
        "Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"
    ]
    
    print("📄 Procurando os links específicos dos PDFs...")
    
    # Encontrar todos os links PDF na página
    pdf_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        for target in target_pdfs:
            if target in href:
                full_url = urljoin(base_url, href)
                pdf_links.append(full_url)
                print(f"✅ Encontrado: {target}")
    
    if not pdf_links:
        print("❌ Nenhum dos PDFs alvo foi encontrado na página!")
        print("🔍 Verifique se os nomes dos arquivos ainda são os mesmos:")
        for target in target_pdfs:
            print(f"- {target}")
        return
    
    # Criar pasta para os anexos
    if not os.path.exists('anexos'):
        os.makedirs('anexos')
    
    downloaded_files = []
    for pdf_url in pdf_links:
        try:
            pdf_name = pdf_url.split('/')[-1]
            pdf_path = f"anexos/{pdf_name}"
            
            print(f"⬇️ Baixando {pdf_name}...")
            pdf_response = requests.get(pdf_url, timeout=15)
            pdf_response.raise_for_status()
            
            with open(pdf_path, 'wb') as f:
                f.write(pdf_response.content)
            
            downloaded_files.append(pdf_path)
            print(f"✔️ Download completo: {pdf_name} ({len(pdf_response.content)/1024:.2f} KB)")
        except Exception as e:
            print(f"❌ Falha ao baixar {pdf_url}: {e}")
    
    if not downloaded_files:
        print("⚠️ Nenhum PDF foi baixado com sucesso!")
        return
    
    print("🗜 Criando arquivo ZIP com os anexos...")
    zip_path = "anexos_compactados.zip"
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in downloaded_files:
            zipf.write(file, os.path.basename(file))
            print(f"📦 Adicionado ao ZIP: {file}")
    
    print(f"\n🎉 Processo concluído com sucesso!")
    print(f"📂 Arquivo ZIP criado em: {os.path.abspath(zip_path)}")
    print(f"📦 Tamanho do ZIP: {os.path.getsize(zip_path)/1024:.2f} KB")
    print(f"📄 PDFs incluídos: {len(downloaded_files)}")

if __name__ == "__main__":
    download_pdfs_and_zip()