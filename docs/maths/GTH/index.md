<!-- ---
password: bangdeptrai
--- -->
# Giải tích hàm

!!! tip
    - Xác định:
        - Cái **đã có**.
        - Cái cần **chứng minh**.
    
    - Từ đó $\rightarrow$ Cái cần **tìm**.

!!! note
    - Giả thuyết $\rightarrow$ Kết quả.
        - Giả thuyết $\rightarrow$ **đã có**.
        - Kết quả $\rightarrow$ **cần tìm**.

## Các phép toán trên tập hợp
### Phép giao

$$
A \cap B = \{ x \: | \: x \in A \wedge x \in B \}
$$

!!! note
    - $A \cap B = B \cap A$
    - $A \cap B \subset A$
    - $A \cap B \subset B$
    - $(A \cap B) \cap C = A \cap (B \cap C)$

### Phép hợp

$$
A \cup B = \{ x \: | \: x \in A \vee x \in B \}
$$

!!! note
    - $A \cup B = B \cup A$
    - $A \subset A \cup B$
    - $B \subset A \cup B$
    - $(A \cup B) \cup C = A \cup (B \cup C)$
    - $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$
    - $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$

### Phép trừ

$$
A \setminus B = \{ x \: | \: x \in A \wedge x \notin B \}
$$

!!! note
    $A \subset X$, $B \subset X$.

    - $A \setminus B = A \cap (X \setminus B)$
    - $X \setminus (X \setminus A) = A$
    - $X \setminus (A \cap B) = (X \setminus A) \cup (X \setminus B)$
    - $X \setminus (A \cup B) = (X \setminus A) \cap (X \setminus B)$

!!! De-Morgan
    - $\overline{A \cup B} = \overline{A} \cap \overline{B}$
    - $\overline{A \cap B} = \overline{A} \cup \overline{B}$