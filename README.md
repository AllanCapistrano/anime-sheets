# anime-sheets

<h3 align="center">
  <a href="https://github.com/AllanCapistrano/anime-sheets/releases/tag/1.0" target="_blank">Modelo da Planilha</a>
</h3>
<p align="center">
  <img src="https://i.imgur.com/b46LpT2.png" alt="Google Sheets">
</p>

---

## 📖 Descrição

> **Crawler para verificar qual é o último episódio dos animes que estão na planilha, basta preencher com a URL[^1] do mesmo.**

[^1]: Verifique quais são os [sites suportados](#-sites-suportados).

### 🌐 Sites Suportados:

- [x] [Assistir Animes](https://assistiranimes.org/)
- [x] [Animes Gratis](https://animesgratis.org)
- [x] [Animes House](https://animeshouse.net/)
- [x] [Animes Online](https://animesonline.nz/)
- [x] [Bakashi TV](https://bakashi.tv/)
- [x] [Goyabu](https://goyabu.com/)

>[!NOTE]
>Possa ser que algum desses sites não existam mais.
---

## 🖥️ Como utilizar

> [!IMPORTANT]  
> A partir da versão [v1.2.0](https://github.com/AllanCapistrano/anime-sheets/tree/v1.2.0) é necessário a instalação da ferramenta [curl](https://curl.se/download.html), então garanta que você possui a mesma instalada em sua máquina.
> Caso esteja utilizando o Sistema Operacional *Windows*, recomendamos o uso do [Git For Windows](https://gitforwindows.org/), nele o [curl](https://curl.se/download.html) já vem instalado por padrão, além de garantir o funcionamento correto do projeto.


### Configurando o Google Planilhas

1. Crie uma planilha[^2] no [Google Planilhas](https://www.google.com/sheets/about/) seguindo o modelo da imagem acima[^3] ou faça o download do [template](https://github.com/AllanCapistrano/anime-sheets/releases/tag/1.0);
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
12. Digite um nome para a conta do serviço, além de uma descrição (opcional), e clique em **Criar e Continuar**;
13. Em **Conceda a essa conta de serviço acesso ao projeto** selecione **Básico ➞ Editor**, clique em **Continuar** e depois clique em **Concluir**;
14. Após isso, clique em **Credenciais** no menu lateral esquerdo, em **Contas de serviço**, clique no email correspondente (ex: test@myproject.iam.gserviceaccount.com);
15. Nessa nova janela, no menu superior, clique em **Chaves**, e depois em **Adicionar chave ➞ Criar nova chave**;
16. Selecione **JSON**[^4] e clique em **Criar**;
17. Volte para a página de [Bibliotecas de APIs](https://console.cloud.google.com/apis/library), busque por **Google Sheets API** e clique em **Ativar**;
18. Faça um Fork deste repositório (caso queira modificá-lo) ou somente clone-o;
19. Coloque o arquivo contendo as credenciais na pasta do projeto;
20. Compartilhe a planilha com o `client_email` que está no arquivo de credenciais (ex: myemail@myproject.iam.gserviceaccount.com);

### Executando o projeto

1. Faça o download das dependências do projeto:
   ```powershell
   pip install -r requirements.txt
   ```
   ou
   ```powershell
   pip3 install -r requirements.txt
   ```
2. Faça uma cópia do arquivo `.env.example` com o nome de `.env`, ou altere o nome do arquivo `.env.example` para `.env`:
   ```powershell
   cp .env.example .env
   ```
   ou
   ```powershell
   mv .env.example .env
   ```
3. Abra o arquivo `.env` e preencha os campos (todos são opcionais):
   1. `CREDENTIALS_FILE` nome do arquivo com a extensão `.json` que contém as credenciais do **Google Drive API**, criado no passo **8** de [Configurando o Google Planilhas](#configurando-o-google-planilhas) ;
   2. `USER_NAME` nome de usuário que deseja;
   3. `SHEET_LINK` URL da sua planilha (a mesma que você utilizou para compartilhar);
   4. `BITLY_TOKEN`[^5] token de acesso do [Bitly](https://bitly.com/) para encurtar as URLs.
4. Após isso, com um terminal aberto no diretório do projeto, basta executar o comando:
   ```powershell
   python main.py
   ```

[^2]: Se não utilizar o nome da planilha como "Animes", será necessário alterar a constante `SHEET_TITLE` no arquivo [`sheets.py`](https://github.com/AllanCapistrano/anime-sheets/blob/main/sheets.py)

[^3]: Caso não siga o modelo da imagem, será necessário alterar as constantes de coluna (`COL_*`) no arquivo [`sheets.py`](https://github.com/AllanCapistrano/anime-sheets/blob/main/sheets.py)

[^4]: Recomenda-se renomear o arquivo `.json` baixado para `creds.json`.

[^5]: As URLs curtas melhoram a exibição da tabela, porém, caso não queira encurtar as URLs basta não preencher esse campo.

---

## 👨‍💻 Autor

| [![Allan Capistrano](https://github.com/AllanCapistrano.png?size=100)](https://github.com/AllanCapistrano) |
| ---------------------------------------------------------------------------------------------------------- |
| [Allan Capistrano](https://github.com/AllanCapistrano)                                                     |

<p>
    <h3>Onde me encontrar:</h3>
    <a href="https://github.com/AllanCapistrano">
        <img src="https://github.com/AllanCapistrano/AllanCapistrano/blob/master/assets/github-square-brands.png" alt="Github icon" width="5%">
    </a>
    &nbsp
    <a href="https://www.linkedin.com/in/allancapistrano/">
        <img src="https://github.com/AllanCapistrano/AllanCapistrano/blob/master/assets/linkedin-brands.png" alt="Linkedin icon" width="5%">
    </a> 
    &nbsp
    <a href="https://mail.google.com/mail/u/0/?view=cm&fs=1&tf=1&source=mailto&to=asantos@ecomp.uefs.br">
        <img src="https://github.com/AllanCapistrano/AllanCapistrano/blob/master/assets/envelope-square-solid.png" alt="Email icon" width="5%">
    </a>
</p>

---

## 🙏 Apoie

**Por favor ⭐️ este repositório caso este projeto seja útil e/ou tenha lhe ajudado.**

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/allancapistrano)

---

## ⚖️ Licença

[GPL-3.0 License](./LICENSE)
