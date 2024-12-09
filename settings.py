"""Module for configuration settings."""
from dataclasses import dataclass


@dataclass(frozen=True)
class BaseSettings:
    """Settings common to both prod and dev runs."""


@dataclass(frozen=True)
class DevSettings(BaseSettings):
    """Developer settings"""

    ROOT = r'C:\Users\gianm\OneDrive\Desktop\PodatStock'
    RATES = ROOT + r'\NBP rates.xlsx'
    INPUTS = ROOT + r'\Files To Be Processed'


@dataclass(frozen=True)
class ProdSettings(BaseSettings):
    """Production settings"""

    ROOT = r''
    RATES = ROOT + r'\NBP rates.xlsx'
    INPUTS = ROOT + r'\Files To Be Processed'
