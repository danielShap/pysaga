from abc import ABC, abstractmethod 
from typing import Callable, Dict


class ActionStep(ABC): 
"""
The ActionStep is the class that represenets a step in the Saga.
A step containts two  methods, action and compenstate. 
The action method includes the the logic action of the step and the compenstate method includes 
the compenstatation logic in case of failure. 
"""
    def __init__(self, **action_step_kwargs): \
        """
        :param action_step_kwargs: Additional arguments passed to the action. 
        the arguments are saved as part of the ActionStep metadata. 
        """
        self._action_step_kwargs = action_step_kwargs
    
    @property
    @abstractmethod
    def _action(self) -> Callable[..., Dict[any, any]]
        """
        :return: The function of the act of the stage.
        """
        pass
        
    
    @property
    @abstractmethod
    def _compenstation(self) -> Callable[..., bool]
        """
        :return: The function of the compenstate of the stage.
        """
        pass
        
    
    def act(self, **action_kwargs) -> Dict[any, any]
        """
        Execute the action of the ActionStep.
        :param action_kwargs: Additional arguments passed to the action.
        :return: Result arguments dict.
        """
        self._action_step_kwargs.update(action_kwargs)
        return self._action(**self._action_step_kwargs)
        
        
    def compenstate(self) -> bool
        """
        Execute the compenstatation of the ActionStep.
        :return: Boolean result if succeeded to execute.
        """
        return self._compenstation(**action_step_kwargs)
        
        
        
        
        
        
        