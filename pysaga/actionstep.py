from abc import ABC, abstractmethod 
from typing import Callable, Dict


class ActionStep(ABC):
    """
    The ActionStep is the class that represents a step in the Saga.
    A step contains two  methods, action and compensate.
    The action method includes the the logic action of the step and the compensate method includes
    the compensation logic in case of failure.
    """

    def __init__(self, **action_step_kwargs):
        """
        :param action_step_kwargs: Additional arguments passed to the action.
        the arguments are saved as part of the ActionStep metadata.
        """
        self._action_step_kwargs = action_step_kwargs
    
    @property
    @abstractmethod
    def _action(self) -> Callable[..., Dict[any, any]]:
        """
        :return: The function of the act of the stage.
        """
        pass

    @property
    @abstractmethod
    def _compensation(self) -> Callable[..., bool]:
        """
        :return: The function of the compensate of the stage.
        """
        pass

    def act(self, **action_kwargs) -> Dict[any, any]:
        """
        Execute the action of the ActionStep.
        :param action_kwargs: Additional arguments passed to the action.
        :return: Result arguments dict.
        """
        self._action_step_kwargs.update(action_kwargs)
        return self._action(**self._action_step_kwargs)

    def compensate(self) -> bool:
        """
        Execute the compensation of the ActionStep.
        :return: Boolean result if succeeded to execute.
        """
        return self._compensation(**self._action_step_kwargs)


class LambdaActionStep(ActionStep):
    """
    The LambdaActionStep class represents an abstract action that gets an action and compensation as a callable.
    The LambdaActionStep handles the logic of act and compensate with the given callables.
    """

    def __init__(self, action: Callable, compensation: Callable, **action_step_kwargs):
        """
        :param action: The method of the action itself.
        :param compensation: The method that reverses the effects of the action after
        an exception raised in the flow of the Saga.
        :param action_step_kwargs: Additional arguments passed to the action.
        the arguments are saved as part of the ActionStep metadata.
        """
        super().__init__(**action_step_kwargs)
        self.__action = action
        self.__compensation = compensation

    @property
    def _action(self) -> Callable[..., Dict[any, any]]:
        return self.__action

    @property
    def _compensation(self) -> Callable[..., bool]:
        return self.__compensation
