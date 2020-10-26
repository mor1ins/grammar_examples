from lark import Transformer, v_args


class ParseToDict(Transformer):
    def __init__(self):
        super().__init__(visit_tokens=True)

    start = dict
    # def start(self, args):
    #     pass

    def __default__(self, data, children, meta):
        # is_dict = '":' in children[0] if len(children) > 0 else False
        # value = '"%s"'
        # if len(children) >= 2 or is_dict:
        #     value = "{ %s }" if is_dict else "[ %s ]"

        result = (data, children[0] if len(children) == 1 else dict(children))

        return result

    def __default_token__(self, token):
        return token.value

