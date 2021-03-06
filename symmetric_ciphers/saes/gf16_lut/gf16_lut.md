# Look Up Table for GF16 multiplication

## Definition of finite field

the irredutible polynomial for this finite fiels is $x^4 + x + 1$.

Therefore, the first step to determine the multiplication matrix is to determine the values to each power of $g$ in this field:
| **Zech's Logarithm** | **Polynomial**      | **Binary** | **Hexadecimal** |
|----------------------|---------------------|------------|-----------------|
| 0                    | 0                   | 0000       | 0x0             |
| $g^0 = g^{15}$       | 1                   | 0001       | 0x1             |
| $g^1$                | $g$                 | 0010       | 0x2             |
| $g^2$                | $g^2$               | 0100       | 0x4             |
| $g^3$                | $g^3$               | 1000       | 0x8             |
| $g^4$                | $g + 1$             | 0011       | 0x3             |
| $g^5$                | $g^2 + g$           | 0110       | 0x6             |
| $g^6$                | $g^3 + g^2$         | 1100       | 0xC             |
| $g^7$                | $g^3 + g + 1$       | 1011       | 0xB             |
| $g^8$                | $g^2 + 1$           | 0101       | 0x5             |
| $g^9$                | $g^3 + g$           | 1010       | 0xA             |
| $g^{10}$             | $g^2 + g + 1$       | 0111       | 0x7             |
| $g^{11}$             | $g^3 + g^2 + g$     | 1110       | 0xE             |
| $g^{12}$             | $g^3 + g^2 + g + 1$ | 1111       | 0xF             |
| $g^{13}$             | $g^3 + g^2 + 1$     | 1101       | 0xD             |
| $g^{14}$             | $g^3 + 1            | 1001       | 0x9             |

Now, let's build the Look up table where the row index is the first operand of multiplication and the column index is the second operand. The multiplication will be done in Zech's Logarithm domain, because it is easier to do multiplication of powers.

