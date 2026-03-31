$name = "Andreas"
$surname = "Nyström"

Write-Host $name
Write-Host "String"
Write-Output $surname # Båda printar men "Write-Output" kan hanteras/skickas vidare

Write-Host "Mitt namn är $name"
Write-Host '$name'

# [int]$int = 24 # Typen bestäms av värdet, default är string
# [string]$string = "string"
# [double]$float = 24.6
# [bool]$bool = $true
# [array]$array = @(1, 2, 3, 4)
# [hashtable]$dictionary = @{key="value"; key2="value2"}


[array]$arr = @(1, 2, 3)
Write-Host $arr
[array]$arr += 4 #Kopierar förra arrayen och lägger till värdet ()
Write-Host $arr

# -eq = equals
# -ne = not equals
# -gt = greater than
# -ge = greater than or equal
# -lt = less than
# -le = less than or equal

if ("A" -eq "a") {
    Write-Host "True"
}

if ("111" -eq 111) {
    Write-Host "True"
}

if ("A" -ceq "a") {
    Write-Host "True"
}else {
    Write-Host "False"
}

if ("A" -eq "A" -or "B" -eq "B") {
   
}

if ("A" -eq "A" -and "B" -eq "B") {
    
}

if (-not "A") {
    
}


[bool]$a = $true

if ($a) {
    Write-Host "True"
}elseif ($false) {
    Write-Host "False"
}else {
    Write-Host "Else"
}


$age = 19
$result = ""

if ($age -gt 18) {
    $result = "Adult"
}else {
    $result = "Child"
}

Write-Host $result

$age = 19

$result = ($age -gt 18) ? "Adult" : "Child"

Write-Host $result

for ($i = 0; $i -le 5; $i++) {
    Write-Host $i
}
Write-Host " "

[array]$numbers = @(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

foreach ($num in $numbers) {
    Write-Host $num
}
Write-Host ""

[array]$numshort = @(1..10)

foreach ($x in $numshort) {
    Write-Host $x
}
Write-Host ""

foreach ($x in 1..10) {
    Write-Host $x -ForegroundColor Red
}

$counter = 0

while ($counter -lt 3) {
    Write-Host $counter
    $counter++
}

do {
    Write-Host ($counter++)
} while ($false)


do {
    Write-Host ($counter++)
} until ($counter -eq 10)


1..3 | ForEach-Object {Write-Host $_}


function Write-Hello {
    param(
        [Parameter(Mandatory=$true)]
        [string]$n
    )
    Write-Host "Hello, $n"
}

function Write-Hello-Alt ([string]$n1){
    Write-Host "Hello, $n1"    
}

Write-Hello 

Write-Hello-Alt Andreas