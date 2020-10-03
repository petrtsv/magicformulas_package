from typing import Dict, Union, Optional, Sequence

from operations import Operation


class Node:
    def __init__(self, name: str = None, latex_sign: str = None, description: str = None, value: float = None,
                 parent_operation: Operation = None,
                 abs_error: float = None,
                 rel_error: float = None, integer: bool = False):
        self.name = name
        self.latex_sign = latex_sign
        self.description = description
        self.value = value
        self.parent_operation = parent_operation
        self.abs_error = abs_error
        self.rel_error = rel_error
        self.is_integer = integer

        if abs_error is not None and rel_error is not None:
            raise ValueError("Absolute and relative errors can not be specified at the same time.")

        if abs_error is None and rel_error is None:
            self.abs_error = 0.0

    def compute(self, params_dict: Optional[Dict[str, Union[float, Sequence[float]]]] = None):
        value = self.value
        abs_error = self.abs_error
        rel_error = self.rel_error
        if value is None:
            if params_dict is not None and self.name is not None and self.name in params_dict.keys() \
                    and params_dict[self.name] is not None:
                if type(params_dict[self.name]) is float:
                    value = params_dict
                elif len(params_dict[self.name]) == 1:
                    value, = params_dict
                elif len(params_dict[self.name]) == 2:
                    value.abs_error = params_dict[self.name]
                else:
                    value, abs_error, rel_error = params_dict[self.name]
            elif self.parent_operation is not None:
                value, abs_error = self.parent_operation.compute()
