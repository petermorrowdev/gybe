"""Gybe transpiler validation errors."""


class InvalidOutputError(Exception):
    """Raised when a transpiler returns an invalid type."""

    def __init__(self):
        """Raise generic validation error message."""
        return super().__init__('Must be a list of gybe.types.K8sResource')
