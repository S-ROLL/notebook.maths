# Chương I: Cơ sở logic
## Mệnh đề
### Phủ định

| $P$ | $\overline{P}$ |
|:-------:|:--------:|
|   1   |   0    |
|   0   |   1    |

### Hội (và)
| $P$ | $Q$ | $P \land Q$ |
|:-------:|:-------:|:-----------:|
|   0   |   0   |     0     |
|   0   |   1   |     0     |
|   1   |   0   |     0     |
|   **1**   |   **1**   |     **1**     |

### Tuyển (hoặc)
| $P$ | $Q$ | $P \lor Q$ |
|:-------:|:-------:|:-----------:|
|   **0**   |   **0**   |     **0**     |
|   0   |   1   |     1     |
|   1   |   0   |     1     |
|   1   |   1   |     1     |

### Kéo theo
| $P$ | $Q$ | $P \to Q$ |
|:-------:|:-------:|:-----------:|
|   0   |   0   |     1     |
|   0   |   1   |     1     |
|   **1**   |   **0**   |     **0**     |
|   1   |   1   |     1     |

### Nếu và chỉ nếu
| $P$ | $Q$ | $P \leftrightarrow Q$ |
|:-------:|:-------:|:-----------:|
|   **0**   |   **0**   |     **1**     |
|   0   |   1   |     0     |
|   1   |   0   |     0     |
|   **1**   |   **1**   |     **1**     |

## Dạng mệnh đề
| Dạng mệnh đề | Ký hiệu | Điều kiện |
|-------|-------|-----------|
| Tương đương logic | $E \Leftrightarrow F$ | $E \leftrightarrow F$ hằng đúng |
| Hệ quả logic | $E \Rightarrow F$ | $E \to F$ hằng đúng |

Qui tắc thay thế: $E \Leftrightarrow F$ thành $E \Leftrightarrow F'$ sao cho $F'$ tương đương logic.

| Quy luật logic | Công thức |
|-------|-------|
| Phủ định của phủ định | $\overline{\overline{P}} \Leftrightarrow P$ |
| De Morgan | $\overline{P \land Q} \Leftrightarrow \overline{P} \lor \overline{Q}$ <br/> $\overline{P \lor Q} \Leftrightarrow \overline{P} \land \overline{Q}$|
| Giao hoán | $P \lor Q \Leftrightarrow Q \lor P$ <br/> $P \land Q \Leftrightarrow Q \land P$ |
| Kết hợp | $(P \lor Q) \lor R \Leftrightarrow P \lor (Q \lor R)$ <br/> $(P \land Q) \land R \Leftrightarrow P \land (Q \land R)$ |
| Phân phối | $P \lor (Q \land R) \Leftrightarrow (P \lor Q) \land (P \lor R)$ <br/> $P \land (Q \lor R) \Leftrightarrow (P \land Q) \lor (P \land R)$ |
| Luỹ đẳng | $P \lor P \Leftrightarrow P$ <br/> $P \land P \Leftrightarrow P$ |
| Trung hoà | $P \lor 0 \Leftrightarrow P$ <br/> $P \land 1 \Leftrightarrow P$ |
| Phần tử bù | $P \land \overline{P} \Leftrightarrow 0$ <br/> $P \lor \overline{P} \Leftrightarrow 1$ |
| Thống trị | $P \land 0 \Leftrightarrow 0$ <br/> $P \lor 1 \Leftrightarrow 1$ |
| Hấp thụ | $P \lor (P \land Q) \Leftrightarrow P$ <br/> $P \land (P \lor Q) \Leftrightarrow P$ |
| Phép kéo theo | $P \to Q \Leftrightarrow \overline{P} \lor Q \Leftrightarrow \overline{Q} \to \overline{P}$


## Quy tắc suy diễn
| Quy tắc suy diễn | Công thức |
|-------|-------|
| Khẳng định | $[(P \to Q) \land P] \to Q$ |
| Phủ định | $[(P \to Q) \land \overline{Q}] \to \overline{P}$ |
| Tam đoạn luận | $[(P \to Q) \land (Q \to R)] \to (P \to R)$ |
| Tam đoạn luận rời | $[(P \lor Q) \land \overline{Q}] \to P$ |
| Nối liền | $(P \land Q) \to (P \land Q)$ |
| Đơn giản | $(P \land Q) \to P$ |
| Mâu thuẫn | $[(P_1 \land \ldots \land P_n) \to h] \Leftrightarrow [(P_1 \land \ldots \land P_n \land \overline{h}) \to 0]$ |
| C/m theo trường hợp | $[(P \to R) \land (Q \to R)] \to [(P \lor Q) \to R]$ |

Phản ví dụ: để cm sai hay ko là hằng đúng ta chỉ cần chỉ ra 1 phản ví dụ.


## Vị từ lượng từ
## Tập hợp
## Ánh xạ
### Phân loại
#### Đơn ánh
#### Toàn ánh
#### Song ánh
### Tích ánh xạ


## Quy nạp