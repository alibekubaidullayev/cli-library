from typing import Callable, Dict, List, Optional, Union


class Element:
    def __init__(self, name: str, action: Union[Callable, "Menu"]) -> None:
        self.name = name
        self.action = action
        self.key = None

    def set_key(self, value: str) -> None:
        self.key = value.lower()

    def set_name(self, value: str) -> None:
        self.name = value

    def __str__(self) -> str:
        return f"[{self.key}] {self.name}"


class Menu:
    _element_counter = 0
    _control_counter = -1
    _labels = "QWERTYUIOP"

    @classmethod
    def give_key(cls) -> int:
        cls._element_counter += 1
        return cls._element_counter

    @classmethod
    def give_cnt(cls) -> str:
        cls._control_counter += 1
        return cls._labels[cls._control_counter]

    def __init__(self, name: str) -> None:
        self._name: str = name
        self._elements: List[Element] = []
        self._controls: List[Element] = []

    def add_element(self, name: str, action: Union[Callable, "Menu"]) -> None:
        el = Element(name=name, action=action)
        el.set_key(str(self.give_key()))
        self._elements.append(el)

    def add_control(self, name: str, action: "Menu") -> None:
        cn = Element(name=name, action=action)
        cn.set_key(self.give_cnt())
        self._controls.append(cn)

    def draw_menu(self) -> None:
        print(f"***{self._name}***")
        print("--------------------------------")
        self.draw_elements()
        print("--------------------------------")
        self.draw_controls()

    def draw_elements(self) -> None:
        for el in self._elements:
            print(el)

    def draw_controls(self) -> None:
        for cn in self._controls:
            print(cn, end=" ")
        print()


if __name__ == "__main__":
    menu = Menu("Main")
    menu.add_element("ASdasd", lambda: print())
    menu.add_element("asgd", lambda: print())
    menu.add_element("gasdgas", lambda: print())
    exit_menu = Menu("Exit")
    menu.add_control("Exit", exit_menu)
    exit_meu = Menu("Exit")
    menu.add_control("t", exit_meu)
    menu.draw_menu()
