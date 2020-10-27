# anime-sheets

<h3 align="center">Modelo da Planilha</h3>
<p align="center">
  <img src="https://i.imgur.com/b46LpT2.png" alt="Google Sheets">
</p>

------------

## 📚 Descrição ##
Crawler que a partir dos dados previamente preenchidos na planilha (nome do anime, temporada, URL, episódio atual), busca as informações desse anime para atualizar os dados da planilha.

O objetito dessa aplicação é que não seja necessário abrir o site para verificar se um episódio novo foi lançado, pois com a utilização desse crawler, o último episódio de todos os animes que estão preencidos na planilha serão atualizados automaticamente.

###### Obs: O crawler foi desenvolvido para verificar o lançamento dos animes no site [Animes House](https://animeshouse.net/), sendo necessário modificações para funcionar em outros sites.

**🔗 Tecnologias utilizadas:**
- [Python](https://www.python.org/)
- [Google Planilhas](https://www.google.com/sheets/about/)

**📊 Dependências:**
- [Requests](https://pypi.org/project/requests/)
- [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [LXML](https://pypi.org/project/lxml/)
- [gspread](https://pypi.org/project/gspread/)
- [oauth2client](https://pypi.org/project/oauth2client/)

------------

## 🖥️ Como utilizar ##

1. Criei uma planilha* no [Google Planilhas](https://www.google.com/sheets/about/) seguindo o modelo da imagem acima*.
2. Obtenha as credenciais para acessar a API do Google Drive e Google Planilhas, [clique aqui](https://www.iperiusbackup.net/pt-br/como-habilitar-a-api-do-google-drive-e-obter-credenciais-de-cliente/) para aprender a obter a credencial do Google Drive (mesmo processo para obter a credencial do Google Planilhas).
3. Faça um Fork deste repositório (caso queira modificá-lo) ou somente clone este repositório.
4. Coloque o arquivo contendo as credenciais na pasta do projeto*.
5. Compartilhe a planilha com o ```client_email``` que está no arquivo de credenciais.
6. Após isso, basta rodar o arquivo [```main.py```](https://github.com/AllanCapistrano/anime-sheets/blob/main/main.py)

###### Obs1: Se não utilizar o nome da planilha como "Animes", é necessário alterar a contante ```SHEET_TITLE``` no arquivo [```sheets.py```](https://github.com/AllanCapistrano/anime-sheets/blob/main/sheets.py) ######
###### Obs2: Caso não siga o modelo da imagem, será necessário alterar as constantes de coluna (```COL_```) no arquivo [```sheets.py```](https://github.com/AllanCapistrano/anime-sheets/blob/main/sheets.py) ######
###### Obs3: Caso não utilize o nome do arquivo como ```creds.json```, é necessário altera a constante ```CREDS_FILE``` no arquivo [```sheets.py```](https://github.com/AllanCapistrano/anime-sheets/blob/main/sheets.py) ######
------------

## 📌 Autor ##
- Allan Capistrano: [Github](https://github.com/AllanCapistrano) - [Linkedin](https://www.linkedin.com/in/allancapistrano/) - [E-mail](https://mail.google.com/mail/u/0/?view=cm&fs=1&tf=1&source=mailto&to=asantos@ecomp.uefs.br)

------------

## ⚖️ Licença ##
[MIT License (MIT)](https://github.com/AllanCapistrano/anime-sheets-/blob/main/LICENSE)
