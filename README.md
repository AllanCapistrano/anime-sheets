# anime-sheets

<h3 align="center">
  <a href="https://github.com/AllanCapistrano/anime-sheets/releases/tag/1.0" target=_blank>Modelo da Planilha</a>
</h3>
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

**🌐 Sites Suportados:**
- [x] Animes House
- [x] Goyabu

------------

## 🖥️ Como utilizar ##

1. Faça o download das dependências listadas acima;
2. Criei uma planilha¹ no [Google Planilhas](https://www.google.com/sheets/about/) seguindo o modelo da imagem acima² ou faça o download do [template](https://github.com/AllanCapistrano/anime-sheets/releases/tag/1.0);
3. Entre na [Google Cloud Plataform](https://console.cloud.google.com) e clique em **Criar Projeto**;
4. Digite o nome do projeto e depois clique em **Criar**;
5. Clique no menu lateral esquerdo, e depois selecione a opção **APIs e serviços**;
6. No menu lateral esquerdo, clique em **Biblioteca**;
7. Na caixa de pesquisa, procure por **Google Drive**;
8. Clique no resultado **Google Drive API**, e clique em **Ativar**;
9. Clique em **Criar Credenciais**;
10. Em **Qual API você usa?** escolha a opção **Google Drive API**;
11. Em **Que dados você acessará?** selecione **Dados do aplicativo**;
12. Em **Você planeja usar esta API com Compute Engine, Kubernetes Engine, App Engine ou Cloud Functions?** selecione **Não, nenhuma**, e clique em **Próxima**;
13. Digite um nome para a conta do serviço, além de uma descrição caso deseje (não obrigatório), e clique em **Criar**;
14. Em **Conceda a essa conta de serviço acesso ao projeto** selecione **Projeto ➞ Editor**, clique em **Continuar** e depois clique em **Concluir**;
15. Na nova janela aberta, em **Contas de serviço**, clique no email correspondente (ex: test@myproject.iam.gserviceaccount.com);
16. Nessa nova janela, no menu superior, clique em **Chaves**, e depois em **Adicionar chave ➞ Criar nova chave**;
17. Selecione **JSON**³ e clique em **Criar***;
18. Volte para a página de [Bibliotecas de APIs](https://console.cloud.google.com/apis/library), busque por **Google Sheets API** e clique em **Ativar**;
19. Faça um Fork deste repositório (caso queira modificá-lo) ou somente clone este repositório;
29. Coloque o arquivo contendo as credenciais na pasta do projeto;
21. Compartilhe a planilha com o ```client_email``` que está no arquivo de credenciais (ex: myemail@myproject.iam.gserviceaccount.com);
22. Coloque o link da planilha na constante ```SHEET_LINK``` no arquivo [```main.py```](https://github.com/AllanCapistrano/anime-sheets/blob/main/sheets.py);
23. Após isso, com um terminal aberto no diretório do projeto, basta executar o comando:
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
[GPL-3.0 License](https://github.com/AllanCapistrano/anime-sheets-/blob/main/LICENSE)
