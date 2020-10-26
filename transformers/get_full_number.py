from lark import Tree, Token, Transformer


class GetFullNumber(Transformer):
    def __default__(self, data, children, meta):
        if data == 'phone':
            code = children[0].children[0]
            number = children[1].children[0]
            children.append(Tree('full', [code + number]))

        return Tree(data, children, meta)
