from typing import List, Callable, Type, Optional, Dict

from pysaga.actionstep import ActionStep, LambdaActionStep


class SagaError(Exception):
    """
    Saga Error is the Exception type raised when an error occurres in one of the Saga's ActionSteps
    The SagaError contains the exception raised in the ActionStep and any raised exceptions in the compensations.
    """

    pass

