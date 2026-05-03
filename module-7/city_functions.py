"""Functions for formatting city and country names."""


def city_country(city, country, population=None, language=None):
    """Return a city and country, optionally including population and language."""
    formatted_city = f"{city.title()}, {country.title()}"

    if population:
        formatted_city += f" - population {population}"

    if language:
        formatted_city += f", {language.title()}"

    return formatted_city


if __name__ == "__main__":
    print(city_country("santiago", "chile"))
    print(city_country("tokyo", "japan", 37400068))
    print(city_country("madrid", "spain", 3223000, "spanish"))
