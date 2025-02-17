# Không gian định chuẩn
## Metric

- **TXĐ:** $X \neq \varnothing$
- $\forall x, y, z \in X:$
    - $d(x,y) \geq 0$, $d(x,y) = 0 \Leftrightarrow x=y$
    - $d(x,y) = d(y,x)$
    - $d(x,y) \leq d(x,z) + d(z,y)$

## Định chuẩn
- **TXĐ:** $(X,+,\cdot)$
- $\forall x, y \in X$ và $\forall \alpha \in \mathbb{R}:$
    - $\|x \| \geq 0$, $\| x \| = 0 \Leftrightarrow x=0$
    - $\| \alpha x \| = |\alpha | \| x \|$
    - $\| x + y \| \leq \| x \| + \| y \|$


## Tập
- **TXĐ:**
    - $(X,d)$ là không gian metric
    - $a \in X$
    - $r > 0$
    - $A \subset X$

- **Quả cầu mở** (tâm $a$, bán kính $r$) trong $X$:

$$
B(a;r) = \{ x \in X | d(a,x) < r \}
$$

- **Quả cầu đóng** (tâm $a$, bán kính $r$) trong $X$:

$$
B'(a;r) = \{ x \in X | d(a,x) \leq r \}
$$

- **Mặt cầu** (tâm $a$, bán kính $r$) trong $X$:

$$
S(a;r) = \{ x \in X | d(a,x) = r \}
$$

### Tập mở

| ĐIỀU KIỆN | VẾ TRÁI || VẾ PHẢI |
|------|------|:------:|------|
| $(X,d)$ <br/> $a \in X$ <br/> $r > 0$ <br/> $A \subset X$ | $A$ là **tập mở** (trong $X$) | $\Leftrightarrow$ | $\forall x \in A$ <br/> $\exists r > 0$ <br/> $B(x;r) \subset A$ |

### Tập đóng

| ĐIỀU KIỆN | VẾ TRÁI || VẾ PHẢI |
|------|------|:------:|------|
| $(X,d)$ <br/> $a \in X$ <br/> $r > 0$ <br/> $A \subset X$ | $A$ là **tập đóng** (trong $X$) | $\Leftrightarrow$ | $X\setminus A$ tập mở |
| $(X,d)$ <br/> $a \in X$ <br/> $r > 0$ <br/> $A \subset X$ | $A$ là **tập đóng** (trong $X$) | $\Leftrightarrow$ | $A = \overline{A}$ (phần dính) |
| $(X,d)$ <br/> $a \in X$ <br/> $r > 0$ <br/> $A \subset X$ | $A$ là **tập đóng** (trong $X$) | $\Leftrightarrow$ | $\forall (x_n) \subset A : x_n \to x \in X \Rightarrow x \in A$ |
| $(X,d)$ <br/> $A \subset Y \subset X$ <br/> $Y$ đóng trong $X$ | $A$ đóng trong $Y$ | $\Leftrightarrow$| $A$ đóng trong $X$|



### Tập bị chặn

| ĐIỀU KIỆN | VẾ TRÁI || VẾ PHẢI |
|------|------|:------:|------|
| $(X,d)$ <br/> $a \in X$ <br/> $r > 0$ <br/> $A \subset X$ | $A$ là **tập bị chặn** | $\Leftrightarrow$ | $\exists a \in X$ <br/> $\exists r > 0$ <br/> $A \subset B(a;r)$ |


## Dãy
### Dãy hội tụ

| ĐIỀU KIỆN | VẾ TRÁI || VẾ PHẢI |
|------|------|:------:|------|
|$(X,d)$ <br/> $(x_n)$|$(x_n)$ **hội tụ** (trong $X$)|$\Leftrightarrow$| $\forall \epsilon > 0$ <br/> $\exists n_0 \in \mathbb{N}: \forall n \geq n_0$ <br/> $d(x_n, x) < \epsilon$|
|$(X,d)$ <br/> $(x_n)$|$(x_n)$ **hội tụ** (trong $X$)|$\Leftrightarrow$| $\exists x \in X: x_n \to x$ khi $n \to \infty$|
|$(X,d)$ <br/> $(x_n)$|$(x_n)$ **hội tụ** (trong $X$)|$\Leftrightarrow$| $\exists x \in X: d(x_n, x) \to 0$ khi $n \to \infty$ |

