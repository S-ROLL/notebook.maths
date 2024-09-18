# Ordinary differential equation
## PTVP CẤP 1
### Tách biến

$$
f(x)dx = g(y)dy
$$

phuong phap

$$
\begin{split}
& \int f(x) dx = \int g(y)dy \\
& F(x) = G(y) + C
\end{split}
$$

### Tuyến tính cấp 1
#### Thuần nhất

$$
y' + p(x)y = 0
$$

phuong phap

$$
\begin{split}
\frac{dy}{dx} &= -p(x)y \\
\frac{1}{y}dy &= -p(x)dx \\
\int \normalsize \frac{1}{y} dy &= -\int p(x)dx \\
\ln |y| &= -\int p(x)dx + \ln |c| \\
\ln |y| - \ln |c| &= -\int p(x)dx \\
\ln |\frac{y}{c}| &= -\int p(x)dx \\
\frac{y}{c} &= e^{-\int p(x)dx} \\
y &= c.e^{-\int p(x)dx}
\end{split}
$$

#### Không thuần nhất

$$
y' + p(x)y = q(x)
$$

phuong phap (biến thiên hằng số)

$$
y' + p(x)y = 0 \implies 
y = C.e^{-\int p(x)dx}
$$

$$
C = C(x)
$$

$$
\begin{cases}
y = C(x).e^{-\int p(x)dx} \\
y' = C'(x).e^{-\int p(x)dx} - p(x)C(x).e^{-\int p(x)dx} \\
\end{cases}
$$

$$\begin{split}
\implies y' + p(x)y &= q(x) \\
C'(x).e^{-\int p(x)dx} - p(x)C(x).e^{-\int p(x)dx}& + p(x)C(x).e^{-\int p(x)dx} = q(x) \\
C'(x).e^{-\int p(x)dx} &= q(x) \\
C'(x) = q(x).&e^{\int p(x)dx} \\
C(x) = \int q(x).&e^{\int p(x)dx} dx +K
\end{split}$$

$$\begin{split}
\implies y &= C(x).e^{-\int p(x)dx} \\
y &= \Bigg(\int q(x).e^{\int p(x)dx} dx +K \Bigg)e^{-\int p(x)dx} \\
\end{split}$$

### Bernoulli

$$
y' + p(x)y = q(x).y^{\alpha}
$$

phuong phap

$$
y^{-\alpha}.y' + p(x)y^{1-\alpha} = q(x)
$$

$$\begin{split}
z &= y^{1- \alpha} \\
z' &= (1-\alpha).y^{-\alpha}.y' \\
y^{-\alpha}.y' &= \frac{1}{1-\alpha} z' \\
\end{split}$$

$$\begin{split}
\implies y^{-\alpha}.y' + p(x)y^{1-\alpha} &= q(x) \\
\frac{1}{1-\alpha} z' + p(x).z &= q(x) \\
z' + (1-\alpha)p(x).z &= q(x)(1-\alpha)
\end{split}$$

### Toàn phần

$$
P(x,y)dx + Q(x,y)dy=0
$$

$$
P'_y = Q'_x
$$

$$\begin{split}
u(x,y) &= \int_{x_0}^x P(x,y_0)dx + \int_{y_0}^y Q(x,y)dy+C \\
&\text{or} \\
u(x,y) &= \int_{x_0}^x P(x,y)dx + \int_{y_0}^y Q(x_0,y)dy+C \\
\end{split}$$

## PTVP CẤP 2
### Thuần nhất 

$$y'' + py' + qy = 0$$

phuong phap

$$
\lambda ^2 + p\lambda + q = 0 \implies \text{ giai ptrinh } \implies \lambda _1, \lambda _2 
$$

- $\lambda _1 \neq \lambda _2 \implies y = C_1.e^{\lambda _1x}+C_2.e^{\lambda _2x}$
- $\lambda _1 = \lambda _2 = \lambda \implies y = (C_1+x.C_2)e^{\lambda x}$
- $\lambda _{1,2}=\alpha \pm i \beta \implies y = e^{\alpha x}(C_1.\cos \beta x + C_2.\sin \beta x)$

### Không thuần nhất

$$
y'' + py' + qy = f(x)
$$

#### 1) $f(x) = e^{ax} Q_n(x)$

phuong phap

$$
y'' + py'+qy = 0 \implies \lambda _1, \lambda _2 \implies y_{tn}
$$

$$\scriptsize (P_n(x) \text{ cung bac voi } Q_n(x), \text{vi du: } P_n(x)=Ax+B)$$

- $a \neq \lambda _1 \: \land \: a \neq \lambda _2 \implies y_r = e^{ax}P_n(x)$ 
- $a = \lambda _1 \lor a = \lambda _2 \implies y_r = xe^{ax}P_n(x)$
- $a = \lambda _1 = \lambda _2 \implies y_r = x^2 e^{ax}P_n(x)$

$$
\begin{split}
\implies y'' + py' + qy &= f(x) \\
y''_r + py'_r + qy_r &= f(x) \\
\implies \text{ He so $A$, $B$,\ldots} \implies & y_r \implies y = y_{tn} + y_r
\end{split}
$$

#### 2) $f(x) = P_n(x)\sin \beta x + Q_m(x)\cos \beta x$

phuong phap

