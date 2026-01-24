def dump2xyz(dump_file_path, xyz_file_path=None, atoms_dict = None):
    """Translate .dump file from LAMMPS in .xyz file. Return str path of new xyz file."""
    if xyz_file_path == None:
        xyz_file_path_core = dump_file_path.split(".")[0:-1:]
        if isinstance(xyz_file_path_core, str):
            xyz_file_path = xyz_file_path_core + ".xyz"
        else:
            xyz_file_path = ".".join(xyz_file_path_core) + ".xyz"
    with open(dump_file_path, "r") as dump:
        file = dump.readlines()
        atoms_num = file[3]

    new_data = []
    coords = 0
    new_data.append(atoms_num)
    new_data.append("Created with NCIL_program_package\n")
    if atoms_dict is None:
        for line in file:
            line_lst = line.split()
            len_line = len(line_lst)
            if len_line == 5:
                coords = 1
                atom_type = line_lst[1]
                coords_lst = [str(round(float(x), 5)).rjust(12) for x in line_lst[2::]]
                new_data.append("".join([atom_type, *coords_lst]) + "\n")      
            elif len_line != 5 and coords == 1:
                coords = 0
                new_data.append(atoms_num)
                new_data.append("Created with NCIL_program_package\n")
    else:
        for line in file:
            line_lst = line.split()
            len_line = len(line_lst)
            if len_line == 5:
                coords = 1
                atom_type = atoms_dict[line_lst[1]]
                coords_lst = [str(round(float(x), 5)).rjust(12) for x in line_lst[2::]]
                new_data.append("".join([atom_type, *coords_lst]) + "\n")      
            elif len_line != 5 and coords == 1:
                coords = 0
                new_data.append(atoms_num)
                new_data.append("Created with NCIL_program_package\n")

    with open(xyz_file_path, "w") as xyz:
        xyz.writelines(new_data)
    
    return xyz_file_path