function* accumulate<T>(
  iterable: Iterable<T>,
  func: (x: T, y: T) => T,
  initial?: T
) {
  let x = initial
  if (x !== undefined) yield x

  for (let y of iterable) {
    x = x === undefined ? y : func(x, y)
    yield x
  }
}
