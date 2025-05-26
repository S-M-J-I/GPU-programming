import triton
import triton.language as tl


@triton.jit
def tanh_kernel(input_ptr, output_ptr, n: int, m: int, BLOCK_SIZE: tl.constexpr):
    # get current thread block id
    pid = tl.program_id(axis=0)

    # calc linear indices for this thread block for BLOCK_SIZE consecutive elements
    block_start = pid * BLOCK_SIZE
    offsets = block_start + tl.arange(0, BLOCK_SIZE)

    # calc total no of elements
    total_elements = n * m

    # Create mask to prevent out-of-bounds access
    mask = offsets < total_elements

    # load input elements
    input_values = tl.load(input_ptr + offsets, mask=mask, other=0.0)

    # calc tanh
    numerator = tl.exp(input_values) - tl.exp(-1 * input_values)
    denominator = tl.exp(input_values) + tl.exp(-1 * input_values)
    tanh = numerator / denominator

    # store to output
    tl.store(output_ptr + offsets, tanh, mask=mask)


def solution(input, output, n: int, m: int):
    BLOCK_SIZE = 1024
    grid_size = triton.cdiv(n * m, BLOCK_SIZE)
    tanh_kernel[(grid_size,)](
        input,
        output,
        n,
        m,
        BLOCK_SIZE=BLOCK_SIZE
    )

    return output