$$
y'' + py'+qy = 0 \implies \lambda _1, \lambda _2 \implies y_{tn}
$$

$$\scriptsize l=\max \{m,n\} \\ R_l(x)=Ax+B \quad H_l(x)=Cx+D$$

- $\pm i\beta \neq \lambda _{1,2} \implies y_r = R_l(x) \sin \beta x + H_l(x) \cos \beta x$
- $\pm i\beta = \lambda _{1,2} \implies y_r = x\big(R_l(x) \sin \beta x + H_l(x) \cos \beta x\big)$

$$
\begin{split}
\implies y'' + py' + qy &= f(x) \\
y''_r + py'_r + qy_r &= f(x) \\
\implies \text{ He so $A$, $B$,$C$,$D$, \ldots} \implies & y_r \implies y = y_{tn} + y_r
\end{split}
$$

#### 3) Biến thiên hằng số

$$
y'' + py'+qy = 0 \implies \lambda _2, \lambda _2 \implies y_{tn} = C_1.y_1(x) + C_2.y_2(x)
$$

$$
C_1 = C_1(x) \\
C_2 = C_2(x) \\
$$

$$
\text{HPT } \implies \begin{cases}
C'_1y_1 + C'_2y_2 = 0 \\
C'_1y'_1 + C'_2y'_2 = f(x)
\end{cases}
\implies C'_1, C'_2 \implies C_1, C_2
$$

$$\implies y = C_1.y_1(x) + C_2.y_2(x)$$

## HỆ PTVP

$$
\begin{cases}
y_1' = f_1(x, y_1, y_2, \ldots, y_n) \\
y_2' = f_2(x, y_1, y_2, \ldots, y_n) \\
\vdots \\
y_n' = f_n(x, y_1, y_2, \ldots, y_n) \\
\end{cases}
$$

### Thế (khử)

$$
\begin{cases}
y' = y + z \quad (1) \\
z' = y + z \quad (2)
\end{cases}
$$

phuong phap

$$
(1) \implies z(y), z'(y) \implies \text{ the vao } (2) \implies z'(y) = y + z(y) \implies \text{ PTVP C2.}
$$

### Vector riêng 

$$
\begin{cases}
\frac{dy}{dt} = y + z \\
\frac{dz}{dt} = y + z
\end{cases}
$$

phuong phap

$$
\implies
\begin{cases}
y' = y + z \\
z' = y + z
\end{cases}
\implies
\begin{cases}
\begin{array}{ccccc}
y' & -y & -z & & = 0 \\
& -y & + z' & +z & =0
\end{array}
\end{cases} (*)
$$

từ $(*) \implies$ pt đặc trưng:

$$
\begin{vmatrix}
\lambda -1 & -1 \\
-1 & \lambda + 1 \\
\end{vmatrix}
= 0 \implies \lambda _1, \lambda _2
$$

voi $\lambda _1$ :

$$
\begin{pmatrix}
\lambda _1 -1 & -1 \\
-1 & \lambda _1 + 1 \\
\end{pmatrix}
\begin{pmatrix}
p_1 \\
p_2
\end{pmatrix}
= 0 
$$

$$
\implies 
\begin{cases}
\text{if } \quad p_1 = k p_2 \implies p_2 = 1 \implies u_1(p_1, p_2). \\
\text{if } \quad p_2 = k p_1 \implies p_1 = 1 \implies u_1(p_1, p_2). \\
\end{cases}
$$

$$
\implies
\begin{cases}
y_1 = p_1 e^{\lambda _1 x} = p_1 e^{\lambda _1 t} \\
z_1 = p_2 e^{\lambda _1 x} = p_2 e^{\lambda _1 t} \\
\end{cases}
$$

voi $\lambda _2$ :

$$
\begin{pmatrix}
\lambda _2 -1 & -1 \\
-1 & \lambda _2 + 1 \\
\end{pmatrix}
\begin{pmatrix}
p_1 \\
p_2
\end{pmatrix}
= 0 
$$

$$ 
\implies 
\begin{cases}
\text{if } \quad p_1 = k p_2 \implies p_2 = 1 \implies u_2(p_1, p_2). \\
\text{if } \quad p_2 = k p_1 \implies p_1 = 1 \implies u_2(p_1, p_2). \\
\end{cases}
$$

$$
\implies
\begin{cases}
y_2 = p_1 e^{\lambda _2 x} = p_1 e^{\lambda _2 t} \\
z_2 = p_2 e^{\lambda _2 x} = p_2 e^{\lambda _2 t} \\
\end{cases}
$$

Ket luan:

$$
\implies
\begin{cases}
y = C_1 y_1 + C_2 y_2 \\
z = C_1 z_1 + C_2 z_2 \\
\end{cases}
$$

## ỨNG DỤNG
### Toả nhiệt, hấp thụ nhiệt

$$
T(t) = T_{\alpha} + (T_0 - T_{\alpha})e^{-rt}
$$

!!! info
    - $T_{\alpha}$: Nhiệt độ môi trường.
    - $T_0$: Nhiệt độ ban đầu.
    - $r$: Hệ số tỉ lệ.

### Rơi tự do

$$
mv'=mg-Kv
$$

### Hỗn hợp

$$
\frac{dy}{dt}= \text{(Tốc độ vào)} - \text{(Tốc độ ra)}
$$