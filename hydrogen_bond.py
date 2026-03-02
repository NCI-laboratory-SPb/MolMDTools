import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Hydrogen_Bond:
    """Class Hydrogen_Bond.
    
    Parameters:
    atoms : list
    List of objects Atom: [Atom-donor, Atom-Hydrogen, Atom-Axceptor]. Sequence is important for calculation coolvar.
    Warning!!! Numeration starts from 0: if number of atom in chemcraft = 20, you should input 19.
    """

    def __init__(self, atoms):
        self.__atoms = atoms
    
    @property
    def atoms(self):
        """Return list of atoms"""
        return self.__atoms

    @property
    def colvar1(self):
        """Return float colvar (dist2-dist1)/2"""
        atoms = self.atoms
        hydrogen = atoms[1]
        donor = atoms[0]
        axceptor = atoms[2]
        colvar1 = (hydrogen.distance(donor)-hydrogen.distance(axceptor))/2
        return colvar1
    
    @property
    def colvar2(self):
        """Return float colvar (dist2+dist1)/2"""
        atoms = self.atoms
        hydrogen = atoms[1]
        donor = atoms[0]
        axceptor = atoms[2]
        colvar2 = (hydrogen.distance(donor)+hydrogen.distance(axceptor))/2
        return colvar2
    

class Hydrogen_Bonds:
    """Class Hydrogen_Bonds.
    
    Parameters:
    h_bonds : list
    List of objects Hydrogen_Bond.
    """

    def __init__(self, h_bonds):
        self.__h_bonds = h_bonds

    @property
    def h_bonds(self):
        """Return list of objs Hydrogen_Bond"""
        return self.__h_bonds

    @property
    def colvars1_list(self):
        """Return obj Colvars_Lists of list of colvar one"""
        colvars1_list = []
        h_bonds = self.h_bonds
        for h_bond in h_bonds:
            colvars1_list.append(h_bond.colvar1)
        return Colvars_Lists(colvars1_list)


class Colvars_Lists:
    """Class Colvars.
    
    Parameters:
    colvars_lsts : np.array
    Array, when row - list of colvar.
    """

    def __init__(self, colvars_lsts):
        self.__colvars_lsts  = colvars_lsts
    
    @property
    def colvars_lsts(self):
        return self.__colvars_lsts
    
    @property
    def dispersion(self):
        """Make list of collective variables disperdions. Return list of floats"""
        dispersions = []
        colvars_lsts = self.colvars_lsts
        for i in range(len(colvars_lsts)):
            disp_val_i = float(np.var(colvars_lsts[i]))
            dispersions.append(disp_val_i)
        return dispersions

    def colvar_transform(self, translation_matrix):
        """Translation_matrix - np.arrey. Translate colvars and retrun new np.arrey of colvars"""
        new_lst = ((self.colvars_lsts.T)@translation_matrix).T
        return Colvars_Lists(new_lst)
    
    def colvars_plot(self):
        """Draw graphs of density of distribution of colvars"""
        colors = ["black", "red", "blue", "green"]
        plt.figure(figsize=(10, 6))

        clvs = self.colvars_lsts
        
        if type(clvs[0]) != list:
            sns.kdeplot(clvs, color='black')
        
        else:
            for ind, clv in enumerate(clvs):
                sns.kdeplot(clv, color=colors[ind%4])
        
        plt.show()
