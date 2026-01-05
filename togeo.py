def convert_to_pdb(input_data):
    structures = input_data.strip().split("\n\n")
    output_data = ""
    struct_num = 1
    for i, structure in enumerate(structures, start=1):
        lines = structure.split('\n')
        desc_line = lines[0]
        energy_line = lines[1]
        atom_lines = lines[2:]
        #struct_num = i
        energy = energy_line.split(",")[1].strip()
        pdb_description = f"BIOGRF 200\nDESCRP co0001_{struct_num}\nRUTYPE SINGLE POINT\nFORMAT ATOM   (a6,1x,i5,1x,a5,1x,a3,1x,a1,1x,a5,3f10.5,1x,a5,i3,i2,1x,f8.5)\n"
        struct_num+=1
        pdb_atoms = ""
        atom_num = 1
        for atom_line in atom_lines:
            parts = atom_line.split()
            atom_type = parts[0]
            x = parts[1]
            y = parts[2]
            z = parts[3]
            pdb_atoms += f"HETATM     {atom_num} {atom_type}         {x}    {y}    {z}   {atom_type}     1 0  0.00000\n"
            atom_num+=1
        pdb_conect = "FORMAT CONECT (a6,12i6)\n"
        pdb_energy = f"END \n"
        output_data += pdb_description + pdb_atoms + pdb_conect + pdb_energy
    return output_data
if __name__ == '__main__':
    input_data = ()
    pdb_output = convert_to_pdb(input_data)
    print(pdb_output)
