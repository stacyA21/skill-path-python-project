"""Generate fake data for project, simulating a customer base of a hairdresser."""

import datetime
import random
from dataclasses import dataclass

import polars as pl
from faker import Faker
from faker.typing import SeedType

LOCALES = ["en"]  # Example to add German and Spanish names too: ["en", "de", "es"]

GENDERS: list[str] = ["M", "F", "X"]
HAIRSTYLES: list[tuple[str, int]] = [
    ("Afro", 47),
    ("Bald", 20),
    ("Braided", 42),
    ("Buzz", 50),
    ("Crew", 37),
    ("DipDyed", 35),
    ("Mohawk", 40),
    ("Pompadour", 38),
    ("Undercut", 45),
    ("Wavy", 33),
]


@dataclass
class CustomerSpecs:
    """Specifications for creating customer data.

    :param num_customers: Number of customers to create.
    :param min_age: Minimum age of a customer. Defaults to 12.
    :param max_age: Maximum age of a customer. Defaults to 80.
    :param prob_whitespace_in_name: Probability that a whitespace gets added in front or after a name. Defaults to 5%.
    """

    num_customers: int
    min_age: int = 12
    max_age: int = 80
    prob_whitespace_in_name: float = 0.05

    def __post_init__(self) -> None:
        """Post-process the dataclass input."""
        if self.min_age > self.max_age:
            raise ValueError(f"Minimum age {self.min_age} exceeds maximum age {self.max_age}.")


@dataclass
class OrderSpecs:
    """Specifications for creating order data.

    :param num_orders_per_day: Number of orders that come in per day. Defaults to 5.
    :param start_date: Date that the data starts at. Defaults to January 1, 2024.
    :param end_date: Date that the data ends at. Defaults to March 31, 2024.
    """

    num_orders_per_day: int = 5
    start_date: datetime.date = datetime.date(2024, 1, 1)
    end_date: datetime.date = datetime.date(2024, 3, 31)

    def __post_init__(self) -> None:
        """Post-process the dataclass input."""
        if self.start_date > self.end_date:
            raise ValueError(f"Start date {self.start_date} exceeds end data {self.end_date}.")


def create_customer_data(specs: CustomerSpecs, fake: Faker | None = None, seed: SeedType | None = None) -> pl.DataFrame:
    """Generate fake customer data.

    :param specs: Specifications to generate a customer.
    :param fake: Faker object. If not given, instantiate default Faker.
    :param seed: Random seed, if desired.
    :return: Data for the customer base, sorted by name.
    """
    fake = fake or Faker(locale=LOCALES)

    if seed:
        fake.seed_instance(seed)
        random.seed(seed)

    data_rows = []
    names_generated = set()

    for _ in range(specs.num_customers):
        gender = random.choice(GENDERS)
        age = random.randint(specs.min_age, specs.max_age)

        match gender:
            case "M":
                name = fake.first_name_male()
            case "F":
                name = fake.first_name_female()
            case _:
                name = fake.first_name_nonbinary()

        full_name = f"{name} {fake.last_name()}"
        if full_name in names_generated:
            continue  # Skip this person, their full name was already created
        names_generated.add(full_name)

        random_float = random.random()
        if random_float < specs.prob_whitespace_in_name:
            full_name = f"{full_name} "
        elif random_float < 2 * specs.prob_whitespace_in_name:
            # Because we use `elif` instead of `if`, we don't need to put `specs.prob_whitespace_in_name < random_float`
            full_name = f" {full_name}"

        data_rows.append({"name": full_name, "age": age, "gender": gender})

    df_customers = pl.from_dicts(data_rows)
    df_customers_deduped = df_customers.unique(subset=["name"])

    if len(df_customers_deduped) != len(df_customers):
        print("Duplicate names found despite specifying. Dropped duplicate names.")
    print(f"Final number of generated customers: {len(df_customers_deduped)}")

    return df_customers_deduped.sort(by=["name"])


def create_order_data(specs: OrderSpecs, customer_names: list[str], seed: SeedType | None = None) -> pl.DataFrame:
    """Create order data.

    :param specs: Specifications to generate a customer.
    :param customer_names: Names of customers that could make an order.
    :param seed: Random seed, if desired.
    :return: Data for the orders, sorted by date and name.
    """
    if len(customer_names) < specs.num_orders_per_day:
        raise ValueError(f"Need at least {specs.num_orders_per_day} customer names but got {len(customer_names)}")

    if seed:
        random.seed(seed)

    data_rows = []
    current_date = specs.start_date

    while current_date <= specs.end_date:
        new_rows = []
        not_chosen_names = customer_names.copy()
        for _ in range(specs.num_orders_per_day):
            hairstyle, costs = random.choice(HAIRSTYLES)
            order = {
                "name": (chosen_name := random.choice(not_chosen_names)),
                "date": current_date,
                "hairstyle": hairstyle,
                "costs": costs,
            }
            not_chosen_names.remove(chosen_name)
            new_rows.append(order)

        data_rows.extend(new_rows)
        current_date += datetime.timedelta(days=1)

    df_orders = pl.from_dicts(data_rows)
    df_orders_deduped = df_orders.unique(subset=["name", "date"])

    if len(df_orders_deduped) != len(df_orders):
        print(f"Duplicate name/date combinations found. Dropped duplicate rows. Final length: {len(df_orders_deduped)}")

    return df_orders_deduped.sort(by=["date", "name"])


def main(
    customer_specs: CustomerSpecs, order_specs: OrderSpecs, fake: Faker | None = None, seed: SeedType | None = None
) -> str:
    """Generate fake data.

    :param customer_specs: Specifications to generate a customer.
    :param order_specs: Specifications to generate an order.
    :param fake: Faker object. If not given, instantiate default Faker.
    :param seed: Random seed, if desired.
    :return: Data string, sorted by date and name. Rows are separated by a semicolon, elements are separated by a comma.
    """
    fake = fake or Faker(locale=LOCALES)

    if seed:
        Faker.seed(seed)
        random.seed(seed)

    df_customers = create_customer_data(specs=customer_specs, fake=fake, seed=seed)

    customer_names = pl.Series(df_customers.select("name")).to_list()
    df_orders = create_order_data(specs=order_specs, customer_names=customer_names, seed=seed)

    df_customers_orders = df_orders.join(df_customers, how="left", on=["name"])
    df_customers_orders = df_customers_orders.sort(by=["date", "name"])

    data_rows: list[str | int] = []

    for row in df_customers_orders.iter_rows(named=True):
        date = row["date"].strftime("%A %d %B %Y")
        data_rows.append(f"{row['name']},{row['age']},{row['gender']},{date},{row['hairstyle']},{row['costs']}")

    return ";".join(data_rows)


if __name__ == "__main__":
    random_seed = "98838658"
    customer_specs = CustomerSpecs(num_customers=10, min_age=12, max_age=80)
    df_customers = create_customer_data(fake=Faker(), specs=customer_specs, seed=random_seed)
    print(df_customers)

    customer_names = pl.Series(df_customers.select("name")).to_list()
    order_specs = OrderSpecs()
    df_orders = create_order_data(specs=order_specs, customer_names=customer_names, seed=random_seed)
    print(df_orders)

    data_string = main(fake=Faker(), customer_specs=customer_specs, order_specs=order_specs, seed=random_seed)
    print(data_string)
