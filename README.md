# nlw-barcode

## 🚀 Projeto
Servidor HTTP em Flask para geração de códigos de barras.</br>
Aplicação desenvolvida durante a Next Level Week, realizada pela [@Rocketseat](https://www.rocketseat.com.br) em fev/24.

<p align="center">
  <img 
    width="50%" 
    alt="barcode"
    src="/github_assets/1234-5678-9000.png"
  />
</p>

## 🛠️ Tecnologias
- [Python](https://www.python.org)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)

## 🗂️ Utilização

### 🐑🐑 Clonando o repositório:

```bash
  $ git clone url-do-projeto.git
  $ cd nlw-barcode                     #change to that directory
```

### 🔨 Setup (opcional):
Iniciar um [ambiente virtual em Python](https://docs.python.org/pt-br/3/library/venv.html):
```bash
  $ pip3 install virtualenv            #download virtualenv package
  $ python3 -m venv .venv              #create ".venv" folder at current dir
  $ . .venv/bin/activate               #start the environment
  $ pip install --upgrade pip          #update pip
```

### ▶️ Rodando o App:
```bash
  $ pip3 install -r requirements.txt   #download dependencies
  $ python3 run_raw.py                 #start the server
```

```bash
  POST http://localhost:4000/create_tag
  Request Body:
  {
    "product_code": "1234-5678-9000"
  }
```
Imagem .png salva do diretório em que o script do servidor estiver rodando!
