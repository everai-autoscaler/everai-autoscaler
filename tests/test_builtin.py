import typing
import unittest

from everai_autoscaler.model import BuiltinAutoScaler, Factors, DecideResult, ArgumentType, AutoScaler


def f(a: AutoScaler):
    ...


def f2(a: BuiltinAutoScaler):
    ...


class A(BuiltinAutoScaler):
    def __init__(self, ):
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
        return A()


class TestBuiltinAutoScaler(unittest.TestCase):
    def test_builtin(self):
        a: BuiltinAutoScaler = A()
        f(a)
