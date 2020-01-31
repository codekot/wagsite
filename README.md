# Wagtail + Angular demo
This is demo project where Wagtail and Angular work together.

###### What is good about that?
You can get a modern web application with CMS functionality faster and at a better cost than before.

#### Before project building
Go to directory which you want to contain project.  
Clone repository:  
```bash
git clone https://github.com/codekot/wagsite
```
Define .env file
```bash
cp .env.example .env
```
And define variables.
`HOST` - set a real host you want to use. 
If you want to run locally you may set `http://127.0.0.1`

### Local run
Create virtualenv:
```bash
pip install virtualenv
python3 -m venv .venv
source .venv/bin/activate
cd ..
```
Install requirements:
```bash
pip install -r requirements.txt
```
And run project
```bash
python manage.py runserver 0.0.0.0:8080
```

#### Production build
1. [Install docker](https://docs.docker.com/install/#server)
2. [Install docker-compose](https://docs.docker.com/compose/install/)
3. Add your user to docker group
    ```bash
    sudo usermod -aG docker {USER}
    ```
4. Re-login
5. Build container:
    ```bash
    docker-compose up -d --build api
    ```
6. Check containers state:
    ```bash
    docker-compose ps
    ```
7. Go for an url [API method for pages](http://0.0.0.0:5000/api/v2/pages/)  
    and check whether page is loaded successfully.

#### Updating production
Run bash script:
```bash
sh docker/update.sh
```

##### See logs (last 100, `api` example)
```bash
docker-compose logs --tail 100 api
```

##### Attach to logger (see logs, while they are writing) 
```bash
docker-compose logs --tail 100 api
```
