data = f"""%dt -> fm, hd
%tl -> jk, hd
%vx -> kc, sz
%sz -> kc
%kj -> tl, hd
%pm -> tb
%fc -> rt
&tb -> sx, qn, vj, qq, sk, pv
%df -> bb
%qq -> jm
%sl -> vz
broadcaster -> hp, zb, xv, qn
&pv -> kh
%gf -> pm, tb
%pb -> hd, kj
%gr -> hd, pb
%gs -> kc, pd
%tx -> df
%jm -> tb, db
%bh -> fl, gz
%rt -> kc, xp
&qh -> kh
%lb -> zm, fl
%pd -> lq
%qn -> sk, tb
%gb -> qq, tb
&xm -> kh
%mv -> hd, gr
%gz -> fl
%js -> mv
%hp -> dt, hd
%nk -> kc, vx
&kh -> rx
%zc -> tx
%mp -> js, hd
%zm -> mb
%xh -> cd, tb
%db -> xh, tb
%sx -> vj
&hz -> kh
%vj -> gb
%zq -> hd
%lj -> fc, kc
%lg -> kc, nk
&fl -> xv, tx, sl, df, qh, zc, zm
&kc -> zb, xp, pd, fc, xm
%lq -> kc, lj
&hd -> hp, js, hz
%mb -> fl, sl
%vz -> fl, bh
%fm -> mp, hd
%bb -> fl, lb
%zb -> gs, kc
%xp -> lg
%jk -> zq, hd
%xv -> zc, fl
%sk -> sx
%cd -> gf, tb"""


test_data1 = f"""broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

test_data = f"""broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

from collections import defaultdict
from dataclasses import dataclass
from typing import Optional

# from collections import defaultdict


class Module:
    def __init__(self, name: str, outputs: list[str]):
        self.name = name
        self.outputs = outputs

    def pulse(self, sender: str, val: bool) -> Optional[bool]:
        raise NotImplemented()


class Broadcaster(Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def pulse(self, sender: str, val: bool) -> Optional[bool]:
        return val

    def serialize_state(self) -> str:
        return "b"


class Output(Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def pulse(self, sender: str, val: bool) -> Optional[bool]:
        pass

    def serialize_state(self) -> str:
        return "o"


class FlipFlop(Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = False

    def pulse(self, sender: str, val: bool) -> Optional[bool]:
        if not val:
            self.state = not self.state
            return self.state

    def serialize_state(self) -> str:
        return str(int(self.state))


class Conjunction(Module):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state: dict[str, bool] = {}

    def add_input(self, name: str):
        self.state[name] = False

    def pulse(self, sender: str, val: bool) -> bool:
        self.state[sender] = val
        return not all(self.state.values())

    def serialize_state(self) -> str:
        return "".join(str(int(v)) for v in self.state.values())


def part1(data):
    # Create modules
    modules: dict[str, Module] = {}
    for module_str in data.split("\n"):
        name_str, output_str = module_str.split(" -> ")
        outputs = output_str.split(", ")
        if name_str[0] == "%":
            name = name_str[1:]
            modules[name] = FlipFlop(name=name, outputs=outputs)
        elif name_str[0] == "&":
            name = name_str[1:]
            modules[name] = Conjunction(name=name, outputs=outputs)
        elif name_str == "broadcaster":
            name = name_str
            modules[name] = Broadcaster(name=name, outputs=outputs)

    # Add the special one
    modules["output"] = Output(name="output", outputs=[])

    # Go through again and add inputs
    for module in modules.values():
        for output in module.outputs:
            to_module = modules.get(output)
            if to_module and isinstance(to_module, Conjunction):
                to_module.add_input(module.name)

    total_low = 0
    total_high = 0
    for i in range(1000):
        to_process: list[tuple[bool, str, str]] = [(False, "button", "broadcaster")]

        while len(to_process):
            val, sender, module_name = to_process.pop(0)
            # print(f"{sender} -{val}-> {module_name}")

            if val is True:
                total_high += 1
            if val is False:
                total_low += 1

            module = modules.get(module_name)
            if not module:
                continue
            next_val = module.pulse(sender=sender, val=val)

            if next_val is not None:
                for output in module.outputs:
                    to_process.append((next_val, module_name, output))

    return total_high * total_low


def part2(data):
    # Create modules
    modules: dict[str, Module] = {}
    for module_str in data.split("\n"):
        name_str, output_str = module_str.split(" -> ")
        outputs = output_str.split(", ")
        if name_str[0] == "%":
            name = name_str[1:]
            modules[name] = FlipFlop(name=name, outputs=outputs)
        elif name_str[0] == "&":
            name = name_str[1:]
            modules[name] = Conjunction(name=name, outputs=outputs)
        elif name_str == "broadcaster":
            name = name_str
            modules[name] = Broadcaster(name=name, outputs=outputs)

    # Add the special one
    # modules["output"] = Output(name="output", outputs=[])

    # Go through again and add inputs
    for module in modules.values():
        for output in module.outputs:
            to_module = modules.get(output)
            if to_module and isinstance(to_module, Conjunction):
                to_module.add_input(module.name)

    ancestors = defaultdict(set)

    # populate ancestors
    for module in modules.values():
        to_process = []

    # Need to find periods of the subcircuits starting at Broadcast to shortcut.
    # When all ancestors have the same value, we are repeating.
    # Once we're repeating, we can look up values at future indexes.
    # For conjunctions, to find when they line up we use the code from day_8

    i = -1
    while True:
        i += 1
        if i % 1000000 == 0:
            print(i)
        to_process: list[tuple[bool, str, str]] = [(False, "button", "broadcaster")]

        while len(to_process):
            val, sender, module_name = to_process.pop(0)
            # print(f"{sender} -{val}-> {module_name}")

            if val is False and module_name == "rx":
                return i

            module = modules.get(module_name)
            if not module:
                continue
            next_val = module.pulse(sender=sender, val=val)

            if next_val is not None:
                for output in module.outputs:
                    to_process.append((next_val, module_name, output))

    raise Exception("not found")


print(part1(data))  # 731517480
print(part2(data))
