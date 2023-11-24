#  скрипт для парсинга инсты

---
## подготовка окружения
1. install python 3.11.5 in https://www.python.org/
2. clone project from github
```shell
git clone https://github.com/Barashov/insta_script.git
```

```shell
cd insta_script
```

3. create virtual environment
```shell
python -m venv venv
```
4. activate virtual environment
#### linux 
```shell
source venv/bin/activate
```
#### windows
```shell
venv\Scripts\activate
```
5. create folder "data"
#### linux
```shell
mkdir data
```
#### windows
```shell
md data
```
6. install db from [link](https://drive.google.com/file/d/18I2TGpjxr1eaT2Y34J8UGlKdpi5K54sT/view) to folder "data"
7. create .env file and paste hiker api token
#### linux 
```shell
touch .env
echo "TOKEN=<token>" > .env
```
#### windows
```shell
echo TOKEN=<token> > .env
```
8. start script 
```shell
python main.py
```
9. to check data install sqlite browser
   [link](https://sqlitebrowser.org/)