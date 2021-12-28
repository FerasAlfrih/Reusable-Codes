class Enigma:
    def __init__(
        self,
        text: str,
        code: list,
        blug_panel: bool,
        blugs={
            "a": False,
            "b": False,
            "c": False,
            "d": False,
            "e": False,
            "f": False,
            "g": False,
            "h": False,
            "i": False,
            "j": False,
            "k": False,
            "l": False,
            "m": False,
        },
    ) -> None:
        self.input = text
        self.code = code
        self.blug_panel = blug_panel
        self.blugs = blugs
        self.order = self.get_keyboard()
        self.original_mirror = self.list2dict()
        self.original = self.list2dict()
        self.output = self.encode()
        self.mixed = None

    def get_keyboard(self):
        new = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            " ",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            ".",
            ",",
            "/",
            "\\",
            "!",
            "@",
            "#",
            "$",
            "%",
            "^",
            "&",
            "(",
            "*",
            ")",
            "_",
            "-",
            "=",
            "+",
            "|",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "0",
            "[",
            "]",
            "{",
            "}",
            "?",
            "`",
            "~",
        ]
        return new

    def list2dict(self):
        new = {}
        for i in self.order:
            new[i] = i
        return new

    def randomize_order(self, order: list, original: dict, code: int):
        new = {}
        n = code
        original = list(original.values())
        while len(order) > 0:
            for i in order:
                index = order.index(i) + n
                if index >= len(order):
                    index = index % len(order)
                j = original[index]
                new[i] = j
                new[j] = i
                order.remove(i)
                original.remove(j)
                if i != j:
                    order.remove(j)
                    original.remove(i)
                n += 1
                if n >= len(order):
                    n = 0

        self.order = self.get_keyboard()
        return new

    def encode(self):
        paragraph = ""
        if self.blug_panel:
            print("blug_panel ON")
        else:
            print("blug_panel OFF")
            for letter in self.input:
                print(letter)
                for code in self.code:
                    if self.code.index(code) == 0:
                        self.mixed = self.randomize_order(
                            self.order, self.original, code
                        )
                    else:
                        self.mixed = self.randomize_order(self.order, self.mixed, code)
                self.code = [code + 1 for code in self.code]
                paragraph += self.mixed[letter]

        return paragraph


text = "FGiR"
lista = {}
eng = Enigma(text, [60, 5, 12560], False)
print(eng.output)
