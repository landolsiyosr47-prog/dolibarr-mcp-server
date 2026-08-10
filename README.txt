# 🚀 Dolibarr MCP Server (Python)

Un serveur MCP (Model Context Protocol) complet pour **Dolibarr** en Python. Pilotez votre ERP Dolibarr directement depuis Claude, ChatGPT (via un client compatible MCP) et d’autres clients MCP.

> **31 outils** pour gérer les clients, factures, devis, commandes, produits, catégories, contacts, projets, SQL et analytics.

---

## 📚 Guide d’installation et d’exécution

### Prérequis

Avant de commencer, assurez-vous d’avoir :

- Python 3.10 ou plus récent (3.11 recommandé)
- XAMPP (Apache et MySQL)
- Une instance Dolibarr accessible
- L’API REST Dolibarr activée
- Une clé API Dolibarr
## 🚀 Installation

### Installer Python

#### Sur Windows

 Télécharger depuis le site officiel**
1. Allez sur [python.org](https://www.python.org)
2. Cliquez sur **"Downloads"** → **"Windows"**
3. Téléchargez **Python 3.11+** (ou version supérieure)
4. Lancez l'installateur
5. ✅ **Important** : Cochez **"Add Python to PATH"**
6. Cliquez sur **"Install Now"**
7. Vérifiez l'installation :
```cmd
python --version
pip --version

#### Sur Linux

**Ubuntu / Debian**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 --version
pip3 --version
```

**Fedora / CentOS**
```bash
sudo dnf install python3 python3-pip
python3 --version
pip3 --version
```

**Arch Linux**
```bash
sudo pacman -S python python-pip
python --version
pip --version
```

## Installer et préparer XAMPP (Windows)

1. Télécharger et installer XAMPP.
2. Ouvrir le **XAMPP Control Panel**.
3. Démarrer **Apache** et **MySQL**.
4. Vérifier qu'ils sont en état **Running**.
5. Ouvrir **http://localhost/phpmyadmin**.
6. Créer la base **dolibarr** si nécessaire et importer la base Dolibarr.
> Si Dolibarr est déjà installé, il suffit de démarrer Apache et MySQL.

### 1. Récupérer le projet localement

téléchargez simplement le dossier du projet depuis votre source de fichiers ou copiez-le dans un répertoire local.

Exemple de structure attendue :

```text
C:\chemin\vers\dolibarr-mcp-server
```

Puis ouvrez ce dossier dans votre terminal :

#### Windows

```powershell
cd C:\chemin\vers\dolibarr-mcp-server
```

#### Linux / macOS

```bash
cd /chemin/vers/dolibarr-mcp-server
```

### 2. Créer un environnement virtuel

#### Windows (PowerShell)

Créer l'environnement :

```powershell
py -3 -m venv .venv
```

Activer l'environnement :

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloque l'exécution :

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Le terminal doit afficher :

```text
(.venv) C:\chemin\vers\dolibarr-mcp-server>
```

#### Windows (CMD)

```cmd
.\.venv\Scripts\activate.bat
```

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer les variables d’environnement

Créez un fichier .env à la racine du projet :

```env
DOLIBARR_URL=https://votre-instance.dolibarr.com
DOLIBARR_KEY=VOTRE_CLE_API_SECRETE
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=password
DB_NAME=dolibarr
```

> Dans Dolibarr, activez l’API REST dans le module approprié, puis récupérez la clé API depuis votre profil utilisateur.

### Vérifier la configuration

Assurez-vous que les paramètres du fichier `.env` correspondent à votre installation.

> Avec XAMPP, le mot de passe de **root** est vide par défaut.

### Vérifier Dolibarr

- Vérifier que Dolibarr est accessible.
- Activer l'API REST.
- Générer une clé API.
- Compléter le fichier `.env`.

### 5. Lancer le serveur MCP

#### Windows

```powershell
py server.py
```

#### Linux / macOS

```bash
python3 server.py
```

Le serveur doit rester en cours d’exécution pendant que vous utilisez l’IA.

### Vérification

Si aucune erreur n'apparaît dans le terminal, le serveur MCP est prêt à recevoir les requêtes MCP.

---

## 🔌 Utilisation avec Claude Desktop

### Windows

Le fichier de configuration se trouve généralement ici :

```text
%APPDATA%\Claude\claude_desktop_config.json
```

Exemple :

```json
{
  "mcpServers": {
    "dolibarr": {
      "command": "C:\\chemin\\vers\\dolibarr-mcp-server\\.venv\\Scripts\\python.exe",
      "args": ["C:\\chemin\\vers\\dolibarr-mcp-server\\server.py"],
      "env": {
        "DOLIBARR_URL": "https://votre-instance.dolibarr.com",
        "DOLIBARR_KEY": "VOTRE_CLE_API_SECRETE"
      }
    }
  }
}
```

### Linux / macOS

Le fichier de configuration se trouve généralement ici :

- macOS : `~/Library/Application Support/Claude/claude_desktop_config.json`
- Linux : `~/.config/Claude/claude_desktop_config.json`

Exemple :

```json
{
  "mcpServers": {
    "dolibarr": {
      "command": "/chemin/vers/dolibarr-mcp-server/.venv/bin/python",
      "args": ["/chemin/vers/dolibarr-mcp-server/server.py"],
      "env": {
        "DOLIBARR_URL": "https://votre-instance.dolibarr.com",
        "DOLIBARR_KEY": "VOTRE_CLE_API_SECRETE"
      }
    }
  }
}
```

Après modification, redémarrez Claude Desktop.

## 💬 Exemples de prompts

Une fois le serveur connecté, vous pouvez demander à l’IA :

- “Liste les clients”
- “Crée un devis pour le client 1”
- “Ajoute une ligne au devis 10 avec le produit 1”
- “Montre les dernières factures”
- “Crée une commande pour le client 5”

---

## ✨ Fonctionnalités (31 outils)

### 🏢 Tiers (Clients / Fournisseurs)
- Lister tous les clients
- Créer un client
- Mettre à jour un client

### 👥 Contacts
- Lister tous les contacts
- Créer un contact
- Mettre à jour un contact

### 🏭 Produits & Services
- Lister les produits/services
- Créer un produit/service
- Mettre à jour un produit/service

### 📋 Projets
- Lister les projets
- Créer un projet

### 📄 Devis & Propositions Commerciales
- Lister les propositions commerciales
- Créer une proposition commerciale
- Ajouter une ligne de proposition
- Valider une proposition

### 📑 Facturation
- Lister les factures
- Créer une facture
- Ajouter une ligne de facture

### 🛒 Commandes
- Lister les commandes
- Créer une commande

### 🏷️ Catégories
- Lister les catégories
- Créer une catégorie

### 🗄️ SQL et Schéma
- Exécuter des requêtes SQL validées
- Charger le schéma Dolibarr depuis `schema/schema.json`

### 📊 Analytics
- Nombre total de clients
- Nombre total de factures
- Chiffre d'affaires total
- Meilleurs clients
- Dernières factures
- Derniers clients

## 📁 Structure du Projet

```
dolibarr-mcp-server/
├── server.py                 # Point d'entrée MCP
├── config.py                 # Configuration et variables d'environnement
├── dolibarr_client.py        # Client API REST Dolibarr
├── database.py               # Connexion et requêtes SQL
├── sql_guard.py              # Sécurité SQL
├── requirements.txt          # Dépendances Python
├── .env                      # Variables d'environnement (à créer)
├── tools/                    # Outils MCP
│   ├── __init__.py
│   ├── clients.py            # Gestion des clients
│   ├── proposals.py          # Gestion des devis
│   ├── invoices.py           # Gestion des factures
│   ├── orders.py             # Gestion des commandes
│   ├── products.py           # Gestion des produits
│   ├── categories.py         # Gestion des catégories
│   ├── contacts.py           # Gestion des contacts
│   ├── projects.py           # Gestion des projets
│   ├── sql.py                # Requêtes SQL personnalisées
│   ├── analytics.py          # Analytics et statistiques
│   └── ...
├── schema/                   # Schéma base de données
├── prompts/                  # Prompts système
└── test/                     # Tests
```

---

## 🔐 Sécurité

- **Ne committez jamais** votre clé API dans un dépôt Git.
- Utilisez un compte Dolibarr dédié avec les **permissions minimales** nécessaires.
- La clé API est transmise uniquement entre votre machine locale et l'instance Dolibarr.
- Les requêtes SQL sont validées avec `sql_guard.py`.

## 📦 Dépendances

- `fastmcp` - Framework MCP en Python
- `requests` - Client HTTP
- `mysql-connector-python` - Accès à la base Dolibarr
- `python-dotenv` - Gestion des variables d'environnement

