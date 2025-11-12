from __future__ import annotations
from abc import abstractmethod
from typing import Optional

from handler import Handler

class EmailHandler(Handler):
    def __init__(self):
        self._next: Optional[Handler] = None

    def set_next(self, h: Handler) -> Handler:
            self._next = h
            return h
    
    @abstractmethod
    def handle(self, request: str) -> Optional[str]:
        if self._next:
            return self._next.handle(request)
        return None

class EmailNotEmptyHandler(EmailHandler):
    def handle(self, request: str) -> Optional[str]:
        if not request:
            return "Email cannot be empty"
        return super().handle(request)

class EmailFormatHandler(EmailHandler):
    def handle(self, request: str) -> Optional[str]:
        if "@" not in request:
            return "Email must contain '@'"
        return super().handle(request)

class EmailLengthHandler(EmailHandler):
    def __init__(self, max_total: int = 20, min_total: int = 6, max_local: int = 10, min_local: int = 3):
        super().__init__()
        self.max_total = max_total
        self.max_local = max_local
        self.min_total = min_total
        self.min_local = min_local

    def handle(self, request: str) -> Optional[str]:
        len_request = len(request)

        if len_request > self.max_total or len_request < self.min_total:
            return f"Email must be between {self.min_total} and {self.max_total} characters long, got {len_request}"
        
        split = request.split("@", 1)
        local = split[0]
        domain = split[1]
        if len(local) > self.max_local or len(local) < self.min_local:
            return f"Local part must be between {self.min_local} and {self.max_local} characters long, got {len(local)}"
        if len(domain) > self.max_local or len(domain) < self.min_local:
            return f"Domain part must be between {self.min_local} and {self.max_local} characters long, got {len(domain)}"
        
        return super().handle(request)


def build_email_chain() -> Handler:
    not_empty = EmailNotEmptyHandler()
    format_h = EmailFormatHandler()
    length_h = EmailLengthHandler(20, 6, 10, 3)

    not_empty.set_next(format_h).set_next(length_h)
    return not_empty

if __name__ == "__main__":
    chain = build_email_chain()
    tests = ["", "user", "user@", "user@site", "user@site.c",
        "user@site.com", "someone@mailinator.com"]
    for e in tests:
        res = chain.handle(e)
        print(f"{e!r} -> {'OK' if res is None else 'ERR: ' + res}")
