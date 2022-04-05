# Kasix-Photography
projekt stworzony na zaliczenie przedmiotu, osadzony w chmurze Azure (brak subskrypcji)
podgląd > https://kasix-photography.herokuapp.com/ 
Jest to wizytówka Pani Kasi, która jest fotografem.
Użytkownik ma możliwość wysłania przez formularz chęci zakupu szkolenia z fotografii. 
Automatyczny email zwrotny do klienta


## Tech/Framework/Apps

### Frontend
- [HTML] [CSS] [BOOTSTRAP]
### Backend
- [PYTHON] [FLASK] 
### Deployment
- [AZURE CLI] [HEROKU]
### Rozszerzenia
[LINK](https://github.com/Kuczli/Strona_Projekt_Grupowy/blob/main/requirements.txt)

Oczywiście projekt jest osadzony na [public repository](https://github.com/Kuczli) w Github


## Instalacja
Pobranie repozytorium
```
git clone https://github.com/Kuczli/Strona_Projekt_Grupowy
```
Edytowanie projektu pod siebie (najważniejsze komendy)
```
py -3 -m venv .venv
.venv/scripts/activate

python -m pip install --upgrade pip
python -m pip install flask
set FLASK_ENV=development
python -m flask run
```
Deployment na Github'a (najważniejsze komendy)
```
git init
git add .
git commit -m "co robimy"
git push
git remote add origin https://github.com/........
git branch -M main
git push -u origin main
```
Deployment na Heroku (najważniejsze pliki/komendy)
```
#podpięcie konta github z heroku
#zmiana pliku z app.py na main.py
main.py
pip install gunicorn
#tworzenie pliku w projekcie Procfile
Procfile
#w pliku:
web: gunicorn main:app
```
Deployment na Azure (najważniejsze komendy)
```
#logowanie
az login

#tworzenie grupy zasobów
az group create -n Kasixphotography -l westeurope

#tworzenie plan App Service
az appservice plan create --name Kasixphotography --resource-group Kasixphotography --sku B1 --is-linux

#tworzenie nową App Service internetową
az webapp create --name Kasixphotography --runtime 'PYTHON|3.9' --plan Kasixphotography --resource-group Kasixphotography --query 'defaultHostName' --output table
```






