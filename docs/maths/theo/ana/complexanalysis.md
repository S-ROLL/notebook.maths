# Complex analysis
## Công thức quan trọng

$$ \large
\begin{split}
z &= x + iy \\
\overline{z} &= x - iy \\
|z| &= \sqrt{x^2 + y^2} \\
|z|^2 &= z \overline{z} \\
|z|&=1 \: \: (z = \cos \varphi + i \sin \varphi )\\
\overline{z} &= \cos \varphi - i \sin \varphi \\
&= \frac{1}{\cos \varphi + i\sin \varphi} \\
&= \frac{1}{z} \\
e^{i \varphi} &= \cos \varphi + i\sin \varphi \\
\cos z &= \frac{e^{iz}+e^{-iz}}{2} \\
\sin z &= \frac{e^{iz}-e^{-iz}}{2i} \\
\\
|z|=R &\rightarrow z = r e^{i \varphi} \\
|z - z_0| = R &\rightarrow z = z_0 + Re^{it} \\
\\
z_k &= \sqrt[n]{|z|} \times e^{i \frac{(k-1)2 \pi + argZ}{n}} \\
\\
|z+w| &\leq |z| + |w| \:\:\:\: \text{for all $z,w \in C$}\\
\end{split}
$$

## PT đường tròn

$$
\begin{split}
(u-a)^2&+(v-b)^2=R^2 \\
\\
u^2+v^2-&2au-2bv+c=0 \\
R^2 &= a^2+b^2-c \\
I&(a;b) \\
\end{split}
$$

## Cauchy - Riemann

$$
\left\{ \Large
  \begin{array}{rcr}
    \frac{\partial u}{\partial x} & = & \frac{\partial v}{\partial y} \\
    \frac{\partial u}{\partial y} & = & - \frac{\partial v}{\partial x} \\
  \end{array}
\right.
\:\:\:\: \text{or} \:\:\:\: \frac{\partial f}{\partial \overline{z}} = 0
$$

## Linear rational function (Hàm phân tuyến tính)

$$
\begin{split}
w = f(z) &= \frac{az+b}{cz+d} \: (c \ne 0) \\
\delta &= - \frac{d}{c}
\end{split}
$$

$\Delta$ la duong tron trong $\overline{\mathbb{C}}$

- $\Delta$ di qua $\delta$ <br/>
$\rightarrow f(\Delta)$ chua $\infty$. <br/>
$\rightarrow f(\Delta)$ la duong thang.

- $\Delta$ khong di qua $\delta$ <br/>
$\rightarrow f(\Delta)$ ko chua $\infty$. <br/>
$\rightarrow f(\Delta)$ la duong tron.

## Dinh ly Cauchy

### Don lien

$$
\int _{\gamma} f(z)dz=0, \forall \gamma \text{ chu tuyen tron trong } D
$$

### Da lien

$$
\begin{split}
\int _{\gamma D} f(z)dz &=0 \\
\int _{\gamma D} f(z)dz = \int_{\gamma_1^+} f(z)dz &+ \int_{\gamma_2^-}f(z)dz + \ldots + \int_{\gamma_n}f(z)dz \\
\end{split}
$$

## CT tich phan Cauchy (Cauchy's Integral Formula) [proof](https://math.libretexts.org/Bookshelves/Analysis/Complex_Variables_with_Applications_(Orloff)/05%3A_Cauchy_Integral_Formula/5.03%3A_Proof_of_Cauchy%27s_integral_formula)

$$
f^{(n)}(z_0)=\frac{n!}{2\pi i}\int_{\gamma D} \frac{f(z)dz}{(z-z_0)^{n+1}}
$$

## Khai triển Taylor

$$
\begin{split}
f(z) &= \sum _{n=0}^{\infty} C_n (z-z_0)^n \\
\\
C_n &= \frac{f^{(n)}(z_0)}{n!} \\
&= \frac{1}{2 \pi i} \int _{\gamma D} \frac{f(z)dz}{(z-z_0)^{n+1}} \: (n=0;1;2;\ldots)\\
\end{split}
$$

## Khai triển Laurent

$$
\begin{split}
f(z) &= \sum _{n= -\infty}^{+\infty} c_n (z-z_0)^n \\
\\
c_n &= \frac{f^{(n)}(z_0)}{n!} \\
&= \frac{1}{2 \pi i} \int _{\gamma d} \frac{f(z)dz}{(z-z_0)^{n+1}} \: (n=0;\pm 1;\pm 2; \ldots)
\end{split}
$$

## Thặng dư (Residue)

$$
res[f,z_0]=C_{-1}=\frac{1}{(m-1)!} \lim_{z\rightarrow z_0} [(z-z_0)^mf(z)]^{m-1}
$$

- Điểm thường (Removable Singularity)

$$
C_n = 0 , \forall n < 0 \rightarrow f \text{ holomorphic at } z_0
$$

- Cực điểm (Pole)

$$
\begin{split}
C_{-m} &\ne 0, C_n = 0,\forall n < -m \\
\\
f(z) = c_{-m} (z-z_0)^{-m}+ & \ldots +c_{-1}(z-z_0)^{-1}+c_0+ \ldots \\
\end{split}
$$

- Điểm bất thường cốt yếu (Essential Singularity)

$$
C_n \ne 0 \text{ at } \infty , \: n < 0
$$

## Thặng dư cho tích phân

$$
\int _{\gamma}f(z)dz = 2\pi i \sum _{k=1}^N res[f,z_k]
$$

## Tích phân hàm lượng giác 

$$
\begin{split}
|z| &= 1 \\
\cos \varphi &= \frac{1}{2} (z+\frac{1}{z}) \\
\\
\sin \varphi &= \frac{1}{2i} (z - \frac{1}{z}) \\
\\
d \varphi &= \frac{dz}{iz}
\end{split}
$$

## Công thức biến đổi

$$
\begin{split}
P(z) &= a_nz^n + a_{n-1}z^{n-1} + \ldots + a_0 \\
& \text{Co nghiem } \alpha _1 , \ldots , \alpha _n \\
\Rightarrow P(z) &= a_n(z-\alpha _1) \ldots (z- \alpha _n) \\
\end{split}
$$

## Nghiệm pt bậc 2

$$ ax^2 + bx + c = 0 $$

$$
\begin{split}
& \Delta = b^2 - 4 ac \\
\end{split}
$$

- $ \Delta > 0 $

$$
\left\{ \large
  \begin{array}{rcr}
  x_1 &=& \frac{-b+\sqrt{\Delta}}{2a} \\
  x_2 &=& \frac{-b-\sqrt{\Delta}}{2a} \\
  \end{array}
\right.
$$

- $ \Delta = 0 $

$$
x_1 = x_2 = \frac{-b}{2a}
$$

- $ \Delta < 0 $ vo nghiem.