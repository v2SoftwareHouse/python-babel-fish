from typing import Callable, Optional, TypeVar

from src.use_case import UseCase
from src.callback_decorator import CallbackDecorator

from src.composite_job_disposable import CompositeJobDisposable
from src.output import Output
from src.use_case_decorator import UseCaseDispatcher
from src.use_case_unit import UseCaseUnit

P = TypeVar('P', bound=object)
R = TypeVar('R', bound=object)

class BaseController(object):
    composite_job_disposable: Optional[CompositeJobDisposable] = None

    def dispatch_use_case(self, param: P, use_case: UseCase[P, R], listener: Callable[[Output[R]], None]) -> any:
        dispatcher = UseCaseDispatcher(use_case, CallbackDecorator(use_case, listener))
        job = dispatcher.dispatch(param)
        if self.composite_job_disposable:
            self.composite_job_disposable.add(job)
        
        return job
    
    def process_use_case(self, param: P, use_case: UseCase[P, R]) -> Output[R]:
        callback = UseCaseUnit.Callback()
        CallbackDecorator(use_case, callback.set).process(param)

        return callback.output
