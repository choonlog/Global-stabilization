import json
from os.path import exists
from boolean3_addon import attr_cy

# def test_this_1():
#     modeltext = '''
#     A= Random
#     B= Random
#     C= Random
#     A*= A or C
#     B*= A and C
#     C*= not A or B
#     '''
#     if not exists('engine.pyx'):
#         attr_cy.build(modeltext)
#     import pyximport; pyximport.install()
#     res = attr_cy.run(samples=1000000, steps=50, debug=False, on_states=['A'], \
#         progress=True)
#     json.dump(res, open('output.json', 'w'), indent=4)

import pandas as pd

text='''
S_WNT=Random
S_Bcl_2=Random
S_CycD=Random
S_NF1=Random
S_cdh1_UbcH10=Random
S_COX412=Random
S_p53_PTEN=Random
S_TCF=Random
S_RAF=Random
S_E_cadh=Random
S_TGFbeta=Random
S_cdc20=Random
S_HIF1=Random
S_ERK=Random
S_PHDs=Random
S_RHEB=Random
S_Rb=Random
S_LDHA=Random
S_CHK1_2=Random
S_PKC=Random
S_E2F=Random
S_ROS=Random
S_Apoptosis=Random
S_Myc=Random
S_VHL=Random
S_eEF2=Random
S_p15=Random
S_TAK1=Random
S_mTOR=Random
S_Dsh=Random
S_CycE=Random
S_AKT=Random
S_DnaDamage=Random
S_IKK=Random
S_ATM_ATR=Random
S_TNFalpha=Random
S_Ras=Random
S_BAX=Random
S_beta_cat=Random
S_cdh1=Random
S_Glut_1=Random
S_AMPK=Random
S_GFs=Random
S_DNARepair=Random
S_GSK_3=Random
S_Nutrients=Random
S_p90=Random
S_CycA=Random
S_Snail=Random
S_GSH=Random
S_CycB=Random
S_Gli=Random
S_FADD=Random
S_Max=Random
S_Caspase8=Random
S_Mdm2=Random
S_TSC1_TSC2=Random
S_RTK=Random
S_NF_kB=Random
S_p27=Random
S_UbcH10=Random
S_Caspase9=Random
S_SmadMiz_1=Random
S_p14=Random
S_SmadE2F=Random
S_p53=Random
S_Cytoc_APAF1=Random
S_E2F_CyclinE=Random
S_hTERT=Random
S_MXI1=Random
S_Bcl_XL=Random
S_Bak=Random
S_FosJun=Random
S_BAD=Random
S_Mutagen=Random
S_VEGF=Random
S_PIP3=Random
S_JNK=Random
S_PI3K=Random
S_Slug=Random
S_PTEN=Random
S_RAGS=Random
S_Hypoxia=Random
S_AcidLactic=Random
S_FOXO=Random
S_GSK_3_APC=Random
S_Miz_1=Random
S_p70=Random
S_AMP_ATP=Random
S_Myc_Max=Random
S_PDK1=Random
S_p53_Mdm2=Random
S_Smad=Random
S_eEF2K=Random
S_p21=Random
S_APC=Random
S_TGFbeta *= S_HIF1
S_DnaDamage *= S_Mutagen or S_ROS
S_p53_Mdm2 *= S_Mdm2 and S_p53
S_AMP_ATP *= not S_Nutrients
S_NF1 *= not S_PKC
S_PKC *= S_RTK or S_WNT
S_RTK *= S_GFs
S_RAGS *= S_Nutrients and not S_Hypoxia
S_Ras *= S_RTK or not S_NF1
S_PI3K *= S_Ras or S_hTERT
S_PTEN *= True
S_PIP3 *= S_PI3K and not S_PTEN or S_PI3K and not S_p53_PTEN or not S_PTEN and not S_p53_PTEN
S_PDK1 *= S_HIF1 or S_Myc_Max or S_PIP3
S_IKK *= S_AKT and S_PKC and S_TAK1 or S_AKT and S_PKC and S_mTOR or S_AKT and S_PKC and not S_PHDs or S_AKT and S_PKC and not S_p53 or S_AKT and S_TAK1 and S_mTOR or S_AKT and S_TAK1 and not S_PHDs or S_AKT and S_TAK1 and not S_p53 or S_AKT and S_mTOR and not S_PHDs or S_AKT and S_mTOR and not S_p53 or S_AKT and not S_PHDs and not S_p53 or S_PKC and S_TAK1 and S_mTOR or S_PKC and S_TAK1 and not S_PHDs or S_PKC and S_TAK1 and not S_p53 or S_PKC and S_mTOR and not S_PHDs or S_PKC and S_mTOR and not S_p53 or S_PKC and not S_PHDs and not S_p53 or S_TAK1 and S_mTOR and not S_PHDs or S_TAK1 and S_mTOR and not S_p53 or S_TAK1 and not S_PHDs and not S_p53 or S_mTOR and not S_PHDs and not S_p53
S_NF_kB *= S_IKK and S_PIP3 or S_IKK and S_Snail or S_IKK and not S_E_cadh or S_PIP3 and S_Snail and not S_E_cadh
S_RAF *= S_PKC or S_Ras
S_ERK *= S_RAF
S_p90 *= S_ERK or S_PDK1
S_AKT *= S_PDK1 and S_PIP3
S_WNT *= S_Gli and not S_p53
S_Dsh *= S_WNT
S_APC *= True
S_GSK_3 *= not S_AKT and not S_Dsh or not S_AKT and not S_mTOR or not S_AKT and not S_p90 or not S_Dsh and not S_mTOR or not S_Dsh and not S_p90 or not S_mTOR and not S_p90
S_GSK_3_APC *= S_APC and S_GSK_3
S_beta_cat *= not S_GSK_3_APC and not S_p53
S_Slug *= S_NF_kB and S_TCF or S_NF_kB and not S_p53_Mdm2 or S_TCF and not S_p53_Mdm2
S_mTOR *= S_AKT and S_RAGS and S_RHEB or S_AKT and S_RAGS and not S_AMPK or S_AKT and S_RHEB and not S_AMPK or S_RAGS and S_RHEB and not S_AMPK
S_HIF1 *= S_Hypoxia and S_Myc_Max and not S_VHL or S_Hypoxia and S_mTOR and not S_VHL or S_Hypoxia and not S_FOXO and not S_VHL or S_Hypoxia and not S_PHDs and not S_VHL or S_Hypoxia and not S_VHL and not S_p53 or S_Myc_Max and S_mTOR and not S_VHL or S_Myc_Max and not S_FOXO and not S_VHL or S_Myc_Max and not S_PHDs and not S_VHL or S_Myc_Max and not S_VHL and not S_p53 or S_mTOR and not S_FOXO and not S_VHL or S_mTOR and not S_PHDs and not S_VHL or S_mTOR and not S_VHL and not S_p53 or not S_FOXO and not S_PHDs and not S_VHL or not S_FOXO and not S_VHL and not S_p53 or not S_PHDs and not S_VHL and not S_p53 or S_Hypoxia and S_Myc_Max and S_mTOR and not S_FOXO or S_Hypoxia and S_Myc_Max and S_mTOR and not S_PHDs or S_Hypoxia and S_Myc_Max and S_mTOR and not S_p53 or S_Hypoxia and S_Myc_Max and not S_FOXO and not S_PHDs or S_Hypoxia and S_Myc_Max and not S_FOXO and not S_p53 or S_Hypoxia and S_Myc_Max and not S_PHDs and not S_p53 or S_Hypoxia and S_mTOR and not S_FOXO and not S_PHDs or S_Hypoxia and S_mTOR and not S_FOXO and not S_p53 or S_Hypoxia and S_mTOR and not S_PHDs and not S_p53 or S_Hypoxia and not S_FOXO and not S_PHDs and not S_p53 or S_Myc_Max and S_mTOR and not S_FOXO and not S_PHDs or S_Myc_Max and S_mTOR and not S_FOXO and not S_p53 or S_Myc_Max and S_mTOR and not S_PHDs and not S_p53 or S_Myc_Max and not S_FOXO and not S_PHDs and not S_p53 or S_mTOR and not S_FOXO and not S_PHDs and not S_p53
S_COX412 *= S_HIF1
S_VHL *= not S_Hypoxia and not S_ROS
S_PHDs *= S_ROS or not S_Hypoxia
S_Myc_Max *= S_Max and S_Myc and not S_MXI1 and not S_SmadE2F and not S_TGFbeta
S_Myc *= S_E2F and S_ERK and S_FosJun or S_E2F and S_ERK and S_Gli or S_E2F and S_ERK and S_NF_kB or S_E2F and S_ERK and S_TCF or S_E2F and S_ERK and not S_HIF1 or S_E2F and S_FosJun and S_Gli or S_E2F and S_FosJun and S_NF_kB or S_E2F and S_FosJun and S_TCF or S_E2F and S_FosJun and not S_HIF1 or S_E2F and S_Gli and S_NF_kB or S_E2F and S_Gli and S_TCF or S_E2F and S_Gli and not S_HIF1 or S_E2F and S_NF_kB and S_TCF or S_E2F and S_NF_kB and not S_HIF1 or S_E2F and S_TCF and not S_HIF1 or S_ERK and S_FosJun and S_Gli or S_ERK and S_FosJun and S_NF_kB or S_ERK and S_FosJun and S_TCF or S_ERK and S_FosJun and not S_HIF1 or S_ERK and S_Gli and S_NF_kB or S_ERK and S_Gli and S_TCF or S_ERK and S_Gli and not S_HIF1 or S_ERK and S_NF_kB and S_TCF or S_ERK and S_NF_kB and not S_HIF1 or S_ERK and S_TCF and not S_HIF1 or S_FosJun and S_Gli and S_NF_kB or S_FosJun and S_Gli and S_TCF or S_FosJun and S_Gli and not S_HIF1 or S_FosJun and S_NF_kB and S_TCF or S_FosJun and S_NF_kB and not S_HIF1 or S_FosJun and S_TCF and not S_HIF1 or S_Gli and S_NF_kB and S_TCF or S_Gli and S_NF_kB and not S_HIF1 or S_Gli and S_TCF and not S_HIF1 or S_NF_kB and S_TCF and not S_HIF1
S_Max *= True
S_MXI1 *= S_HIF1
S_TSC1_TSC2 *= S_AMPK and S_HIF1 and S_p53 and not S_AKT or S_AMPK and S_HIF1 and S_p53 and not S_ERK or S_AMPK and S_HIF1 and S_p53 and not S_RAF or S_AMPK and S_HIF1 and S_p53 and not S_p90 or S_AMPK and S_HIF1 and not S_AKT and not S_ERK or S_AMPK and S_HIF1 and not S_AKT and not S_RAF or S_AMPK and S_HIF1 and not S_AKT and not S_p90 or S_AMPK and S_HIF1 and not S_ERK and not S_RAF or S_AMPK and S_HIF1 and not S_ERK and not S_p90 or S_AMPK and S_HIF1 and not S_RAF and not S_p90 or S_AMPK and S_p53 and not S_AKT and not S_ERK or S_AMPK and S_p53 and not S_AKT and not S_RAF or S_AMPK and S_p53 and not S_AKT and not S_p90 or S_AMPK and S_p53 and not S_ERK and not S_RAF or S_AMPK and S_p53 and not S_ERK and not S_p90 or S_AMPK and S_p53 and not S_RAF and not S_p90 or S_AMPK and not S_AKT and not S_ERK and not S_RAF or S_AMPK and not S_AKT and not S_ERK and not S_p90 or S_AMPK and not S_AKT and not S_RAF and not S_p90 or S_AMPK and not S_ERK and not S_RAF and not S_p90 or S_HIF1 and S_p53 and not S_AKT and not S_ERK or S_HIF1 and S_p53 and not S_AKT and not S_RAF or S_HIF1 and S_p53 and not S_AKT and not S_p90 or S_HIF1 and S_p53 and not S_ERK and not S_RAF or S_HIF1 and S_p53 and not S_ERK and not S_p90 or S_HIF1 and S_p53 and not S_RAF and not S_p90 or S_HIF1 and not S_AKT and not S_ERK and not S_RAF or S_HIF1 and not S_AKT and not S_ERK and not S_p90 or S_HIF1 and not S_AKT and not S_RAF and not S_p90 or S_HIF1 and not S_ERK and not S_RAF and not S_p90 or S_p53 and not S_AKT and not S_ERK and not S_RAF or S_p53 and not S_AKT and not S_ERK and not S_p90 or S_p53 and not S_AKT and not S_RAF and not S_p90 or S_p53 and not S_ERK and not S_RAF and not S_p90 or not S_AKT and not S_ERK and not S_RAF and not S_p90
S_RHEB *= not S_TSC1_TSC2
S_p53 *= S_CHK1_2 and S_HIF1 or S_CHK1_2 and not S_Bcl_2 or S_CHK1_2 and not S_Mdm2 or S_HIF1 and not S_Bcl_2 or S_HIF1 and not S_Mdm2 or not S_Bcl_2 and not S_Mdm2
S_Bcl_2 *= S_NF_kB and not S_BAD and not S_BAX or S_NF_kB and not S_BAD and not S_p53 or S_NF_kB and not S_BAX and not S_p53
S_BAX *= S_JNK and S_p53 and not S_Bcl_2 or S_JNK and S_p53 and not S_HIF1 or S_JNK and not S_Bcl_2 and not S_HIF1 or S_p53 and not S_Bcl_2 and not S_HIF1
S_BAD *= not S_AKT and not S_HIF1 and not S_RAF and not S_p90
S_Bcl_XL *= not S_BAD and not S_p53
S_Rb *= not S_CycA and not S_CycB and not S_CycD and not S_CycE or not S_CycA and not S_CycB and not S_CycD and not S_Mdm2 or not S_CycA and not S_CycB and not S_CycE and not S_Mdm2 or not S_CycA and not S_CycD and not S_CycE and not S_Mdm2 or not S_CycB and not S_CycD and not S_CycE and not S_Mdm2
S_E2F *= S_E2F and not S_CycA and not S_Rb or S_E2F and not S_CycB and not S_Rb or not S_CycA and not S_CycB and not S_Rb
S_p14 *= False
S_CycA *= S_CycA and S_E2F_CyclinE and S_cdh1_UbcH10 and not S_Rb and not S_cdc20 or S_CycA and S_E2F_CyclinE and S_cdh1_UbcH10 and not S_Rb and not S_p21 or S_CycA and S_E2F_CyclinE and S_cdh1_UbcH10 and not S_Rb and not S_p27 or S_CycA and S_E2F_CyclinE and S_cdh1_UbcH10 and not S_cdc20 and not S_p21 or S_CycA and S_E2F_CyclinE and S_cdh1_UbcH10 and not S_cdc20 and not S_p27 or S_CycA and S_E2F_CyclinE and S_cdh1_UbcH10 and not S_p21 and not S_p27 or S_CycA and S_E2F_CyclinE and not S_Rb and not S_cdc20 and not S_p21 or S_CycA and S_E2F_CyclinE and not S_Rb and not S_cdc20 and not S_p27 or S_CycA and S_E2F_CyclinE and not S_Rb and not S_p21 and not S_p27 or S_CycA and S_E2F_CyclinE and not S_cdc20 and not S_p21 and not S_p27 or S_CycA and S_cdh1_UbcH10 and not S_Rb and not S_cdc20 and not S_p21 or S_CycA and S_cdh1_UbcH10 and not S_Rb and not S_cdc20 and not S_p27 or S_CycA and S_cdh1_UbcH10 and not S_Rb and not S_p21 and not S_p27 or S_CycA and S_cdh1_UbcH10 and not S_cdc20 and not S_p21 and not S_p27 or S_CycA and not S_Rb and not S_cdc20 and not S_p21 and not S_p27 or S_E2F_CyclinE and S_cdh1_UbcH10 and not S_Rb and not S_cdc20 and not S_p21 or S_E2F_CyclinE and S_cdh1_UbcH10 and not S_Rb and not S_cdc20 and not S_p27 or S_E2F_CyclinE and S_cdh1_UbcH10 and not S_Rb and not S_p21 and not S_p27 or S_E2F_CyclinE and S_cdh1_UbcH10 and not S_cdc20 and not S_p21 and not S_p27 or S_E2F_CyclinE and not S_Rb and not S_cdc20 and not S_p21 and not S_p27 or S_cdh1_UbcH10 and not S_Rb and not S_cdc20 and not S_p21 and not S_p27
S_CycB *= not S_cdc20 and not S_cdh1 and not S_p21 and not S_p27 and not S_p53
S_CycD *= S_FosJun and S_Gli and S_Myc_Max and S_NF_kB and S_TCF and not S_GSK_3 or S_FosJun and S_Gli and S_Myc_Max and S_NF_kB and not S_FOXO and not S_GSK_3 or S_FosJun and S_Gli and S_Myc_Max and S_NF_kB and not S_GSK_3 and not S_p15 or S_FosJun and S_Gli and S_Myc_Max and S_NF_kB and not S_GSK_3 and not S_p21 or S_FosJun and S_Gli and S_Myc_Max and S_NF_kB and not S_GSK_3 and not S_p27 or S_FosJun and S_Gli and S_Myc_Max and S_TCF and not S_FOXO and not S_GSK_3 or S_FosJun and S_Gli and S_Myc_Max and S_TCF and not S_GSK_3 and not S_p15 or S_FosJun and S_Gli and S_Myc_Max and S_TCF and not S_GSK_3 and not S_p21 or S_FosJun and S_Gli and S_Myc_Max and S_TCF and not S_GSK_3 and not S_p27 or S_FosJun and S_Gli and S_Myc_Max and not S_FOXO and not S_GSK_3 and not S_p15 or S_FosJun and S_Gli and S_Myc_Max and not S_FOXO and not S_GSK_3 and not S_p21 or S_FosJun and S_Gli and S_Myc_Max and not S_FOXO and not S_GSK_3 and not S_p27 or S_FosJun and S_Gli and S_Myc_Max and not S_GSK_3 and not S_p15 and not S_p21 or S_FosJun and S_Gli and S_Myc_Max and not S_GSK_3 and not S_p15 and not S_p27 or S_FosJun and S_Gli and S_Myc_Max and not S_GSK_3 and not S_p21 and not S_p27 or S_FosJun and S_Gli and S_NF_kB and S_TCF and not S_FOXO and not S_GSK_3 or S_FosJun and S_Gli and S_NF_kB and S_TCF and not S_GSK_3 and not S_p15 or S_FosJun and S_Gli and S_NF_kB and S_TCF and not S_GSK_3 and not S_p21 or S_FosJun and S_Gli and S_NF_kB and S_TCF and not S_GSK_3 and not S_p27 or S_FosJun and S_Gli and S_NF_kB and not S_FOXO and not S_GSK_3 and not S_p15 or S_FosJun and S_Gli and S_NF_kB and not S_FOXO and not S_GSK_3 and not S_p21 or S_FosJun and S_Gli and S_NF_kB and not S_FOXO and not S_GSK_3 and not S_p27 or S_FosJun and S_Gli and S_NF_kB and not S_GSK_3 and not S_p15 and not S_p21 or S_FosJun and S_Gli and S_NF_kB and not S_GSK_3 and not S_p15 and not S_p27 or S_FosJun and S_Gli and S_NF_kB and not S_GSK_3 and not S_p21 and not S_p27 or S_FosJun and S_Gli and S_TCF and not S_FOXO and not S_GSK_3 and not S_p15 or S_FosJun and S_Gli and S_TCF and not S_FOXO and not S_GSK_3 and not S_p21 or S_FosJun and S_Gli and S_TCF and not S_FOXO and not S_GSK_3 and not S_p27 or S_FosJun and S_Gli and S_TCF and not S_GSK_3 and not S_p15 and not S_p21 or S_FosJun and S_Gli and S_TCF and not S_GSK_3 and not S_p15 and not S_p27 or S_FosJun and S_Gli and S_TCF and not S_GSK_3 and not S_p21 and not S_p27 or S_FosJun and S_Gli and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p21 or S_FosJun and S_Gli and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p27 or S_FosJun and S_Gli and not S_FOXO and not S_GSK_3 and not S_p21 and not S_p27 or S_FosJun and S_Gli and not S_GSK_3 and not S_p15 and not S_p21 and not S_p27 or S_FosJun and S_Myc_Max and S_NF_kB and S_TCF and not S_FOXO and not S_GSK_3 or S_FosJun and S_Myc_Max and S_NF_kB and S_TCF and not S_GSK_3 and not S_p15 or S_FosJun and S_Myc_Max and S_NF_kB and S_TCF and not S_GSK_3 and not S_p21 or S_FosJun and S_Myc_Max and S_NF_kB and S_TCF and not S_GSK_3 and not S_p27 or S_FosJun and S_Myc_Max and S_NF_kB and not S_FOXO and not S_GSK_3 and not S_p15 or S_FosJun and S_Myc_Max and S_NF_kB and not S_FOXO and not S_GSK_3 and not S_p21 or S_FosJun and S_Myc_Max and S_NF_kB and not S_FOXO and not S_GSK_3 and not S_p27 or S_FosJun and S_Myc_Max and S_NF_kB and not S_GSK_3 and not S_p15 and not S_p21 or S_FosJun and S_Myc_Max and S_NF_kB and not S_GSK_3 and not S_p15 and not S_p27 or S_FosJun and S_Myc_Max and S_NF_kB and not S_GSK_3 and not S_p21 and not S_p27 or S_FosJun and S_Myc_Max and S_TCF and not S_FOXO and not S_GSK_3 and not S_p15 or S_FosJun and S_Myc_Max and S_TCF and not S_FOXO and not S_GSK_3 and not S_p21 or S_FosJun and S_Myc_Max and S_TCF and not S_FOXO and not S_GSK_3 and not S_p27 or S_FosJun and S_Myc_Max and S_TCF and not S_GSK_3 and not S_p15 and not S_p21 or S_FosJun and S_Myc_Max and S_TCF and not S_GSK_3 and not S_p15 and not S_p27 or S_FosJun and S_Myc_Max and S_TCF and not S_GSK_3 and not S_p21 and not S_p27 or S_FosJun and S_Myc_Max and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p21 or S_FosJun and S_Myc_Max and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p27 or S_FosJun and S_Myc_Max and not S_FOXO and not S_GSK_3 and not S_p21 and not S_p27 or S_FosJun and S_Myc_Max and not S_GSK_3 and not S_p15 and not S_p21 and not S_p27 or S_FosJun and S_NF_kB and S_TCF and not S_FOXO and not S_GSK_3 and not S_p15 or S_FosJun and S_NF_kB and S_TCF and not S_FOXO and not S_GSK_3 and not S_p21 or S_FosJun and S_NF_kB and S_TCF and not S_FOXO and not S_GSK_3 and not S_p27 or S_FosJun and S_NF_kB and S_TCF and not S_GSK_3 and not S_p15 and not S_p21 or S_FosJun and S_NF_kB and S_TCF and not S_GSK_3 and not S_p15 and not S_p27 or S_FosJun and S_NF_kB and S_TCF and not S_GSK_3 and not S_p21 and not S_p27 or S_FosJun and S_NF_kB and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p21 or S_FosJun and S_NF_kB and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p27 or S_FosJun and S_NF_kB and not S_FOXO and not S_GSK_3 and not S_p21 and not S_p27 or S_FosJun and S_NF_kB and not S_GSK_3 and not S_p15 and not S_p21 and not S_p27 or S_FosJun and S_TCF and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p21 or S_FosJun and S_TCF and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p27 or S_FosJun and S_TCF and not S_FOXO and not S_GSK_3 and not S_p21 and not S_p27 or S_FosJun and S_TCF and not S_GSK_3 and not S_p15 and not S_p21 and not S_p27 or S_FosJun and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p21 and not S_p27 or S_Gli and S_Myc_Max and S_NF_kB and S_TCF and not S_FOXO and not S_GSK_3 or S_Gli and S_Myc_Max and S_NF_kB and S_TCF and not S_GSK_3 and not S_p15 or S_Gli and S_Myc_Max and S_NF_kB and S_TCF and not S_GSK_3 and not S_p21 or S_Gli and S_Myc_Max and S_NF_kB and S_TCF and not S_GSK_3 and not S_p27 or S_Gli and S_Myc_Max and S_NF_kB and not S_FOXO and not S_GSK_3 and not S_p15 or S_Gli and S_Myc_Max and S_NF_kB and not S_FOXO and not S_GSK_3 and not S_p21 or S_Gli and S_Myc_Max and S_NF_kB and not S_FOXO and not S_GSK_3 and not S_p27 or S_Gli and S_Myc_Max and S_NF_kB and not S_GSK_3 and not S_p15 and not S_p21 or S_Gli and S_Myc_Max and S_NF_kB and not S_GSK_3 and not S_p15 and not S_p27 or S_Gli and S_Myc_Max and S_NF_kB and not S_GSK_3 and not S_p21 and not S_p27 or S_Gli and S_Myc_Max and S_TCF and not S_FOXO and not S_GSK_3 and not S_p15 or S_Gli and S_Myc_Max and S_TCF and not S_FOXO and not S_GSK_3 and not S_p21 or S_Gli and S_Myc_Max and S_TCF and not S_FOXO and not S_GSK_3 and not S_p27 or S_Gli and S_Myc_Max and S_TCF and not S_GSK_3 and not S_p15 and not S_p21 or S_Gli and S_Myc_Max and S_TCF and not S_GSK_3 and not S_p15 and not S_p27 or S_Gli and S_Myc_Max and S_TCF and not S_GSK_3 and not S_p21 and not S_p27 or S_Gli and S_Myc_Max and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p21 or S_Gli and S_Myc_Max and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p27 or S_Gli and S_Myc_Max and not S_FOXO and not S_GSK_3 and not S_p21 and not S_p27 or S_Gli and S_Myc_Max and not S_GSK_3 and not S_p15 and not S_p21 and not S_p27 or S_Gli and S_NF_kB and S_TCF and not S_FOXO and not S_GSK_3 and not S_p15 or S_Gli and S_NF_kB and S_TCF and not S_FOXO and not S_GSK_3 and not S_p21 or S_Gli and S_NF_kB and S_TCF and not S_FOXO and not S_GSK_3 and not S_p27 or S_Gli and S_NF_kB and S_TCF and not S_GSK_3 and not S_p15 and not S_p21 or S_Gli and S_NF_kB and S_TCF and not S_GSK_3 and not S_p15 and not S_p27 or S_Gli and S_NF_kB and S_TCF and not S_GSK_3 and not S_p21 and not S_p27 or S_Gli and S_NF_kB and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p21 or S_Gli and S_NF_kB and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p27 or S_Gli and S_NF_kB and not S_FOXO and not S_GSK_3 and not S_p21 and not S_p27 or S_Gli and S_NF_kB and not S_GSK_3 and not S_p15 and not S_p21 and not S_p27 or S_Gli and S_TCF and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p21 or S_Gli and S_TCF and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p27 or S_Gli and S_TCF and not S_FOXO and not S_GSK_3 and not S_p21 and not S_p27 or S_Gli and S_TCF and not S_GSK_3 and not S_p15 and not S_p21 and not S_p27 or S_Gli and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p21 and not S_p27 or S_Myc_Max and S_NF_kB and S_TCF and not S_FOXO and not S_GSK_3 and not S_p15 or S_Myc_Max and S_NF_kB and S_TCF and not S_FOXO and not S_GSK_3 and not S_p21 or S_Myc_Max and S_NF_kB and S_TCF and not S_FOXO and not S_GSK_3 and not S_p27 or S_Myc_Max and S_NF_kB and S_TCF and not S_GSK_3 and not S_p15 and not S_p21 or S_Myc_Max and S_NF_kB and S_TCF and not S_GSK_3 and not S_p15 and not S_p27 or S_Myc_Max and S_NF_kB and S_TCF and not S_GSK_3 and not S_p21 and not S_p27 or S_Myc_Max and S_NF_kB and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p21 or S_Myc_Max and S_NF_kB and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p27 or S_Myc_Max and S_NF_kB and not S_FOXO and not S_GSK_3 and not S_p21 and not S_p27 or S_Myc_Max and S_NF_kB and not S_GSK_3 and not S_p15 and not S_p21 and not S_p27 or S_Myc_Max and S_TCF and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p21 or S_Myc_Max and S_TCF and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p27 or S_Myc_Max and S_TCF and not S_FOXO and not S_GSK_3 and not S_p21 and not S_p27 or S_Myc_Max and S_TCF and not S_GSK_3 and not S_p15 and not S_p21 and not S_p27 or S_Myc_Max and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p21 and not S_p27 or S_NF_kB and S_TCF and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p21 or S_NF_kB and S_TCF and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p27 or S_NF_kB and S_TCF and not S_FOXO and not S_GSK_3 and not S_p21 and not S_p27 or S_NF_kB and S_TCF and not S_GSK_3 and not S_p15 and not S_p21 and not S_p27 or S_NF_kB and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p21 and not S_p27 or S_TCF and not S_FOXO and not S_GSK_3 and not S_p15 and not S_p21 and not S_p27 or S_FosJun and S_Gli and S_Myc_Max and S_NF_kB and S_TCF and not S_FOXO and not S_p15 or S_FosJun and S_Gli and S_Myc_Max and S_NF_kB and S_TCF and not S_FOXO and not S_p21 or S_FosJun and S_Gli and S_Myc_Max and S_NF_kB and S_TCF and not S_FOXO and not S_p27 or S_FosJun and S_Gli and S_Myc_Max and S_NF_kB and S_TCF and not S_p15 and not S_p21 or S_FosJun and S_Gli and S_Myc_Max and S_NF_kB and S_TCF and not S_p15 and not S_p27 or S_FosJun and S_Gli and S_Myc_Max and S_NF_kB and S_TCF and not S_p21 and not S_p27 or S_FosJun and S_Gli and S_Myc_Max and S_NF_kB and not S_FOXO and not S_p15 and not S_p21 or S_FosJun and S_Gli and S_Myc_Max and S_NF_kB and not S_FOXO and not S_p15 and not S_p27 or S_FosJun and S_Gli and S_Myc_Max and S_NF_kB and not S_FOXO and not S_p21 and not S_p27 or S_FosJun and S_Gli and S_Myc_Max and S_NF_kB and not S_p15 and not S_p21 and not S_p27 or S_FosJun and S_Gli and S_Myc_Max and S_TCF and not S_FOXO and not S_p15 and not S_p21 or S_FosJun and S_Gli and S_Myc_Max and S_TCF and not S_FOXO and not S_p15 and not S_p27 or S_FosJun and S_Gli and S_Myc_Max and S_TCF and not S_FOXO and not S_p21 and not S_p27 or S_FosJun and S_Gli and S_Myc_Max and S_TCF and not S_p15 and not S_p21 and not S_p27 or S_FosJun and S_Gli and S_Myc_Max and not S_FOXO and not S_p15 and not S_p21 and not S_p27 or S_FosJun and S_Gli and S_NF_kB and S_TCF and not S_FOXO and not S_p15 and not S_p21 or S_FosJun and S_Gli and S_NF_kB and S_TCF and not S_FOXO and not S_p15 and not S_p27 or S_FosJun and S_Gli and S_NF_kB and S_TCF and not S_FOXO and not S_p21 and not S_p27 or S_FosJun and S_Gli and S_NF_kB and S_TCF and not S_p15 and not S_p21 and not S_p27 or S_FosJun and S_Gli and S_NF_kB and not S_FOXO and not S_p15 and not S_p21 and not S_p27 or S_FosJun and S_Gli and S_TCF and not S_FOXO and not S_p15 and not S_p21 and not S_p27 or S_FosJun and S_Myc_Max and S_NF_kB and S_TCF and not S_FOXO and not S_p15 and not S_p21 or S_FosJun and S_Myc_Max and S_NF_kB and S_TCF and not S_FOXO and not S_p15 and not S_p27 or S_FosJun and S_Myc_Max and S_NF_kB and S_TCF and not S_FOXO and not S_p21 and not S_p27 or S_FosJun and S_Myc_Max and S_NF_kB and S_TCF and not S_p15 and not S_p21 and not S_p27 or S_FosJun and S_Myc_Max and S_NF_kB and not S_FOXO and not S_p15 and not S_p21 and not S_p27 or S_FosJun and S_Myc_Max and S_TCF and not S_FOXO and not S_p15 and not S_p21 and not S_p27 or S_FosJun and S_NF_kB and S_TCF and not S_FOXO and not S_p15 and not S_p21 and not S_p27 or S_Gli and S_Myc_Max and S_NF_kB and S_TCF and not S_FOXO and not S_p15 and not S_p21 or S_Gli and S_Myc_Max and S_NF_kB and S_TCF and not S_FOXO and not S_p15 and not S_p27 or S_Gli and S_Myc_Max and S_NF_kB and S_TCF and not S_FOXO and not S_p21 and not S_p27 or S_Gli and S_Myc_Max and S_NF_kB and S_TCF and not S_p15 and not S_p21 and not S_p27 or S_Gli and S_Myc_Max and S_NF_kB and not S_FOXO and not S_p15 and not S_p21 and not S_p27 or S_Gli and S_Myc_Max and S_TCF and not S_FOXO and not S_p15 and not S_p21 and not S_p27 or S_Gli and S_NF_kB and S_TCF and not S_FOXO and not S_p15 and not S_p21 and not S_p27 or S_Myc_Max and S_NF_kB and S_TCF and not S_FOXO and not S_p15 and not S_p21 and not S_p27
S_CycE *= S_E2F and not S_CycA and not S_Rb and not S_p21 and not S_p27
S_cdh1 *= S_cdc20 and not S_CycA or S_cdc20 and not S_CycB or not S_CycA and not S_CycB
S_cdc20 *= S_CycB and not S_cdh1
S_UbcH10 *= S_CycA and S_CycB or S_CycA and S_UbcH10 or S_CycA and S_cdc20 or S_CycA and not S_cdh1 or S_CycB and S_UbcH10 or S_CycB and S_cdc20 or S_CycB and not S_cdh1 or S_UbcH10 and S_cdc20 or S_UbcH10 and not S_cdh1 or S_cdc20 and not S_cdh1
S_p27 *= S_HIF1 and S_SmadMiz_1 and not S_AKT and not S_CycA and not S_CycB or S_HIF1 and S_SmadMiz_1 and not S_AKT and not S_CycA and not S_CycD or S_HIF1 and S_SmadMiz_1 and not S_AKT and not S_CycA and not S_Myc_Max or S_HIF1 and S_SmadMiz_1 and not S_AKT and not S_CycB and not S_CycD or S_HIF1 and S_SmadMiz_1 and not S_AKT and not S_CycB and not S_Myc_Max or S_HIF1 and S_SmadMiz_1 and not S_AKT and not S_CycD and not S_Myc_Max or S_HIF1 and S_SmadMiz_1 and not S_CycA and not S_CycB and not S_CycD or S_HIF1 and S_SmadMiz_1 and not S_CycA and not S_CycB and not S_Myc_Max or S_HIF1 and S_SmadMiz_1 and not S_CycA and not S_CycD and not S_Myc_Max or S_HIF1 and S_SmadMiz_1 and not S_CycB and not S_CycD and not S_Myc_Max or S_HIF1 and not S_AKT and not S_CycA and not S_CycB and not S_CycD or S_HIF1 and not S_AKT and not S_CycA and not S_CycB and not S_Myc_Max or S_HIF1 and not S_AKT and not S_CycA and not S_CycD and not S_Myc_Max or S_HIF1 and not S_AKT and not S_CycB and not S_CycD and not S_Myc_Max or S_HIF1 and not S_CycA and not S_CycB and not S_CycD and not S_Myc_Max or S_SmadMiz_1 and not S_AKT and not S_CycA and not S_CycB and not S_CycD or S_SmadMiz_1 and not S_AKT and not S_CycA and not S_CycB and not S_Myc_Max or S_SmadMiz_1 and not S_AKT and not S_CycA and not S_CycD and not S_Myc_Max or S_SmadMiz_1 and not S_AKT and not S_CycB and not S_CycD and not S_Myc_Max or S_SmadMiz_1 and not S_CycA and not S_CycB and not S_CycD and not S_Myc_Max or not S_AKT and not S_CycA and not S_CycB and not S_CycD and not S_Myc_Max
S_p21 *= S_HIF1 and S_SmadMiz_1 and S_p53 or S_HIF1 and S_SmadMiz_1 and not S_AKT or S_HIF1 and S_SmadMiz_1 and not S_Myc_Max or S_HIF1 and S_SmadMiz_1 and not S_hTERT or S_HIF1 and S_p53 and not S_AKT or S_HIF1 and S_p53 and not S_Myc_Max or S_HIF1 and S_p53 and not S_hTERT or S_HIF1 and not S_AKT and not S_Myc_Max or S_HIF1 and not S_AKT and not S_hTERT or S_HIF1 and not S_Myc_Max and not S_hTERT or S_SmadMiz_1 and S_p53 and not S_AKT or S_SmadMiz_1 and S_p53 and not S_Myc_Max or S_SmadMiz_1 and S_p53 and not S_hTERT or S_SmadMiz_1 and not S_AKT and not S_Myc_Max or S_SmadMiz_1 and not S_AKT and not S_hTERT or S_SmadMiz_1 and not S_Myc_Max and not S_hTERT or S_p53 and not S_AKT and not S_Myc_Max or S_p53 and not S_AKT and not S_hTERT or S_p53 and not S_Myc_Max and not S_hTERT or not S_AKT and not S_Myc_Max and not S_hTERT
S_Mdm2 *= S_AKT and S_p53 or S_AKT and not S_ATM_ATR or S_AKT and not S_p14 or S_p53 and not S_ATM_ATR or S_p53 and not S_p14 or not S_ATM_ATR and not S_p14
S_Smad *= S_TGFbeta or S_TNFalpha
S_SmadMiz_1 *= S_Miz_1 and S_Smad
S_SmadE2F *= S_Smad
S_p15 *= S_Miz_1 or S_SmadMiz_1
S_FADD *= S_TNFalpha
S_Caspase8 *= S_FADD
S_Bak *= S_Caspase8
S_JNK *= S_TGFbeta
S_FOXO *= True
S_FosJun *= S_ERK or S_JNK
S_ROS *= False
S_AMPK *= S_AMP_ATP or S_ATM_ATR or S_HIF1 or not S_GFs
S_Cytoc_APAF1 *= S_BAX and S_Bak and S_Caspase8 and S_p53 or S_BAX and S_Bak and S_Caspase8 and not S_AKT or S_BAX and S_Bak and S_Caspase8 and not S_Bcl_2 or S_BAX and S_Bak and S_Caspase8 and not S_Bcl_XL or S_BAX and S_Bak and S_p53 and not S_AKT or S_BAX and S_Bak and S_p53 and not S_Bcl_2 or S_BAX and S_Bak and S_p53 and not S_Bcl_XL or S_BAX and S_Bak and not S_AKT and not S_Bcl_2 or S_BAX and S_Bak and not S_AKT and not S_Bcl_XL or S_BAX and S_Bak and not S_Bcl_2 and not S_Bcl_XL or S_BAX and S_Caspase8 and S_p53 and not S_AKT or S_BAX and S_Caspase8 and S_p53 and not S_Bcl_2 or S_BAX and S_Caspase8 and S_p53 and not S_Bcl_XL or S_BAX and S_Caspase8 and not S_AKT and not S_Bcl_2 or S_BAX and S_Caspase8 and not S_AKT and not S_Bcl_XL or S_BAX and S_Caspase8 and not S_Bcl_2 and not S_Bcl_XL or S_BAX and S_p53 and not S_AKT and not S_Bcl_2 or S_BAX and S_p53 and not S_AKT and not S_Bcl_XL or S_BAX and S_p53 and not S_Bcl_2 and not S_Bcl_XL or S_BAX and not S_AKT and not S_Bcl_2 and not S_Bcl_XL or S_Bak and S_Caspase8 and S_p53 and not S_AKT or S_Bak and S_Caspase8 and S_p53 and not S_Bcl_2 or S_Bak and S_Caspase8 and S_p53 and not S_Bcl_XL or S_Bak and S_Caspase8 and not S_AKT and not S_Bcl_2 or S_Bak and S_Caspase8 and not S_AKT and not S_Bcl_XL or S_Bak and S_Caspase8 and not S_Bcl_2 and not S_Bcl_XL or S_Bak and S_p53 and not S_AKT and not S_Bcl_2 or S_Bak and S_p53 and not S_AKT and not S_Bcl_XL or S_Bak and S_p53 and not S_Bcl_2 and not S_Bcl_XL or S_Bak and not S_AKT and not S_Bcl_2 and not S_Bcl_XL or S_Caspase8 and S_p53 and not S_AKT and not S_Bcl_2 or S_Caspase8 and S_p53 and not S_AKT and not S_Bcl_XL or S_Caspase8 and S_p53 and not S_Bcl_2 and not S_Bcl_XL or S_Caspase8 and not S_AKT and not S_Bcl_2 and not S_Bcl_XL or S_p53 and not S_AKT and not S_Bcl_2 and not S_Bcl_XL
S_Caspase9 *= S_Cytoc_APAF1
S_Apoptosis *= S_Caspase8 or S_Caspase9
S_E_cadh *= not S_NF_kB or not S_Slug or not S_Snail
S_Glut_1 *= S_AKT and S_HIF1 or S_AKT and S_Myc_Max or S_HIF1 and S_Myc_Max
S_hTERT *= S_AKT and S_HIF1 and S_Myc_Max and S_NF1 and S_NF_kB and not S_SmadMiz_1 and not S_eEF2 and not S_p53
S_VEGF *= S_HIF1 or S_Myc_Max
S_E2F_CyclinE *= S_CycE and S_E2F
S_cdh1_UbcH10 *= S_UbcH10 and S_cdh1
S_TAK1 *= S_TNFalpha
S_GSH *= S_Myc_Max or S_NF_kB or S_p21
S_TCF *= S_beta_cat and not S_TAK1
S_Miz_1 *= not S_Myc_Max
S_p70 *= S_PDK1 or S_mTOR
S_ATM_ATR *= S_DnaDamage
S_CHK1_2 *= S_ATM_ATR
S_DNARepair *= S_ATM_ATR
S_eEF2K *= S_p70 or S_p90
S_eEF2 *= not S_eEF2K
S_p53_PTEN *= S_PTEN and S_p53
S_LDHA *= S_HIF1 and S_Myc_Max
S_AcidLactic *= S_LDHA
S_Snail *= S_NF_kB and S_Smad and not S_GSK_3 and not S_p53
'''
# if not exists('engine.pyx'):
attr_cy.build(text)

import pyximport; pyximport.install()
import engine

def test_this_2():
    result = engine.main(samples=1000000, steps=50, debug=False, \
        progress=True, on_states=[], off_states=[])

    json.dump(result, open('test_attr_cy_long.json', 'w'), indent=4)