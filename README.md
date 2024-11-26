# 📝 Énoncé : Générateur de mots de passe avec interface graphique

Dans cet exercice, tu vas créer une application Python avec une interface graphique pour générer des mots de passe sécurisés. L'objectif est d'utiliser la bibliothèque **Tkinter** pour créer une interface utilisateur intuitive.

---

## 🎯 Objectif
Créer une application graphique qui permet de :
- Choisir la **longueur** du mot de passe à générer.
- Inclure ou non des **chiffres** dans le mot de passe.
- Inclure ou non des **caractères spéciaux** dans le mot de passe.
- Afficher le mot de passe généré directement dans l'interface.

---

## 🚀 Fonctionnalités à implémenter

### 1️⃣ Entrée pour la longueur du mot de passe
- L'utilisateur doit pouvoir entrer un nombre entier correspondant à la longueur souhaitée du mot de passe.

### 2️⃣ Options supplémentaires
- **Utilisation de chiffres** :
  - Ajouter une case à cocher qui permet d'inclure des chiffres dans le mot de passe.
- **Utilisation de caractères spéciaux** :
  - Ajouter une case à cocher qui permet d'inclure des caractères spéciaux (`!@#$%^&*`, etc.).

### 3️⃣ Génération du mot de passe
- Le programme doit générer un mot de passe aléatoire avec les options choisies (chiffres, caractères spéciaux) en utilisant la bibliothèque **random**.
- Afficher le mot de passe généré directement dans l'interface graphique.

---

## 💡 Conseils
1. **Organisation de l'interface** :
   - Utilise des widgets Tkinter comme `Entry`, `Checkbutton`, `Label`, et `Button`.
   - Place les éléments dans un cadre (`Frame`) avec une mise en page claire.

2. **Bibliothèques utiles** :
   - `random` pour choisir des caractères aléatoires.
   - `string` pour accéder aux lettres (`ascii_letters`), chiffres (`digits`) et caractères spéciaux (`punctuation`).

3. **Validation des entrées utilisateur** :
   - Vérifie que la longueur saisie est bien un nombre entier positif avant de générer le mot de passe.

---

## 🔍 Exemple de fonctionnement

Voici à quoi devrait ressembler ton application :

1. L'utilisateur entre la longueur souhaitée, coche ou décoche les options **chiffres** et **caractères spéciaux**.
2. Lorsqu'il clique sur "Générer", un mot de passe aléatoire est affiché.

---

### Interface utilisateur (Exemple) :

```plaintext
[ Longueur du mot de passe : [_________] ]

[ ] Utiliser des chiffres  
[ ] Utiliser des caractères spéciaux  

[   Générer   ]

Mot de passe généré : a7B!cDe4$
