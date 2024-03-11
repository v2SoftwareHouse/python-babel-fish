from src.error_output import ErrorOutput
from src.use_case import UseCase
from src.output import Output
from src.use_case_decorator import UseCaseDecorator
from typing import Callable, TypeVar

P = TypeVar('P')
R = TypeVar('R')

class CallbackDecorator(UseCaseDecorator[P, R]):
    def __init__(self, use_case: UseCase[P, R], callback: Callable[[Output[R]], None]):
        super().__init__(use_case)
        self.callback = callback

    def on_result(self, output: Output[R]):
        super().on_result(output)
        self.callback(output)

    def on_error(self, error: Exception):
        super().on_error(error)
        self.callback(ErrorOutput(error))
