# ReLU

Problem can be found [here](https://tensara.org/problems/relu).

## Performance

---
### Tesla T4

#### Language: Triton
Time: 28.31 ms\
Performance: 26.96 GFLOPS

Benchmarks:

| Testcase  | Runtime (ms) | Performance (GFLOPS) |
| --------- | ------------ | -------------------- |
| Test Case | Runtime (ms) | GFLOPS               |
| 4096x4096 | 135.94       | 24.74                |
| 6144x4096 | 0.93         | 26.94                |
| 4096x7168 | 1.08         | 27.30                |
| 4096x8192 | 1.23         | 27.31                |
| 8192x8192 | 2.35         | 28.51                |
---
### H100

#### Language: Triton
Time: 5.63 ms\
Performance: 249.63 GFLOPS

Benchmarks:
| Testcase  | Runtime (ms) | GFLOPS |
| --------- | ------------ | ------ |
| 4096x4096 | 27.58        | 187.48 |
| 6144x4096 | 0.11         | 237.07 |
| 4096x7168 | 0.12         | 251.55 |
| 4096x8192 | 0.13         | 263.38 |
| 8192x8192 | 0.22         | 308.68 |
