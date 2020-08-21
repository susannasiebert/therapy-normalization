"""A base class for normalizing therapy terms."""
from abc import ABC, abstractmethod
from collections import namedtuple

IDENTIFIER_PREFIXES = {
    'casRegistry': 'chemidplus',
    'pubchemCompound': 'pubchem.compound',
    'pubchemSubstance': 'pubchem.substance',
    'chembl': 'chembl.compound',
    'rxnorm': 'rxcui',
    'drugbank': 'drugbank'
}


class Base(ABC):
    """The normalizer base class."""

    def __init__(self, *args, **kwargs):
        """Initialize the normalizer."""
        self._data = None
        self._exact_index = dict()
        self._lower_index = dict()
        self._records = dict()
        self._load_data(*args, **kwargs)

    @abstractmethod
    def _load_data(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def normalize(self, term):
        """Normalize term to wikidata concept"""
        raise NotImplementedError

    NormalizerResponse = namedtuple(
        'NormalizerResponse',
        ['input_term', 'match_type', 'therapy_records']
    )