# Documentation en ligne !

## I. Ecrire la doc
Pour le second exercice, nous devions écrire une documentation de toute la prairie.

La documentation nous permet de présenter le travail en cours.

## II. Mise en ligne

La deuxième étape, la mise en ligne
J'ai donc utilisé github pour mettre en ligne sur un site statique ma documetation

1. J'ai créé un github workflow sur git c'est un script qui s'execute pour créer une environnement virtuel avec toutes les dépendances nécessaire pour la mise en ligne. Voici le script


```py
name: ci 
on:
  push:
    branches:
      - main
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Configure Git Credentials
        run: |
          git config user.name github-actions[bot]
          git config user.email 41898282+github-actions[bot]@users.noreply.github.com
      - uses: actions/setup-python@v5
        with:
          python-version: 3.x
      - run: echo "cache_id=$(date --utc '+%V')" >> $GITHUB_ENV 
      - uses: actions/cache@v4
        with:
          key: mkdocs-material-${{ env.cache_id }}
          path: ~/.cache 
          restore-keys: |
            mkdocs-material-
      - run: pip install mkdocs
      - run: cd prairie_doc
      - run: mkdocs gh-deploy --force -f prairie_doc/mkdocs.yml
      #prout grkgifgkfiqgeq
```
Après j'ai configurer ma gh-pages, puis avec la ligne de commande : 

```bash
mkdocs gh-deploy
```
J'ai pu déployé le site et le rendre disponible




