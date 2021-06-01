# anime-sheets

<h3 align="center">Modelo da Planilha</h3>
<p align="center">
  <img src="https://i.imgur.com/b46LpT2.png" alt="Google Sheets">
</p>

------------

## 📚 Descrição ##
Crawler que a partir dos dados previamente preenchidos na planilha (nome do anime, temporada, URL, episódio atual), busca as informações desse anime para atualizar os dados da planilha.

O objetivo desta aplicação é que não seja necessário abrir o site para verificar se um episódio novo foi lançado, pois com a utilização desse crawler, o último episódio de todos os animes que estão preenchidos na planilha serão atualizados automaticamente.

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

1. Criei uma planilha¹ no [Google Planilhas](https://www.google.com/sheets/about/) seguindo o modelo da imagem acima²;
2. Entre na [Google Cloud Plataform](https://console.cloud.google.com) e clique em **Criar Projeto**;
3. Digite o nome do projeto e depois clique em **Criar**;
4. Clique no menu lateral esquerdo, e depois selecione a opção **APIs e serviços**;
5. No menu lateral esquerdo, clique em **Biblioteca**;
6. Na caixa de pesquisa, procure por **Google Drive**;
7. Clique no resultado **Google Drive API**, e clique em **Ativar**;
8. Clique em **Criar Credenciais**;
9. Em **Qual API você usa?** escolha a opção **Google Drive API**;
10. Em **Que dados você acessará?** selecione **Dados do aplicativo**;
11. Em **Você planeja usar esta API com Compute Engine, Kubernetes Engine, App Engine ou Cloud Functions?** selecione **Não, nenhuma**, e clique em **Próxima**;
12. Digite um nome para a conta do serviço, além de uma descrição caso deseje (não obrigatório), e clique em **Criar**;
13. Em **Conceda a essa conta de serviço acesso ao projeto** selecione **Projeto ➞ Editor**, clique em **Continuar** e depois clique em **Concluir**;
14. Na nova janela aberta, em **Contas de serviço**, clique no email correspondente (ex: test@myproject.iam.gserviceaccount.com);
15. Nessa nova janela, no menu superior, clique em **Chaves**, e depois em **Adicionar chave ➞ Criar nova chave**;
16. Selecione **JSON**³ e clique em **Criar***;
17. Volte para a página de [Bibliotecas de APIs](https://console.cloud.google.com/apis/library), busque por **Google Sheets API** e clique em **Ativar**;
18. Faça um Fork deste repositório (caso queira modificá-lo) ou somente clone este repositório;
29. Coloque o arquivo contendo as credenciais na pasta do projeto;
20. Compartilhe a planilha com o ```client_email``` que está no arquivo de credenciais (ex: myemail@myproject.iam.gserviceaccount.com);
21. Coloque o link da planilha na constante ```SHEET_LINK``` no arquivo [```main.py```](https://github.com/AllanCapistrano/anime-sheets/blob/main/sheets.py);
22. Após isso, com um terminal aberto no diretório do projeto, basta executar o comando:
```powershell
$ python main.py
```

###### Obs1: Se não utilizar o nome da planilha como "Animes", é necessário alterar a contante ```SHEET_TITLE``` no arquivo [```sheets.py```](https://github.com/AllanCapistrano/anime-sheets/blob/main/sheets.py) ######
###### Obs2: Caso não siga o modelo da imagem, será necessário alterar as constantes de coluna (```COL_```) no arquivo [```sheets.py```](https://github.com/AllanCapistrano/anime-sheets/blob/main/sheets.py) ######
###### Obs3: Recomenda-se renomear o arquivo ```.json``` baixado para ```creds.json```, caso contrário, é necessário alterara constante ```CREDS_FILE``` no arquivo [```sheets.py```](https://github.com/AllanCapistrano/anime-sheets/blob/main/sheets.py)  ######

------------

## 📌 Autor ##
- Allan Capistrano: [Github](https://github.com/AllanCapistrano) - [Linkedin](https://www.linkedin.com/in/allancapistrano/) - [E-mail](https://mail.google.com/mail/u/0/?view=cm&fs=1&tf=1&source=mailto&to=asantos@ecomp.uefs.br)

------------

## ⚖️ Licença ##
[MIT License (MIT)](https://github.com/AllanCapistrano/anime-sheets-/blob/main/LICENSE)
