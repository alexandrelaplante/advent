from __future__ import annotations

from dataclasses import dataclass

INPUT = """x00: 1
x01: 1
x02: 0
x03: 0
x04: 0
x05: 1
x06: 0
x07: 1
x08: 1
x09: 0
x10: 1
x11: 0
x12: 0
x13: 1
x14: 0
x15: 0
x16: 1
x17: 0
x18: 1
x19: 0
x20: 0
x21: 1
x22: 1
x23: 0
x24: 0
x25: 1
x26: 1
x27: 0
x28: 0
x29: 1
x30: 0
x31: 0
x32: 1
x33: 0
x34: 1
x35: 1
x36: 1
x37: 1
x38: 0
x39: 0
x40: 1
x41: 1
x42: 1
x43: 1
x44: 1
y00: 1
y01: 0
y02: 1
y03: 1
y04: 0
y05: 0
y06: 1
y07: 1
y08: 0
y09: 1
y10: 1
y11: 1
y12: 1
y13: 1
y14: 0
y15: 0
y16: 0
y17: 1
y18: 0
y19: 1
y20: 0
y21: 1
y22: 1
y23: 0
y24: 1
y25: 0
y26: 1
y27: 1
y28: 0
y29: 0
y30: 1
y31: 1
y32: 1
y33: 1
y34: 1
y35: 0
y36: 1
y37: 0
y38: 0
y39: 1
y40: 1
y41: 0
y42: 1
y43: 0
y44: 1

x36 XOR y36 -> bbk
sfc XOR sdv -> z15
ncj XOR gdc -> z43
vvr AND ggf -> rqg
stp OR qwr -> kbw
x25 XOR y25 -> vbw
wjm OR ghg -> jtc
x23 AND y23 -> rks
drw OR kbq -> btn
hcc AND kqp -> jkc
y08 XOR x08 -> kgn
btn XOR sgv -> z02
kbw XOR jnv -> z18
mqh OR vkh -> jds
vvr XOR ggf -> z09
nrr XOR qwg -> z30
y07 XOR x07 -> cnk
kbk XOR hbw -> z37
sgh OR hfn -> mjn
y15 AND x15 -> gms
tpf XOR sft -> z11
qvn XOR sgr -> z01
kbv AND csv -> sdp
x32 XOR y32 -> tkt
y22 XOR x22 -> fhn
qdf OR qbj -> brn
y14 AND x14 -> wgj
cqc OR rnr -> ksv
gws OR tfb -> vst
brn XOR jkv -> z33
tmh XOR qch -> z44
fcq OR qhs -> wwt
vng AND gfs -> rpk
y24 XOR x24 -> hkf
x39 AND y39 -> vkh
y06 XOR x06 -> srn
fhn XOR fvq -> z22
y42 XOR x42 -> jdf
x38 XOR y38 -> jjj
rks OR rdh -> kpb
qvf XOR jmm -> z41
y01 AND x01 -> kbq
jsk AND pkq -> gdh
mms OR gdh -> fvq
fpw AND jjj -> fdd
bbk XOR fcn -> z36
x43 AND y43 -> dfg
npr XOR hfv -> z19
y08 AND x08 -> ctv
jkc OR vvb -> bkk
y26 AND x26 -> pwf
nnn OR cvn -> gdc
vpd OR dtb -> z45
x44 XOR y44 -> tmh
pbj OR dfg -> qch
y41 AND x41 -> gmm
x25 AND y25 -> sfh
y40 XOR x40 -> gqd
y20 AND x20 -> kvs
nmq OR jmn -> rjb
pkq XOR jsk -> z21
x04 XOR y04 -> gbh
x04 AND y04 -> scp
pcf OR mqt -> tpf
x31 AND y31 -> cps
fhn AND fvq -> wdf
y11 XOR x11 -> sft
srn AND fhb -> cqc
bpq OR crp -> hbw
gvj OR kvs -> jsk
kmd AND vvv -> rdh
y16 AND x16 -> rnq
thk AND wnk -> z39
sfh OR qgg -> bhv
y02 XOR x02 -> sgv
qvn AND sgr -> drw
x34 AND y34 -> sgh
y42 AND x42 -> nnn
qvf AND jmm -> pgm
sck OR kms -> hcc
msf XOR tkt -> z32
rjb AND btj -> wts
y18 AND x18 -> mgt
jdf AND nmw -> cvn
kqp XOR hcc -> z12
qpg OR csr -> djn
x12 XOR y12 -> kqp
x19 XOR y19 -> hfv
gps AND bkk -> jvj
x14 XOR y14 -> vng
x13 AND y13 -> rqn
wwt XOR vbw -> z25
ggh OR pwf -> nct
nmw XOR jdf -> z42
y23 XOR x23 -> vvv
gbh XOR whq -> z04
vtj OR fpn -> nrr
x05 AND y05 -> gdk
kpb AND hkf -> fcq
x10 AND y10 -> pcf
jtc XOR sng -> z03
vvv XOR kmd -> z23
gps XOR bkk -> z13
x09 XOR y09 -> ggf
y03 XOR x03 -> sng
kwv OR ctv -> z08
y03 AND x03 -> fcv
y18 XOR x18 -> jnv
y39 XOR x39 -> wnk
x27 XOR y27 -> njn
jnv AND kbw -> hrv
y09 AND x09 -> nbb
x31 XOR y31 -> btj
gms OR ngf -> pvv
rpk OR wgj -> sdv
bhv XOR wnf -> z26
wnk XOR thk -> mqh
pgn OR qsw -> fpw
y15 XOR x15 -> sfc
x35 XOR y35 -> qgs
djn XOR ptk -> tfb
pvv XOR rnq -> z16
cnk AND ksv -> tss
x38 AND y38 -> fkp
y26 XOR x26 -> wnf
sdp OR gdk -> fhb
x00 AND y00 -> qvn
x37 AND y37 -> qsw
dpg OR mqp -> jpb
btn AND sgv -> ghg
jpb XOR kpm -> z34
y34 XOR x34 -> kpm
kpb XOR hkf -> z24
qgs AND mjn -> ckr
hfv AND npr -> tvp
y10 XOR x10 -> vkt
gvw AND kgn -> kwv
ncj AND gdc -> pbj
y05 XOR x05 -> kbv
x24 AND y24 -> qhs
gbh AND whq -> jgs
kbg XOR hth -> z17
gvw XOR kgn -> vvr
ksv XOR cnk -> z07
pvv AND rnq -> mcc
x40 AND y40 -> vnr
x17 AND y17 -> qwr
mgt OR hrv -> npr
gwp AND vst -> fpn
tvp OR cqb -> tbr
y41 XOR x41 -> qvf
x21 AND y21 -> mms
nct AND njn -> qpg
tmh AND qch -> vpd
y37 XOR x37 -> kbk
x20 XOR y20 -> pkb
nbb OR rqg -> nsm
x21 XOR y21 -> pkq
y00 XOR x00 -> z00
kpm AND jpb -> hfn
y11 AND x11 -> sck
qwg AND nrr -> nmq
x43 XOR y43 -> ncj
jvj OR rqn -> gfs
scp OR jgs -> csv
y01 XOR x01 -> sgr
fcn AND bbk -> bpq
y22 AND x22 -> mmc
y36 AND x36 -> crp
x13 XOR y13 -> gps
hjm OR tss -> gvw
fcv OR wmt -> whq
wdg OR vnr -> jmm
mcc OR bkr -> kbg
pgm OR gmm -> nmw
jkv AND brn -> mqp
kbk AND hbw -> pgn
jds XOR gqd -> z40
fkp OR fdd -> thk
nsm XOR vkt -> z10
bhv AND wnf -> ggh
x29 AND y29 -> vtj
y32 AND x32 -> qbj
jgr OR ckr -> fcn
x35 AND y35 -> jgr
wts OR cps -> msf
x27 AND y27 -> csr
y16 XOR x16 -> bkr
y28 XOR x28 -> ptk
qgs XOR mjn -> z35
vkt AND nsm -> mqt
rjb XOR btj -> z31
x30 XOR y30 -> qwg
y07 AND x07 -> hjm
srn XOR fhb -> z06
x12 AND y12 -> vvb
y19 AND x19 -> cqb
hth AND kbg -> stp
vbw AND wwt -> qgg
mmc OR wdf -> kmd
vng XOR gfs -> z14
gqd AND jds -> wdg
x33 XOR y33 -> jkv
kbv XOR csv -> z05
pkb XOR tbr -> z20
y30 AND x30 -> jmn
x06 AND y06 -> rnr
gwp XOR vst -> z29
sfc AND sdv -> ngf
x33 AND y33 -> dpg
pkb AND tbr -> gvj
tkt AND msf -> qdf
tpf AND sft -> kms
jjj XOR fpw -> z38
sng AND jtc -> wmt
ptk AND djn -> gws
x29 XOR y29 -> gwp
y44 AND x44 -> dtb
nct XOR njn -> z27
x17 XOR y17 -> hth
y28 AND x28 -> z28
x02 AND y02 -> wjm"""

