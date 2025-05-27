# 1D Average Pooling

Problem can be found [here](https://tensara.org/problems/avg-pool-1d).

## Performance

---
### H100

#### Language: Triton
Time: 4.77 ms\
Performance: 329.95 GFLOPS

Benchmarks:

| Testcase                  | Runtime (ms) | Performance (GFLOPS) |
| ------------------------- | ------------ | -------------------- |
| H=2097152, K=7, S=4, P=3  | 26.83        | 66.99                |
| H=4194304, K=2, S=1, P=0  | 0.29         | 157.77               |
| H=8388608, K=3, S=2, P=1  | 0.30         | 208.10               |
| H=16777216, K=4, S=2, P=1 | 0.09         | 415.51               |
| H=33554432, K=3, S=1, P=1 | 0.62         | 731.39               |
| H=67108864, K=5, S=3, P=2 | 0.50         | 399.94               |
---
### A100

#### Language: Triton
Time: 23.94 ms\
Performance: 218.60 GFLOPS

Benchmarks:
| Testcase                  | Runtime (ms) | GFLOPS |
| ------------------------- | ------------ | ------ |
| H=2097152, K=7, S=4, P=3  | 141.79       | 40.08  |
| H=4194304, K=2, S=1, P=0  | 0.35         | 87.66  |
| H=8388608, K=3, S=2, P=1  | 0.36         | 121.65 |
| H=16777216, K=4, S=2, P=1 | 0.14         | 259.48 |
| H=33554432, K=3, S=1, P=1 | 0.49         | 422.86 |
| H=67108864, K=5, S=3, P=2 | 0.54         | 379.84 |
