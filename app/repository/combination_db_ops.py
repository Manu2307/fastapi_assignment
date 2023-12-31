
from app.lib.singleton import Singleton
from app.models import Combinations
from app.repository.common_ops import CommonDbOperations


class CombinationDBOperations(metaclass=Singleton):
    def __init__(self):
        self.model = Combinations

    def create_combination(self, register_dict, commit=True):
        ops = CommonDbOperations(self.model)
        user = ops.create_record(register_dict, commit)
        return user

