import triton
import triton.language as tl


@triton.jit
def relu_kernel(input_ptr, output_ptr, n_rows, n_cols, BLOCK_SIZE: tl.constexpr):
    # get current thread block id
    pid = tl.program_id(axis=0)

    # calc linear indices for this thread block for BLOCK_SIZE consecutive elements
    block_start = pid * BLOCK_SIZE
    offsets = block_start + tl.arange(0, BLOCK_SIZE)

    # calc total number of elements (output)
    total_elements = n_rows * n_cols

    # create a mask to prevent out-of-bounds mem access
    mask = offsets < total_elements

    # load input values from memory and directly map memory offset (linear -> find better way to do this?)
    input_values = tl.load(input_ptr + offsets, mask=mask, other=0.0)

    # calc relu
    relu_values = tl.maximum(0.0, input_values)

    # store results to output memory
    tl.store(output_ptr + offsets, relu_values, mask=mask)


def solution(input, output, n: int, m: int):
    total_elements = n * m

    BLOCK_SIZE = 1024  # from doc

    # get gpu grid / number of thread blocks needed
    grid_size = triton.cdiv(total_elements, BLOCK_SIZE)

    # run kernel
    relu_kernel[(grid_size,)](
        input,
        output,
        n,
        m,
        BLOCK_SIZE=BLOCK_SIZE,
    )

    return output
