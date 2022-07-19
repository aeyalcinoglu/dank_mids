
import multicall

GAS_LIMIT = multicall.constants.GAS_LIMIT
OVERRIDE_CODE = multicall.constants.MULTICALL2_BYTECODE

# When you get these call responses back from the multicall, we know there was some problem with execution.
# If you make the exact same calls without multicall, you will get an Exception not a response. 
# TODO: Replicate brownie's logic for detecting reverts.
BAD_HEXES = [
    # Chainlink feeds no access
    "0x08c379a0000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000094e6f206163636573730000000000000000000000000000000000000000000000",
    # Mint is paused, ironbank
    "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000e6d696e7420697320706175736564000000000000000000000000000000000000",
    # Invalid Ether transfer
    "0x08c379a000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000016496e76616c6964206574686572207472616e7366657200000000000000000000",
    # Non Empty Data
    "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000e4e4f4e5f454d5054595f44415441000000000000000000000000000000000000",
    # msg.sig is not assigned to submodule
    "0x08c379a0000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000246d73672e736967206973206e6f742061737369676e656420746f207375626d6f64756c6500000000000000000000000000000000000000000000000000000000",
    # only wrapped native contract could send native token
    "0x08c379a0000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000346f6e6c792077726170706564206e617469766520636f6e747261637420636f756c642073656e64206e617469766520746f6b656e000000000000000000000000",
    # Controller Rejected
    "0x08c379a000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000013434f4e54524f4c4c45525f52454a454354454400000000000000000000000000",
    # Diamond: Function does not exist
    "0x08c379a0000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000204469616d6f6e643a2046756e6374696f6e20646f6573206e6f74206578697374",
]
