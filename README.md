# RR/IO Bulk Driven Class AB OpAmp with Improved Composite Transistors using SkyWater 130 nm PDK

Requires [Open PDKs](https://github.com/RTimothyEdwards/open_pdks) and Sky130 PDK to run simulations

## Opamp-A

### Schematic
![alt Opamp-A schematic](https://github.com/lhrodovalho/AICSP2022RAIL/blob/main/lib/amp/images/opampa.png)

### Netlist

[Link](https://github.com/lhrodovalho/AICSP2022RAIL/blob/main/lib/amp/ngspice/ampa.spice)

<details> <summary></summary>
  
```
* Operational amplifier A

.subckt ampa im ip o ib vdd vss 

x1nb ib  ib  dn1 vss n2_2
x1na dn1 ib  vss vss n1_4

x2pa dp2 gpa vdd vdd p1_4
x2pb gpa gpa dp2 vdd p2_2
x2pc gpb gpb gpa vdd p1_4
x2pd gpb gpb gpa vdd p1_4
x2nb gpb ib  dn2 vss n2_2
x2na dn2 ib  vss vss n1_4

x3pa dp3 gpa vdd vdd p1_4
x3pb gnb gpa dp3 vdd p2_2
x3nd gnb gnb gna vss n1_4
x3nc gnb gnb gna vss n1_4
x3nb gna gna dn3 vss n2_2
x3na dn3 gna vss vss n1_4

x4pa dp4 gpa vdd vdd p1_4
x4pb x   gpa dp4 vdd p2_2
x4pc yl  vss x   im  p4_1
x4nb kl  kl  yl  vss n2_2
x4na yl  kl  vss vss n1_4

x5pa dp5 gpa vdd vdd p1_4
x5pb x   gpa dp5 vdd p2_2
x5pc yr  vss x   ip  p4_1
x5nb kr  kl  yr  vss n2_2
x5na yr  kl  vss vss n1_4

x6pa dp6 gpa vdd vdd p1_4
x6pb jl  gpa dp6 vdd p2_2
x6pc kl  gpb jl  vdd p1_4
x6nc jl  gnb kl  vss n1_4
x6nb kl  kl  yl  vss n2_2
x6na yl  kl  vss vss n1_4

x7pa dp7 gpa vdd vdd p1_4
x7pb jr  gpa dp7 vdd p2_2
x7pc kr  gpb jr  vdd p1_4
x7nc jr  gnb kr  vss n1_4
x7nb kr  kl  yr  vss n2_2
x7na yr  kl  vss vss n1_4

x8pa dp8 jr  vdd vdd p2_2
x8pb o   jr  dp8 vdd p4_1
x8nb o   kr  dn8 vss n4_1
x8na dn8 kr  vss vss n2_2

cj o jr 0.8p
ck o kr 0.8p

.ends
```
</details>

## Opamp-B

### Schematic
![alt Opamp-B schematic](https://github.com/lhrodovalho/AICSP2022RAIL/blob/main/lib/amp/images/opampb.png)

### Netlist

[Link](https://github.com/lhrodovalho/AICSP2022RAIL/blob/main/lib/amp/ngspice/ampb.spice)

<details> <summary></summary>
  
```
* Operational amplifier B

.subckt ampb im ip o ib vdd vss 

x1nb ib  ib  dn1 vss n2_2
x1na dn1 ib  vss vss n1_4

x2pa dp2 gpa vdd vdd p1_4
x2pb gpa gpa dp2 bpa p2_2
x2pc gpb gpb gpa vdd p1_4
x2pd gpb gpb gpa vdd p1_4
x2nb gpb ib  dn2 vss n2_2
x2na dn2 ib  vss vss n1_4

x3pa dp3 gpa vdd vdd p1_4
x3pb gnb gpa dp3 bpa p2_2
x3nd gnb gnb gna vss n1_4
x3nc gnb gnb gna vss n1_4
x3nb gna gna dn3 bna n2_2
x3na dn3 gna vss vss n1_4

x4pa dp4 gpa vdd vdd p1_4
x4pb x   gpa dp4 bpa p2_2
x4pc yl  vss x   im  p4_1
x4nb kl  kl  yl  bna n2_2
x4na yl  kl  vss vss n1_4

x5pa dp5 gpa vdd vdd p1_4
x5pb x   gpa dp5 bp  p2_2
x5pc yr  vss x   ip  p4_1
x5nb kr  kl  yr  bn  n2_2
x5na yr  kl  vss vss n1_4

x6pa dp6 gpa vdd vdd p1_4
x6pb jl  gpa dp6 bpa p2_2
x6pc kl  gpb jl  vdd p1_4
x6nc jl  gnb kl  vss n1_4
x6nb kl  kl  yl  bna n2_2
x6na yl  kl  vss vss n1_4

x7pa dp7 gpa vdd vdd p1_4
x7pb jr  gpa dp7 bpa p2_2
x7pc kr  gpb jr  vdd p1_4
x7nc jr  gnb kr  vss n1_4
x7nb kr  kl  yr  bna n2_2
x7na yr  kl  vss vss n1_4

x8pa dp8 jr  vdd vdd p2_2
x8pb o   jr  dp8 bpb p4_1
x8nb o   kr  dn8 bnb n4_1
x8na dn8 kr  vss vss n2_2

x9pa gpa gpa bpa bpa p4_1
x9na gna gna bna bna n4_1

x9pb gpa gpa bpb bpb p4_1
x9nb gna gna bnb bnb n4_1

cbp bp vdd 1p
cbn bn vss 1p

cj o jr 0.75p
ck o kr 0.75p

.ends
```
</details>

## Transistor Arrays

### Schematic

![alt Array schematic](https://github.com/lhrodovalho/AICSP2022RAIL/blob/main/lib/amp/images/array.png)

### Netlist

[Link](https://github.com/lhrodovalho/AICSP2022RAIL/blob/main/lib/amp/ngspice/array.spice)

<details> <summary></summary>

```
* array

.subckt n1_1 D G S B
X0 D G X B sky130_fd_pr__nfet_g5v0d10v5 ad=7e+11p pd=4.7e+06u as=7e+11p ps=4.7e+06u w=2.0 l=0.5 m=4
X1 X G S B sky130_fd_pr__nfet_g5v0d10v5 ad=7e+11p pd=4.7e+06u as=7e+11p ps=4.7e+06u w=2.0 l=0.5 m=4
.ends

.subckt n1_2 D G S B
XD D G X B n1_1
XS X G S B n1_1
.ends

.subckt n2_1 D G S B
XL D G S B n1_1
XR D G S B n1_1
.ends

.subckt n1_4 D G S B
XD D G X B n1_2
XS X G S B n1_2
.ends

.subckt n2_2 D G S B
XL D G S B n1_2
XR D G S B n1_2
.ends

.subckt n4_1 D G S B
XL D G S B n2_1
XR D G S B n2_1
.ends

.subckt p1_1 D G S B
X0 D G S B sky130_fd_pr__pfet_g5v0d10v5 ad=7e+11p pd=4.7e+06u as=7e+11p ps=4.7e+06u w=2.0 l=0.5 m=8
.ends

.subckt p1_2 D G S B
XD D G X B p1_1
XS X G S B p1_1
.ends

.subckt p2_1 D G S B
XL D G S B p1_1
XR D G S B p1_1
.ends

.subckt p1_4 D G S B
XD D G X B p1_2
XS X G S B p1_2
.ends

.subckt p2_2 D G S B
XL D G S B p1_2
XR D G S B p1_2
.ends

.subckt p4_1 D G S B
XL D G S B p2_1
XR D G S B p2_1
.ends

```
