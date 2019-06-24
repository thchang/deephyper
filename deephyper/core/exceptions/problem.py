"""Exceptions related with problem definition.
"""

from deephyper.core.exceptions import DeephyperError


class SpaceDimNameMismatch(DeephyperError):
    """"Raised when 2 set of keys are not corresponding for a given Problem.
    """

    def __init__(self, ref, space):
        self.ref, self.space = ref, space

    def __str__(self):
        return f'Some reference\'s dimensions doesn\'t exist in this space: {filter(lambda k: k in self.space, self.ref.keys())}'


class SpaceNumDimMismatch(DeephyperError):
    """Raised when 2 set of keys doesn't have the same number of keys for a given
    Problem."""

    def __init__(self, ref, space):
        self.ref, self.space = ref, space

    def __str__(self):
        return f'The reference has {len(self.ref)} dimensions when the space has {len(self.space)}. Both should have the same number of dimensions.'


class SpaceDimNameOfWrongType(DeephyperError):
    """Raised when a dimension name of the space is not a string."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Dimension name: '{self.value}' is of type == {type(self.value)} when should be 'str'!"


class SpaceDimValueOfWrongType(DeephyperError):
    """Raised when a dimension value of the space is not a string."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Dimension value: '{self.value}' is of type == {type(self.value)} when should be either 'tuple' or 'list'!"


class SpaceDimValueNotInSpace(DeephyperError):
    """Raised when a dimension value of the space is in the coresponding dimension's space."""

    def __init__(self, value, name_dim, space_dim):
        self.value = value
        self.name_dim = name_dim
        self.space_dim = space_dim

    def __str__(self):
        return f"Dimension value: '{self.value}' is not in dim['{self.name_dim}':{self.space_dim}!"


class SearchSpaceBuilderIsNotCallable(DeephyperError):
    """Raised when a search space builder is not a callable."""

    def __init__(self, parameter):
        self.parameter = parameter

    def __str__(self):
        raise f"The search space builder {self.parameter} should be a callable when it is not!"


class SearchSpaceBuilderMissingParameter(DeephyperError):
    """Raised when a missing parameter is detected in a callable which creates a Structure.

        Args:
            missing_parameter (str): name of the missing parameter.
    """

    def __init__(self, missing_parameter):
        self.missing_parameter = missing_parameter

    def __str__(self):
        return f"The callable which creates a Structure is missing a '{self.missing_parameter}' parameter!"


class SearchSpaceBuilderMissingDefaultParameter(DeephyperError):
    """Raised when a parameter of a search space builder is missing a default value."""

    def __init__(self, parameter):
        self.parameter = parameter

    def __str__(self):
        return f"The parameter {self.parameter} must have a default value!"


class ProblemPreprocessingIsNotCallable(DeephyperError):
    """Raised when the preprocessing parameter is not callable."""

    def __init__(self, parameter):
        self.parameter = parameter

    def __str__(self):
        return f"The parameter {self.parameter} must be a callable."


class ProblemKindAlreadySet(DeephyperError):
    """Raised when the problem kind (regression|classification) has already been set and the user is trying to change it."""

    def __init__(self, problem):
        self.problem = problem

    def __str__(self):
        if self.problem.space['regression']:
            kind = 'regression'
        else:
            kind = 'classification'
        return f"The problem kind has already been set to: '{kind}', you cannot change it."


class ProblemLoadDataIsNotCallable(DeephyperError):
    """Raised when the load_data parameter is not callable."""

    def __init__(self, parameter):
        self.parameter = parameter

    def __str__(self):
        return f"The parameter {self.parameter} must be a callable."
