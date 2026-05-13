import numpy as np

class Molecule:
    """Class Molecule.
    
    Parameters:
    atoms : list
    """

    def __init__(self, atoms, cell=None):
        self.__atoms = atoms
        self.__cell = cell

    @property
    def atoms_num(self):
        return len(self.__atoms)

    @property
    def atoms(self):
        return self.__atoms

    @property
    def cell(self):
        return self.__cell
    
    @cell.setter
    def cell(self, cell):
        if type(cell) == list and len(cell) == 3 and all(type(x) in [int, float] for x in cell):
            self.__cell = cell

    @property
    def center_of_mass(self):
        """Return tuple of 3 floats - coords of center of mass of molecule"""
        mass_sum = 0
        x_sum = 0
        y_sum = 0
        z_sum = 0

        for atom in self.__atoms:
            atom_coords = atom.coords
            mass_sum += atom.mass
            x_sum += atom.mass * atom_coords[0]
            y_sum += atom.mass * atom_coords[1]
            z_sum += atom.mass * atom_coords[2]

        return (x_sum / mass_sum, y_sum / mass_sum, z_sum / mass_sum)
    

class Dist_Matrix:
    """Class Dist_Matrix

    Parameters:
    dist_matrix : np_array(dists(obj Atom[i] of obj Molecule, obj Atom[j] of obj Molecule))
    """

    def __init__(self, molecule):

        dists = []
        atoms = molecule.atoms
        n = molecule.atoms_num

        for i, atom in enumerate(atoms):
            dists_from_i_atom = []
            for j in range(0, i):
                dists_from_i_atom.append(atom.distance(atoms[j]))
            dists_from_i_atom.append(0)
            dists.append(dists_from_i_atom)
        
        for i in range(0, n):
            for j in range(i+1, n):
                dists[i].append(dists[j][i])

        self.__dist_matrix = np.array(dists)
        
    @property
    def dist_matrix(self):
        return self.__dist_matrix