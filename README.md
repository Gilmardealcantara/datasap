# datasap

## Students' Academic Performance Dataset (xAPI-Edu-Data)

Aplicação para a analize e vizualização de dados acadêmos extraídos de 
https://www.kaggle.com/aljarah/xAPI-Edu-Data


## Deploy 
É aconselhavel instalar o virtualenv e criar ambientes virtuais no python

Instale as dependencias do python

```python 
pip install -r requirements.txt
```
Crie um base de dados chamada 'datasap' no postgress

Execute migrations
```python 
python manage.py  db init 
python manage.py  db migrate
python manage.py  db upgrade
```

Carregar dados do csv no banco
``` python
python manage.py load 

```

Fazer agregação de dados
``` python
python manage.py agg

```

Executar testes
``` python
python manage.py test

```

Iniciar Servidor

``` python
python manage.py runserver

```
