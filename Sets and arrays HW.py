
def find_symmetric_difference(set1, set2, label):
    
    sym_diff = set1.symmetric_difference(set2)
    print(f"{label}. Symmetric Difference: {sym_diff}")


set1_a = {'blue', 'green'}
set2_a = {'blue', 'yellow'}
find_symmetric_difference(set1_a, set2_a, "A")


set1_b = {1, 2, 3, 4, 5}
set2_b = {1, 5, 6, 7, 8, 9}
find_symmetric_difference(set1_b, set2_b, "B")

