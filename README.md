# Brasil.IO - Dados abertos para um Brasil mais ligado

### O Problema

Muitos dados públicos brasileiros estão disponíveis (principalmente depois da
criação da Lei de Acesso à Informação), mas não necessariamente acessíveis.
Mesmo que a informação esteja disponível, nem sempre ela está disponível em um
formato legível por máquina, ou utilizando um formato aberto, ou possui
descrição (metadados) que facilitem a interpretação (manual ou automática)
desses dados. **Quanto menos acessível é uma informação, mais perto de ser
fechada ela está**.

Além do problema relativo à acessibilidade, não existe um lugar comum em que
todos os dados disponíveis estejam organizados e catalogados, dificultando
ainda mais o acesso (ou a descoberta que esse tipo de informação está
disponível).

O objetivo do projeto não é concorrer com iniciativas correlatas do Governo
(como o dados.gov.br) e de outras organizações -- pelo contrário, gostaríamos
de disponibilizar os dados que essas organizações já disponibilizam, porém de
forma integrada e estruturada, permitindo a qualquer um (independente de
vínculo) possa disponibilizar dados, independente da fonte.


### A Solução

O projeto Brasil.IO foi criado com o objetivo de ser referência para quem
procura ou quer publicar dados abertos sobre o Brasil de forma organizada,
legível por máquina e usando padrões abertos. O projeto foi idealizado e está
sendo desenvolvido por Álvaro Justen, com a colaboração de outros
desenvolvedores.


### Colabore

Para rodar o projeto em sua máquina, certifique-se de que você tem instalados:

- git
- [pyenv](https://github.com/pyenv/pyenv) com
  [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) e Python 3.6.4
- [docker](https://www.docker.com/)

Siga os passos:

```bash
# Clonar o repositório:
git clone git@github.com:turicas/brasil.io.git

# Criar um virtualenv:
pyenv virtualenv 3.6.4 brasil.io

# Criar containers
cd brasil.io
source .activate

# Instalar dependências
pip install -r requirements.txt

# Criar schema e popular base de dados
python manage.py migrate
python manage.py update_data
```

## Deploying on Dokku

Dokku is a very small plataform-as-a-service software, it works like Heroku
and can be used to easily deploy apps in your own infrastructure.

- On remote machine:
  - Install dokku
  - Install needed plugins:
    - `dokku plugin:install https://github.com/dokku/dokku-postgres.git postgres`
    - `dokku plugin:install https://github.com/dokku/dokku-letsencrypt.git`
  - Run `dokku apps:create brasilio-web`
- On local machine:
  - `git remote add dokku dokku@HOSTNAME:brasilio-web`
  - `git push dokku master`
- On remote machine:
  - `dokku postgres:create brasilio-pgsql`
  - `dokku postgres:expose brasilio-pgsql`
  - `dokku postgres:link brasilio-pgsql brasilio-web`
  - `dokku config:set brasilio-web DEBUG=False`
  - `dokku ps:scale brasilio-web web=4`
  - `dokku domains:add brasilio-web brasil.io`
  - `dokku domains:add brasilio-web api.brasil.io`
  - `dokku domains:add brasilio-web www.brasil.io`
  - `dokku letsencrypt brasilio-web`
  - Put `.csv.xz` files inside `/root/data` and run: `dokku storage:mount brasilio-web /root/data:/data`
  - `dokku run brasilio-web /bin/bash`
  - Inside container:
    - `cd /app && python manage.py migrate`
    - `cd /app && python manage.py createsuperuser`
    - `cd /app && python manage.py update_data`
    - `cd /app && python manage.py import_data <dataset-slug> /data/<filename.csv.xz>`


### Licença

[GNU General Public License version 3](https://www.gnu.org/licenses/gpl.html)
