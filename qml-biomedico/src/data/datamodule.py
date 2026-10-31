# src/data/datamodule.py
from pathlib import Path
import torch
from torch.utils.data import DataLoader
from torchvision import transforms
import medmnist
from medmnist import INFO


class MedDataModule:
    """Gestiona la descarga, transformación y DataLoaders de MedMNIST."""

    def __init__(
        self,
        flag: str = "pneumoniamnist",
        batch_size: int = 32,
        data_dir: str = "data",
        num_workers: int = 2
    ):
        self.flag = flag.lower()
        self.batch_size = batch_size
        self.data_dir = Path(data_dir)
        self.num_workers = num_workers

        # Obtener metadatos y clase del sub-dataset
        if self.flag not in INFO:
            raise ValueError(f"Flag '{self.flag}' no válida. Opciones: {list(INFO.keys())}")
            
        self.info = INFO[self.flag]
        self.DataClass = getattr(medmnist, self.info["python_class"])

        # Pipeline de transformaciones: Imagen PIL -> Tensor -> Escalado
        self.transform = transforms.Compose([
            transforms.ToTensor(),
            # Normaliza a media 0.5 y std 0.5 -> rango [-1, 1]
            transforms.Normalize(mean=[0.5], std=[0.5])
        ])

    def setup(self):
        """Descarga los datos si no existen en local e inicializa los splits."""
        self.data_dir.mkdir(parents=True, exist_ok=True)

        self.train_dataset = self.DataClass(
            split="train",
            transform=self.transform,
            download=True,
            root=str(self.data_dir)
        )
        self.val_dataset = self.DataClass(
            split="val",
            transform=self.transform,
            download=True,
            root=str(self.data_dir)
        )
        self.test_dataset = self.DataClass(
            split="test",
            transform=self.transform,
            download=True,
            root=str(self.data_dir)
        )

    def train_dataloader(self) -> DataLoader:
        return DataLoader(
            self.train_dataset,
            batch_size=self.batch_size,
            shuffle=True,
            num_workers=self.num_workers
        )

    def val_dataloader(self) -> DataLoader:
        return DataLoader(
            self.val_dataset,
            batch_size=self.batch_size,
            shuffle=False,
            num_workers=self.num_workers
        )

    def test_dataloader(self) -> DataLoader:
        return DataLoader(
            self.test_dataset,
            batch_size=self.batch_size,
            shuffle=False,
            num_workers=self.num_workers
        )