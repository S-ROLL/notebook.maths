
```mermaid
gantt
    title Bancie's Schedule
    dateFormat DD-MM-YY
    section IELTS
        r0: milestone, r0, 19-06-24, 0d
        na_15: na_15, 19-06-24, 0.1d
        na_12: na_12, after na_15, 0.2d
        na_14: na_14, after na_12, 0.3d
        na_13: na_13, after na_14, 0.3d
        na_3: na_3, after na_13, 0.5d
        na_16: na_16, after na_3, 0.7d
        bt_1: bt_1, after na_16, 1d
        bt_2: bt_2, after bt_1, 1d
        bt_3: bt_3, after bt_2, 1d
        bt_4: bt_4, after bt_3, 1d
        bt_5: bt_5, after bt_4, 1d
        bt_6: bt_6, after bt_5, 1d
        bt_7: bt_7, after bt_6, 1d
        bt_8: bt_8, after bt_7, 1d
        bt_9: bt_9, after bt_8, 1d
        bt_10: bt_10, after bt_9, 1d
        bt_11: bt_11, after bt_10, 1d
        bt_12: bt_12, after bt_11, 1d
        bt_13: bt_13, after bt_12, 1d
        bt_14: bt_14, after bt_13, 1d
        bt_15: bt_15, after bt_14, 1d
        bt_16: bt_16, after bt_15, 1d
        bt_17: bt_17, after bt_16, 1d
        bt_18: bt_18, after bt_17, 1d
        bt_19: bt_19, after bt_18, 1d
        bt_20: bt_20, after bt_19, 1d
        py_1: py_1, after bt_20, 0.7d
        py_2: py_2, after py_1, 0.9d
        py_3: py_3, after py_2, 0.9d
        py_4: py_4, after py_3, 1.4d
        py_5: py_5, after py_4, 0.7d
        na_1: na_1, after py_5, 1.4d
        na_2: na_2, after na_1, 1.4d
        na_4: na_4, after na_2, 1.4d
        na_5: na_5, after na_4, 1.4d
        py_6: py_6, after na_5, 0.5d
        py_7: py_7, after py_6, 0.9d
        na_6: na_6, after py_7, 1.4d
        sbe_1: sbe_1, after na_6, 2.3d
        sbe_2: sbe_2, after sbe_1, 1.3d
        sbe_3: sbe_3, after sbe_2, 1.6d
        sbe_4: sbe_4, after sbe_3, 1.3d
        sbe_5: sbe_5, after sbe_4, 1.8d
        sbe_6: sbe_6, after sbe_5, 1d
        sbe_7: sbe_7, after sbe_6, 2.1d
        sbe_8: sbe_8, after sbe_7, 1d
        sbe_9: sbe_9, after sbe_8, 2.1d
        sbe_10: sbe_10, after sbe_9, 1d
        sbe_11: sbe_11, after sbe_10, 0.5d
        sbe_12: sbe_12, after sbe_11, 0.8d
        sbe_13: sbe_13, after sbe_12, 1.3d
        sbe_14: sbe_14, after sbe_13, 2.3d
        sbe_15: sbe_15, after sbe_14, 2.3d
        sbe_16: sbe_16, after sbe_15, 1.6d
        sbe_17: sbe_17, after sbe_16, 1.6d
        sbe_18: sbe_18, after sbe_17, 1.3d
        sbe_19: sbe_19, after sbe_18, 0.8d
        na_7: na_7, after sbe_19, 1.4d
        na_8: na_8, after na_7, 1.4d
        na_9: na_9, after na_8, 1.4d
        py_8: py_8, after na_9, 1.6d
        py_9: py_9, after py_8, 1.4d
        na_10: na_10, after py_9, 1.4d
        na_11: na_11, after na_10, 1.4d
        py_10: py_10, after na_11, 1.1d
        sbe_20: sbe_20, after py_10, 1.8d

        %---release time---
        r (bt_2): milestone, after r0, 1d
        r (bt_3): milestone, after r0, 3d
        r (bt_4): milestone, after r0, 6d
        r (bt_5): milestone, after r0, 8d
        r (bt_6): milestone, after r0, 10d
        r (bt_7): milestone, after r0, 13d
        r (bt_8): milestone, after r0, 15d
        r (bt_9): milestone, after r0, 17d
        r (bt_10): milestone, after r0, 20d
        r (bt_11): milestone, after r0, 22d
        r (bt_12): milestone, after r0, 24d
        r (bt_13): milestone, after r0, 27d
        r (bt_14): milestone, after r0, 29d
        r (bt_15): milestone, after r0, 31d
        r (bt_16): milestone, after r0, 34d
        r (bt_17): milestone, after r0, 36d
        r (bt_18): milestone, after r0, 38d
        r (bt_19): milestone, after r0, 41d
        r (bt_20): milestone, after r0, 43d
```


