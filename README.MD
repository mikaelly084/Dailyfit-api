# DailyFit

O **DailyFit** é uma plataforma web voltada para alimentação e organização da rotina. O projeto possui uma interface para acompanhamento de refeições, hábitos e progresso, além de uma API desenvolvida para futuramente realizar o gerenciamento e armazenamento dos dados.

## Estrutura do projeto

- `templates/` → contém o `index.html` e demais páginas HTML.
- `static/css/` → contém os arquivos de estilização CSS.
- `static/js/` → contém os arquivos JavaScript e funcionalidades da interface.
- `main.py` → responsável pela API desenvolvida com FastAPI.

## API e servidor

Para iniciar o servidor durante o desenvolvimento, o comando utilizado é:

```bash
uvicorn main:app --reload

Obs: No momento, o servidor não funcionará completamente, pois ainda é necessário que seja desenvolvido e configurado o banco de dados do projeto.

O banco de dados será responsável por armazenar os dados utilizados pelas rotas da API, permitindo que informações como usuários, refeições, hábitos, progresso e outros dados da aplicação sejam registrados e consultados.

Por isso, a próxima etapa do projeto é a criação e integração do banco de dados com a API. Após essa integração, as rotas poderão gravar e recuperar os dados corretamente.