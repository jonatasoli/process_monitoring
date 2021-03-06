# Monitoring Process

Sistema de Monitoramento de processos.


## Como desenvolver?

1.  Clone o repositório.
2.  Crie um virtualenv com Python 3.6
3.  Ative o virtualenv.
4.  Instale as dependências.
5.  Configure a instância com o .env
6.  Execute os testes.


``` console
git clone https://github.com/jonatasoli/.process_monitoring.git monitoring
cd wttd
python -m venv .monitoring
source .monitoring/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test

```
## Como fazer o deploy?

1. Crie uma instância no heroku
2. Envie as configuraçoes para o heroku
3. Define uma SECRET_KEY segura para instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

``` console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```
