from lark import Tree, Transformer, Discard


class BlackList(Transformer):
    def __init__(self, tokens):
        super().__init__(visit_tokens=True)
        if not isinstance(tokens, list):
            tokens = [tokens]
        self.ignore_list = tokens.copy()

    def __default__(self, data, children, meta):
        if data in self.ignore_list:
            raise Discard

        return Tree(data, children, meta)

    def __default_token__(self, token):
        if token.type in self.ignore_list:
            raise Discard

        return token
