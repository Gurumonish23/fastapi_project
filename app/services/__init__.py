# Import all service functions to make them available for use in the application
from .example_service import (
    get_examples,
    create_example,
    get_example_by_id,
    update_example,
    delete_example
)

# This file serves as a package initializer for the services module
# It allows for easy import of all service functions from this module
# Example usage:
# from app.services import get_examples, create_example