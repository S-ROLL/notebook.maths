# Giải tích hàm

## C1: Không gian metric
## C2: Không gian định chuẩn

### VD1

Cho $X=C[0;1]$ là không gian các ánh xạ liên tục $f:[0;1] \to \mathbb{R}$. Với mỗi $f \in X$, đặt $\parallel f \parallel _X = \underset{t \in [0;1]}{\max}|f(t)|$. Xét

$$
\begin{split}
T : X &\to& &\mathbb{R} \\
f &\mapsto& &T(f) = f(0) - 2f(1)
\end{split}
$$

a) Chứng minh $T$ là ánh xạ tuyến tính liên tục.

b) Tính $\parallel T \parallel _{L(X, \mathbb{R})}$.

### VD2

Cho $X=C[1;2]$ là không gian các ánh xạ liên tục $f:[1;2] \to \mathbb{R}$. Với mỗi $f \in X$, đặt $\parallel f \parallel _X = \underset{t \in [1;2]}{\max}|f(t)|$. Xét

$$
\begin{split}
T : X &\to& &\mathbb{R} \\
f &\mapsto& &T(f) = f\bigg( \frac{3}{2} \bigg) - 2f(2)
\end{split}
$$

a) Chứng minh $T$ là ánh xạ tuyến tính liên tục.

b) Tính $\parallel T \parallel _{L(X, \mathbb{R})}$.

### VD3

Cho $X=C[0;1]$ là không gian các ánh xạ liên tục $f:[0;1] \to \mathbb{R}$. Với mỗi $f \in X$, đặt $\parallel f \parallel _X = \underset{t \in [0;1]}{\max}|f(t)|$. Xét

$$
\begin{split}
T : X &\to& &X \\
f &\mapsto& &T(f)
\end{split}
$$

Trong đó $T(f)$ là hàm cho bởi $T(f)(t) = f(0) - tf(t), \: \forall t \in [0;1]$.

a) Chứng minh $T$ là ánh xạ tuyến tính liên tục.

b) Tính $\parallel T \parallel _{L(X, X)}$.


## C3: Định lý

### VD1

Cho $(\mathbb{R}^2, \parallel \cdot \parallel)$ là không gian định chuẩn với $\parallel \cdot \parallel \: : \: \mathbb{R}^2 \to \mathbb{R}$ được xác định bởi $\parallel x \parallel = \sqrt{x_1^2 + x_2^2}, \: \forall x = (x_1, x_2) \in \mathbb{R}^2$. Trên $(\mathbb{R}^2, \parallel \cdot \parallel)$, cho không gian con $M = \{ (x_1, x_2) \in \mathbb{R}^2 : x_1 = x_2 \}$ và phiếm hàm $f$ tuyến tính liên tục thoả $f(x) = x_1 + x_2, \: \forall x = (x_1, x_2) \in M$. Theo định lý Hahn-Banach tồn tại phiếm hàm $f$ tuyến tính liên tục trên $\mathbb{R}$ sao cho $F(x) = f(x), \: \forall x \in M$ và $\parallel F \parallel _{L(\mathbb{R}^2, \mathbb{R})} = \parallel f \parallel _{L(M,\mathbb{R})}$. Tìm $F$.


## C5: Không gian Hilbert

### VD1

Cho $H=\mathbb{R}^3$ với tích vô hướng thông thường. Xét

$$
\begin{split}
T : \mathbb{R}^3 &\to& &\mathbb{R} \\
x = (x_1, x_2, x_3) &\mapsto& &T(x) = 2x_1 - x_2 + 3x_3
\end{split}
$$

a) Chứng minh $T$ là ánh xạ tuyến tính liên tục.

b) Tìm $y \in H, \: T(x) = \langle x, y \rangle, \: \forall x \in H$.

c) Tính $\parallel T \parallel _{H^*}$ và $\parallel y \parallel _H$.