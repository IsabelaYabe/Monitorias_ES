from functools import wraps
from typing import Any, Callable

type Data = dict[str, Any]
type ExportFn = Callable[[data], None] # [[args], return]

EXPORTERS: dict[str, ExportFn] = {}

def register_exporter(name: str):
    def decorator(fn: ExportFn):
        @wraps(fn)
        def wrapper(*args, **kwargs) -> Any:
            return fn(*args, **kwargs)

        EXPORTERS[name] = wrapper
        return wrapper

    return decorator

@register_exporter("pdf")
def export_pdf(data: Data) -> None:
    print(f"Exporting to PDF: {data}")

@register_exporter("epub")
def export_epub(data: Data) -> None:
    print(f"Exporting to EPub: {data}")

def export_data(data: Data, format: str) -> None:
    exporter = EXPORTERS.get(format)    
    if exporter is None:
        raise ValueError(f"No exporter found for: {format}")
    exporter(data)

def main() -> None:
    data: Data = {"Title": "O Alienista", "Author": "Machado de Assis", "Content": "..."}

    export_data(data, "pdf")
    export_data(data, "epub")

if __name__ == "__main__":
    main()
