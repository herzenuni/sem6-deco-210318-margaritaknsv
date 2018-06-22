import functools

def once(func):
	@functools.wraps(func)
	def inner(*args, **kwargs):
		if not inner.called:
			inner.result = func(*args, **kwargs)
			inner.called = True

		return inner.result

	inner.called = False
	return inner


@once
def initset():
  print("Initialization")
  return 2**2


print(initset())
print(initset())