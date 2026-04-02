import subprocess

images = [
    "./logo-azerty-arab_16.png",
    "./logo-azerty-arab_256.png",
    "./logo-azerty-arab_32.png",
    "./logo-azerty-arab_48.png",
]

output = "icon.ico"

cmd = ["convert"] + images + [output]

subprocess.run(cmd, check=True)

print("ICO créé avec succès !")
