$paths = @("HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*")    # Registry sökvägar

foreach ($path in $paths){     # Loopar över och går in i varje sökväg

    foreach ($entry in $path){     # Loopar över och sparar det objektet som ska vara Google Chrome, resten av objekten ignoreras
    $e = Get-ItemProperty $entry | Where-Object {$_.DisplayName -like "*Google Chrome*"}
    }

    if ($e.DisplayName -like "*Google Chrome*") {     # Om det sparade objektet är Chrome (genom att kolla namnet), meddelas att det är installerat och var det söktes efter
    Write-Host "Chrome is installed, searched in ($path)"
    }
    else {
    Write-Host "Chrome is not installed, searched in ($path)"
    }
}



