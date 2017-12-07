from omi import *

try:
    from utils import *
except ImportError:
    import sys
    sys.path.insert(0, '..')
    from utils import *


def real64a_test():
    be = BookEnd('real64a_test')

    val0 = random.uniform(-1e307, 1e307)
    val1 = random.uniform(-1e307, 1e307)
    while float_eq(val0, val1):
        val1 = random.uniform(-1e307, 1e307)
    val2 = random.uniform(-1e307, 1e307)
    while float_eq(val0, val2) or \
            float_eq(val1, val2):
        val2 = random.uniform(-1e307, 1e307)
    val3 = random.uniform(-1e307, 1e307)
    while float_eq(val0, val3) or \
            float_eq(val1, val3) or \
            float_eq(val2, val3):
        val3 = random.uniform(-1e307, 1e307)
    val4 = random.uniform(-1e307, 1e307)
    while float_eq(val0, val4) or \
            float_eq(val1, val4) or \
            float_eq(val2, val4) or \
            float_eq(val3, val4):
        val4 = random.uniform(-1e307, 1e307)

    #BookEndPrint ('val0: {0}'.format (val0))
    #BookEndPrint ('val1: {0}'.format (val1))
    #BookEndPrint ('val2: {0}'.format (val2))
    #BookEndPrint ('val3: {0}'.format (val3))
    #BookEndPrint ('val4: {0}'.format (val4))

    rval = True

    # init (empty)
    v0 = MI_Real64A()
    if MI_REAL64A != v0.getType():
        BookEndPrint('----- getType failed')
        rval = False
    if v0.count() != 0:
        BookEndPrint('----- empty init failed')
        rval = False

    # test getValueAt (out of range) **error**
    try:
        v0.getValueAt(0)
    except IndexError:
        pass
    else:
        BookEndPrint('----- getValueAt (out of range) failed')
        rval = False
    try:
        v0.getValueAt(-1)
    except IndexError:
        pass
    else:
        BookEndPrint('----- getValueAt (out of range) failed')
        rval = False
    try:
        v0.getValueAt(1)
    except IndexError:
        pass
    else:
        BookEndPrint('----- getValueAt (out of range) failed')
        rval = False

    # test getValueAt (invalid type) **error**
    try:
        v0.getValueAt('zero')
    except ValueError:
        pass
    else:
        BookEndPrint('----- getValueAt (empty - invalid literal) failed')
        rval = False

    # PyList init
    v1 = MI_Real64A([val0, val1, val2])
    if v1.count() != 3:
        BookEndPrint('----- PyList init failed')
        rval = False
    if not float_eq(v1.getValueAt(0), val0) or \
            not float_eq(v1.getValueAt(1), val1) or \
            not float_eq(v1.getValueAt(2), val2) or \
            not float_eq(v1.getValueAt(-3), val0) or \
            not float_eq(v1.getValueAt(-2), val1) or \
            not float_eq(v1.getValueAt(-1), val2):
        BookEndPrint('----- PyList init or getValueAt failed')
        rval = False

    # test getValueAt (out of range) **error**
    try:
        v1.getValueAt(-4)
    except IndexError:
        pass
    else:
        BookEndPrint('----- getValueAt (out of range) failed')
        rval = False
    try:
        v1.getValueAt(3)
    except IndexError:
        pass
    else:
        BookEndPrint('----- getValueAt (out of range) failed')
        rval = False

    # test getValueAt (invalid type) **error**
    try:
        v1.getValueAt('one')
    except ValueError:
        pass
    else:
        BookEndPrint('----- getValueAt (invalid type) failed')
        rval = False

    # PyTuple init
    v2 = MI_Real64A((val0, val1, val2))
    if v2.count() != 3 or \
            not float_eq(v2.getValueAt(0), val0) or \
            not float_eq(v2.getValueAt(1), val1) or \
            not float_eq(v2.getValueAt(2), val2):
        BookEndPrint('----- PyTuple init failed')
        rval = False

    # init from None **error**
    # try:
    #    v3 = MI_Real64A (None)
    # except ValueError:
    #    pass
    # else:
    #    BookEndPrint ('----- None init failed')
    #    rval = False
    v3 = MI_Real64A(None)
    if v3.count() != 0:
        BookEndPrint('----- None init failed')
        rval = False

    # init from invalid literal value **error**
    try:
        v4 = MI_Real64A('four')
    except ValueError:
        pass
    else:
        BookEndPrint('----- init to invalid literal failed')
        rval = False

    # PyList init (None) **error**
    try:
        v5 = MI_Real64A([val0, None, val2])
    except ValueError:
        pass
    else:
        BookEndPrint('----- PyList init (None value) failed')
        rval = False

    # PyList init (underflow value) **error**
    try:
        v6 = MI_Real64A([val0, -1e309, val2])
    except ValueError:
        pass
    else:
        BookEndPrint('----- PyList init (underflow value) failed')
        rval = False

    # PyList init (overflow value) **error**
    try:
        v7 = MI_Real64A([val0, 1e309, val2])
    except ValueError:
        pass
    else:
        BookEndPrint('----- PyList init (overflow value) failed')
        rval = False

    # PyList init (invalid type) **error**
    try:
        v8 = MI_Real64A([val0, 'eight', val2])
    except ValueError:
        pass
    else:
        BookEndPrint('----- PyList init (invalid type) failed')
        rval = False

    # PyTuple init (None) **error**
    try:
        v9 = MI_Real64A((val0, None, val2))
    except ValueError:
        pass
    else:
        BookEndPrint('----- PyTuple init (None value) failed')
        rval = False

    # PyTuple init (underflow value) **error**
    try:
        v10 = MI_Real64A((val0, -1e309, val2))
    except ValueError:
        pass
    else:
        BookEndPrint('----- PyTuple init (underflow value) failed')
        rval = False

    # PyTuple init (overflow value) **error**
    try:
        v11 = MI_Real64A((val0, 1e309, val2))
    except ValueError:
        pass
    else:
        BookEndPrint('----- PyTuple init (overflow value) failed')
        rval = False

    # PyTuple init (invalid type) **error**
    try:
        v12 = MI_Real64A((val0, 'twelve', val2))
    except ValueError:
        pass
    else:
        BookEndPrint('----- PyTuple init (invalid type) failed')
        rval = False

    # setValueAt
    v13 = MI_Real64A((val0, val1, val2))
    v13.setValueAt(0, val4)
    if v13.count() != 3 or \
            not float_eq(v13.getValueAt(0), val4) or \
            not float_eq(v13.getValueAt(1), val1) or \
            not float_eq(v13.getValueAt(2), val2):
        BookEndPrint('----- setValueAt failed')
        rval = False
    v13.setValueAt(1, val0)
    if v13.count() != 3 or \
            not float_eq(v13.getValueAt(0), val4) or \
            not float_eq(v13.getValueAt(1), val0) or \
            not float_eq(v13.getValueAt(2), val2):
        BookEndPrint('----- setValueAt failed')
        rval = False
    v13.setValueAt(2, val1)
    if v13.count() != 3 or \
            not float_eq(v13.getValueAt(0), val4) or \
            not float_eq(v13.getValueAt(1), val0) or \
            not float_eq(v13.getValueAt(2), val1):
        BookEndPrint('----- setValueAt failed')
        rval = False
    v13.setValueAt(-1, val2)
    if v13.count() != 3 or \
            not float_eq(v13.getValueAt(0), val4) or \
            not float_eq(v13.getValueAt(1), val0) or \
            not float_eq(v13.getValueAt(2), val2):
        BookEndPrint('----- setValueAt failed')
        rval = False
    v13.setValueAt(-2, val1)
    if v13.count() != 3 or \
            not float_eq(v13.getValueAt(0), val4) or \
            not float_eq(v13.getValueAt(1), val1) or \
            not float_eq(v13.getValueAt(2), val2):
        BookEndPrint('----- setValueAt failed')
        rval = False
    v13.setValueAt(-3, val0)
    if v13.count() != 3 or \
            not float_eq(v13.getValueAt(0), val0) or \
            not float_eq(v13.getValueAt(1), val1) or \
            not float_eq(v13.getValueAt(2), val2):
        BookEndPrint('----- setValueAt failed')
        rval = False

    # setValueAt (index out of range) **error**
    try:
        v13.setValueAt(-4, val3)
    except IndexError:
        if v13.count() != 3 or \
                not float_eq(v13.getValueAt(0), val0) or \
                not float_eq(v13.getValueAt(1), val1) or \
                not float_eq(v13.getValueAt(2), val2):
            BookEndPrint('----- setValueAt (index out of range) failed')
            rval = False
    else:
        BookEndPrint('----- setValueAt (index out of range) failed')
        rval = False
    try:
        v13.setValueAt(3, val3)
    except IndexError:
        if v13.count() != 3 or \
                not float_eq(v13.getValueAt(0), val0) or \
                not float_eq(v13.getValueAt(1), val1) or \
                not float_eq(v13.getValueAt(2), val2):
            BookEndPrint('----- setValueAt (index out of range) failed')
            rval = False
    else:
        BookEndPrint('----- setValueAt (index out of range) failed')
        rval = False

    # setValueAt (index invalid type) **error**
    try:
        v13.setValueAt('one', val3)
    except ValueError:
        if v13.count() != 3 or \
                not float_eq(v13.getValueAt(0), val0) or \
                not float_eq(v13.getValueAt(1), val1) or \
                not float_eq(v13.getValueAt(2), val2):
            BookEndPrint('----- setValueAt (index invalid type) failed')
            rval = False
    else:
        BookEndPrint('----- setValueAt (index invalid type) failed')
        rval = False

    # setValueAt (value underflow) **error**
    try:
        v13.setValueAt(1, -1e309)
    except ValueError:
        if v13.count() != 3 or \
                not float_eq(v13.getValueAt(0), val0) or \
                not float_eq(v13.getValueAt(1), val1) or \
                not float_eq(v13.getValueAt(2), val2):
            BookEndPrint('----- setValueAt (value underflow) failed')
            rval = False
    else:
        BookEndPrint('----- setValueAt (value underflow) failed')
        rval = False

    # setValueAt (value overflow)
    try:
        v13.setValueAt(1, 1e309)
    except ValueError:
        if v13.count() != 3 or \
                not float_eq(v13.getValueAt(0), val0) or \
                not float_eq(v13.getValueAt(1), val1) or \
                not float_eq(v13.getValueAt(2), val2):
            BookEndPrint('----- setValueAt (value overflow) failed')
            rval = False
    else:
        BookEndPrint('----- setValueAt (value overflow) failed')
        rval = False

    # setValueAt (value invalid type) **error**
    try:
        v13.setValueAt(1, 'thirteen')
    except ValueError:
        if v13.count() != 3 or \
                not float_eq(v13.getValueAt(0), val0) or \
                not float_eq(v13.getValueAt(1), val1) or \
                not float_eq(v13.getValueAt(2), val2):
            BookEndPrint('----- setValueAt (value invalid type) failed')
            rval = False
    else:
        BookEndPrint('----- setValueAt (value invalid type) failed')
        rval = False

    # append
    v14 = MI_Real64A()
    v14.append(val0)
    if v14.count() != 1 or \
            not float_eq(v14.getValueAt(0), val0):
        BookEndPrint('----- append failed')
        rval = False
    v14.append(val1)
    if v14.count() != 2 or \
            not float_eq(v14.getValueAt(0), val0) or \
            not float_eq(v14.getValueAt(1), val1):
        BookEndPrint('----- append failed')
        rval = False
    v14.append(val2)
    if v14.count() != 3 or \
            not float_eq(v14.getValueAt(0), val0) or \
            not float_eq(v14.getValueAt(1), val1) or \
            not float_eq(v14.getValueAt(2), val2):
        BookEndPrint('----- append failed')
        rval = False

    # append (value underflow) **error**
    try:
        v14.append(-1e309)
    except ValueError:
        if v14.count() != 3 or \
                not float_eq(v14.getValueAt(0), val0) or \
                not float_eq(v14.getValueAt(1), val1) or \
                not float_eq(v14.getValueAt(2), val2):
            BookEndPrint('----- append (value underflow) failed')
            rval = False
    else:
        BookEndPrint('----- append (value underflow) failed')
        rval = False

    # append (value overflow)
    try:
        v14.append(1e309)
    except ValueError:
        if v14.count() != 3 or \
                not float_eq(v14.getValueAt(0), val0) or \
                not float_eq(v14.getValueAt(1), val1) or \
                not float_eq(v14.getValueAt(2), val2):
            BookEndPrint('----- append (value overflow) failed')
            rval = False
    else:
        BookEndPrint('----- append (value overflow) failed')
        rval = False

    # append (value invalid type) **error**
    try:
        v14.append('fourteen')
    except ValueError:
        if v14.count() != 3 or \
                not float_eq(v14.getValueAt(0), val0) or \
                not float_eq(v14.getValueAt(1), val1) or \
                not float_eq(v14.getValueAt(2), val2):
            BookEndPrint('----- append (value invalid type) failed')
            rval = False
    else:
        BookEndPrint('----- append (value invalid type) failed')
        rval = False

    # insert
    v15 = MI_Real64A()
    v15.insert(0, val1)
    if v15.count() != 1 or \
            not float_eq(v15.getValueAt(0), val1):
        BookEndPrint('----- insert failed')
        rval = False
    v15.insert(0, val0)
    if v15.count() != 2 or \
            not float_eq(v15.getValueAt(0), val0) or \
            not float_eq(v15.getValueAt(1), val1):
        BookEndPrint('----- insert failed')
        rval = False
    v15.insert(2, val3)
    if v15.count() != 3 or \
            not float_eq(v15.getValueAt(0), val0) or \
            not float_eq(v15.getValueAt(1), val1) or \
            not float_eq(v15.getValueAt(2), val3):
        BookEndPrint('----- insert failed')
        rval = False
    v15.insert(2, val2)
    if v15.count() != 4 or \
            not float_eq(v15.getValueAt(0), val0) or \
            not float_eq(v15.getValueAt(1), val1) or \
            not float_eq(v15.getValueAt(2), val2) or \
            not float_eq(v15.getValueAt(3), val3):
        BookEndPrint('----- insert failed')
        rval = False

    # insert using negative indices
    v16 = MI_Real64A([val2])
    v16.insert(-1, val0)
    if v16.count() != 2 or \
            not float_eq(v16.getValueAt(0), val0) or \
            not float_eq(v16.getValueAt(1), val2):
        BookEndPrint('----- insert (negative index) failed')
        rval = False
    v16.insert(-1, val1)
    if v16.count() != 3 or \
            not float_eq(v16.getValueAt(0), val0) or \
            not float_eq(v16.getValueAt(1), val1) or \
            not float_eq(v16.getValueAt(2), val2):
        BookEndPrint('----- insert (negative index) failed')
        rval = False

    # insert (index out of bounds) **error**
    try:
        v16.insert(4, val3)
    except IndexError:
        if v16.count() != 3 or \
                not float_eq(v16.getValueAt(0), val0) or \
                not float_eq(v16.getValueAt(1), val1) or \
                not float_eq(v16.getValueAt(2), val2):
            BookEndPrint('----- insert (index out of bounds) failed')
            rval = False
    else:
        BookEndPrint('----- insert (index out of bounds) failed')
        rval = False
    try:
        v16.insert(-4, val3)
    except IndexError:
        if v16.count() != 3 or \
                not float_eq(v16.getValueAt(0), val0) or \
                not float_eq(v16.getValueAt(1), val1) or \
                not float_eq(v16.getValueAt(2), val2):
            BookEndPrint('----- insert (index out of bounds) failed')
            rval = False
    else:
        BookEndPrint('----- insert (index out of bounds) failed')
        rval = False

    # insert (index invalid type) **error**
    try:
        v16.insert('sixteen', val3)
    except ValueError:
        if v16.count() != 3 or \
                not float_eq(v16.getValueAt(0), val0) or \
                not float_eq(v16.getValueAt(1), val1) or \
                not float_eq(v16.getValueAt(2), val2):
            BookEndPrint('----- insert (index invalid type) failed')
            rval = False
    else:
        BookEndPrint('----- insert (index invalid type) failed')
        rval = False

    # insert (value out of range) **error**
    try:
        v16.insert(1, -1e309)
    except ValueError:
        if v16.count() != 3 or \
                not float_eq(v16.getValueAt(0), val0) or \
                not float_eq(v16.getValueAt(1), val1) or \
                not float_eq(v16.getValueAt(2), val2):
            BookEndPrint('----- insert (value out of range) failed')
            rval = False
    else:
        BookEndPrint('----- insert (value out of range) failed')
        rval = False
    try:
        v16.insert(1, 1e309)
    except ValueError:
        if v16.count() != 3 or \
                not float_eq(v16.getValueAt(0), val0) or \
                not float_eq(v16.getValueAt(1), val1) or \
                not float_eq(v16.getValueAt(2), val2):
            BookEndPrint('----- insert (value out of range) failed')
            rval = False
    else:
        BookEndPrint('----- insert (value out of range) failed')
        rval = False

    # value type invalid
    try:
        v16.insert(1, 'sixteen')
    except ValueError:
        if v16.count() != 3 or \
                not float_eq(v16.getValueAt(0), val0) or \
                not float_eq(v16.getValueAt(1), val1) or \
                not float_eq(v16.getValueAt(2), val2):
            BookEndPrint('----- insert (value invalid type) failed')
            rval = False
    else:
        BookEndPrint('----- insert (value invalid type) failed')
        rval = False

    # pop
    v17 = MI_Real64A((val0, val1, val2, val3))
    t17 = v17.pop()
    if not float_eq(t17, val3) or \
            v17.count() != 3 or \
            not float_eq(v17.getValueAt(0), val0) or \
            not float_eq(v17.getValueAt(1), val1) or \
            not float_eq(v17.getValueAt(2), val2):
        BookEndPrint('----- pop failed')
        rval = False
    t17 = v17.pop(1)
    if not float_eq(t17, val1) or \
            v17.count() != 2 or \
            not float_eq(v17.getValueAt(0), val0) or \
            not float_eq(v17.getValueAt(1), val2):
        BookEndPrint('----- pop failed')
        rval = False
    v17.insert(1, val1)
    t17 = v17.pop(0)
    if not float_eq(t17, val0) or \
            v17.count() != 2 or \
            not float_eq(v17.getValueAt(0), val1) or \
            not float_eq(v17.getValueAt(1), val2):
        BookEndPrint('----- pop failed')
        rval = False
    v17.insert(0, val0)
    t17 = v17.pop(2)
    if not float_eq(t17, val2) or \
            v17.count() != 2 or \
            not float_eq(v17.getValueAt(0), val0) or \
            not float_eq(v17.getValueAt(1), val1):
        BookEndPrint('----- pop failed')
        rval = False

    # pop (negative indices)
    v18 = MI_Real64A((val0, val1, val2))
    t18 = v18.pop(-2)
    if not float_eq(t18, val1) or \
            v18.count() != 2 or \
            not float_eq(v18.getValueAt(0), val0) or \
            not float_eq(v18.getValueAt(1), val2):
        BookEndPrint('----- pop failed')
        rval = False
    v18.insert(1, val1)
    t18 = v18.pop(-3)
    if not float_eq(t18, val0) or \
            v18.count() != 2 or \
            not float_eq(v18.getValueAt(0), val1) or \
            not float_eq(v18.getValueAt(1), val2):
        BookEndPrint('----- pop failed')
        rval = False
    v18.insert(0, val0)
    t18 = v18.pop(-1)
    if not float_eq(t18, val2) or \
            v18.count() != 2 or \
            not float_eq(v18.getValueAt(0), val0) or \
            not float_eq(v18.getValueAt(1), val1):
        BookEndPrint('----- pop failed')
        rval = False

    # pop (empty array) **error**
    v19 = MI_Real64A()
    try:
        v19.pop()
    except IndexError:
        pass
    else:
        BookEndPrint('----- pop (empty array) failed')
        rval = False

    v20 = MI_Real64A((val0, val1, val2))
    try:
        v20.pop(3)
    except IndexError:
        if v20.count() != 3 or \
                not float_eq(v20.getValueAt(0), val0) or \
                not float_eq(v20.getValueAt(1), val1) or \
                not float_eq(v20.getValueAt(2), val2):
            BookEndPrint('----- pop (index out of range) failed')
            rval = False
    else:
        BookEndPrint('----- pop (index out of range) failed')
        rval = False
    try:
        v20.pop(-4)
    except IndexError:
        if v20.count() != 3 or \
                not float_eq(v20.getValueAt(0), val0) or \
                not float_eq(v20.getValueAt(1), val1) or \
                not float_eq(v20.getValueAt(2), val2):
            BookEndPrint('----- pop (index out of range) failed')
            rval = False
    else:
        BookEndPrint('----- pop (index out of range) failed')
        rval = False

    # pop (index invalid type) **error**
    try:
        v20.pop('twenty')
    except ValueError:
        if v20.count() != 3 or \
                not float_eq(v20.getValueAt(0), val0) or \
                not float_eq(v20.getValueAt(1), val1) or \
                not float_eq(v20.getValueAt(2), val2):
            BookEndPrint('----- pop (index invalid type) failed')
            rval = False
    else:
        BookEndPrint('----- pop (index invalid type) failed')
        rval = False

    # test get value
    vals21 = (val0, val1, val2, val3)
    v21 = MI_Real64A(vals21)
    i = 0
    for v in v21:
        if not float_eq(v.value, vals21[i]):
            BookEndPrint('----- iterator (get value) failed')
            rval = False
        i += 1

    # iterator set value
    v22 = MI_Real64A((val0, val1, val2))
    vals22 = (val1, val2, val3)
    i = 0
    for v in v22:
        v.value = vals22[i]
        i += 1
    if v22.count() != 3 or \
            not float_eq(v22.getValueAt(0), val1) or \
            not float_eq(v22.getValueAt(1), val2) or \
            not float_eq(v22.getValueAt(2), val3):
        BookEndPrint('----- iterator (set value) failed')
        rval = False

    # iterator set value (out of range) **error**
    for v in v22:
        try:
            v.value = -1e309
        except ValueError:
            if v22.count() != 3 or \
                    not float_eq(v22.getValueAt(0), val1) or \
                    not float_eq(v22.getValueAt(1), val2) or \
                    not float_eq(v22.getValueAt(2), val3):
                BookEndPrint('----- iterator (set value out of range) failed')
                rval = False
        else:
            BookEndPrint('----- iterator (set value out of range) failed')
            rval = False
    for v in v22:
        try:
            v.value = 1e309
        except ValueError:
            if v22.count() != 3 or \
                    not float_eq(v22.getValueAt(0), val1) or \
                    not float_eq(v22.getValueAt(1), val2) or \
                    not float_eq(v22.getValueAt(2), val3):
                BookEndPrint('----- iterator (set value out of range) failed')
                rval = False
        else:
            BookEndPrint('----- iterator (set value out of range) failed')
            rval = False

    # iterator set value (invalid type)
    for v in v22:
        try:
            v.value = 'twenty-two'
        except ValueError:
            if v22.count() != 3 or \
                    not float_eq(v22.getValueAt(0), val1) or \
                    not float_eq(v22.getValueAt(1), val2) or \
                    not float_eq(v22.getValueAt(2), val3):
                BookEndPrint('----- iterator (set value invalid type) failed')
                rval = False
        else:
            BookEndPrint('----- iterator (set value invalid type) failed')
            rval = False

    if not rval:
        BookEndPrint('!!!!!  Tests have failed! (MI_Real64A)')

    return rval
