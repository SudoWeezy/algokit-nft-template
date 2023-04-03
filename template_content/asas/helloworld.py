import beaker
import pyteal as pt

app = beaker.Application("HelloWorldApp").apply(deploy_time_immutability_control).apply(deploy_time_permanence_control)


@app.external
def hello(name: pt.abi.String, *, output: pt.abi.String) -> pt.Expr:
    return output.set(pt.Concat(pt.Bytes("Hello, "), name.get()))
