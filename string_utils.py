

def split_by_capitals(formula):
    apperapper = []
    new_formula = []
    for i in range(len(formula)):
      if formula[i].isupper() == True:
        apperapper.append(i)
    print(apperapper)
    if apperapper:
      for i in range(len(apperapper) -1):
        print(i)
        new_word = formula[apperapper[i]:apperapper[i+1]]
        new_formula.append(new_word)
      last_word = formula[apperapper[len(apperapper) - 1]:]
      new_formula.append(last_word)
      print(new_formula)
    elif formula:
      new_formula.append(formula)
    return new_formula

def split_at_number(formula):
    num = []
    for i in range(len(formula)):
      if formula[i].isdigit() == True:
        num = formula[i:]
        letter = formula [0:i]
        num = int(num)
        return (letter, num)
    return (formula ,1)

def count_atoms_in_molecule(molecular_formula):
    dic = {}
    for atom in split_by_capitals(molecular_formula):
        atom_name, atom_count = split_at_number(atom)      
        dic [atom_name] = atom_count
    return dic




def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
