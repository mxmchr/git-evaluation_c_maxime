# README.md

## Table des matières
- [Installation](#installation)
- [Exécution](#exécution)
- [Réponses aux questions](#réponses-aux-questions)
- [Structure du dépôt](#structure-du-dépôt)

## Installation
1. Assurez-vous d'avoir Python 3 installé sur votre système. Si ce n'est pas le cas, vous pouvez le télécharger et l'installer depuis [le site officiel de Python](https://www.python.org/).
   Vous pouvez aussi l'installer sous linux :

   ```sh
    sudo apt update
    sudo apt install python3

   ```

3. Clonez ce dépôt vers votre machine locale en utilisant la commande suivante :

    ```sh
    git clone https://github.com/mxmchr/git-evaluation_c_maxime.git
    ```

4. Accédez au répertoire de votre projet :

    ```sh
    cd git-evaluation_c_maxime
    ```

## Exécution
Vous pouvez ensuite lancer le programe de cette manière :

```sh
python3 minitrice.py
```

ou encore :

```sh
python3 generator.py <num> | python3 minitrice.py
```

## Réponses aux questions
Les réponses aux questions adressées sur git :

1. **Git est un gestionnaire de version décentralisé. Qu’est ce que cela signifie ? Quel est le rôle joué par un dépôt central sur GitHub ou GitLab dans ce cas ? Justifier.**
   - Un gestionnaire de version décentralisé signifie que chaque utilisateur a une copie complète de l'historique du dépôt. Un dépôt central sur GitHub ou GitLab sert de dépot central pour les utilisateus afin de synchroniser leurs travaux et faciliter la collaboration.

2. **À quoi sert la commande `git fetch -p` ?**
   - La commande `git fetch -p` sert à récupérer les changements depuis le dépôt distant et à supprimer les branches distantes qui ont été supprimées.

3. **Dans quelles conditions est-ce qu’un conflit apparaît avec git ?**
   - Un conflit apparaît lorsque deux modifications incompatibles sont apportées à la même partie d'un fichier dans deux branches différentes.

4. **Lorsque vous résolvez un conflit, quelle est la dernière commande git que vous devez exécuter ?**
   - La dernière commande à exécuter est `git commit` pour enregistrer les résolutions de conflit.

5. **Depuis GitHub, après avoir accepté une contribution sur la branche principale, que devez vous faire pour mettre à jour votre branche principale localement ?**
   - Vous devez exécuter `git pull` pour mettre à jour votre branche principale localement.

6. **Quelle est la différence entre les commandes `git reset --soft` et `git reset --hard` ? Donner un cas d’usage pratique et courant pour chacune de ces commandes.**
   - `git reset --soft` déplace le HEAD à un commit spécifique sans modifier l'index ni l'arborescence de travail, utile pour modifier le message d'un commit.
   - `git reset --hard` réinitialise l'index et l'arborescence de travail au commit spécifié, supprimant les modifications locales, utile pour abandonner des modifications locales indésirables.

7. **Voici le log d’un dépôt git :**
9f64652 - (HEAD -> main) 3 (il y a 2 secondes) <p. schuhmacher>
68cd016 - 2 (il y a 18 secondes) <p. schuhmacher>
d47267f - 1 (il y a 43 secondes) <p. schuhmacher>

**Quelle est la (ou les) commande à exécuter pour transformer les commits 9f64652 et 68cd016 en un seul commit avec un nouveau message ?**
- La commande à exécuter est `git rebase -i HEAD~2` et changer `pick` en `squash` pour le deuxième commit, puis modifier le message lors de l'édition.

8. **Pourquoi est-il déconseillé de rebase une branche publique (branche sur laquelle travaille aussi d’autres personnes) ?**
- Il est déconseillé de rebase une branche publique car cela réécrit l'historique des commits, ce qui peut causer des problèmes de synchronisation et des conflits pour les autres contributeurs.

## Structure du dépôt

- **good-expression.txt**: Fichier texte contenant des expressions.
- **minitrice.py**: Fichier script de calcul.
- **generator.py**: Fichier script de calcul.
- **README.md**: Fichier Markdown que vous lisez actuellement, contenant des instructions et des informations sur le projet.
- **results**: Répertoire où sont stockés les résultats des calculs.
- **test**: Répertoire contenant les fichiers de test pour votre application.