```mermaid
gantt
    title Bancie's Schedule
    udehcS sdateFormat DD-MM-YY
    section IELTS
        %(d) FINAL EXAM: milestone, 06-07-2025, 0d

        %---KHOÁ BASIC IELTS_29---
        (r) BASIC: done, milestone, 18-06-24, 0d
        (d) BASIC: milestone, 01-08-24, 0d

        %---KHOÁ PRONOUNCITAION---
        (r) PHÁT ÂM: done, milestone, p1, 14-06-24, 0d
        (d) PHÁT ÂM: milestone, after p1, 20d

        %---KHOÁ INTER IELTS_22---
        %(r) INTER: milestone, 27-08-24, 0d
        %(d) INTER: milestone, 26-10-24, 0d

    section STATISTICS
        %---SBE (prec)---
        (d) SBE: milestone, 01-09-24, 0d

    section PYTHON
        %---tutorial (prec)---
        (r) TUTORIALS: milestone, py1, 20-06-24, 0d
        (d) TUTORIALS: milestone, after py1, 20d

    section MACHINE LEARNING
```

# Contents
- [Basic formula](https://github.com/S-ROLL/notebook.maths/blob/main/Maths/BASIC-FORMULA/basic.ipynb)
- [Calculus]()
  - [Complex analysis](https://github.com/S-ROLL/notebook.maths/blob/main/Maths/CALCULUS/Complex-Analysis/ca.ipynb)
  - [Numerical methods](https://github.com/S-ROLL/notebook.maths/blob/main/Maths/CALCULUS/Numerical-Methods/nm.ipynb)
  - [Measure theory](https://github.com/S-ROLL/notebook.maths/blob/main/Maths/CALCULUS/Measure-theory/measure.ipynb)
  - [Differential equation](https://github.com/S-ROLL/notebook.maths/blob/main/Maths/CALCULUS/Differential-equation/differential.ipynb)
- [Set theory](https://github.com/S-ROLL/notebook.maths/blob/main/Maths/NUMBER-THEORY/Set-theory/set-theory.ipynb)
- [Probability]()
  - [Applied statistics](https://github.com/S-ROLL/notebook.maths/blob/main/Maths/PROBABILITY/Applied-Statistics/advance/advance-AS.ipynb)
  - [Machine learning](https://github.com/S-ROLL/notebook.maths/blob/main/Maths/PROBABILITY/Machine-Learning/ml.ipynb)
- [Optimization]()
  - [LFP](https://github.com/S-ROLL/notebook.maths/blob/main/NCKH/LFP/theory/LFP.ipynb)
  - [MILP]()
    - [Theory](https://github.com/S-ROLL/notebook.maths/blob/main/NCKH/MILP/theory/nckh.ipynb)
    - [Tests](https://github.com/S-ROLL/notebook.maths/blob/main/NCKH/MILP/tests/test_nckh.ipynb)

[Drive](https://drive.google.com/drive/u/1/folders/1HARdf9ZS6k-OPniwOIoeQKNms1sTe28c)
