# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("8:16 PM", "459:44", "tuesday"))


# Run unit tests automatically
main(module='test_module', exit=False)