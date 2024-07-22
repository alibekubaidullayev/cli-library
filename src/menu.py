from typing import Callable, Dict, List, Optional, Union


class Button:
    def __init__(self, name: str, action: Union[Callable, "Menu"]):
        self.name = name
        self.action = action
        self.key = None

    def set_key(self, value: str) -> None:
        self.key = value


class Menu:
    def __init__(self, name: str, root: bool = False) -> None:
        self.name: str = name
        self.previous: Optional["Menu"] = None
        self.available: List["Menu"] = []
        self.elements: Dict[str, Union[Callable, "Menu"]] = {}
        self.elements_mapping: Dict[int, str] = {}
        self.available_mapping: Dict[str, "Menu"] = {}
        self.root = root

    def set_available(self, av: List["Menu"]) -> None:
        self.available = av

    def get_available(self) -> List["Menu"]:
        if self.previous and not self.root:
            return [*self.available, self.previous]
        return self.available

    def set_mapping(self) -> None:
        if self.elements_mapping and self.available_mapping:
            return

        for i, el in enumerate(self.elements.keys()):
            self.elements_mapping[i + 1] = el

        keys = "QWERTYUIOP"
        for i, av in enumerate(self.get_available()):
            self.available_mapping[keys[i]] = av

    def add_available(self, menu: "Menu") -> None:
        self.available.append(menu)

    def add_element(
        self,
        name: str,
        func_menu: Union[Callable, "Menu"],
    ) -> None:
        self.elements[name] = func_menu

    def draw_menu(self) -> None:
        self.set_mapping()
        print(f"Menu: {self.name}")
        print()
        self.draw_elements()
        self.draw_available()

    def draw_elements(self) -> None:
        for i, el in enumerate(self.elements.keys()):
            print(f"{i + 1}. {el}")

    def draw_available(self) -> None:
        for key, value in self.available_mapping.items():
            print(f"{key}. {value}", end="|")
        print()

    def get_mapping(self) -> Dict[str, Union[Callable, "Menu"]]:
        mapping: Dict[str, Union[Callable, "Menu"]] = {}
        self.set_mapping()

        for i, el in self.elements_mapping.items():
            mapping[str(i)] = self.elements[el]

        for key, av in self.available_mapping.items():
            mapping[key] = av

        return mapping

    def __repr__(self) -> str:
        return self.name
