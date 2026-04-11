;-------------------------------------------------------------------------------
; Partie ajoutée automatiquement par makefile après génération pour la gestion
; de l’icone de systray
;-------------------------------------------------------------------------------

global mainIcon = A_ScriptDir . "\icon.ico"
global dullIcon = A_ScriptDir . "\dull_icon.ico"

; Définir une icône au systray
Menu, Tray, Icon, %A_ScriptDir%\icon.ico

; Fonction pour mettre à jour l’icône selon l’état réel
UpdateTrayIcon() {
    global mainIcon, dullIcon
    if (A_IsSuspended)
        Menu, Tray, Icon, %dullIcon%
    else
        Menu, Tray, Icon, %mainIcon%
}

; Au démarrage
UpdateTrayIcon()

; Timer toutes les 500ms pour détecter l’état
SetTimer, CheckSuspend, 500
return

CheckSuspend:
UpdateTrayIcon()
return
