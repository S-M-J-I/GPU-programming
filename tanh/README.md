# Tanh

Problem can be found [here](https://tensara.org/problems/tanh).

## Performance

---
### Tesla T4

#### Language: Triton
Time: 27.45 ms\
Performance: 26.88 GFLOPS

Benchmarks:

| Testcase  | Runtime (ms) | Performance (GFLOPS) |
| --------- | ------------ | -------------------- |
| 4096x4096 | 131.61       | 24.73                |
| 6144x4096 | 0.94         | 26.92                |
| 4096x7168 | 1.08         | 27.25                |
| 4096x8192 | 1.23         | 27.40                |
| 8192x8192 | 2.39         | 28.10                |
---

### H100

#### Language: Triton
Time: 5.89 ms\
Performance: 246.73 GFLOPS

Benchmarks:
| Testcase  | Runtime (ms) | GFLOPS |
| --------- | ------------ | ------ |
| 4096x4096 | 28.87        | 183.17 |
| 6144x4096 | 0.11         | 233.99 |
| 4096x7168 | 0.12         | 250.12 |
| 4096x8192 | 0.13         | 259.60 |
| 8192x8192 | 0.22         | 306.78 |
