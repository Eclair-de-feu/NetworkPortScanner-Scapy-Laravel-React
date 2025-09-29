# Network Port Scanner with Scapy, Laravel, and React

Ce projet permet de scanner les ports ouverts sur un réseau local avec **Scapy**, stocker les résultats via une **API Laravel**, et les afficher sous forme de graphique avec **React**.

## Structure du projet
```
/
├── scapy/
│   └── scan.py          # Script Python pour scanner les ports ouverts
├── backend/
│   └── (Laravel)        # API Laravel pour recevoir et stocker les résultats
└── frontend/
    └── (React)         # Interface pour afficher les résultats en graphique
```

## Prérequis
- Python 3.x (pour Scapy)
- PHP 8.x, Composer (pour Laravel)
- Node.js (pour React)

## Installation
### 1. Cloner le dépôt
```bash
git clone https://github.com/Eclair-de-feu/NetworkPortScanner-Scapy-Laravel-React.git
cd NetworkPortScanner-Scapy-Laravel-React
```

### 2. Configurer le backend (Laravel)
```bash
cd backend
composer install
cp .env.example .env
php artisan key:generate
php artisan migrate
php artisan serve
```

### 3. Configurer le frontend (React)
```bash
cd ../frontend
npm install
npm run dev
```

### 4. Lancer le scan
```bash
cd ../scapy
sudo python3 scan.py
```

## Fonctionnalités
- Scapy : Scan des ports ouverts sur le réseau local.
- Laravel : API pour recevoir et stocker les résultats.
- React : Affichage des résultats sous forme de graphique.

## Auteur
Eclair-de-feu