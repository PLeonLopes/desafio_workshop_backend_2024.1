
# API de Localização e Clima

Esta é uma API simples criada para fornecer informações específicas sobre cidades globalmente. Através dela, os usuários podem acessar dados atualizados sobre a cidade escolhida, incluindo coordenadas geográficas, temperatura atual e outras informações sobre diversas cidades ao redor do mundo.


## Tecnologias Utilizadas

- **Python** - Linguagem de Programação
- **Django Framework** (Rest/Template) e **Boostrap Framework** - Frameworks Web


## Instalação

Para instalar e testar a API é necessário um ambiente de virtual do python (venv), na pasta da aplicação, abra o terminal e digite:


```bash
  python -m venv venv
```
Depois é necessário ativar o ambiente virtual, para isso, digite:

```bash
  .\venv\Scripts\activate 
```
Para utilizar o projeto, faz-se necessário a instalação de suas dependências, que estão localizadas em [requirements.txt](https://github.com/PLeonLopes/desafio_workshop_backend_2024.1/blob/main/requirements.txt). Para isso, importaremos todas as dependências através do terminal:

```bash
  pip install -r requirements.txt 
```

Finalmente, poderemos rodar o projeto, no terminal, digite: 

```bash
  python .\manage.py runserver
```

## Uso da Aplicação

Para usar esta ferramenta, é necessário acessar a url: http://127.0.0.1:8000/

Após acessar a url, você já está na página principal do projeto. Podendo fazer requisições para a API EXTERNA "Current weather data".

Para acessar informações sobre uma cidade específica, insira o nome da cidade na barra de pesquisa e envie a solicitação. Os dados da cidade serão exibidos no campo abaixo, incluindo o código do país, coordenadas geográficas, temperatura atual (C°), sensação térmica, umidade do ar e pressão atmosférica.


> [!IMPORTANT]
> Observe atentamente as informações sobre caracteres especiais abaixo da barra de pesquisa. O funcionamento adequado da API pode ser comprometido se as instruções não forem seguidas estritamente.