TEST = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""


@dataclass
class Gate:
    type: str
    w1: str
    w2: str
    out: str

    def op(self, a: bool, b: bool) -> bool:
        if self.type == "AND":
            return a and b
        elif self.type == "OR":
            return a or b
        elif self.type == "XOR":
            return a != b
        raise


@dataclass
class Wire:
    value: bool | None
    gates: list[Gate]
    from_gate: Gate | None


def part1(INPUT: str) -> None:
    initial, gates = INPUT.split("\n\n")

    wires: dict[str, Wire] = {}

    for row in initial.split("\n"):
        name, value = row.split(": ")
        wires[name] = Wire(value=value == "1", gates=[], from_gate=None)

    for row in gates.split("\n"):
        ops, out = row.split(" -> ")
        w1, type, w2 = ops.split(" ")

        gate = Gate(type=type, w1=w1, w2=w2, out=out)

        if wire := wires.get(out):
            wire.from_gate = gate
        else:
            wires[out] = Wire(value=None, gates=[], from_gate=gate)

        for w in [w1, w2]:
            if wire := wires.get(w):
                wire.gates.append(gate)
            else:
                wires[w] = Wire(value=None, gates=[gate], from_gate=None)

    def calc(w: str) -> bool:
        wire = wires[w]
        if wire.value is not None:
            return wire.value

        if gate := wire.from_gate:
            wire.value = gate.op(calc(gate.w1), calc(gate.w2))
            return wire.value
        raise

    output = []
    for name, wire in wires.items():
        if name.startswith("z"):
            output.append((name, calc(name)))

    binary = "".join("1" if v else "0" for n, v in reversed(sorted(output)))
    print(int(binary, 2))


