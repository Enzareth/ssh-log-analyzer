# 🔐 SSH Log Analyzer

> Outil Python permettant d'analyser des logs SSH afin d'identifier les tentatives de connexion suspectes.

## 📌 Présentation

SSH Log Analyzer est un projet Python réalisé dans le cadre de mon apprentissage en administration systèmes, réseaux et cybersécurité.

L'objectif est d'analyser automatiquement des journaux SSH afin d'extraire les informations importantes, produire des statistiques et identifier les adresses IP présentant un comportement potentiellement suspect.

Le projet est développé progressivement afin d'améliorer mes connaissances en Python et en cybersécurité.

## 🚀 Fonctionnalités

- Lecture et analyse de fichiers de logs SSH
- Détection des connexions :
  - `Accepted`
  - `Failed`
  - `Invalid user`
- Extraction des informations :
  - Date
  - Type d'événement
  - Utilisateur
  - Adresse IP
  - Port
- Comptage des tentatives par adresse IP
- Analyse des échecs par IP
- Détection d'IP suspectes
- Classification selon le taux d'échec :
  - 🟢 Neutre
  - 🟠 À surveiller
  - 🔴 Suspect

## 📊 Détection

Le niveau de suspicion est actuellement basé sur la proportion d'échecs par rapport au nombre total de tentatives.

### Calcul

Échecs :

`Failed + Invalid user`

Total :

`Failed + Invalid user + Accepted`

Taux d'échec :

`Échecs / Total`

### Classification

| Taux d'échec | Niveau |
|---|---|
| ≤ 33,3 % | 🟢 Neutre |
| > 33,3 % et ≤ 66,7 % | 🟠 À surveiller |
| > 66,7 % | 🔴 Suspect |

## 📁 Structure du projet

```text
ssh-log-analyzer/
├── main.py
├── logs/
│   ├── demo.log
│   └── ...
├── README.md
└── ...

## 🚀 Futures mises à jour

Le projet est développé progressivement. Plusieurs évolutions sont prévues afin d'améliorer sa robustesse, ses fonctionnalités et sa facilité d'utilisation.

### 🔎 V9 — Parser SSH plus robuste
- Ne plus dépendre uniquement des positions fixes dans les lignes.
- Rechercher les informations à partir de mots-clés (`for`, `from`, `port`, etc.).
- Gérer des formats de logs SSH différents.
- Prendre en compte les messages du type `message repeated X times`.

### 📁 V10 — Export des résultats
- Export des analyses au format CSV.
- Export des analyses au format JSON.
- Conservation du niveau de suspicion et des statistiques par IP.

### 🖥️ V11 — Utilisation interactive
- Permettre à l'utilisateur de choisir le fichier à analyser.
- Vérifier que le fichier correspond à un format de logs SSH compatible.
- Gérer les erreurs de fichier et les fichiers invalides.

### 🌐 V12 — Compatibilité multi-systèmes
- Support de différents formats de logs SSH Linux.
- Support des logs OpenSSH sous Windows.
- Détection automatique du format du fichier.

> ℹ️ Cette roadmap est évolutive et pourra être modifiée au fur et à mesure du développement du projet.