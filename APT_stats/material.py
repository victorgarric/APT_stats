from mendeleev import element as elem


class glob_element:
    """
    For material class internal usage only
    Stocks the name, mass, abundance and inner abundance of a given atom
    """

    def __init__(self, name, mass, rate, score=1.):
        self.name = name + str(mass)
        self.mass = mass
        self.rate = rate
        self.score = score


class material:
    """
    material class object

    Material is defined by elements and their composition
    """

    def __init__(self, elements, wt=True, impurity=None):
        """

        :param elements: a dictionary of elements and composition
        :param wt: a boolean. True for weight percent, False for atomic
        :param impurity: a list of impurities to be declared if need be
        """
        self.elements = []
        if wt == True:
            total_n = 0
            for element in elements:
                total_n += elements[element] / elem(element).mass
            for element in elements:
                elements[element] = elements[element] / elem(element).mass / total_n
        for system in elements:
            for isotope in elem(system).isotopes:
                if type(isotope.abundance) in (float, int):
                    self.elements.append(
                        glob_element(name=elem(system).symbol, mass=isotope.mass_number, rate=isotope.abundance,
                                     score=elements[system]))

        if impurity is not None:
            for system in impurity:
                for isotope in elem(system).isotopes:
                    if type(isotope.abundance) in (float, int):
                        self.elements.append(
                            glob_element(name=elem(system).symbol, mass=isotope.mass_number, rate=isotope.abundance,
                                         score=1E20))
