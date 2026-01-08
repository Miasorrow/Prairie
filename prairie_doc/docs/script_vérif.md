# Documentation vérification

Nous voulons vérifier que nous avons bien tout installer sur notre ordinateur à l'aide du script suivant : 

```ps1
$python = python --version 
$nodeversion =  (Get-Package -Name "Node.js").Version
$chrome = (Get-Package -Name "Google Chrome").Version
$calcul =  ((2+2))
Write-Host $python + $nodeversion + $chrome + "2+2 =" + $calcul
```

[Voici le lien vers l exo :](https://github.com/Miasorrow/Prairie/tree/e807e959c52df987a0c8c13a4b6bfd10373bd5c3/prairie_doc)

