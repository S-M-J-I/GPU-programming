import triton
import triton.language as tl


@triton.jit
def avg_pool_1d_kernel(input_ptr, output_ptr, input_size, output_size, kernel_size, stride, padding, BLOCK_SIZE: tl.constexpr):
    pid = tl.program_id(axis=0)
    block_start = pid * BLOCK_SIZE
    offsets = block_start + tl.arange(0, BLOCK_SIZE)
    mask = offsets < output_size

    # init accumulator vector for the sum
    sum_values = tl.zeros([BLOCK_SIZE], dtype=tl.float32)

    # we need to sum k consecutive input elements
    for m in range(kernel_size):
        # input_indices = S * offset value + m - P
        input_indices = stride * offsets + m - padding

        # mask for valid input indices (within bounds)
        # handles both negative indices (left padding)
        # indices >= input_size (right padding)
        valid_mask = (input_indices >= 0) & (input_indices < input_size) & mask

        input_values = tl.load(
            input_ptr + input_indices,
            mask=valid_mask,
            other=0.0
        )

        sum_values += input_values

    # 1 / k (sum)
    avg_values = sum_values / kernel_size

    tl.store(output_ptr + offsets, avg_values, mask=mask)


def solution(input, kernel_size: int, stride: int, padding: int, output, H: int):
    input_size = input.shape[0]
    output_size = int(((H + (2 * padding) - kernel_size) / stride) + 1)
    BLOCK_SIZE = 256
    grid_size = triton.cdiv(output_size, BLOCK_SIZE)

    avg_pool_1d_kernel[(grid_size,)](
        input,
        output,
        input_size,
        output_size,
        kernel_size,
        stride,
        padding,
        BLOCK_SIZE=BLOCK_SIZE,
    )

    return output
