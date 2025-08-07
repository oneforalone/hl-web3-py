import json

from solcx import compile_files, install_solc

SOLC_VERSION = "0.8.13"

install_solc(SOLC_VERSION)


def compile_contract(name: str):
    compiled_sol = compile_files(
        [f"contracts/{name}.sol"],
        output_values=["abi", "bin"],
        solc_version=SOLC_VERSION,
    )
    _id, contract_interface = compiled_sol.popitem()
    abi = contract_interface["abi"]
    with open(f"abis/{name}.json", "w") as f:
        json.dump(abi, f)


if __name__ == "__main__":
    compile_contract("CoreWriter")
