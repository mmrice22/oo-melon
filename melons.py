"""Classes for melon orders."""
class AbstractMelonOrder:
    def __init__(self, species, qty, tax, order_type):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax
        self.order_type = order_type

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == "christmas":
            base_price *= 1.5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    def __init__(self, species, qty):
        super().__init__(species, qty, .08, "domestic")
    """Initialize melon order attributes."""
        

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, 0.17, "international")
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        return super().get_total() + 3

class GovernmentMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, 0, "government")
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed

order0 = GovernmentMelonOrder("watermelon", 6)
order1 = DomesticMelonOrder("watermelon", 6)
print(order0.get_total())
print(order1.get_total())