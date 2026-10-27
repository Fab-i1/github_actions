from pathlib import Path

# Chemin du dossier courant
current_dir = Path.cwd()
print(f"Contenu du dossier : {current_dir}\n")

# Parcourir les éléments
for path in sorted(current_dir.iterdir()):
    type_item = "DOSSIER" if path.is_dir() else "FICHIER"
    print(f"[{type_item}] {path.name}")