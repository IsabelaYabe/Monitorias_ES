from __future__ import annotations

from abc import ABCMeta
from typing import Any, Dict, Type


class SingletonABCMeta(ABCMeta):
    """
    Singleton per concrete class.
    Always returns the same instance for each class.
    """
    _instances: Dict[Type[Any], Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls in cls._instances:
            inst = cls._instances[cls]

            new_ui = kwargs.get("ui", None)
            if new_ui is None and len(args) >= 1:
                new_ui = args[0]

            if new_ui is not None and hasattr(inst, "ui"):
                if inst.ui.__class__ is not new_ui.__class__:
                    raise ValueError(
                        f"{cls.__name__} já foi criado com {inst.ui.__class__.__name__}. "
                        f"Não pode recriar com {new_ui.__class__.__name__}."
                    )

            return inst

        inst = super().__call__(*args, **kwargs)
        cls._instances[cls] = inst
        return inst

    @classmethod
    def reset(cls, target_cls: Type[Any]) -> None:
        """testes/demonstração no mesmo run."""
        cls._instances.pop(target_cls, None)
