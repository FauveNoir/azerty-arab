import subprocess
from PIL import Image, ImageEnhance
import re
from pathlib import Path

# Répertoire du script
script_dir = Path(__file__).parent


def dullifiy(input_image=None):

    # Charger l'image
    print(input_image.__str__())
    img = Image.open(input_image.__str__())

    # Ajuster la luminosité (100 = normal)
    enhancer_brightness = ImageEnhance.Brightness(img)
    img = enhancer_brightness.enhance(1.0)

    # Ajuster la saturation (50% → 0.5)
    enhancer_color = ImageEnhance.Color(img)
    img = enhancer_color.enhance(0.5)

    # Nouveau nom
    new_filename = re.sub(r"(.*)(\.png)$", r"\1_DULL\2", input_image.__str__())

    # Sauvegarder
    img.save(new_filename)

    # retour du nouveau nom
    return new_filename

images = [
    script_dir / "logo-azerty-arab_16.png",
    script_dir / "logo-azerty-arab_256.png",
    script_dir / "logo-azerty-arab_32.png",
    script_dir / "logo-azerty-arab_48.png",
]

dull_images = []

for an_Image in images:
    dull_images.append( dullifiy(an_Image))

main_output = script_dir / "icon.ico"
dull_output = script_dir / "dull_icon.ico"

create_main_icon = ["convert"] + images + [main_output]
create_dull_icon = ["convert"] + dull_images + [dull_output]

subprocess.run(create_main_icon, check=True)
subprocess.run(create_dull_icon, check=True)

print("ICO créé avec succès !")
