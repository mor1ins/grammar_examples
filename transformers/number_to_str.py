from lark import Tree, Token, Transformer


class NumberToStr(Transformer):
    def __default__(self, data, children, meta):
        if data == 'number':
            number = "".join(children)
            return Tree(data, [number], meta)

        return Tree(data, children, meta)

