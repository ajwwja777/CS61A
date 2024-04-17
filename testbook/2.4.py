"""
>>> celsius = connector('Celsius')
>>> fahrenheit = connector('Fahrenheit')
"""

def converter(c, f):
    """用约束条件连接 c 到 f，将摄氏度转换为华氏度."""
    u, v, w, x, y = [connector() for _ in range(5)]
    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)
    constant(w, 9)
    constant(x, 5)
    constant(y, 32)


# >>> converter(celsius, fahrenheit)

# >>> celsius['set_val']('user', 25)
# Celsius = 25
# Fahrenheit = 77.0

# >>> fahrenheit['set_val']('user', 212)
# Contradiction detected: 77.0 vs 212

# >>> celsius['forget']('user')
# Celsius is forgotten
# Fahrenheit is forgotten

# >>> fahrenheit['set_val']('user', 212)
# Fahrenheit = 212
# Celsius = 100.0

# >>> connector ['set_val'](source, value)  """表示 source 在请求连接器将当前值设为 value"""
# >>> connector ['has_val']()  """返回连接器是否已经具有值"""
# >>> connector ['val']  """是连接器的当前值"""
# >>> connector ['forget'](source)  """告诉连接器 source 请求遗忘它的值"""
# >>> connector ['connect'](source)  """告诉连接器参与新的约束，即 source"""

# >>> constraint['new_val']()  """表示与约束相连的某个连接器具有新的值。"""
# >>> constraint['forget']()  """表示与约束相连的某个连接器遗忘了值。"""


from operator import add, sub
def adder(a, b, c):
    """约束 a+b=c"""
    return make_ternary_constraint(a, b, c, add, sub, sub)

def make_ternary_constraint(a, b, c, ab, ca, cb):
    """约束 ab(a,b)=c，ca(c,a)=b，cb(c,b)=a"""
    def new_value():
        av, bv, cv = [connector['has_val']() for connector in (a, b, c)]
        if av and bv:
            c['set_val'](constraint, ab(a['val'], b['val']))
        elif av and cv:
            b['set_val'](constraint, ca(c['val'], a['val']))
        elif bv and cv:
            a['set_val'](constraint, cb(c['val'], b['val']))
    def forget_value():
        for connector in (a, b, c):
            connector['forget'](constraint)
    constraint = {'new_val': new_value, 'forget': forget_value}
    for connector in (a, b, c):
        connector['connect'](constraint)
    return constraint

from operator import mul, truediv
def multiplier(a, b, c):
    """约束 a*b=c"""
    return make_ternary_constraint(a, b, c, mul, truediv, truediv)

def constant(connector, value):
    """常量赋值"""
    constraint = {}
    connector['set_val'](constraint, value)
    return constraint

def connector(name=None):
    """限制条件之间的连接器"""
    informant = None
    constraints = []
    def set_value(source, value):
        nonlocal informant
        val = connector['val']
        if val is None:
            informant, connector['val'] = source, value
            if name is not None:
                print(name, '=', value)
            inform_all_except(source, 'new_val', constraints)
        else:
            if val != value:
                print('Contradiction detected:', val, 'vs', value)
    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(name, 'is forgotten')
            inform_all_except(source, 'forget', constraints)
    connector = {'val': None,
                 'set_val': set_value,
                 'forget': forget_value,
                 'has_val': lambda: connector['val'] is not None,
                 'connect': lambda source: constraints.append(source)}
    return connector

def inform_all_except(source, message, constraints):
    """告知信息除了 source 外的所有约束条件"""
    for c in constraints:
        if c != source:
            c[message]()