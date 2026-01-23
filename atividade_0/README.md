## Objetivo da Atividade 0

Implementar um mini-editor com:

* **UI multiplataforma** (Windows/Mac) com *famílias coerentes* de componentes.
* **Criação de documentos extensível** (novos tipos sem mexer na base).
* **Reuso de instâncias por chave** (mesmo nome → mesmo documento).
* **Histórico de estado do documento** com **save/revert**.

---

## O que você precisa entregar (requisitos + critérios de aceite)

### RF-01 — Abstract Factory (UI por família)

**Necessário**

* Uma interface `InterfaceFactory` com métodos tipo:

  * `create_window() -> Window`
  * `create_cursor() -> Cursor`
* Implementações:

  * `WindowsInterfaceFactory`
  * `MacInterfaceFactory`
* Produtos:

  * `Window` (abstrato) + `WindowsWindow`, `MacWindow`
  * `Cursor` (abstrato) + `WindowsCursor`, `MacCursor`

**Aceite**

* Ao trocar a fábrica, a aplicação passa a usar *apenas* produtos daquela família.
* Não existe `if windows else mac` dentro do código da aplicação para criar UI.

---

### RF-02 — Factory Method (criação de Document)

**Necessário**

* Classe base `Application` com:

  * método público `new_document(name: str) -> Document`
  * método protegido/abstrato `_create_document(name: str) -> Document` (**Factory Method**)
* Subclasse `TextEditor(Application)` implementa `_create_document` e decide o concreto (`TextDocument`).

**Aceite**

* Para criar um novo tipo de documento (ex.: `MarkdownDocument`), você cria uma nova subclasse de `Application` **ou** muda apenas a implementação do `_create_document` (sem alterar o fluxo base do `new_document`).

---

### RF-03 — Multiton (um documento por nome)

**Necessário**

* A pasta de documentos: `self._documents: dict[str, Document]`
* Um decorator (ou lógica interna) que garante:

  * se já existe doc com a chave, retorna o mesmo objeto
  * se não existe, cria e armazena

**Aceite**

* `app.new_document("a")` chamado 2x retorna o **mesmo** objeto (mesmo `id()`).
* `app.new_document("b")` cria outro.

> Observação importante: Multiton é pro **documento** (por nome).
---

### RF-04 — Save/Revert (Memento)

**Necessário**

* `Document` mantém o estado (por exemplo `content: str`) e um histórico:

  * `save()` grava um snapshot
  * `revert()` restaura o último snapshot (ou um snapshot específico)
* Implementação simples e boa:

  * `self._history: list[Memento]`
  * `Memento` é um dataclass imutável com o estado

**Aceite**

* Depois de editar conteúdo:

  * `save()` registra o estado atual
  * novas edições não apagam o histórico
  * `revert()` volta exatamente ao último estado salvo

### RF-05 — Singleton (Application única)

**Necessário**
  * Garantir que apenas uma instância de `Application` possa ser criada.
  * A primeira chamada define a UI (InterfacceFactory).
  * Se tentar recriar a applicação com outra UI, o sistema deve **impedir**, para não ficar inconsistente.

**Aceite**
  * `TextEditor(WindowsFactory()) is TextEditor(WindowsFactory()) → True`.
  * `TextEditor(WindowsFactory())` seguido de `TextEditor(MacFactory())` deve **levantar erro**.

---

## Estrutura de pastas 

```
atividade0/
  main.py
  app/
    __init__.py
    application.py
    documents/
      __init__.py
      document.py
      text_document.py
      memento.py
    interface/
      __init__.py
      factory.py
      products.py
      concretas.py
```

`__init__.py` para definir pacote e expor import.

---

## Design das classes

### 1) Abstract Factory (UI)

* `InterfaceFactory` cria produtos abstratos `Window` e `Cursor`.
* Implementações concretas devolvem os concretos correspondentes.

### 2) Factory Method (Document)

* `Application.new_document()` define o fluxo padrão:

  * obter instância via Multiton
  * criar usando `_create_document()` quando necessário

### 3) Multiton (Document por chave)

* Pode ser:

  * decorator `@multiton(key_arg="name", attr_name="_documents")`

### 4) Memento (Save/Revert)

* `TextDocument` (ou `Document`) implementa:

  * `save()` → push snapshot
  * `revert()` → pop snapshot e restaurar

---

## Fluxo “de demonstração” (o que seu `main.py` tem que provar)

1. UI por família:

* `TextEditor(WindowsInterfaceFactory()).show_ui()` desenha Window+Cursor Windows.
* `TextEditor(MacInterfaceFactory()).show_ui()` desenha Window+Cursor Mac.

2. Multiton:

* `d1 = app.new_document("notes")`
* `d2 = app.new_document("notes")`
* `d1 is d2` deve ser `True`.

3. Save/Revert:

* `d1.write("A")` → `save()`
* `d1.write("B")`
* `revert()` → volta pra `"A"`.

## Checklist

* [ ] `InterfaceFactory` + 2 fábricas concretas (Windows/Mac)
* [ ] `Window` e `Cursor` abstratos + concretos correspondentes
* [ ] `Application.new_document()` com fluxo padrão
* [ ] `_create_document()` abstrato e implementado em `TextEditor`
* [ ] Multiton por nome (mesmo documento para mesma chave)
* [ ] `save()` / `revert()` com Memento imutável
* [ ] `main.py` demonstrando os 3 comportamentos (UI / Multiton / Save-Revert)
* [ ] Singleton da aplicação, uma instância de `TextEditor`
