# scripts/download_data.py
import sys
from pathlib import Path

# Añadir raíz al sys.path para importar src
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.data.datamodule import MedDataModule

def main():
    print("Iniciando descarga y validación de MedMNIST (PneumoniaMNIST)...")
    dm = MedDataModule(flag="pneumoniamnist", batch_size=16, data_dir="data")
    dm.setup()

    loader = dm.train_dataloader()
    images, labels = next(iter(loader))

    print("\n--- Verificación de Tensores ---")
    print(f"Batch Shape: {images.shape}")   # Salida esperada: torch.Size([16, 1, 28, 28])
    print(f"Labels Shape: {labels.shape}")  # Salida esperada: torch.Size([16, 1])
    print(f"Rango de valores: min={images.min():.2f}, max={images.max():.2f}")
    print("Datos listos en el directorio local ./data/")

if __name__ == "__main__":
    main()