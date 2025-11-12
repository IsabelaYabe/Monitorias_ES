from __future__ import annotations
from abc import abstractmethod
from typing import Optional

from handler import Handler

class PasswordHandler(Handler):
    def __init__(self): 
        self._next: Optional[Handler] = None

    def set_next(self, h: Handler) -> Handler: 
        self._next = h
        return h

    @abstractmethod
    def handle(self, req: str) -> Optional[str]:
        if self._next: 
            return self._next.handle(req)
        return None

class NotEmptyHandler(PasswordHandler):
    def handle(self, req: str) -> Optional[str]:
        if not req:
            return "Password cannot be empty"  
        return super().handle(req)

class MinLengthHandler(PasswordHandler):
    def __init__(self, n=8): 
        super().__init__() 
        self.n = n
    
    def handle(self, req: str) -> Optional[str]:
        if len(req) < self.n:
            return f"Password must have at least {self.n} characters"
        return super().handle(req)

class NotCommonHandler(PasswordHandler):
    def __init__(self):
        super().__init__()
        self._COMMON = {"123456", "password", "qwerty", "111111", "abc123", "Password123"}

    def handle(self, req: str) -> Optional[str]:  
        if req in self._COMMON:
            return "Password is too common"
        return super().handle(req)

def build_password_checker() -> Handler:
    not_empty = NotEmptyHandler()
    min_len   = MinLengthHandler(8)
    not_common= NotCommonHandler()

    not_empty.set_next(min_len).set_next(not_common)
    return not_empty

if __name__ == "__main__":
    chain = build_password_checker()
    passwords = ["", "short", "123456", "validPass123"]

    for pwd in passwords:
        result = chain.handle(pwd)
        if result:
            print(f"Password '{pwd}' is invalid: {result}")
        else:
            print(f"Password '{pwd}' is valid.")