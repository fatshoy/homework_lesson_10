from pydantic import BaseModel


data = {
    'age': 45,
    'name': 'Peter',
    'children': [
        {
        'age': 3,
        'name': 'Alice'
        }
    ],
    'married': True,
    'city': None
}


class Children(BaseModel):
    age: int
    name: str


class Adult(BaseModel):
    age: int
    name: str
    children: list[Children] = None
    married: bool
    city: str = None


r = Adult(**data)
print(r)