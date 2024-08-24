$x = r \cos (\theta), y = r \sin (\theta) \quad (1)$
Do thay doi 1 goc nen
$x' = r \cos (\theta + \varphi), y' = r \sin (\theta + \varphi)$
Ta co ct
$$
\begin{split}
\cos (\theta + \varphi) &= \cos (\theta) \cos (\varphi) - \sin (\theta) \sin (\varphi) \\
\sin (\theta + \varphi) &= \sin (\theta) \cos (\varphi) + \cos (\theta) \sin (\varphi)
\end{split}
$$
Vay
$$
\begin{split}
x' &=r(\cos (\theta) \cos (\varphi) - \sin (\theta) \sin (\varphi)) \\
y' &= r(\sin (\theta) \cos (\varphi) + \cos (\theta) \sin (\varphi))
\end{split}
$$
Tu $(1)$ ta duoc
$$
\begin{split}
x' &= x \cos (\varphi) - y \sin (\varphi) \\
y' &= x \sin(\varphi) + y \cos (\varphi)
\end{split}
$$
Bieu dien duoi dang ma tran:
$$
\begin{bmatrix}
x' \\
y'
\end{bmatrix} =
\begin{bmatrix}
\cos (\varphi) & -\sin (\varphi) \\
\sin (\varphi) & \cos (\varphi)
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
$$

Trong do cs chinh tac la
$$
\begin{bmatrix}
\cos (\varphi) & -\sin (\varphi) \\
\sin (\varphi) & \cos (\varphi)
\end{bmatrix}
$$