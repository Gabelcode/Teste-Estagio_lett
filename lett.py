import requests
from bs4 import BeautifulSoup



#pagina que vamos trabalhar
url ='https://www.netshoes.com.br/casual/tenis?mi=hm_ger_mntop_C-DEP-casual&psn=Menu_Top'

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
produtos = soup.find_all('div', class_='item-card card-desktop card-with-rating lazy-price item-desktop--3')
ultima_pagina= soup.find('a', class_='last')

for i in range(1,int(ultima_pagina)):
        url_pag = f'https://www.netshoes.com.br/casual/tenis?nsCat=Artificial&page={i}2'        
        site = requests.get(url_pag, headers=headers)
        soup = BeautifulSoup(site.content, 'html.parser')
        produtos = soup.find_all('div', class_='item-card card-desktop card-with-rating lazy-price item-desktop--3')
        
        with open ('precos_produtos.csv', 'a', newline='', enconding='UTF-8') as f:
                for produto in produtos:

                        marca = produto.find('div', class_='item-card__description__product-name').get_text().strip()
                try: 
                        preco = produto.find('span', class_='haveInstallments').get_text().strip()
                
                except:
                        preco = '0'

                linha = marca + ';' + preco + ';' 
                print(linha)
                f.write(linha)
        print(url_pag)



