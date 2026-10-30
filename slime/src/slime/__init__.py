from .environment import initial_lattice, build_base_lattice, show_lattice, filter_lattice
# __all__ = [
#     "environment"
# ]
def main() -> None:
    print("Hello from slime!")
    lattice = build_base_lattice()
    for _ in range(1, 30):
        show_lattice(lattice)
        lattice = filter_lattice(lattice)

