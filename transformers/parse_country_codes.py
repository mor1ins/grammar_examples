from lark import Tree, Token, Transformer


class ParseCountryCodes(Transformer):
    def __default__(self, data, children, meta):
        if data == 'country_code':
            token = children[0]
            children = [
                Tree('country', [token.type]),
                Tree('value', [token.value])
            ]

        return Tree(data, children, meta)
