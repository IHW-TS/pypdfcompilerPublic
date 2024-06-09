# PDFCompressor

PDFCompressor est une application simple pour compresser plusieurs fichiers PDF. L'outil utilise Ghostscript pour réaliser la compression des fichiers, permettant de réduire la taille des fichiers PDF sans perte de qualité significative. Une version améliorée avec une interface utilisateur optimisée est prévue pour une prochaine mise à jour.

## Fonctionnalités

- Sélection de plusieurs fichiers PDF pour la compression.
- Choix du niveau de compression : `screen`, `ebook`, `printer`, `prepress`, et `default`.
- Réinitialisation de la sélection des fichiers.
- Sauvegarde des fichiers compressés avec un nom et un emplacement spécifié par l'utilisateur.

## Utilisation

1. **Téléchargement et Exécution :**
   - Téléchargez l'application compilée depuis [les releases](https://github.com/IHW-TS/pypdfcompiler/releases).
   - Extrayez le contenu et exécutez `PDFCompressor.exe`.

2. **Sélection des fichiers :**
   - Cliquez sur le bouton "Select PDFs" pour choisir les fichiers PDF à compresser.

3. **Choix du niveau de compression :**
   - Sélectionnez le niveau de compression souhaité dans le menu déroulant.

4. **Compression et Sauvegarde :**
   - Cliquez sur "Compress" pour compresser les fichiers.
   - Choisissez l'emplacement de sauvegarde et le nom du fichier compressé.

5. **Réinitialisation de la sélection :**
   - Cliquez sur "Reset" pour effacer la sélection de fichiers.

## Dépendances

L'application utilise Ghostscript pour la compression des PDF. Ghostscript est inclus avec l'exécutable, donc aucune installation supplémentaire n'est nécessaire.

## Compilation

Si vous souhaitez compiler le projet par vous-même, suivez les instructions ci-dessous :

1. **Pré-requis :**
   - Installez [Python](https://www.python.org/downloads/).
   - Installez [PyInstaller](https://pyinstaller.org/).

   ```bash
   pip install pyinstaller
   ```
   
2.Téléchargement du projet

Clonez le dépôt GitHub :

```bash
git clone https://github.com/votre-utilisateur/PDFCompressor.git
cd PDFCompressor
```

3.Compilation :

Utilisez PyInstaller pour créer l'exécutable :

```bash
Copier le code
pyinstaller PDFCompressor.spec
```
L'exécutable sera généré dans le répertoire dist/PDFCompressor.

## Prochaines Versions

Je travaille actuellement sur une version 2 de PDFCompressor avec une interface utilisateur améliorée et plus intuitive. Restez à l'écoute pour les mises à jour !

## Contributions

Les contributions sont les bienvenues ! Si vous avez des suggestions ou des améliorations, n'hésitez pas à créer une issue ou à soumettre une pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
