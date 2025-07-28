from prettytable import PrettyTable

table = PrettyTable()

# table.field_names = ["Name", "Age"]
# table.add_rows(
#     [
#     ["Joshua", 29],
#     ["Alonge", 60],
#     ]
# )

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)