# Determined by running part2 and reading the output
SWAPS = {
    "z28": "tfb",
    "tfb": "z28",
    "z39": "mqh",
    "mqh": "z39",
    "z08": "vvr",
    "vvr": "z08",
    "bkr": "rnq",
    "rnq": "bkr",
}


def part2(INPUT: str) -> None:
    initial, gates = INPUT.split("\n\n")

    wires: dict[str, Wire] = {}

    for row in initial.split("\n"):
        name, value = row.split(": ")
        wires[name] = Wire(value=value == "1", gates=[], from_gate=None)

    for row in gates.split("\n"):
        ops, out = row.split(" -> ")
        w1, type, w2 = ops.split(" ")

        out = SWAPS.get(out) or out

        gate = Gate(type=type, w1=w1, w2=w2, out=out)

        if wire := wires.get(out):
            wire.from_gate = gate
        else:
            wires[out] = Wire(value=None, gates=[], from_gate=gate)

        for w in [w1, w2]:
            if wire := wires.get(w):
                wire.gates.append(gate)
            else:
                wires[w] = Wire(value=None, gates=[gate], from_gate=None)

    def calc(w: str) -> bool:
        wire = wires[w]
        if wire.value is not None:
            return wire.value

        if gate := wire.from_gate:
            wire.value = gate.op(calc(gate.w1), calc(gate.w2))
            return wire.value
        raise

    len_x = 1 + int(sorted(x for x in wires.keys() if x.startswith("x"))[-1][1:])
    len_y = 1 + int(sorted(y for y in wires.keys() if y.startswith("y"))[-1][1:])
    len_z = 1 + int(sorted(z for z in wires.keys() if z.startswith("z"))[-1][1:])

    def run(x: int, y: int) -> int:
        # reinitialize
        for wire in wires.values():
            wire.value = None

        # set x
        for i in range(len_x):
            wires["x" + str(i).zfill(2)].value = False
        for i, b in enumerate(reversed(bin(x))):
            if b == "b":
                break
            wires["x" + str(i).zfill(2)].value = b == "1"

        # set y
        for i in range(len_y):
            wires["y" + str(i).zfill(2)].value = False
        for i, b in enumerate(reversed(bin(y))):
            if b == "b":
                break
            wires["y" + str(i).zfill(2)].value = b == "1"

        # calc z
        output = []
        for name, wire in wires.items():
            if name.startswith("z"):
                output.append((name, calc(name)))

        binary = "".join("1" if v else "0" for n, v in reversed(sorted(output)))
        return int(binary, 2)

    for i in range(len_x):
        n = str(i).zfill(2)
        x = wires["x" + n]
        y = wires["y" + n]

        # I expect x00 and y00 to go to XOR and AND
        xor_1 = None
        and_1 = None
        for gate in x.gates:
            if gate.type == "XOR":
                xor_1 = gate.out
            elif gate.type == "AND":
                and_1 = gate.out

        # I expect the result of the XOR to go to XOR and AND
        xor_2 = None
        and_2 = None
        if xor_1:
            for gate in wires[xor_1].gates:
                if gate.type == "XOR":
                    xor_2 = gate.out
                elif gate.type == "AND":
                    and_2 = gate.out
        if not xor_2:
            print("anomaly: bit", n, "missing xor_2", xor_1, wires[xor_1].gates)
        if not and_2:
            print("anomaly: bit", n, "missing and_2", xor_1, wires[xor_1].gates)
        if xor_2 and xor_2 != "z" + n:
            print("anomaly: bit", n, f"must swap z{n} with {xor_2}")

        # I expect the two ANDs to be ORed
        if and_1:
            if len(wires[and_1].gates) != 1:
                print(
                    "anomaly: ",
                    n,
                    "wrong number of outputs for and_1",
                    and_1,
                    wires[and_1].gates,
                )
            else:
                or_1 = wires[and_1].gates[0]
                if or_1.type != "OR":
                    print("anomaly:", n, "and_1 is not outputing to an OR")
                if and_2 not in [or_1.w1, or_1.w2]:
                    print("anomaly:", n, "or_1 does not have both ands as input")
        print(xor_2, and_2)

    # PROGRAM ANALYSIS:
    # z28 is certainly one of the ones that needs to be swapped, since it depends only on one gate
    # and does not take previous gates into account (which means it can't be calculating carry)
    # it's an input AND, so we can swap it
    # z08 is not the result of a XOR, it's OR
    # z39 is not the result of XOR, it's AND
    #
    # From running more code:
    # z28 <-> tfb
    # z39 <-> mqh

    # wires_from_gates = [w for w in wires.values() if w.from_gate]
    # length = len(wires_from_gates)

    # checking all possible 4 pairs is completely infeasible
    # length = 30
    # c = 0
    # for w1a in range(length):
    #     print(f"{w1a}/{length}")
    #     for w1b in range(w1a, length):
    #         for w2a in range(w1a, length):
    #             for w2b in range(w2a, length):
    #                 for w3a in range(w2a, length):
    #                     for w3b in range(w3a, length):
    #                         for w4a in range(w3a, length):
    #                             for w4b in range(w4a, length):
    #                                 c += 1
    # print(c)

    # Figure out which output bits are impacted by which gates
    # Figure out which output bits are wrong
    # try all possible pairs within wrong bit impacting gates?
    # if I can narrow it down from 222 to ~25 gates I can brute force

    # print(run(1, 4))
    # print(2**43 == run(2**43 - 1, 1))
    # print(2**43 == run(1, 2**43 - 1))

    print(",".join(sorted(SWAPS.keys())))


# part1(INPUT)
part2(INPUT)
