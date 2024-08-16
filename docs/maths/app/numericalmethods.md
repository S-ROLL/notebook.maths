# Numerical methods
## Nội suy
### Newton

- Sai phân tiến

$$
\begin{split}
f_n(x) &= f(x_0)+ (x-x_0)f[x_1,x_0]+ (x-x_0)(x-x_1)f[x_2,x_1,x_0] \\
&+ \ldots + (x-x_0)\ldots (x-x_{n-1})f[x_n,x_{n-1},\ldots , x_0] \\
\: \\
f[x_n,&x_{n-1},\ldots ,x_0] = \frac{f[x_n,x_{n-1},\ldots ,x_1]-f[x_{n-1},\ldots ,x_0]}{x_n-x_0}
\end{split}
$$

- Sai phân lùi

$$
\begin{split}
P_n(x) &= y_n + (x-x_n) + f[x_n,x_{n-1}] + (x-x_n)(x-x_{n-1})f[x_n,x_{n-1},x_{n-2}] \\
\: \\
&+ \ldots + (x-x_n) \ldots (x-x_1)f[x_n,x_{n-1}, \ldots , x_0] \\
\end{split}
$$

### Bình phương tối thiểu

- $y_i = a + bx_i$

$$
\begin{split}
\rightarrow \varepsilon _i &= y_i - a -bx_i \\
\: \\
S = \sum _{i=0}^n \varepsilon _i^2 &= \sum _{i=0}^n (y_i - a - bx_i)^2 \\
\: \\
S_{\text{min}} \Rightarrow
\left\{
  \begin{array}{rcr}
  S_a^{'} &=& 0 \\
  S_b^{'} &=& 0
  \end{array}
\right.
& \Rightarrow
\left\{
  \begin{array}{rcr}
  na + b \sum x_i &=& \sum y_i \\
  a \sum x_i + b \sum x_i^2 &=& \sum x_i y_i
  \end{array}
\right.
\end{split} \\
$$

- $y_i = a +bx_i +cx_i^2$

$$
S_{\text{min}} \Rightarrow
\left\{
  \begin{array}{rcr}
  na + b \sum x_i + c \sum x_i^2 &=& \sum y_i \\
  a \sum x_i + b \sum x_i^2 + c \sum x_i^3 &=& \sum x_i y_i \\
  a \sum x_i^2 +b \sum x_i^3 + c \sum x_i^4 &=& \sum x_i^2 y_i
  \end{array}
\right.
$$

## Đạo hàm & tích phân xác định
### Hình thang

$$
\begin{split}
I &= \frac{h}{2} [y_0 + 2(y_1 + \ldots + y_{n-1}) + y_n] \\
\: \\
| I - I_t | & \leq \frac{M}{12} h^2 (b-a) \\
h &= \frac{b-a}{n} \\
M &= \text{max}|f^{(2)}(x)|
\end{split}
$$

### Simpson

$$
\begin{split}
I = \frac{h}{3} [(y_0 + y_{2n}) + 4(y_1+y_3+ & \ldots + y_{2n-1}) + 2(y_2+y_4+ \ldots + y_{2n-2})] \\
\: \\
|I-I_s| & \leq \frac{M}{180} h^4 (b-a) \\
h &= \frac{b-a}{2n} \\
M &= \text{max} |f^{(4)}(x)|
\end{split}
$$

## Nghiệm phương trình phi tuyến
### Lặp đơn

$$
\left\{
  \begin{array}{rcr}
  x_0 & \text{chọn trước} \in [a;b] \\
  x_{n+1} &= \varphi (x_n) \: \: \forall n \geq 0
  \end{array}
\right.
$$

$$
\begin{split}
|x_n - \alpha | & \leq \frac{q}{1-q}|x_n - x_{n-1}| \\
| \varphi (x)^{'}| = \ldots &= q < 1 \: \: \forall x \in \text{khoảng}
\end{split}
$$

!!! Note
    - $\varphi (x)^{'}>0 \Rightarrow$ chon $x_0$ bat ky $\in [a,b]$.
    - $\varphi (x)^{'}<0 \Rightarrow$ chon $x_0$
    - $f(a)f(\frac{a+b}{2})<0 \Rightarrow x_0=a$
    - $f(b)f(\frac{a+b}{2})<0 \Rightarrow x_0=b$

### Newton - Raphson

$$
\left\{
  \begin{array}{rcr}
  x_0 & \text{chọn trước} \in [a;b] \\
  x_{n+1} &= x_n - \frac{f(x_n)}{f^{'}(x_n)} \: \: \forall n \geq 0
  \end{array}
\right.
$$

$$
\begin{split}
|x_n - \alpha | \leq \frac{|f(x_n)|}{m} & < \varepsilon \\
\Rightarrow |f(x_n)| & < m \varepsilon \\
0 < m = \text{min}|f^{'}(a \text{ or } b)| &\leq |f^{'}(x)| \\
\end{split}
$$

!!! note
    - $f(a)$ cung dau $f^{''} \Rightarrow x_0=a$ <br/>
    - $f(b)$ cung dau $f^{''} \Rightarrow x_0=b$ <br/>

### Dây cung

$$
\begin{split}
x_1 &= \frac{af(b) - bf(a)}{f(b)-f(a)} \\
\\
|x_n - \alpha | & \leq \frac{|f(x_n)|}{m} < \varepsilon \\
& \Rightarrow |f(x_n)| < m \varepsilon \\
0 < m &= \text{min}|f^{'}(a \text{ or } b)| \leq |f^{'}(x)| \\
\end{split}
$$

!!! note
    - $f(a)f(x_1) < 0 \rightarrow [a,x_1] \: \: \text{la KPL nghiem moi}$
    - $f(x_1)f(b) < 0 \rightarrow [x_1,b] \: \: \text{la KPL nghiem moi}$

## Nghiệm HPT

### Gauss

$$
\begin{split}
\overline{A} = (A|B) &= \left(\begin{array}{ccc|c}
a_{11} & a_{12} & a_{13} & b_{1} \\
a_{21} & a_{22} & a_{23} & b_{2} \\
a_{31} & a_{32} & a_{33} & b_{3}
\end{array}\right) \\
\\
& \text{max }\{|a_{11}|,|a_{12}|,|a_{13}|\} \\
\\
a^{'}_{12} &= \frac{a_{12}}{a_{11}}, a^{'}_{13}=\frac{a_{13}}{a_{11}},b^{'}_{1}=\frac{b_1}{a_{11}} \\
\\
a^{'}_{22}&=\frac{\begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{vmatrix}}{a_{11}}, a^{'}_{23}= \frac{\begin{vmatrix} a_{11} & a_{13} \\ a_{21} & a_{23} \end{vmatrix}}{a_{11}} , b^{'}_2= \frac{\begin{vmatrix} a_{11} & b_1 \\ a_{21} & b_2 \end{vmatrix}}{a_{11}}\\
\\
a^{'}_{32}&=\frac{\begin{vmatrix} a_{11} & a_{12} \\ a_{31} & a_{32} \end{vmatrix}}{a_{11}}, a^{'}_{33}= \frac{\begin{vmatrix} a_{11} & a_{13} \\ a_{31} & a_{33} \end{vmatrix}}{a_{11}} , b^{'}_3= \frac{\begin{vmatrix} a_{11} & b_1 \\ a_{31} & b_3 \end{vmatrix}}{a_{11}}\\
\end{split}
$$

$$
\begin{split}
& \text{lặp lại cho tới khi} \\
\\
\overline{A} &= \left(\begin{array}{ccc|c}
1 & a^{'}_{12} & a^{'}_{13} & b^{'}_{1} \\
0 & 1 & a^{''}_{23} & b^{''}_{2} \\
0 & 0 & 1 & b^{'''}_{3}
\end{array}\right) \\
\end{split}
$$

### Lặp đơn

$$
\begin{split}
AX&=b \Rightarrow X=BX+g \\
\end{split}
$$

$$
\left\{
  \begin{split}
  x^{(0)} &= g \\
  x^{m} &= Bx^{m-1}+g
  \end{split}
\right.
$$

$$
\begin{split}
\parallel x^{(m)}-x^*\parallel _p &\leq \frac{\parallel B \parallel_p^{(m)}}{1-\parallel B\parallel _p}\parallel x^{(0)}-x^{(1)}\parallel _p \: (p=0;1) \\
\\
\parallel B\parallel _0 &= \text{max} \sum |b_{ij}| (\text{theo dong}) < 1 \\
& \text{or} \\
\parallel B\parallel _1 &= \text{max} \sum |b_{ij}| (\text{theo cot}) < 1 \\
\end{split}
$$