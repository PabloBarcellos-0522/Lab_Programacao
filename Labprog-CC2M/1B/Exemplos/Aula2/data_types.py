'''
DataTypes:
- Text: str
- Numeric: int, float, complex
- Sequence: list, tuple, range
- Mapping: dict
- Set: set, frozenset
- Boolean: bool
- Binary: bytes, bytearray, memoryview
- None: NoneType
'''

x = 5
y = 5.5

print(type(x))
print(type(y))

nomes = ["Renato", "Gabriel", "João"]

print(type(nomes))

aluno = {
  'nome': 'remato',
  'idade': 20,
  'nota': 8.5
}

print(type(aluno))

vazia = None

print(type(vazia))