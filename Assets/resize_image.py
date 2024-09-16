from PIL import Image
import os

# Liste des dossiers source
source_folders = [
    "/Users/raphaelrossi/Desktop/RR Website/Assets/Extraverted paintings", 
    "/Users/raphaelrossi/Desktop/RR Website/Assets/La capitale vol.II",
    "/Users/raphaelrossi/Desktop/RR Website/Assets/La capitales Tomes 1 et 2"
    "/Users/raphaelrossi/Desktop/RR Website/Assets/Madame Bovary"
    "/Users/raphaelrossi/Desktop/RR Website/Assets/Quartier Latin"
    "/Users/raphaelrossi/Desktop/RR Website/Assets/Vingtième prix de la fondation Ricard"
    "/Users/raphaelrossi/Desktop/RR Website/Assets/Watch to earn"
   "/Users/raphaelrossi/Desktop/RR Website/Assets/Which drinking buddy are you"



]  # Ajoute ici autant de dossiers que nécessaire

# Dossier parent de destination (racine)
output_parent_folder = "/Users/raphaelrossi/Desktop/Resized_Images"  # Dossier racine où les images redimensionnées seront sauvegardées

# Dimensions souhaitées
new_width = 1400  # Largeur souhaitée
new_height = 788  # Hauteur souhaitée

# Créer le dossier parent de sortie s'il n'existe pas
if not os.path.exists(output_parent_folder):
    os.makedirs(output_parent_folder)

# Redimensionner et rogner les images de chaque dossier source
for source_folder in source_folders:
    # Nom du dossier de sortie correspondant au dossier source
    output_folder = os.path.join(output_parent_folder, os.path.basename(source_folder))

    # Créer le dossier de sortie correspondant s'il n'existe pas
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Traiter les images dans chaque dossier source
    for filename in os.listdir(source_folder):
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):  # Filtre les fichiers image
            img_path = os.path.join(source_folder, filename)
            with Image.open(img_path) as img:
                # Obtenir les dimensions actuelles de l'image
                img_ratio = img.width / img.height
                new_ratio = new_width / new_height

                # Redimensionner tout en gardant le ratio
                if img_ratio > new_ratio:
                    # L'image est plus large que le ratio souhaité, on redimensionne selon la hauteur
                    img = img.resize((int(new_height * img_ratio), new_height), Image.ANTIALIAS)
                else:
                    # L'image est plus haute que le ratio souhaité, on redimensionne selon la largeur
                    img = img.resize((new_width, int(new_width / img_ratio)), Image.ANTIALIAS)

                # Rogner l'image pour obtenir les dimensions exactes
                left = (img.width - new_width) / 2
                top = (img.height - new_height) / 2
                right = (img.width + new_width) / 2
                bottom = (img.height + new_height) / 2

                img_cropped = img.crop((left, top, right, bottom))

                # Sauvegarder l'image redimensionnée et rognée dans le dossier de sortie correspondant
                output_path = os.path.join(output_folder, filename)
                img_cropped.save(output_path)
                print(f"Image {filename} redimensionnée et sauvegardée à {output_path}")

print("Toutes les images de tous les dossiers ont été redimensionnées et rognées.")
