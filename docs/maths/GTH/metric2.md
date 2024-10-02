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

!!! note
    $\overline{A}$ là **tập đóng** & là **tập đóng nhỏ nhất** chứa $A$

### Phần trong ($\overset{\circ}{A}$)

| ĐIỀU KIỆN | VẾ TRÁI || VẾ PHẢI |
|------|------|:------:|------|
| $(X,d)$ <br/> $A \subset X$ <br/> $a \in X$ | $x \in \overset{\circ}{A}$ | $\Leftrightarrow$ | $\exists r > 0$ <br/> $B(x,r) \subset A$ |



!!! note
    - $\overset{\circ}{A}$ là **tập mở** & là **tập mở lớn nhất** chứa trong $A$

    - $\overset{\circ}{A} \subset A \subset \overline{A}$

## Vết của tập mở (đóng)

!!! note
    - $\forall a \in Y$, $\forall r > 0$
        - $B_Y(a,r) = Y \cap B_X(a,r)$
    
    - $V \subset X$, $V \cap Y$ là **vết** của $V$ lên $Y$

| ĐIỀU KIỆN | VẾ TRÁI || VẾ PHẢI |
|------|------|:------:|------|
| $(X,d)$ <br/> $A \subset Y \subset X$ <br/> $Y \neq \varnothing$ | $A$ **mở** trong $Y$ | $\Leftrightarrow$ | $\exists V$ mở trong $X$ <br/> $A = V \cap Y$ |
| $(X,d)$ <br/> $A \subset Y \subset X$ <br/> $Y \neq \varnothing$ | $A$ **đóng** trong $Y$ | $\Leftrightarrow$ | $\exists F$ đóng trong $X$ <br/> $A = F \cap Y$ |
| $(X,d)$ <br/> $A \subset Y \subset X$ <br/> $Y \neq \varnothing$ | $A$ **mở (đóng)** trong $Y$ | $\Leftrightarrow$ | $A$ là vết của tập mở (đóng) trong $X$ lên $Y$ |
| $(X,d)$ <br/> $A \subset Y \subset X$ <br/> $Y \neq \varnothing$ | $A$ **mở (đóng)** trong $X$ | $\Rightarrow$ | $A$ mở (đóng) trong $Y$ |
| $(X,d)$ <br/> $A \subset Y \subset X$ <br/> $Y \neq \varnothing$ | $A$ **mở (đóng)** trong $Y$ <br/> $Y$ **mở (đóng)** trong $X$ | $\Rightarrow$ | $A$ mở (đóng) trong $X$ |


## Kgian metric con đầy đủ, compắc

| ĐIỀU KIỆN | VẾ TRÁI || VẾ PHẢI |
|------|------|:------:|------|
| $(X,d)$ <br/> $Y \subset X$ | $Y$ **đầy đủ** | $\Rightarrow$ | $Y$ đóng trong $X$ |
| $(X,d)$ <br/> $Y \subset X$ | $Y$ **đóng** trong $X$ <br/> $X$ **đầy đủ** | $\Rightarrow$ | $Y$ đầy đủ |
| $(X,d)$ <br/> $\varnothing \neq Y \subset X$ | $Y$ **compac** | $\Rightarrow$ | $Y$ đầy đủ <br/> $Y$ bị chặn (tập đóng)|
| $(X,d)$ <br/> $\varnothing \neq Y \subset X$ | $Y$ **đóng** trong $X$ <br/> $X$ **compac** | $\Rightarrow$ | $Y$ compac|


## Tiền compắc

| ĐIỀU KIỆN | VẾ TRÁI || VẾ PHẢI |
|------|------|:------:|------|
|$(X,d)$|$X$ **tiền compac** | $\Leftrightarrow$ | $\forall \epsilon > 0$ <br/> $\exists x_1, x_2 , \ldots, x_n \in X$ <br/> $X \subset \mathop{\bigcup}\limits_{i=1}^{n} B(x_i, \epsilon)$ |
| $(X,d)$ | $X$ **compac** | $\Leftrightarrow$ | $X$ tiền compac <br/> $X$ đầy đủ |


## Ánh xạ liên tục