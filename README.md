# Hogwards API

## Pré-requis

Pour la réalisation de l'API Hogwarts, le système de gestion de base de données relationnelles utilisé est MySQL. L'ensemble des dépendances se situent dans le fichier suivant : requirements.txt

## Utilisation 

Une fois le serveur lancé à l'aide de la commande ```uvicorn main:app --reload```, rendez-vous à l'adresse suivante pour y accèder : 

```
http://127.0.0.1:8000
```

## Information 

### Modélisation de la base de données

Ma base de données se nomme Hogwards. Elle présente une seule table 'wizards' et les champs suivants : id, firstname, lastname et house (c.f photo ci-dessous).

<img width="571" alt="Capture d’écran 2023-02-23 à 16 01 50" src="https://user-images.githubusercontent.com/70972077/220956803-ae124685-9c5d-48e0-86bf-f67fd1209d4d.png">


Création de la table 'wizard' :

```sql
-- hogwarts.wizards definition

CREATE TABLE `wizards` (
  `id` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `house` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

### Architecture du projet 

L'architecture de ce projet est le suivant :

```
├── app/
│   ├── main.py
│   ├── database.py
│   ├── api.py
│   ├── exceptions/
│   │   └── exceptions.py
│   ├── models/
│   │   └── wizard.py 
│   ├── routes/
│   │   └── wizard.py
│   ├── templates/
│       └── wizard.py 
│
├── test/
│    └── unit/
│         └── app/
│              └── test_main.py
│
├── requirements.txt
```


### Présentation de l'API 

Méthode employée : CRUD. Les différents routes/endpoints sont disponibles à l'adresse suivante : 

```
http://127.0.0.1:8000/docs
```

<img width="1440" alt="Capture d’écran 2023-02-23 à 16 38 13" src="https://user-images.githubusercontent.com/70972077/220956903-f22e049e-cf61-4ef1-a1aa-1e048a89358e.png">


GET http://127.0.0.1:8000/wizards récupère la liste de tous les sorciers  
GET http://127.0.0.1:8000/wizards/{id} récupère la liste d'un sorcier ou d'une sorcière particulière  
POST http://127.0.0.1:8000/wizards permet d'ajouter un sorcier ou d'une sorcière particulière  
PUT http://127.0.0.1:8000/wizards/{id} permet de modifier les données d'un seul sorcier ou sorcière  
DELETE http://127.0.0.1:8000/wizards/{id} permet de supprimer les données d'un seul sorcier ou sorcière  


### Tests unitaires

Les tests unitaires se trouvent dans le dossier cd test/unit/app et s'exécute à l'aide de la commande suivante sous mac:

```
python3 test/unit/app/test_main.py
```
