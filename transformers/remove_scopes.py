from lark import Tree, Token, Transformer


class RemoveScopes(Transformer):
    def __default__(self, data, children, meta):
        return Tree(data.split("__")[-1], children, meta)

    def __default_token__(self, token):
        return Token(token.type.split("__")[-1], token.value)