### Dãy Cauchy

| ĐIỀU KIỆN | VẾ TRÁI || VẾ PHẢI |
|------|------|:------:|------|
|$(X,d)$ <br/> $(x_n)$|$(x_n)$ **dãy Cauchy** (trong $X$)|$\Leftrightarrow$| $\forall \epsilon > 0$ <br/> $\exists n_0 \in \mathbb{N} : \forall m, n \geq n_0$ <br/> $d(x_m, x_n) < \epsilon$ |

### Dãy bị chặn

| ĐIỀU KIỆN | VẾ TRÁI || VẾ PHẢI |
|------|------|:------:|------|
|$(X,d)$ <br/> $(x_n)$|$(x_n)$ **dãy bị chặn** (trong $X$)|$\Leftrightarrow$| $\exists a \in X$ <br/> $\exists r > 0 : (x_n) \subset B(a;r)$ |
|$(X,d)$ <br/> $(x_n)$|$(x_n)$ **dãy bị chặn** (trong $X$)|$\Leftrightarrow$| $\forall n \in \mathbb{N}$ <br/> $x_n \in B(a;r)$ |

## Đầy đủ

| ĐIỀU KIỆN | VẾ TRÁI || VẾ PHẢI |
|------|------|:------:|------|
| $(X,d)$ | $(X,d)$ **đầy đủ** |$\Leftrightarrow$| $\forall (x_n) \subset X$ <br/> $(x_n)$ dãy Cauchy $\Rightarrow (x_n)$ hội tụ |

!!! tip
    - Lấy $(x_n) \subset X$
    - $(x_n)$ dãy Cauchy
    - C/m $(x_n)$ hội tụ.

## Compắc


| ĐIỀU KIỆN | VẾ TRÁI || VẾ PHẢI |
|------|------|:------:|------|
| $(X,d)$ | $(X,d)$ **compắc** | $\Leftrightarrow$ | $\forall (x_n) \subset X$ <br/> $\exists (x_{n_k}) \subset (x_n)$ : $(x_{n_k})$ hội tụ |

!!! tip
    - Lấy $(x_n) \subset X$
    - C/m $(x_n)$ có dãy con $(x_{n_k}) \subset (x_n)$ sao cho $(x_{n_k})$ hội tụ.

<!-- ## Thu hẹp
## Metric tích

$x = (x_1, x_2, \ldots , x_n) \in X$

$y = (y_1, y_2, \ldots , y_n) \in X$

$X = X_1 \times X_2 \times \ldots \times X_n$

$$
d(x,y) = \sqrt{\sum_{i=1}^n d_i^2 (x_i, y_i)}
$$


## Ánh xạ liên tục

$(X,d)$

$(Y,d)$

$f : X \to Y$

- $f$ liên tục tại $a \in X$
    - $\forall \epsilon >0$
    - $\exists \delta > 0$
    - $\forall x \in X$
    - $d_X (x,a) < \delta \Rightarrow d_Y(f(x), f(a)) < \epsilon$
    
    *hoặc*

    - $\forall \epsilon >0$
    - $\exists \delta > 0$
    - $\forall x \in X$
    - $x \in B_X(a,\delta) \Rightarrow f(x) \in B_Y(f(a), \epsilon)$

    *hoặc*

    - $\forall (x_n) \subset X$
    - $x_n \to a \Rightarrow f(x_n) \to f(a)$

- $f$ liên tục trên $X$
    - $f$ liên tục tại mọi $x \in X$ -->

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