__author__: str = "730677548"


def main_planner(guests: int) -> None:
    """Main function to wrap every item needed for the party."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(round(cost(tea_bags(guests), treats(guests)), 1)))


def tea_bags(people: int) -> int:
    """Number of tea bags needed based on the number of guests."""
    return people * 2


def treats(people: int) -> int:
    """The number of treats based on the number of teas guests drink."""
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Cost of teas and treats."""
    return float((tea_count * 0.50) + (treat_count * 0.75))


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
