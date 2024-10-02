# Kết quả
## Giao/hợp các tập mở (đóng)
- **TXD:**
    - $(X,d)$
    - $\forall i \in I$
    - $(A_i)_{i \in I} \subset X$
    - $A_i=\varnothing$
### Mở
- $A_i$ mở $\Rightarrow$ $\underset{i \in I}{\bigcup} A_i$ mở
- $A_i$ mở ($I$ hữu hạn)$\Rightarrow$ $\underset{i \in I}{\bigcap}A_i$ mở
### Đóng
- $A_i$ đóng $\Rightarrow$ $\underset{i \in I}{\bigcap}A_i$ đóng
- $A_i$ đóng ($I$ hữu hạn) $\Rightarrow$ $\underset{i \in I}{\bigcup} A_i$ đóng
## Phần dính, phần trong
### Phần dính ($\overline{A}$)

| ĐIỀU KIỆN | VẾ TRÁI || VẾ PHẢI |
|------|------|:------:|------|
|$(X,d)$ <br/> $A \subset X$ <br/> $a \in X$|$x \in \overline{A}$| $\Leftrightarrow$ |$\forall r > 0$ <br/> $B(x,r) \cap A \neq \varnothing$|
|$(X,d)$ <br/> $A \subset X$ <br/> $a \in X$ <br/> $x \in X$|$x \in \overline{A}$|$\Leftrightarrow$|$\exists (x_n) \subset A : x_n \to x \in X \Rightarrow x \in A$|
| $(X,d)$ <br/> $A \subset X$ <br/> $x \in X$ |$x \in \overline{A}$| $\Leftrightarrow$ | $\exists (x_n) \subset A : x_n \to x \text{ khi } n \to \infty$|

!!! info
    - $\overline{A}$
        - Tập đóng
        - Tập đóng nhỏ nhất chứa $A$

### Phần trong ($\overset{\circ}{A}$)

| ĐIỀU KIỆN | VẾ TRÁI || VẾ PHẢI |
|------|------|:------:|------|
| $(X,d)$ <br/> $A \subset X$ <br/> $a \in X$ | $x \in \overset{\circ}{A}$ | $\Leftrightarrow$ | $\exists r > 0$ <br/> $B(x,r) \subset A$ |



!!! info
    - $\overset{\circ}{A}$
        - Tập mở
        - Tập mở lớn nhất chứa trong $A$

!!! note
    $\overset{\circ}{A} \subset A \subset \overline{A}$

## Vết của tập mở (đóng)

!!! info
    - $\forall a \in Y$, $\forall r > 0$
        - $B_Y(a,r) = Y \cap B_X(a,r)$


## Tiền compắc
## Ánh xạ liên tục