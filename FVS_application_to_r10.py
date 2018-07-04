import json
from os.path import exists
from boolean3_addon import attr_cy

modeltext = '''
AKT= Random
AP1= Random
Apoptosis= Random
ATF2= Random
ATM= Random
BCL2= Random
CREB= Random
DNA_damage= Random
DUSP1= Random
EGFR= Random
EGFR_stimulus= Random
ELK1= Random
ERK= Random
FGFR3= Random
FGFR3_stimulus= Random
FOS= Random
FOXO3= Random
FRS2= Random
GAB1= Random
GADD45= Random
GRB2= Random
Growth_Arrest= Random
JNK= Random
JUN= Random
MAP3K1_3= Random
MAX= Random
MDM2= Random
MEK1_2= Random
MSK= Random
MTK1= Random
MYC= Random
p14= Random
p21= Random
p38= Random
p53= Random
p70= Random
PDK1= Random
PI3K= Random
PKC= Random
PLCG= Random
PPP2CA= Random
Proliferation= Random
PTEN= Random
RAF= Random
RAS= Random
RSK= Random
SMAD= Random
SOS= Random
SPRY= Random
TAK1= Random
TAOK= Random
TGFBR= Random
TGFBR_stimulus= Random


AKT*= PDK1 and not PTEN
AP1*= JUN and (FOS or ATF2)
Apoptosis*= not BCL2 and not ERK and FOXO3 and p53
ATF2*= JNK or p38
ATM*= DNA_damage
BCL2*= CREB and AKT
CREB*= MSK
DNA_damage*= DNA_damage
DUSP1*= CREB
EGFR*= (EGFR_stimulus or SPRY) and not (PKC or GRB2)
EGFR_stimulus*= EGFR_stimulus
ELK1*= ERK or JNK or p38
ERK*= MEK1_2
FGFR3*= FGFR3_stimulus and not (GRB2 or PKC)
FGFR3_stimulus*= FGFR3_stimulus
FOS*= ERK and RSK and (ELK1 or CREB)
FOXO3*= JNK and not AKT
FRS2*= FGFR3 and not SPRY and not GRB2
GAB1*= GRB2 or PI3K
GADD45*= SMAD or p53
GRB2*= EGFR or FRS2 or TGFBR
Growth_Arrest*= p21
JNK*= (TAOK and MAP3K1_3) or (MAP3K1_3 and MTK1) or (TAOK and MTK1) or (TAK1 and MTK1) or (TAK1 and MAP3K1_3) or (TAK1 and TAOK) or ((TAOK or MTK1 or MAP3K1_3 or TAK1) and not DUSP1)
JUN*= JNK
MAP3K1_3*= RAS
MAX*= p38
MDM2*= (p53 or AKT) and not p14
MEK1_2*= (RAF or MAP3K1_3) and not (PPP2CA or AP1)
MSK*= ERK or p38
MTK1*= GADD45
MYC*= (MSK and MAX) or (MSK and AKT)
p14*= MYC
p21*= not AKT and p53
p38*= (TAOK and MAP3K1_3) or (MAP3K1_3 and MTK1) or (TAOK and MTK1) or (TAK1 and MTK1) or (TAK1 and MAP3K1_3) or (TAK1 and TAOK) or ((TAOK or MTK1 or MAP3K1_3 or TAK1) and not DUSP1)
p53*= (ATM and p38) or ((ATM or p38) and not MDM2)
p70*= PDK1 and ERK
PDK1*= PI3K
PI3K*= GAB1 or (RAS and SOS)
PKC*= PLCG
PLCG*= EGFR or FGFR3
PPP2CA*= p38
Proliferation*= p70 and MYC and not p21
PTEN*= p53
RAF*= (RAS or PKC) and not (ERK or AKT)
RAS*= SOS or PLCG
RSK*= ERK
SMAD*= TGFBR
SOS*= GRB2 and not RSK
SPRY*= ERK
TAK1*= TGFBR
TAOK*= ATM
TGFBR*= TGFBR_stimulus
TGFBR_stimulus*= TGFBR_stimulus
'''

attr_cy.build(modeltext)

import pyximport; pyximport.install()

res = attr_cy.run(samples=100000, steps=100, debug=False, progress=True, on_states=['DNA_damage', 'TGFBR_stimulus', 'p53', 'p38', 'PKC', 'GRB2', 'GAB1'], off_states=['EGFR_stimulus', 'ERK', 'FGFR3_stimulus'])
# on_states=['A01', 'A51'], off_states=['A38', 'A40']
# debug needs to be changed to 'True' to check trajectory
json.dump(res, open('FVS_application_to_r10.json', 'w'), indent=4)