## Multiplication table
| ****               | **0x0 (0)** | **0x1 ($g^0$)** | **0x2 ($g^1$)** | **0x3 ($g^4$)** | **0x4 ($g^2$)** | **0x5 ($g^8$)** | **0x6 ($g^5$)** | **0x7 ($g^{10}$)** | **0x8 ($g^3$)** | **0x9 ($g^{14}$)** | **0xA ($g^9$)** | **0xB ($g^7$)** | **0xC ($g^6$)** | **0xD ($g^{13}$)** | **0xE ($g^{11}$)** | **0xF ($g^{12}$)** |
|--------------------|-------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|--------------------|-----------------|--------------------|-----------------|-----------------|-----------------|--------------------|--------------------|--------------------|
| **0x0 (0)**        | 0           | 0               | 0               | 0               | 0               | 0               | 0               | 0                  | 0               | 0                  | 0               | 0               | 0               | 0                  | 0                  | 0                  |
| **0x1 ($g^0$)**    | 0           | **0x1 ($g^0$)** | 0x2 ($g^1$)     | 0x3 ($g^4$)     | 0x4 ($g^2$)     | 0x5 ($g^8$)     | 0x6 ($g^5$)     | 0x7 ($g^{10}$)     | 0x8 ($g^3$)     | 0x9 ($g^{14}$)     | 0xA ($g^9$)     | 0xB ($g^7$)     | 0xC ($g^6$)     | 0xD ($g^{13}$)     | 0xE ($g^{11}$)     | 0xF ($g^{12}$)     |
| **0x2 ($g^1$)**    | 0           | 0x2 ($g^1$)     | 0x4 ($g^2$)     | 0x6 ($g^5$)     | 0x8 ($g^3$)     | 0xA ($g^9$)     | 0xC ($g^6$)     | 0xE ($g^{11}$)     | 0x3 ($g^4$)     | **0x1 ($g^0$)**    | 0x7 ($g^{10}$)  | 0x5 ($g^8$)     | 0xB ($g^7$)     | 0x9 ($g^{14}$)     | 0xF ($g^{12}$)     | 0xD ($g^{13}$)     |
| **0x3 ($g^4$)**    | 0           | 0x3 ($g^4$)     | 0x6 ($g^5$)     | 0x5 ($g^8$)     | 0xC ($g^6$)     | 0xF ($g^{12}$)  | 0xA ($g^9$)     | 0x9 ($g^{14}$)     | 0xB ($g^7$)     | 0x8 ($g^3$)        | 0xD ($g^{13}$)  | 0xE ($g^{11}$)  | 0x7 ($g^{10}$)  | 0x4 ($g^2$)        | **0x1 ($g^0$)**    | 0x2 ($g^1$)        |
| **0x4 ($g^2$)**    | 0           | 0x4 ($g^2$)     | 0x8 ($g^3$)     | 0xC ($g^6$)     | 0x3 ($g^4$)     | 0x7 ($g^{10}$)  | 0xB ($g^7$)     | 0xF ($g^{12}$)     | 0x6 ($g^5$)     | 0x2 ($g^1$)        | 0xE ($g^{11}$)  | 0xA ($g^9$)     | 0x5 ($g^8$)     | **0x1 ($g^0$)**    | 0xD ($g^{13}$)     | 0x9 ($g^{14}$)     |
| **0x5 ($g^8$)**    | 0           | 0x5 ($g^8$)     | 0xA ($g^9$)     | 0xF ($g^{12}$)  | 0x7 ($g^{10}$)  | 0x2 ($g^1$)     | 0xD ($g^{13}$)  | 0x8 ($g^3$)        | 0xE ($g^{11}$)  | 0xB ($g^7$)        | 0x4 ($g^2$)     | **0x1 ($g^0$)** | 0x9 ($g^{14}$)  | 0xC ($g^6$)        | 0x3 ($g^4$)        | 0x6 ($g^5$)        |
| **0x6 ($g^5$)**    | 0           | 0x6 ($g^5$)     | 0xC ($g^6$)     | 0xA ($g^9$)     | 0xB ($g^7$)     | 0xD ($g^{13}$)  | 0x7 ($g^{10}$)  | **0x1 ($g^0$)**    | 0x5 ($g^8$)     | 0x3 ($g^4$)        | 0x9 ($g^{14}$)  | 0xF ($g^{12}$)  | 0xE ($g^{11}$)  | 0x8 ($g^3$)        | 0x2 ($g^1$)        | 0x4 ($g^2$)        |
| **0x7 ($g^{10}$)** | 0           | 0x7 ($g^{10}$)  | 0xE ($g^{11}$)  | 0x9 ($g^{14}$)  | 0xF ($g^{12}$)  | 0x8 ($g^3$)     | **0x1 ($g^0$)** | 0x6 ($g^5$)        | 0xD ($g^{13}$)  | 0xA ($g^9$)        | 0x3 ($g^4$)     | 0x4 ($g^2$)     | 0x2 ($g^1$)     | 0x5 ($g^8$)        | 0xC ($g^6$)        | 0xB ($g^7$)        |
| **0x8 ($g^3$)**    | 0           | 0x8 ($g^3$)     | 0x3 ($g^4$)     | 0xB ($g^7$)     | 0x6 ($g^5$)     | 0xE ($g^{11}$)  | 0x5 ($g^8$)     | 0xD ($g^{13}$)     | 0xC ($g^6$)     | 0x4 ($g^2$)        | 0xF ($g^{12}$)  | 0x7 ($g^{10}$)  | 0xA ($g^9$)     | 0x2 ($g^1$)        | 0x9 ($g^{14}$)     | **0x1 ($g^0$)**    |
| **0x9 ($g^{14}$)** | 0           | 0x9 ($g^{14}$)  | **0x1 ($g^0$)** | 0x8 ($g^3$)     | 0x2 ($g^1$)     | 0xB ($g^7$)     | 0x3 ($g^4$)     | 0xA ($g^9$)        | 0x4 ($g^2$)     | 0xD ($g^{13}$)     | 0x5 ($g^8$)     | 0xC ($g^6$)     | 0x6 ($g^5$)     | 0xF ($g^{12}$)     | 0x7 ($g^{10}$)     | 0xE ($g^{11}$)     |
| **0xA ($g^9$)**    | 0           | 0xA ($g^9$)     | 0x7 ($g^{10}$)  | 0xD ($g^{13}$)  | 0xE ($g^{11}$)  | 0x4 ($g^2$)     | 0x9 ($g^{14}$)  | 0x3 ($g^4$)        | 0xF ($g^{12}$)  | 0x5 ($g^8$)        | 0x8 ($g^3$)     | 0x2 ($g^1$)     | **0x1 ($g^0$)** | 0xB ($g^7$)        | 0x6 ($g^5$)        | 0xC ($g^6$)        |
| **0xB ($g^7$)**    | 0           | 0xB ($g^7$)     | 0x5 ($g^8$)     | 0xE ($g^{11}$)  | 0xA ($g^9$)     | **0x1 ($g^0$)** | 0xF ($g^{12}$)  | 0x4 ($g^2$)        | 0x7 ($g^{10}$)  | 0xC ($g^6$)        | 0x2 ($g^1$)     | 0x9 ($g^{14}$)  | 0xD ($g^{13}$)  | 0x6 ($g^5$)        | 0x8 ($g^3$)        | 0x3 ($g^4$)        |
| **0xC ($g^6$)**    | 0           | 0xC ($g^6$)     | 0xB ($g^7$)     | 0x7 ($g^{10}$)  | 0x5 ($g^8$)     | 0x9 ($g^{14}$)  | 0xE ($g^{11}$)  | 0x2 ($g^1$)        | 0xA ($g^9$)     | 0x6 ($g^5$)        | **0x1 ($g^0$)** | 0xD ($g^{13}$)  | 0xF ($g^{12}$)  | 0x3 ($g^4$)        | 0x4 ($g^2$)        | 0x8 ($g^3$)        |
| **0xD ($g^{13}$)** | 0           | 0xD ($g^{13}$)  | 0x9 ($g^{14}$)  | 0x4 ($g^2$)     | **0x1 ($g^0$)** | 0xC ($g^6$)     | 0x8 ($g^3$)     | 0x5 ($g^8$)        | 0x2 ($g^1$)     | 0xF ($g^{12}$)     | 0xB ($g^7$)     | 0x6 ($g^5$)     | 0x3 ($g^4$)     | 0xE ($g^{11}$)     | 0xA ($g^9$)        | 0x7 ($g^{10}$)     |
| **0xE ($g^{11}$)** | 0           | 0xE ($g^{11}$)  | 0xF ($g^{12}$)  | **0x1 ($g^0$)** | 0xD ($g^{13}$)  | 0x3 ($g^4$)     | 0x2 ($g^1$)     | 0xC ($g^6$)        | 0x9 ($g^{14}$)  | 0x7 ($g^{10}$)     | 0x6 ($g^5$)     | 0x8 ($g^3$)     | 0x4 ($g^2$)     | 0xA ($g^9$)        | 0xB ($g^7$)        | 0x5 ($g^8$)        |
| **0xF ($g^{12}$)** | 0           | 0xF ($g^{12}$)  | 0xD ($g^{13}$)  | 0x2 ($g^1$)     | 0x9 ($g^{14}$)  | 0x6 ($g^5$)     | 0x4 ($g^2$)     | 0xB ($g^7$)        | **0x1 ($g^0$)** | 0xE ($g^{11}$)     | 0xC ($g^6$)     | 0x3 ($g^4$)     | 0x8 ($g^3$)     | 0x7 ($g^{10}$)     | 0x5 ($g^8$)        | 0xA ($g^9$)        |
