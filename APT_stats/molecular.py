# All objects in this file are not meant to be directly manipulated by the user

class molecular:
    """
    molecular class object
    molecular stocks information about atom contents inside and is capable of comparing two objects by their mass
    """

    def __init__(self, name, molecule, charge=0):
        self.name = name
        self.elements = []
        self.mass = molecule['mass']
        self.probability = molecule['probability']
        self.charge = charge
        for atom in molecule['elements']:
            self.elements.append(atom)

    def __eq__(self, other):
        return self.mass == other.mass

    def __ne__(self, other):
        return self.mass != other.mass

    def __gt__(self, other):
        return self.mass > other.mass

    def __ge__(self, other):
        return self.mass >= other.mass

    def __lt__(self, other):
        return self.mass < other.mass

    def __le__(self, other):
        return self.mass <= other.mass

    def get_charge(self, n0, n1):
        res = []
        for item in list(range(n0, n1 + 1)):
            res.append(item)
        return res


class mol_container:
    """
    mol_container class object
    objective of the container is too gather all molecules and refuse an instance in cas of redundancy
    """

    def __init__(self):
        self.molecules = []
        self.names = []
        self.dict = {}

    def add_molecule(self, molecule):
        if molecule.name in self.names:
            pass
        else:
            self.molecules.append(molecule)
            self.names.append(molecule.name)
            self.dict[molecule.name] = molecule

    def sort(self):
        self.molecules.sort()


class ion_container:
    """
    ion_container class object
    object to contain molecules with charges
    """

    def __init__(self):
        self.dict = {}
        self.molecules = []

    def add_molecule(self, molecule):
        self.molecules.append(molecule)

    def sort(self):
        self.molecules.sort()
