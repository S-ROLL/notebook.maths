## Important Information
### Useful list
- [Integer programming](https://en.wikipedia.org/wiki/Integer_programming)
- [Computational complexity theory](https://en.wikipedia.org/wiki/Computational_complexity_theory)
- [Branch and bound](https://en.wikipedia.org/wiki/Branch_and_bound)
### Checking list
- [ ] [Convex optimization](https://en.wikipedia.org/wiki/Convex_optimization)
- [ ] [Interior-point method](https://en.wikipedia.org/wiki/Interior-point_method)
- [ ] [Cutting-plane method](https://en.wikipedia.org/wiki/Cutting-plane_method)
- [ ] [Nonlinear programming](https://en.wikipedia.org/wiki/Nonlinear_programming)
### Octave
- Checking O(n)
```
n = 1:100;
big_o = 2 .^n;
for i = 1:rows(n)
  for j = 1:columns(n)
    disp(sprintf("2 ^ %d = %d", n(i, j), big_o(i, j)));
  end
end
```
