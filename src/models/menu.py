from typing import Callable, Dict, List, Optional, Union


class Element:
    """
    Класс представляющий из себя "кнопку". Хранит в себе название, ключ (тригер) и действие (или меню)

    Атрибуты:
    -   name (str): название кнопки которое будет отображено
    -   action (Callable, Menu): функция, или меню которое хранится в этом элементе
    -   key (str): ключ по которому активируется action
    """

    def __init__(
        self,
        action: Union[Callable, "Menu"],
        name: str,
        key: Optional[str] = None,
    ) -> None:
        self.name = name
        self.action = action
        self.key = key

    def set_key(self, value: str) -> None:
        self.key = value.upper()

    def set_name(self, value: str) -> None:
        self.name = value

    def __str__(self) -> str:
        return f"[{self.key}] {self.name}"

    def __len__(self) -> int:
        return len(self.name) + 4

    def __repr__(self) -> str:
        return f"[[{self.key}] {self.name} {self.action}]"


class Menu:
    """
    Класс, представляющий меню. Хранит в себе элементы и управляющие элементы меню.

    Атрибуты:
    - _name (str): название меню.
    - _elements (List[Element]): список элементов меню.
    - _controls (List[Element]): список управляющих элементов меню.
    - _previous (Optional[Menu]): ссылка на предыдущее меню.
    - _root (bool): является ли это корневым меню.
    - _mapping (Dict[Optional[str], Union[Callable, Menu]]): отображение ключей на действия или подменю.
    """

    _element_counter: int = 0
    _control_counter: int = -1
    _labels: str = "QWERTYUIOP"

    def __init__(self, name: str, root: bool = False) -> None:
        self._name: str = name
        self._elements: List[Element] = []
        self._controls: List[Element] = []
        self._previous: Optional["Menu"] = None
        self._root: bool = root
        self._mapping: Dict[Optional[str], Union[Callable, "Menu"]] = {}

        if self._root:
            self.add_control(name="Exit", action=lambda: exit(), key="x")

    def give_key(self) -> int:
        """
        Выдает ключ от 1 до inf+ в списке элементов
        """
        self._element_counter += 1
        return self._element_counter

    def give_cnt(self) -> str:
        """
        Выдает ключ от Q до P для управляющих элементов в меню
        Так как иметь больше 3-4 управляющих элементов в меню не
        целесобразно я ограничился только буквами от Q до P на верхнем ряду клавиатуры
        """
        self._control_counter += 1
        return self._labels[self._control_counter]

    def get_name(self) -> str:
        return self._name

    def set_prev(self, prev: "Menu") -> None:
        if not self._root and not self._previous:
            self._previous = prev
            self.add_control(self._previous, "Prev")
            self.set_mapping()

    def add_element(
        self, action: Union[Callable, "Menu"], name: Optional[str] = None
    ) -> None:
        if isinstance(action, Menu):
            el_name = name or action.get_name()
        else:
            el_name = name or action.__name__

        el = Element(name=el_name, action=action)
        el.set_key(str(self.give_key()))
        self._elements.append(el)

    def add_control(
        self, action: Union[Callable, "Menu"], name: str, key: Optional[str] = None
    ) -> None:
        if key:
            key = key.upper()
        cn = Element(name=name, action=action, key=key)
        if not key:
            cn.set_key(self.give_cnt())
        self._controls.append(cn)

    def draw_menu(self) -> None:
        print(f"***{self._name}***")
        self.draw_frame()
        self.draw_elements()
        self.draw_frame()
        self.draw_controls()
        self.draw_frame()

    def draw_elements(self) -> None:
        for el in self._elements:
            print(el)

    def draw_frame(self) -> None:
        print("-" * self.get_controls_len())

    def get_controls_len(self) -> int:
        """
        Функция нужна для отрисовки рамок по размеру с панелью элементов
        """
        return sum([len(cn) for cn in self._controls]) + len(self._controls)

    def draw_controls(self) -> None:
        for cn in self._controls:
            print(cn, end=" ")
        print()

    def set_mapping(self) -> None:
        """
        Выставляет ключ и соотвествующий элемент для внешнего доступа
        """
        self._mapping = {el.key: el.action for el in self._elements}
        self._mapping.update({cn.key: cn.action for cn in self._controls})

    def get_mapping(self) -> Dict[Optional[str], Union[Callable, "Menu"]]:
        """
        Возвращает ключ-элемент соотвествующий этой меню
        """
        self.set_mapping()
        return self._mapping

    def __repr__(self) -> str:
        return f"{self._name}"
