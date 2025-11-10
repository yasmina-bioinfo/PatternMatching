@echo off
echo ===================================================
echo 🔄 Synchronisation automatique avec GitHub...
echo ===================================================

REM Étape 1 : Ajouter tous les fichiers modifiés
git add .

REM Étape 2 : Créer un commit avec date et heure
git commit -m "Auto-update %date% %time%"

REM Étape 3 : Envoyer les changements vers GitHub
git push

echo ✅ Synchronisation terminée avec succès !
pause
