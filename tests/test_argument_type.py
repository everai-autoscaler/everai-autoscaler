import typing
import unittest

from everai_autoscaler.model import BuiltinAutoScaler, DecideResult, Factors, ArgumentType


class A:
    def __call__(self) -> str:
        return '9'


class B(BuiltinAutoScaler):
    def __init__(self,
                 o1: ArgumentType,
                 o2: ArgumentType,
                 ) -> None:
        ...

    def decide(self, factors: Factors) -> DecideResult:
        return DecideResult(max_workers=3)

    @classmethod
    def scheduler_name(cls) -> str:
        return 'queue'

    @classmethod
    def autoscaler_name(cls) -> str:
        return 'a'

    def autoscaler_arguments(self) -> typing.Dict[str, ArgumentType]:
        return dict()

    @classmethod
    def from_arguments(cls, arguments: typing.Dict[str, str]) -> BuiltinAutoScaler:
        return B(**arguments)


class ArgumentTypeTest(unittest.TestCase):
    def test_argument_type(self):
        a = B(o1='3', o2=A())
        b = B(o1=3, o2=A())
