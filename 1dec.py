import hashlib
import functools


@functools.singledispatch
def hash(arg):
    type_name = type(arg).__name__
    assert False, "Неподдерживаемый тип объекта: " + type_name


@hash.register(str)
def _(arg):
    result = hashlib.md5(bytes(arg, 'utf-8')).hexdigest()
    return result

@hash.register(list)
def _(arg):
    result = type(arg)()
    for i in arg:
        result.append(hashlib.md5(bytes(i, 'utf-8')).hexdigest())
    return result


@hash.register(tuple)
def _(arg):
    result = []
    for i in arg:
        result.append(hashlib.md5(bytes(i, 'utf-8')).hexdigest())
    return tuple(result)


@hash.register(set)
def _(arg):
    result = []
    for i in arg:
        result.append(hashlib.md5(bytes(i, 'utf-8')).hexdigest())
    return set(result)


@hash.register(dict)
def _(arg):
    keys = arg.keys()
    values = []
    for i in arg.values():
        values.append(hashlib.md5(bytes(i, 'utf-8')).hexdigest())
    result = dict.fromkeys(keys, None)
    result.update(zip(keys, values))
    return result


print(hash('Done'))
print(hash({'Hello': 'Goodbye', 'Hi': 'Bye'}))

if __name__ == '__main__':
    import unittest

    class MyTests(unittest.TestCase):

        def test1(self):
            self.assertEqual(hash("hello"), ("5d41402abc4b2a76b9719d911017c592"))
            self.assertEqual(hash("goodbye"), ("69faab6268350295550de7d587bc323d"))
        def test2(self):
            self.assertEqual(hash(["my", "name"]), (["6864f389d9876436bc8778ff071d1b6c","b068931cc450442b63f5b3d276ea4297"]))
            self.assertEqual(hash(["hello","world"]), (["5d41402abc4b2a76b9719d911017c592","7d793037a0760186574b0282f2f435e7"]))
        def test3(self):
            self.assertEqual(hash({"my": "name"}), ({"my":"b068931cc450442b63f5b3d276ea4297"}))
            self.assertEqual(hash({"hello": "world"}), ({"hello":"7d793037a0760186574b0282f2f435e7"}))

    unittest.main(verbosity=2)


