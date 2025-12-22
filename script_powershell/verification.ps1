$python = python --version 
$nodeversion =  (Get-Package -Name "Node.js").Version
$chrome = (Get-Package -Name "Google Chrome").Version
$calcul =  ((2+2))
Write-Host $python + $nodeversion + $chrome + "2+2 =" + $calcul